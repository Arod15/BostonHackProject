from flask import render_template
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from key import MY_ID, AUTH_KEY

app = Flask(__name__)

# Your Account SID from twilio.com/console
account_sid = MY_ID
# Your Auth Token from twilio.com/console
auth_token  = AUTH_KEY

client = Client(account_sid, auth_token)

bot_num = "+16672399678"

# Some global variables
year = 0
female = False
male = False
symptoms = []

#def sendSMS(text, user): #LOL dont need it Ashley will fix
#    message = client.messages.create(
#        to=user,
#        from_= bot_num,
#        body=text)
#    print(message.sid)
#    return


@app.route("/", methods=['GET', 'POST'])
def background_check():
    resp = MessagingResponse()
    resp.message("Hello. First, we must do a quick background check.")
    print(str(resp))
    resp.message("Are you biologically male or female?")
    print(str(resp))

    gender_resp = request.values.get('Body', None)

    gender_wait = True
    while gender_wait:
        if gender_resp.toLowercase == "female":
            female = true
            gender_wait = False

        elif gender_resp.toLowercase == "male":
            male = true
            gender_wait = False

        else:
            resp.message("Please text \"male\" or \"female\.")
            print(str(resp))

    resp.message("What year were you born?")
    print(str(resp))


    year_resp = request.values.get('Body', None)

    year_wait = True
    while year_wait:
        if year > 1900:
            year = year_resp
            year_wait = False

        else:
            resp.message("The probability of you being that old is quite low. Please put a more realistic year.")
            print(str(resp))
