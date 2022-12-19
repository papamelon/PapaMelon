import discord
from discord.ext import commands
import os
import sys
import urllib.request
import json
import emoji
import asyncio

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
        
        # 번역할 문장 변수 선언
        lan = str(message.content[6:])
        
        # Papago OpenAPI 사용 문장
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
            lang = json.loads(result)

            # 번역할 타겟 언어 선택
            response = await message.channel.send("문장을 어떤 언어로 번역 하시겠습니까?")
            await response.add_reaction("🇰🇷")
            await response.add_reaction("🇺🇸")
            await response.add_reaction("🇯🇵")
            await response.add_reaction("🇨🇳")
            await response.add_reaction("🇩🇪")

            try:
                def check(reaction, user):
                    return str(reaction) in ['🇰🇷', '🇺🇸', '🇯🇵', '🇨🇳', '🇩🇪'] and \
                    user == message.author and reaction.message.id == response.id
                    
                reaction, user = await app.wait_for('reaction_add', check=check, timeout=30.0)
            except asyncio.TimeoutError:
                await message.channel.send("너무 반응이 오래걸려요.")
                await response.delete()
            else:
                await translation.translation(message, lang, reaction)
                await response.delete()

app.run(TOKEN.DISCORD_BOT_TOKEN)