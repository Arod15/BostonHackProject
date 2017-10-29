from flask import render_template
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from key import MY_ID, AUTH_KEY

app = Flask(__name__)
app.secret_key = "test"

# @app.route("/")
# def homepage():
#     return render_template("index.html")
# if __name__ == "__main__":
#     app.run(debug=True)




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

def sendSMS(text, user): #LOL dont need it Ashley will fix
    message = client.messages.create(
        to=user,
        from_= bot_num,
        body=text)
    print(message.sid)
    resp = MessagingResponse()
    resp.message(message)
    return str(resp)


@app.route("/", methods=['GET', 'POST'])
def background_check():
    counter = session.get('counter', 0)
    counter += 1

    session['counter'] = counter

    resp = MessagingResponse()
    fr_num = request.values.get('From', None)
    sendSMS("Hello. First, we must do a quick background check.", fr_num)
    
    sendSMS("Are you biologically male or female?", fr_num)
    

    gender_wait = True
    while gender_wait:
        resp = MessagingResponse()
        gender_resp = request.values.get('Body', None)
        if gender_resp.lower() == "female":
            female = True
            gender_wait = False

        elif gender_resp.lower() == "male":
            male = True
            gender_wait = False

        else:
            resp = MessagingResponse()
            resp.message("Please text \"male\" or \"female\.")
            print(str(resp))

    resp = MessagingResponse()
    sendSMS("What year were you born?", fr_num)
    print(str(resp))

    year_wait = True
    while year_wait:
        resp = MessagingResponse()
        year_resp = request.values.get('Body', None)
        if int(year_resp) > 1900:
            year = int(year_resp)
            year_wait = False

        else:
            resp = MessagingResponse()
            resp.message("The probability of you being that old is quite low. Please put a more realistic year.")
            print(str(resp))

if __name__ == "__main__":
     app.run(debug=True)
