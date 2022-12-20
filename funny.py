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

    print(rand_ment)

    # 문제 출제
    await message.channel.send(rand_ment[0])

    def check(m):
        return m.author == message.author and m.channel == message.channel

    try:
        msg = await app.wait_for('message', check=check, timeout=30.0)

    except asyncio.TimeoutError:
        await message.send("정답은 "+rand_ment[1]+" 입니다.")
        
    else:
        if msg.content == rand_ment[1]:
            await message.channel.send("정답입니다!")
        else:
            await message.channel.send("틀렸습니다.. 정답은 "+rand_ment[1]+" 입니다.")