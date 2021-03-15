# SMS Trigger Overview
This project originally came out of my Youth Baseball project and the desire for each coach to be able to access their own lineup and pitcher info quickly and without my oversight. As it is a part time job, I know that I will not always be accessible when the coaches want their data. The more I could automate the process, the less it would rely on me and the better the organization could be!

## Inspiration/Foundation
Ultimately, this code borrowed heavily from Javed Shaikh's informative [blog post](https://shaikhu.com/how-to-trigger-a-job-or-program-from-anywhere-with-a-sms). A million thanks to him for sharing his expertise. My departures from his code were just personalizing it to my own needs but ultimately this was the most complete explanation I found to devise an SMS trigger for a Python script without paying extra for a platform like WayScript.

## Initial Idea and Adjustment
At first, I had wanted to my Twilio number to receive a SMS, trigger the code, and reply with the recently generated lineup and pitch info (refer to [previous section](WebScrape.md) to understand how the statistics were updated). I had originally called the statistic calculation file to import the appropriate string variable which would run the statistic calculation code completely. If I provided an incorrect trigger, I my loop would run correctly and I would receive the 'Invalid Request' reply. But if I provided the correct trigger ('14u'), I would see the code run successfully on my computer but not receive a text back nor the 200 OK response in the ngrok terminal. After some helpful Reddit consultations, I found the Twilio logs and discoverd that they have a 15 second timeout. I adjusted my expectations and realized that I could run the code nightly and save the string I wanted to send locally. The script could then access the local text quickly and provide the coaches with the same information much more quickly and efficiently than if I reran the original statistic recalculation code every SMS trigger.  

## Code
Here is my working code which accesses a locally saved file and quickly sends a game ready lineup and pitcher information to the coach. 
```
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

```
Here you can see the final result (certain information blocked out to protect identities):
![image](https://user-images.githubusercontent.com/80477575/111109312-8581e280-8528-11eb-939e-da981cda2a1d.png)


## Moving Forward
* I am looking forward to building a server where I can house my codes and trigger all my Python scripts remotely through SMS
* I need to add elif commands for each script (each youth baseball team, fantasy soccer teams, etc.)
