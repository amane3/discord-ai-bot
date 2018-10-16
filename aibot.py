#coding:utf-8
import requests
import discord
import os
import pya3rt


client = discord.Client()
token = 'NTAxNzUxNzYwNDI0MDA5NzQw.Dqd8bQ.VL4LkCCqoojc6TJBhBvySPkVakQ'

apikey = 'DZZ8NihF7ve85p7bO0SeEnLeUoNarw5b'
url = 'https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk'  
ai_response = pya3rt.TalkClient(apikey)
   

@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):
    if client.user.id in message.content:
       if client.user != message.author:
          msg = message.content
          msg = msg.lstrip("<@501751760424009740>")       
          response = ai_response.talk(msg)
          reply = response['results'][0]['reply'] + 'めう'
          await client.send_message(message.channel,reply)

    
    

client.run(token)