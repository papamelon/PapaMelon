import discord
from discord.ext import commands
import os
import sys
import urllib.request
import json
import emoji
import asyncio

import school_eat
import funny
import cleaning
import slots
import translation
import TOKEN
 
intent = discord.Intents.default()
intent.message_content = True

app = commands.Bot(command_prefix='pp ', intents=intent)
 
# 봇이 준비되면 실행할 문장들
@app.event
async def on_ready():
    print('Done!')
    await app.change_presence(status=discord.Status.online, activity=None)


# 메시지 이벤트 발생시
@app.event
async def on_message(message):
    # 번역 기능을 위한 코드
    if message.content.startswith("pp 번역 "):
        
        # 번역할 문장 변수 선언
        lan = str(message.content[6:])
        
        # translation.lang 함수에 값 넘기기
        await translation.lang(app, message, lan)

    
    # 슬롯 기능을 위한 코드
    elif message.content.startswith("pp 슬롯"):

        # slots.slot 함수에 값 넘기기
        await slots.slot(message)


    # 청소 기능을 위한 코드
    elif message.content.startswith("pp 청소 "):
        # 청소할 문장 갯수
        amount = str(message.content[6:])

        # cleaning.clean 로 메세지와 청소할 양 넘기기
        await cleaning.clean(message, amount)


    # 아재개그 기능을 위한 코드
    elif message.content.startswith("pp 아재개그"):
        await funny.funny_chat(message, app)


    elif message.content.startswith("pp 급식 "):
        # 학교 이름 저장할 변수
        text = str(message.content[6:])

        # school_eat에 eat 함수에 학교이름과 메시지 넘겨주기
        await school_eat.eat(message, text)

# 토큰을 사용하여 봇 실행하기
app.run(TOKEN.DISCORD_BOT_TOKEN)