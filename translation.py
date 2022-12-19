import discord
import os
import sys
import urllib.request
import TOKEN
import json

async def kr_to_en_translation(message):
        client_id = TOKEN.CLIENT_ID
        client_secret = TOKEN.CLIENT_SECRET

        lan = str(message.content[6:])

        encText = urllib.parse.quote(lan)
        data = "source=ko&target=en&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            answer = json.loads(result)
            await message.channel.send(answer['message']['result']['translatedText'])


async def en_to_kr_translation(message):
        client_id = TOKEN.CLIENT_ID
        client_secret = TOKEN.CLIENT_SECRET

        lan = str(message.content[6:])

        encText = urllib.parse.quote(lan)
        data = "source=en&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            answer = json.loads(result)
            await message.channel.send(answer['message']['result']['translatedText'])