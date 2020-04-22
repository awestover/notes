from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME="username@gmail.com",
    MAIL_PASSWORD="EMAIL PASSWORD DONT FREAKING PUT A PASSWORD HERE AND THEN PUSH TO GITHUB THAT WOULD BE SO DUMB"
)
mail = Mail(app)

@app.route('/send-mail/')
def send_mail():
    try:
        msg = Message("Send Mail Tutorial!",
        sender="username@gmail.com",
        recipients=["otherusername@gmail.com"])
        msg.body = "This is a second test email. I hope it finds you well."
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return(str(e)) 

if __name__ == "__main__":
    app.run()

