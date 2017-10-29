from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    resp = MessagingResponse()
    
    msg=resp.message(str(client.messages.list()))
    #msg.media("https://assets-auto.rbl.ms/13273cc2f3968434cec2e5a95ff8e334d7d2d83e342f1a7bce298921eda06399")
    return str(resp)



if __name__ == "__main__":
	app.run(debug=True)