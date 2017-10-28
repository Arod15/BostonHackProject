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

# Some global variables
year = 0
female = false
male = false
symptoms = []

#def sendSMS(text, user): #LOL dont need it Ashley will fix
#    message = client.messages.create(
#        to=user,
#        from_= bot_num,
#        body=text)
#    print(message.sid)
#    return


@app.route("/sms", methods=['GET', 'POST'])
def background_check():
    resp = MessagingResponse()
    resp.message("Hello. First, we must do a quick background check.")
    resp.message("Are you biologically male or female?")

    gender_resp = request.values.get('Body', None)

    gender_wait = True
    while gender_wait:
        if body.lowercase == "female":
            female = true
            gender_wait = False

        elif body.lowercase == "male":
            male = true
            gender_wait = False

        else:
            resp.message("Please text \"male\" or \"female\.")

    resp.message("What year were you born?")

    year_resp = request.values.get('Body', None)

    year_wait = True
    while year_wait:
        if year > 1900:
            year = year_resp
            year_wait = False

        else:
            resp.message("The probability of you being that old is quite low. Please put a more realistic year.")
