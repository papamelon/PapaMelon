import discord
import os
import sys
import urllib.request
import TOKEN
import asyncio

async def clean(message, amount):

    # 디스코드 서버 채널 관리자(administrator) 권한을 갖고있는 사람만 청소 가능
    if message.author.guild_permissions.administrator:
        await message.delete()
        await message.channel.purge(limit=int(amount))

        embed=discord.Embed(title="🧹 청소 성공", description=amount+" 개의 메세지가 삭제되었습니다.", color=0x04ff00)
        embed.add_field(name="청소한 사람", value=message.author, inline=False)
        embed.set_footer(text="papaMelon 청소 기능")
        await message.channel.send(embed=embed)
        

    # 메시지 보낸사람이 관리자가 아닐경우 청소 실패
    else:
        embed=discord.Embed(title="❌ 청소 실패", description="관리자 권한이 없어서 청소를 할수 없어요", color=0xff0000)
        embed.set_footer(text="papaMelon 청소 기능")
        await message.channel.send(embed=embed)
