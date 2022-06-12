# Bot-systems-check
This procedure is for receiving alerts via Telegram if a radio repeater (or other system) is no longer reachable on the internet side.
You need a computer with linux and the python3 language. The systems are checked with the PING command.

First step, create a Telegram Bot:
contact the father of all bots, @BotFather, on telegram.

By typing "/newbot" the BotFather will ask you for a name to assign to your bot, you can use whatever you want. Then you will need to assign them a username that ends with the word "bot", for example:

name: <b>my_control</b>

username: <b>my_control_bot</b>

If everything is available for use, a Token will be communicated (<b>take note!!</b>).

Now you need to create a channel on Telegram, as a type: <b>public</b>. Click on the name of the newly created channel at the top and select administrators, then add administrator.  Add the bot you created just now as a contact by searching for it by typing @my_control_bot for example.

At this point we need to obtain the ID of the channel created, to be used in our script.
Using the Token received before, write in the browser:

http://api.telegram.org/bot<BOT TOKEN>/getUpdates?offset=0

For example the link should become something like this http://api.telegram.org/bot123457:789099345/getUpdates?offset=0

You should land on a page with JSON codes inside, if it says "ok": false it means that you have done something wrong.

Write any message within the channel created in the previous step and reload the page with the link previously composed with the token bot.
If everything went well you will notice that there will be a lot of additional information.
What we need is ID within chat. A series of numbers that will begin with the -. For example -3184917874.
  
  Second step: download the <b>send_bot_msg.sh</b> and <b>check_systems.py</b> files in the same folder on your Linux system and edit the first file by inserting your Bot Token and chat ID. Try sending a test message to the channel:
  
  <b>sh send_bot_msg.sh "test message"</b>
  
If everything has been processed correctly we should have in response a series of information starting with "ok": true and in the channel the message transmitted.
  
  Third step, edit the <b>check_systems.py</b> file in the section that contains the IPs and names of the systems we want to monitor. We can also vary the sending times and number of checks, by acting on the constants:

<b>IS_DEAD</b> = how many PINGs to send before declaring the system dead
  
<b>CHECK_TIME</b> = every how many seconds to send the PING command
  
<b>ALERT_MSG</b> = every how many seconds to send the unreachable system alert
  
<b>STATUS_MSG</b> = how often to send a summary message of all systems being monitored, in seconds
  
<b>STOP_MSG</b> = after how many attempts to stop sending alerts related to that unresponsive system
  
<b>MY_MSG</b> = the warning message
 
  As a last step copy the <b>check_systems.service</b> file in <b>/lib/systemd/system</b> and edit it by setting the right paths. The service can then be started with the command "systemctl start check_systems.service" (use stop to stop it and status to check its operation). To set the service at startup of the Linux system, use the command: "systemctl enable check_systems.service" (disable to remove).
  
  <b>Notice:</b> for our radio repeaters we use a VPN to access them, so every single system has its own IP. PING cannot pass via NAT. However, this solution can be easily extended to understand if there is connectivity on a high-altitude location or if a server is operating on the network side.
  
David ik5xmk@gmail.com
