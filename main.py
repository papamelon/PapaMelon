import discord
from discord.ext import commands
import os
import sys
import urllib.request
import json

import translation
import TOKEN
 
intent = discord.Intents.default()
intent.message_content = True

app = commands.Bot(command_prefix='pp ', intents=intent)
 
@app.event
async def on_ready():
    print('Done!')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.event
async def on_message(message):
    if message.content.startswith("pp 번역 "):
        
        lan = str(message.content[6:])
        
        client_id = TOKEN.CLIENT_ID
        client_secret = TOKEN.CLIENT_SECRET
        encQuery = urllib.parse.quote(lan)
        data = "query=" + encQuery
        url = "https://openapi.naver.com/v1/papago/detectLangs"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            answer = json.loads(result)
            print(answer)
            await translation.en_to_kr_translation(message)

app.run(TOKEN.DISCORD_BOT_TOKEN)