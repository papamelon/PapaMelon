import discord
from discord.ext import commands
import os
import sys
import urllib.request
import json
import emoji
import asyncio


import helping
import music
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

    elif message.content.startswith("pp 도움말"):
        await helping.helping(message)



    else:
        
        if message.content.startswith("pp 들어와"):
            await music.come(message)

        elif message.content.startswith("pp 나가"):
            await music.나가(message)

        elif message.content.startswith("pp URL재생 "):
            url = str(message.content[9:])
            await music.URL재생(message, url)

        elif message.content.startswith("pp 재생 "):
            name = str(message.content[6:])
            await music.재생(message, name)

        elif message.content.startswith("pp 멜론차트"):
            await music.멜론차트(message)

        elif message.content.startswith("pp 일시정지"):
            await music.일시정지(message)

        elif message.content.startswith("pp 다시재생"):
            await music.다시재생(message)

        elif message.content.startswith("pp 노래끄기"):
            await music.노래끄기(message)
        
        elif message.content.startswith("pp 지금노래"):
            await music.지금노래(message)

        elif message.content.startswith("pp 대기열추가 "):
            name = str(message.content[9:])
            await music.대기열추가(message, name)

        elif message.content.startswith("pp 대기열삭제 "):
            number = str(message.content[9:])
            await music.대기열삭제(message, number)

        elif message.content.startswith("pp 목록초기화"):
            await music.목록초기화(message)

        elif message.content.startswith("pp 목록재생"):
            await music.목록재생(message, app)

        elif message.content.startswith("pp 목록"):
            await music.목록(message)

        elif message.content.startswith("pp 가사 "):
            name = str(message.content[6:])
            await music.가사(message, name)
    

# 토큰을 사용하여 봇 실행하기
app.run(TOKEN.DISCORD_BOT_TOKEN)