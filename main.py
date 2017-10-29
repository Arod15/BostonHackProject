from flask import render_template
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
from key import MY_ID, AUTH_KEY

app = Flask(__name__)
app.secret_key = "test"

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
dicnumb = {}

def sendSMS(text, user): 
    message = client.messages.create(
        to=user,
        from_= bot_num,
        body=text)
    print(message.sid)

# def receiveSMS():
#     message = client.messages() \
#                 .fetch()
#     print(message.body.encode('utf-8'))
#     return message

def check_in_dicnumb(number, message):
    global dicnumb
    if number not in dicnumb.keys():
        dicnumb[number] = [message]
    else:
        dicnumb[number].append(message)

@app.route("/", methods=['GET', 'POST'])
def fullBackgroundCheck():
    counter = session.get('counter', 0)
    counter += 1
    session['counter'] = counter
    fr_num = request.values.get('From', None) # get_number
    init_resp = request.values.get("Body", None) # get_firstmessage
    check_in_dicnumb(fr_num, init_resp)
    sendSMS("Hello. First, we must do a quick background check.", fr_num)
    
    #Function 1: Bio gender
    gender_check()

    #Function 2: Year
    birth_check()    


def gender_check():
    fr_num = request.values.get('From', None) # get_number
    # init_resp = request.values.get("Body", None) # get_firstmessage
    # check_in_dicnumb(fr_num, init_resp) # checks if number is in dict
    # sendSMS("Hello. First, we must do a quick background check.", fr_num)

    # print(str(init_resp))
    # resp = MessagingResponse()

    sendSMS("Are you biologically male or female?", fr_num)
    
    gender_wait = True
    while gender_wait:
        respa = MessagingResponse()
        respa.message()
        print(str(respa) + '\n')
        gender_resp = request.values.get('Body', None)
        return
        if gender_resp.split(" ")[0].lower() == "female":
            female = True
            gender_wait = False

        elif gender_resp.split(" ")[0].lower() == "male":
            male = True
            gender_wait = False

        else:
            sendSMS("Please text \"male\" or \"female.\"", fr_num)
            print(str(resp) + '\n')
    return 


def birth_check():
    fr_num = request.values.get('From', None) # get_number
    init_resp = request.values.get("Body", None) # get_firstmessage
    
    sendSMS("What year were you born?", fr_num)
    year_wait = True
    while year_wait:
        resp = MessagingResponse()
        year_resp = request.values.get('Body', None) #breaks cuz it takes the body of first input
        if int(year_resp) < 1900:
            year = int(year_resp)
            year_wait = False

        else:
            sendSMS("The probability of you being that old is quite low. Please put a more realistic year.", fr_num)
            print(str(resp))
    return

if __name__ == "__main__":
     app.run(debug=True)
# Get phone numbers
# get_numbers = request.values.get("From", None)