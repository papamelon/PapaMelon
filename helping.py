import discord
import os
import sys
import urllib.request
import TOKEN
import asyncio

async def helping(message):
    embed=discord.Embed(title="PapaMelon 기능 설명", description="papamelon 도움말", color=0x00ff04)
    embed.add_field(name="pp 번역 [ 번역할 문장 ]", value="입력한 문장을 선택 언어로 번역 해줍니다", inline=True)
    embed.add_field(name="pp 슬롯", value="슬롯을 돌립니다", inline=True)
    embed.add_field(name="pp 청소 [ 문장 갯수 ]", value="입력한 수만큼 채널의 메세지를 삭제합니다", inline=True)
    embed.add_field(name="pp 아재개그", value="봇이 문제를 출제하고 정답을 맞춰야합니다", inline=True)
    embed.add_field(name="pp 급식 [ 학교 이름 ]", value="입력한 학교의 하루 급식을 알려줍니다", inline=True)
    embed.add_field(name="pp 도움말", value="papaMelon 사용법을 알려줍니다", inline=True)
    embed.add_field(name="pp 들어와", value="봇이 사용자가 참가한 음성채팅방에 참가합니다", inline=True)
    embed.add_field(name="pp 나가", value="봇이 음성채팅방을 나갑니다", inline=True)
    embed.add_field(name="pp 재생 [ 노래이름 ]", value="입력한 노래를 재생합니다", inline=True)
    embed.add_field(name="pp URL재생 [ URL ]", value="입력한 URL을 재생합니다", inline=True)
    embed.add_field(name="pp 멜론차트", value="멜론차트를 재생합니다", inline=True)
    embed.add_field(name="pp 일시정지", value="음악을 일시정지 합니다", inline=True)
    embed.add_field(name="pp 다시재생", value="음악을 다시 재생 합니다", inline=True)
    embed.add_field(name="pp 노래끄기", value="재생중인 음악을 끕니다", inline=True)
    embed.add_field(name="pp 지금노래", value="지금 재생중인 노래의 이름을 알려줍니다", inline=True)
    embed.add_field(name="pp 대기열추가 [ 제목 ]", value="입력한 노래를 대기열에 추가합니다", inline=True)
    embed.add_field(name="pp 대기열삭제 [ 순서 ]", value="입력한 순서의 대기열을 삭제합니다", inline=True)
    embed.add_field(name="pp 목록초기화", value="대기열을 초기화 합니다", inline=True)
    embed.add_field(name="pp 목록재생", value="대기열을 재생합니다", inline=True)
    embed.add_field(name="pp 목록", value="대기열을 전부 알려줍니다", inline=True)
    embed.add_field(name="pp 가사 [ 노래 이름 ]", value="입력한 노래의 가사를 알려줍니다", inline=True)
    embed.set_footer(text="papaMelon 기능 설명")
    await message.channel.send(embed=embed)