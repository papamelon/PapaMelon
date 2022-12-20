import discord
import os
import sys
import urllib.request
import TOKEN
import asyncio

from fun_ment import funny_ment

import random

async def funny_chat(message, app):
    # rand_ment[0] 은 문제, rand_ment[1] 은 문제에 대한 정답
    rand_ment = random.choice(list(funny_ment.items()))

    # 문제 출제
    embed=discord.Embed(title="아재개그", description=rand_ment[0], color=0x00ffcc)
    embed.set_footer(text="papaMelon 아재개그 기능")
    await message.channel.send(embed=embed)

    # pp 아재개그 친 사람이 답장하는지 확인, 같은 채널인지 확인
    def check(m):
        return m.author == message.author and m.channel == message.channel

    # message 이벤트가 발생할때까지 wait
    try:
        msg = await app.wait_for('message', check=check, timeout=30.0)
        
    # 시간초과 시 예외처리
    except asyncio.TimeoutError:
        embed=discord.Embed(title="시간초과", description="정답은 "+rand_ment[1]+" 입니다.", color=0xff0000)
        embed.set_footer(text="papaMelon 아재개그 기능")
        await message.channel.send(embed=embed)

    # 사용자가 입력시 실행
    else:
        # 정답이랑 입력이랑 같다면 실행할 문장
        if msg.content == rand_ment[1]:
            embed=discord.Embed(title="정답을 정확히 맞추셨네요!", description="정답은 "+rand_ment[1]+" 입니다.", color=0x04ff00)
            embed.set_footer(text="papaMelon 아재개그 기능")
            await message.channel.send(embed=embed)

        # 정답이랑 입력이 다를시 실행할 문장
        else:
            embed=discord.Embed(title="틀렸습니다.", description="정답은 "+rand_ment[1]+" 입니다.", color=0xff0000)
            embed.set_footer(text="papaMelon 아재개그 기능")
            await message.channel.send(embed=embed)