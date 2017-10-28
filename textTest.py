from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse, Message

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = MessagingResponse()
    resp.message("Hi Janice!")

    return str(resp)

if __name__ == "__main__":
	app.run(debug=True)