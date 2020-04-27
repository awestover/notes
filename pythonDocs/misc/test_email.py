from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME="EMAIL",
    MAIL_PASSWORD="PASSWORD"
)
mail = Mail(app)

@app.route("/")
def index():
    return "<h1>wowwww</h1>"

@app.route('/send-mail/')
def send_mail():
    try:
        msg = Message("Send Mail Tutorial!",
        sender=app.config.get("MAIL_USERNAME"),
        recipients=["alek.westover@gmail.com"])
        msg.body = "This is a second test email. I hope it finds you well."
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return(str(e)) 

if __name__ == "__main__":
    app.run(port="80")

