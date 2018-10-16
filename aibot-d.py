#coding:utf-8
import requests
import discord
import os
import json
from datetime import datetime

client = discord.Client()
token = 'NTAxNzUxNzYwNDI0MDA5NzQw.Dqd8bQ.VL4LkCCqoojc6TJBhBvySPkVakQ'

apikey = '6963576a624d31473343366767302e2f7770753564442e4f5832344c566c524942686b6b755553614c5434'
endpoint = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY=REGISTER_KEY'  
url = endpoint.replace('REGISTER_KEY',apikey)


def ai_response(msg,time = ''):
    payload = {
    'language' : 'ja-JP',
    'appRecvTime' : time,
    'appSendTime' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'voiceText' : msg,
    'botId': 'Chatting',
    'appId':'59f4939f-0d96-40ef-9180-276e0c3b9711'
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
          msg = msg.lstrip("<@501751760424009740>")       
          response = ai_response(msg)
          reply = response.replace('。','') + 'めう'
          await client.send_message(message.channel,reply)

    

client.run(token)