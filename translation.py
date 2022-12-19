import discord
import os
import sys
import urllib.request
import TOKEN
import json
import emoji


def reaction_to_emoji(answer_reaction):
    if emoji.demojize(answer_reaction) == emoji.emojize(':flag: United States:'):
        return "en"
    elif emoji.demojize(answer_reaction) == emoji.demojize('🇰🇷'):
        return "ko"
    elif emoji.demojize(answer_reaction) == emoji.demojize('🇯🇵'):
        return "ja"
    elif emoji.demojize(answer_reaction) == emoji.demojize('🇩🇪'):
        return "de"
    elif emoji.demojize(answer_reaction) == emoji.emojize(':flag: China:'):
        return "zh-CN"
    else:
        return "error"

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
        print(emoji.demojize(reaction))

        toCon = reaction_to_emoji(reaction)
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