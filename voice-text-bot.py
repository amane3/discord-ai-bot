#coding:utf-8
import requests
import feedparser
import discord
from boto3.session import Session
import os

bucket = 'discordbot-sebot' 
key_prefix = '' 

session = Session(
    aws_access_key_id='AKIAJVCIYKAWWUVRF6JQ',
    aws_secret_access_key='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',
    region_name='ap-northeast-1',
)


s3 = session.resource('s3')
for object in s3.Bucket(bucket).objects.all():
    obj = s3.Object(bucket,object.key)
    response = obj.get()
    body = response['Body'].read()
    
    s3.Bucket(bucket).download_file(object.key,object.key)

client = discord.Client()
token = 'NDk5NTk3OTAzMDAyODYxNTg4.DqCwbQ.C-sytFVdbYO3NVCFlturge4Nxgs'

def news():  
  rss_url = "https://news.yahoo.co.jp/pickup/computer/rss.xml"
  
  
  news_dic = feedparser.parse(rss_url)
  titles = ""
  links = ""
  for entry in news_dic.entries:
        titles += entry.title  + ",      ,"
        links += entry.title + "\n" + "<" + entry.link+ ">" + "\n"

  return links


@client.event
async def on_ready():
    print('ログインしました')


voice = None
player = None

@client.event
async def on_message(message):
    global voice, player
    if message.author.bot:
       return
    if message.author.voice_channel is None:
       
       return
    if voice == None:
       voice = await client.join_voice_channel(client.get_channel("263557329507581952"))
    elif(voice.is_connected() == True):
        if player == None:
           return
        if(player.is_playing()):
            player.stop()
        await voice.move_to(message.author.voice_channel)
    if message.content.startswith('!cmd'):
       reply = 'Command List'+'\n'+'\n'+'--japanese meme--'+'\n'+'デデーン:!ddn'+'\n'+'ありがとう:!thx'+'\n'+'おやすみ:!oyasumi'+'\n'+'大丈夫だ、問題ない:!mondainai'+'\n'+'神は言っている:!god'+'\n'+'--INM--'+'\n'+'デデドン:dddn'+'\n'+'ファッ:!fa'+'\n'+'あーもうめちゃくちゃだよ:!mecha'+'\n'+'そうだよ:!soudayo'+'\n'+'やりますねぇ:!yarimasu'+'\n'+'あーおとしちゃった:!otosita'+'\n'+'だめみたいっすね:!dame'+'\n'+'もうゆるさねぇからな:!yurusan'+'\n'+'かしこま:!kasikoma'+'\n'+'\n'+'--english meme--'+'\n'+'Help!!:!help'+'\n'+'GTA:!gta'+'\n'+'You what:!uwhat'+'\n'+'Victory!victory'+'\n'+'Just Do It:!doit'+'\n'+'Shut The Fuck Up:!stfu'+'\n'+'I say wat wat in the butt:!watwatt'+'\n'+'\n'+'--insturmental meme--'+'\n'+'Horn:!horn'+'\n'+'Noisy Violin:!sad'+'\n'+'\n'+'--middle east meme--'+'\n'+'アッラーアクバル:!alak'
       await client.send_message(message.channel,reply)

    if message.content.startswith('!news'):
       reply = news()
  
    if message.content.startswith('!ddn'):
       reply = "デデーン"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player(body)
       player.start()
    
    if message.content.startswith('!thx'):
       reply = "ありがとう"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('thx.wav')
       player.start()

    if message.content.startswith('!oyasumi'):
       reply = "おやすみ"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('oyasumi.wav')
       player.start()
 
    if message.content.startswith('!mondainai'):
       reply = "大丈夫だ、問題ない"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('mondainai.wav')
       player.start()
    
    if message.content.startswith('!god'):
       reply = "神は言っている"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('god.wav')
       player.start()

    if message.content.startswith('!dddn'):
       reply = "デデドン"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('dddn.wav')
       player.start()
    
    if message.content.startswith('!fa'):
       reply = "ファッ"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('fa.mp3')
       player.start()
     
    if message.content.startswith('!mecha'):
       reply = "あーもうめちゃくちゃだよ"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('mecha.wav')
       player.start()
    
    if message.content.startswith('!soudayo'):
       reply = "そうだよ"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('soudayo.wav')
       player.start()
    
    if message.content.startswith('!yarimasu'):
       reply = "やりますねぇ"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('yarimasu.wav')
       player.start()

    if message.content.startswith('!otosita'):
       reply = "あーおとしちゃった"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('otosita.wav')
       player.start()

    if message.content.startswith('!dame'):
       reply = "だめみたいっすね"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('dame.wav')
       player.start()

    if message.content.startswith('!yurusan'):
       reply = "もうゆるさねぇからな"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('yurusan.wav')
       player.start()

    if message.content.startswith('!kasikoma'):
       reply = "かしこま"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('kasikoma.wav')
       player.start()

    if message.content.startswith('!help'):
       reply = "Help!!"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('help.mp3')
       player.start()

    if message.content.startswith('!gta'):
       reply = "GTA"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('gta.mp3')
       player.start()

    if message.content.startswith('!horn'):
       reply = "Horn"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('Horn.mp3')
       player.start()

    if message.content.startswith('!sad'):
       reply = "Noisy Violin"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('sad.mp3')
       player.start()
    
    if message.content.startswith('!uwhat'):
       reply = "You what"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('youwhat.mp3')
       player.start()

    if message.content.startswith('!victory'):
       reply = "victory"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('victory.mp3')
       player.start()

    if message.content.startswith('!alak'):
       reply = "アッラーアクバル"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('alak.mp3')
       player.start()

    if message.content.startswith('!doit'):
       reply = "JUST DO IT"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('doit.mp3')
       player.start()

    if message.content.startswith('!stfu'):
       reply = "SHUT THE FUCK UP"
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('stfu.mp3')
       player.start()
 
    if message.content.startswith('!watwat'):
       reply = "I say wat wat in the butt "
       await client.send_message(message.channel,reply)
       player = voice.create_ffmpeg_player('watwat.mp3')
       player.start()

client.run(token)