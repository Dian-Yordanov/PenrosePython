__author__ = 'zyan'
# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC53d28f419faa0e6571046b8db0629e0b"
auth_token  = "a95329d734fcda0a20da363743dd37bc"
client = TwilioRestClient(account_sid, auth_token)

sms = client.sms.messages.create(body="Jenny please?! I love you <3",
    to="+4407479265143",
    from_="+441163262195")
print sms.sid