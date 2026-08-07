import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, jsonify

app = Flask(__name__)

# Configuration for email
SENDER_EMAIL = "Rtepess2@gmail.com"
APP_PASSWORD = "uuctqjuiftdumicm"
RECIPIENT = "S_shaharkhan@outlook.com"

def send_test_email():
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT
    msg['Subject'] = "Render Web Command Dispatch"
    msg.attach(MIMEText("Hello from your cloud-hosted AI command link!", 'plain'))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT, msg.as_string())

@app.route("/")
def home():
    return jsonify({"status": "AI is online and ready for commands!"})

@app.route("/send-mail")
def trigger_email():
    try:
        send_test_email()
        return jsonify({"success": True, "message": "Email sent successfully!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
