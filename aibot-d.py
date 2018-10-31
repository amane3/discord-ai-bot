#coding:utf-8
import requests
import discord
import os
import json
from datetime import datetime

client = discord.Client()
token = 'XXXXXXXXXXXXXXXXXXX'

apikey = 'XXXXXXXXXXXXXXXXXXXX'
url = endpoint.replace('REGISTER_KEY',apikey)


def ai_response(msg,time = ''):
    payload = {
    'language' : 'ja-JP',
    'appRecvTime' : time,
    'appSendTime' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'voiceText' : msg,
    'botId': 'Chatting',
    'appId':'XXXXXXXXXXXXXXXXXXX'
    } 
    headers = {'Content-type': 'application/json;charset=UTF-8'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    data = r.json()
    response = data['systemText']['expression']
    time = data['serverSendTime']
    return(response)


@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):
    if client.user.id in message.content:
       if client.user != message.author:
          msg = message.content
          msg = msg.lstrip("<XXXXXXXXXXXXXXXXXXXXXX>")       
          response = ai_response(msg)
          reply = response.replace('。','') + 'めう'
          await client.send_message(message.channel,reply)

    

client.run(token)