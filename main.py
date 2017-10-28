from flask import render_template
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=true)



# Your Account SID from twilio.com/console
account_sid = "AC0dba325e11f49a8384fe1d9cf7e237e5"
# Your Auth Token from twilio.com/console
auth_token  = "1c1002ab99bb77ca50c9adb69a121683"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16672399678",
    from_="+14108183657",
    body="Hello from Python!")

print(message.sid)
