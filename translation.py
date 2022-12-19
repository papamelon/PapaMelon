import discord
import os
import sys
import urllib.request
import TOKEN
import json
import emoji


# def reaction_to_emoji(answer_reaction):
#     answer_emoji = emoji.demojize(answer_reaction)
#     print(answer_emoji)
#     if answer_emoji == emoji.demojize('🇰🇷'):
#         return "ko"
#     elif answer_emoji == emoji.demojize('🇺🇸'):
#         return "en"
#     elif answer_emoji == emoji.demojize('🇨🇳'):
#         return "zh-CN"
#     elif answer_emoji == emoji.demojize('🇯🇵'):
#         return "ja"
#     elif answer_emoji == emoji.demojize('🇩🇪'):
#         return "de"
#     else:
#         return "error"

# 들어온 메세지, 감지된 언어, 바꿀 언어가 함수의 인자로 들어옴
async def translation(message, result, reaction):
        # Papago OpenAPI 셋업
        client_id = TOKEN.CLIENT_ID
        client_secret = TOKEN.CLIENT_SECRET

        # 번역할 문장 변수 선언
        lan = str(message.content[6:])

        # 감지된 언어 코드 (ex: ko, en ..)
        lang = str(result['langCode'])

        encText = urllib.parse.quote(lan)
        
        print(lang, reaction)

        toCon = ""

        if reaction == "🇰🇷":
            toCon = "ko"
        elif reaction == "🇺🇸":
            toCon = "en"
        elif reaction == "🇯🇵":
            toCon = "ja"
        elif reaction == "🇨🇳":
            toCon = "zh-CN"
        elif reaction == "🇩🇪":
            toCon = "de"
        else:
            toCon = "error"

        print(toCon)

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
            await message.channel.send(answer['message']['result']['translatedText'])