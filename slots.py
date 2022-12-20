import discord
import os
import sys
import urllib.request
import TOKEN
import asyncio

import random

# 채널에 보낸 메시지를 인자로 받는 slot 함수
async def slot(message, slot):
    
    emoji_list = ['🍓', '🍒', '🥕', '🍎', '🍌', '7️⃣']

    choice1 = random.choice(emoji_list)
    choice2 = random.choice(emoji_list)
    choice3 = random.choice(emoji_list)

    def create_embed(ch1, ch2, ch3):
        embed = discord.Embed(title="💰 슬롯머신이 돌아갑니다", color=0xed07cf)
        embed.add_field(name="첫번째", value="[ "+ch1+" ]", inline=True)
        embed.add_field(name="두번째", value="[ "+ch2+" ]", inline=True)
        embed.add_field(name="세번째", value="[ "+ch3+" ]", inline=True)
        embed.set_footer(text="papaMelon 슬롯 기능")
        return embed

    await asyncio.sleep(1.5)

    embed1 = create_embed(choice1, "", "")
    await slot.edit(embed=embed1)
    await asyncio.sleep(1.5)

    embed2 = create_embed(choice1, choice2, "")
    await slot.edit(embed=embed2)
    await asyncio.sleep(1.5)

    embed3 = create_embed(choice1, choice2, choice3)
    await slot.edit(embed=embed3)
    await asyncio.sleep(1.5)

    fail_embed=discord.Embed(title="💣 꽝", description="맞은게 하나도 없네요..", color=0xed0707)
    fail_embed.set_footer(text="papaMelon 슬롯 기능")

    double_embed=discord.Embed(title="💵 더블", description="2개 맞았어요.", color=0xfff700)
    double_embed.set_footer(text="papaMelon 슬롯 기능")

    success_embed=discord.Embed(title="💎 당첨", description="3개 전부 맞았어요!!", color=0x00e1ff)
    success_embed.set_footer(text="papaMelon 슬롯 기능")

    if choice1 == choice2 == choice3:
        await message.channel.send(embed=success_embed)
    elif choice1 == choice2:
        await message.channel.send(embed=double_embed)
    elif choice1 == choice3:
        await message.channel.send(embed=double_embed)
    elif choice2 == choice3:
        await message.channel.send(embed=double_embed)
    else:
        await message.channel.send(embed=fail_embed)