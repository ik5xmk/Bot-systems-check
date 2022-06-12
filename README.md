# Bot-systems-check
Procedure for receiving alerts via Telegram if a radio repeater (or other system) is no longer reachable on the internet side.
==============================================================================================================================

First step, create a Telegram Bot:
contact the father of all bots, @BotFather, on telegram.

By typing "/newbot" the BotFather will ask you for a name to assign to your bot, you can use whatever you want. Then you will need to assign them a username that ends with the word "bot":

example
name: my_control
username: my_control_bot

If everything is available for use, a Token will be communicated (take note!!).

Now you need to create a channel on Telegram, as a type: public. Click on the name of the newly created channel at the top and select administrators, then add administrator.  Add the bot you created just now as a contact by searching for it by typing @my_control_bot for example.

At this point we need to obtain the ID of the channel created, to be used in our script.
Using the Token received before, write in the browser:

http://api.telegram.org/bot<BOT TOKEN>/getUpdates?offset=0

For example the link should become something like this http://api.telegram.org/bot123457:789099345/getUpdates?offset=0

You should land on a page with JSON codes inside, if it says ok: false it means that you have done something wrong.

Write any message within the channel created in the previous step and reload the page with the link previously composed with the token bot.
If everything went well you will notice that there will be a lot of additional information.
What we need is ID within chat. A series of numbers that will begin with the -. For example -3184917874.
