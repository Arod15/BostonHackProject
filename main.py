from flask import render_template
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import key.py

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=true)


# Your Account SID from twilio.com/console
account_sid = MY_ID
# Your Auth Token from twilio.com/console
auth_token  = AUTH_KEY

client = Client(account_sid, auth_token)

bot_num = "+16672399678"

message = client.messages.create(
        "+15558675309",
        body="Jenny please?! I love you <3",
        from_="+14158141829",
        media_url="http://www.example.com/hearts.png")

print(message.sid)

# Some global variables
age = 0
female = false
male = false
symptoms = []


def sendSMS(text, user): #LOL dont need it Ashley will fix
    message = client.messages.create(
        to=user,
        from_= bot_num,
        body=text)
    print(message.sid)
    return

def background_check(user):
    sendSMS("Hello. First, we must do a quick background check.", user)
    sendSMS("Are you biologically male or female?", user)
    gender_wait = True
    while gender_wait:
        if input().lowercase == "female":
            female = true
            gender_wait = False

        elif input().lowercase == "male":
            male = true
            gender_wait = False

        else:
            sendSMS("Please text \"male\" or \"female\.")
