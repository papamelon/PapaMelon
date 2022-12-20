from urllib.error import HTTPError
import discord
import os
import sys
import urllib.request
import TOKEN
import json
import emoji
import asyncio

async def lang(app, message, lang):

        # Papago OpenAPI 사용 문장
        client_id = TOKEN.CLIENT_ID
        client_secret = TOKEN.CLIENT_SECRET
        encQuery = urllib.parse.quote(lang)
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
            embed=discord.Embed(title="🌐 문장을 어떤 언어로 번역 하시겠습니까?", color=0x0a11e6)
            embed.set_footer(text="papaMelon 번역 기능") 
            response = await message.channel.send(embed=embed)
            await response.add_reaction("🇰🇷")
            await response.add_reaction("🇺🇸")
            await response.add_reaction("🇯🇵")
            await response.add_reaction("🇨🇳")
            await response.add_reaction("🇩🇪")
            await response.add_reaction("🇫🇷")
            await response.add_reaction("🇮🇹")
            await response.add_reaction("🇪🇸")
            await response.add_reaction("🇵🇹")

            try:
                def check(reaction, user):
                    return str(reaction) in ['🇰🇷', '🇺🇸', '🇯🇵', '🇨🇳', '🇩🇪', '🇫🇷', '🇮🇹', '🇪🇸', '🇵🇹'] and \
                    user == message.author and reaction.message.id == response.id

                reaction, user = await app.wait_for('reaction_add', check=check, timeout=30.0)
            except asyncio.TimeoutError:
                embed=discord.Embed(title="⏱️ 반응 입력 시간이 초과되었습니다.", color=0xe60a0a)
                embed.set_footer(text="papaMelon 번역 기능")
                await message.channel.send(embed=embed) 
                await response.delete()
            else:
                await translation(message, lang, reaction)
                await response.delete()


# 들어온 메세지, 감지된 언어, 바꿀 언어가 함수의 인자로 들어옴
async def translation(message, result, reaction):
    # 예외처리를 위한 트라이무 구문
    try:
        # Papago OpenAPI 셋업
        client_id = TOKEN.CLIENT_ID
        client_secret = TOKEN.CLIENT_SECRET

        # 번역할 문장 변수 선언
        lan = str(message.content[6:])

        # 감지된 언어 코드 (ex: ko, en ..)
        lang = str(result['langCode'])

        encText = urllib.parse.quote(lan)

        toCon = ""

        # 사용자가 적은 문장을 이모지 이름으로 변환
        reaction_emoji = str(reaction)

        # 이모지에 대응 되는 국가 코드
        contury = {
            "🇰🇷" : "ko",
            "🇺🇸" : "en",
            "🇯🇵" : "ja",
            "🇨🇳" : "zh-CN",
            "🇩🇪" : "de",
            "🇵🇹" : "pt",
            "🇪🇸" : "es",
            "🇮🇹" : "it",
            "🇫🇷" : "fr"
        }

        # 누른 이모지 반응에 따라 toCon에 다른 값 저장
        for key in contury.keys():
            if reaction_emoji == key:
                toCon = contury[key]

        # source 와 target 이 동일하면 오류가 발생하기 때문에 예외 처리
        if lang == toCon:
            embed=discord.Embed(title="🚫 언어가 동일하여 번역 할 수 없습니다.", color=0xe60a0a)
            embed.set_footer(text="papaMelon 번역 기능")
            await message.channel.send(embed=embed) 

        else: 
            data = "source=" + lang + "&target=" + toCon + "&text=" + encText
            
            url = "https://openapi.naver.com/v1/papago/n2mt"

            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id",client_id)
            request.add_header("X-Naver-Client-Secret",client_secret)
            response = urllib.request.urlopen(request, data=data.encode("utf-8"))
            rescode = response.getcode()
            if(rescode==200):
                response_body = response.read()
                trans = response_body.decode('utf-8')
                answer = json.loads(trans)
                embed=discord.Embed(title="📜 번역결과", color=0x1fea37)
                embed.add_field(name="번역할 문장", value=lan, inline=False)
                embed.add_field(name="번역된 문장", value=answer['message']['result']['translatedText'], inline=True)
                embed.set_footer(text="papaMelon 번역 기능")
                await message.channel.send(embed=embed)

    # 잘못된 형식의 문장 예외처리
    except HTTPError:
        embed=discord.Embed(title="🚫 문장의 형식이 잘못되었습니다.", color=0xe60a0a)
        embed.set_footer(text="papaMelon 번역 기능")
        await message.channel.send(embed=embed)