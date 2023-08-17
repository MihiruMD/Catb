from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').lower()

    response = MessagingResponse()
    msg = response.message()

    if 'hello' in incoming_msg:
        msg.body("Hi there! How can I help you today?")
    elif 'bye' in incoming_msg:
        msg.body("Goodbye! Have a great day.")
    else:
        msg.body("I'm sorry, I don't understand that.")

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
