import os
import random
from twilio.rest import TwilioRestClient
import subprocess
import sys
from time import strftime



# returns 'None' if the key doesn't exist
#TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
#TWILIO_AUTH_TOKEN  = os.environ.get('TWILIO_AUTH_TOKEN')


# Phone numbers
my_number  = ''
to_number = ''

reasons = [
  'Keep coding',
  'Debug it',
  ' Akshay '
]

client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

client.messages.create(
    to=to_number,
    from_=my_number,
    body="Its all messed up. " + random.choice(reasons)
)

print "Message sent at " + strftime("%a, %d %b %Y %H:%M:%S")
