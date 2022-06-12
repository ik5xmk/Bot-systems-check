#!/bin/bash

# set your BOT TOKEN and your CHAT ID number
# if curl is not present, install as "apt install curl"

 curl -s -X POST https://api.telegram.org/bot5594875427:ABHIbYrPlg6bG1D_pxrSqnT01dtCZOGnpIo/sendMessage -d chat_id=-1021453100923 -d text="$1"
