from twilio.rest import Client
import os

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC3164c98a567b2204823bf77cd674d481'
auth_token = 'c60d3e1bd3439b7c15466c320e30cdd4'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello, this is Dr. Banh's office. Please reply with a number from the following options \n 1 - Make an Appointment \n 2 - Cancel an appointment \n 3 - Check time and date of appointment\n 4 - Speak to a represenative ",
                     from_='+12562861625',
                     to='+14153162408'
                 )



print(message.sid)