import threading
import os
import time

# config your systems as IP:DESC
systems = {"10.11.12.14" :"IR5ZYK Momigno C4FM",
           "10.11.12.10" :"IR5ZYJ Momigno DMR",
           "10.11.12.22" :"IR5UBO Incontro DSTAR",
           "10.11.12.26" :"IR5ZXZ Giovi DMR",
           "10.11.12.30" :"IR5ZYL Bagno a Ripoli C4FM",
           "10.11.12.34" :"IR5UDN Incontro C4FM",
           "10.11.12.38" :"IR5ZYA Incontro3 DSTAR",
           "10.11.12.54" :"IR5ANC Giovi AN-C DSTAR",
           "10.11.12.58" :"IR5ANB Giovi AN-B DSTAR",
           "10.11.12.74" :"FUTAND Futa C4FM",
           "10.11.12.82" :"IR5ZYD Agliale DMR",
           "10.11.12.90" :"AMIATA C4FM",
           "10.11.12.106":"AMIATB DSTAR",
           "10.11.12.138":"IR5UCQ Giovi C4FM",
           "10.11.12.86" :"IR5UEC Lucca DMR"}

# config initial value as IP:0
# 0 = system is available
reports = { "10.11.12.14" :0,
            "10.11.12.10" :0,
            "10.11.12.22" :0,
            "10.11.12.26" :0,
            "10.11.12.30" :0,
            "10.11.12.34" :0,
            "10.11.12.38" :0,
            "10.11.12.54" :0,
            "10.11.12.58" :0,
            "10.11.12.74" :0,
            "10.11.12.82" :0,
            "10.11.12.90" :0,
            "10.11.12.106":0,
            "10.11.12.138":0,
            "10.11.12.86" :0}

IS_DEAD    = 3           # number of ping before system is set as dead!
CHECK_TIME = 300         # seconds before new check
ALERT_MSG  = 1800        # seconds before new alert msg is sent
STATUS_MSG = 14400       # seconds before new global status msg is sent
STOP_MSG   = IS_DEAD + 6 # number of checks after that to stop alert msg and say "out of order" in status msg
MY_MSG     = "non raggiungibile"

def ping():
  while True:
    for host in systems:
      # do a ping
      # print(f"Ping to {systems[host]}")
      response = os.system("ping -c 1 " + host + " >/dev/null")
      if response == 0:
        # host is alive
        reports[host] = 0
      else:
        # host is not responding
        reports[host] = reports[host] + 1
        if reports[host] >= 1000: reports[host] = 1000 # we can use this setting for future features...
      time.sleep(2)

    # print(reports)
    # wait for other round
    time.sleep(CHECK_TIME)

def alert():
  while True:
    for host in systems:
      if reports[host] > IS_DEAD:
        # print(f"Sendind alert message about {systems[host]} via Telegram Bot\n")
        if reports[host] > STOP_MSG:
          pass # do nothing at the moment
        else:
          os.system(f"sh ./send_bot_msg.sh \"{systems[host]} {MY_MSG}\" >/dev/null")

    # wait for other round
    time.sleep(ALERT_MSG)

def status():
  while True:
    s = f"Systems check:\nIS_DEAD={IS_DEAD}n\nCHECK_TIME={CHECK_TIME}s\nALERT_MSG={ALERT_MSG}s\nSTATUS_MSG={STATUS_MSG}s\nSTOP_MSG={STOP_MSG}n\n\n"
    for host in reports:
      if reports[host] > STOP_MSG:
        s = s + systems[host] + "/UNAVAILABLE\n" # the system is out of order/no network alive
      else:
        s = s + systems[host] + "/" + str(reports[host]*CHECK_TIME) + "s\n"

    os.system(f"sh ./send_bot_msg.sh \"{s}\" >/dev/null")
    # wait for other round
    time.sleep(STATUS_MSG)


# init threads
threading.Thread(target=ping).start()
threading.Thread(target=alert).start()
threading.Thread(target=status).start()

while True:
    time.sleep(2)
