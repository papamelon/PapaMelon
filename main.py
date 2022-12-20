import discord
from discord.ext import commands
import os
import sys
import urllib.request
import json
import emoji
import asyncio

import cleaning
import slots
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
    # 번역 기능을 위한 코드
    if message.content.startswith("pp 번역 "):
        
        # 번역할 문장 변수 선언
        lan = str(message.content[6:])
        
        # translation.lang 함수에 값 넘기기
        await translation.lang(app, message, lan)

    
    # 슬롯 기능을 위한 코드
    elif message.content.startswith("pp 슬롯"):
        embed=discord.Embed(title="슬롯머신이 돌아갑니다", color=0xed07cf)
        embed.add_field(name="첫번째", value="[ ]", inline=True)
        embed.add_field(name="두번째", value="[ ]", inline=True)
        embed.add_field(name="세번째", value="[ ]", inline=True)
        embed.set_footer(text="papaMelon 슬롯 기능")
        slot = await message.channel.send(embed=embed)

        # slots.slot 함수에 값 넘기기
        await slots.slot(message, slot)


    elif message.content.startswith("pp 청소 "):
        # 청소할 문장 갯수
        amount = str(message.content[6:])

        # cleaning.clean 로 메세지와 청소할 양 넘기기
        await cleaning.clean(message, amount)

# 토큰을 사용하여 봇 실행하기
app.run(TOKEN.DISCORD_BOT_TOKEN)