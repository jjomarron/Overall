from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pathlib import Path
import os

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def command():
    number = request.form['From']
    message_body = request.form['Body']
    action = message_body.split()[0]
    response = 'command '+ action + ' executed'

    if action.lower()== '14u':
        txt = Path('C:\\Users\\Jack\\Documents\\Work\\Chicago Stars\\Python.Line Up\\14u.txt').read_text()
        response=txt

    elif action.lower()== 'job2':
        command = "/usr/bin/python3 ~/scripts/job2.py"
        os.popen(command)

    else:
        response = "Invalid Request"

    resp = MessagingResponse()
    resp.message(response)
    return str(resp)

if __name__ == '__main__':
    app.run()
