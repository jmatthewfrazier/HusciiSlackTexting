from twilio.rest import Client
from flask import Flask, request
from flask_slack import Slack

app = Flask(__name__)
slack = Slack(app)
account_sid = "AC036c070d9956779506ebc5c01e3dcb2c"
auth_token = "b4078883c04623b7f15dfd75b92ceba2"

client = Client(account_sid, auth_token)

@app.route('/text', methods=['POST', 'GET'])
def send(**args):
	print(args.get('text'))
	client.messages.create(
		to="+12535145920", from_="+12532011626",
		body="Hello there")
	return args.get('text')

if __name__ == '__main__':
	app.run()