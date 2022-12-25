import discord
from discord.ext import commands
import os
import sys
import urllib.request
import json
import emoji
import asyncio

from . import music
from . import school_eat
from . import funny
from . import cleaning
from . import slots
from . import translation
from . import TOKEN
 
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



    else:
        user = [] #유저가 입력한 노래 저장하는 배열
        musictitle = [] #넌 노래들의 노래 제목
        song_queue = [] #넌 노래들의 링크
        musicnow = [] #현재 출력되는 노래

        userF = [] #유저의 정보를 저장하느 배열
        userFlist = [] #유저 개인별 노래저장하는 배열
        allplaylist = [] #플레이리스트 배열
        
        if message.content.startswith("pp 들어와"):
            await music.come(message)

        elif message.content.startswith("pp 나가"):
            await music.나가(message)

        elif message.content.startswith("pp URL 재생 "):
            url = str(message.content[10:])
            await music.URL재생(message, url)

        elif message.content.startswith("pp 재생 "):
            name = str(message.content[6:])
            await music.재생(message, name, musicnow, user, musictitle, song_queue)

        elif message.content.startswith("pp 멜론차트"):
            await music.멜론차트(message)

        elif message.content.startswith("pp 일시정지"):
            await music.일시정지(message, musicnow)

        elif message.content.startswith("pp 다시재생"):
            await music.다시재생(message, musicnow)

        elif message.content.startswith("pp 노래끄기"):
            await music.노래끄기(message, musicnow)
        
        elif message.content.startswith("pp 지금노래"):
            await music.지금노래(message, musicnow)

        elif message.content.startswith("pp 대기열추가 "):
            name = str(message.content[9:])
            await music.대기열추가(message, name, user, musictitle, musicnow, song_queue)

        elif message.content.startswith("pp 대기열삭제 "):
            number = str(message.content[9:])
            await music.대기열삭제(message, number, musicnow, user, musictitle, song_queue)

        elif message.content.startswith("pp 목록"):
            await music.목록(message, musictitle)

        elif message.content.startswith("pp 목록초기화"):
            await music.목록초기화(message, musicnow, user, musictitle, song_queue)

        elif message.content.startswith("pp 목록재생"):
            await music.목록재생(message, user, musicnow, song_queue, musictitle, app)

        elif message.content.startswith("pp 가사 "):
            name = str(message.content[6:])
            await music.가사(message, name)
    

# 토큰을 사용하여 봇 실행하기
app.run(TOKEN.DISCORD_BOT_TOKEN)