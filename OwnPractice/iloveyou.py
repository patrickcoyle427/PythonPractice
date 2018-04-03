#!/usr/bin/python3

'''
iloveyou.py - Asks for the user's Twilio account SID, AuthToken, the number
              they are texting and the number it is from and sends a text
              message that says 'I love you :)'.

'''

from twilio.rest import Client
import datetime, time

# I have it asking for all the data for 2 reasons:

# 1. it is more secure to have the user enter their info each time.
# 2. The version I wrote that is not on github has my wife's phone number in it
#    and I doubt she wants it online.

accountSID = input('Please enter your account SID: ')
authToken = input('Please enter your authentication token: ')

send_to = input('Please enter the number you are messaging: ')
sent_from = input('Please enter the number you are texting from: ')

clinet = Client(accountSID, authToken)
#Creates an instance of the Client class, used to send the texts.

next_day = datetime.datetime(1, 1, 1)
#Low number so that the script will always text the first time it is run

while True:

    now = datetime.datetime.now()
    #Checks the current time

    if now > next_day:

        client.api.account.messages.create(
            to=send_to,
            from_=sent_from,
            body = 'I love you! :)')

        next_day = now + datetime.timedelta(days=1)
        #Updates next_day so that 1 day from another text will be sent

    time.sleep(3600)
    #Checks every hour
