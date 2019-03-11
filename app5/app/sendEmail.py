from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'umairunofficial123@gmail.com'
app.config['MAIL_PASSWORD'] = 'ugnofficial0a0'
#app.config.from_pyfile('D:/FYPNov/NewInstallation/Neo4jData/myproject/app/flask/Lib/site-packages/flask/config.py')

mail = Mail(app) 

@app.route("/mailSend")
def index():
    msg = Message(subject='Invitation by Smart Assistant', 
    	sender='umairunofficial123@gmail.com', recipients=['mrumairbhatti9@gmail.com'])
    msg.body = "testing"
    msg.html = '<p>Hi you have been invited by the membership of Smart Assistant. Please join to have it in your daily life. Regards</p><a href="http://repairwala.pk/">Join Smart Assistant</a>'
    mail.send(msg)
    return 'Message Sent!'

if __name__=='__main__':
	app.run(debug=True)
