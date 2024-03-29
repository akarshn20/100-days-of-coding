import os
from twilio.rest import Client

TWILIO_SID = os.environ.get('APP_SID')
TWILIO_AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = "+15642444257"
TWILIO_VERIFIED_NUMBER = "+919606366222"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )

        print(message.sid)

