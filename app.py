from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])




def incoming_sms():

    user_reply = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()
    options = {'1':"Hello, please reply with your full name, date and time", '2': "Please reply with your full name", '3': "Please reply with your name", '4': "Sorry there are not represenatives available to talk" }

    # Determine the right reply for this message
    try:
        resp.message(options[user_reply])
    except:
        print("user did not choose correctly")
        resp.message("Please reply from one of the options")


    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
