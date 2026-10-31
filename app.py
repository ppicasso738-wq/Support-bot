
import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "WhatsApp AI Bot is alive!"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if (
            mode == "subscribe"
            and token == os.environ.get("VERIFY_TOKEN")
        ):
            return challenge, 200

        return "Verification failed", 403

    data = request.get_json(silent=True)
    print("Incoming WhatsApp webhook:", data)

    return "EVENT_RECEIVED", 200
