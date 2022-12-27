import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import time
import asyncio
import bs4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
from webdriver_manager.chrome import ChromeDriverManager
import lxml
import ffmpeg

user = [] #유저가 입력한 노래 저장하는 배열
musictitle = [] #넌 노래들의 노래 제목
song_queue = [] #넌 노래들의 링크
musicnow = [] #현재 출력되는 노래

userF = [] #유저의 정보를 저장하느 배열
userFlist = [] #유저 개인별 노래저장하는 배열
allplaylist = [] #플레이리스트 배열

def title(msg, musictitle, musicnow):
    global music

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    chromedriver_dir = "/Users/junho/Documents/python-project/chromedriver"
    driver = webdriver.Chrome(chromedriver_dir, options=options)
    driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
    source = driver.page_source
    bs = bs4.BeautifulSoup(source, 'lxml')
    entire = bs.find_all('a', {'id': 'video-title'})
    entireNum = entire[0]
    music = entireNum.text.strip()
    
    musictitle.append(music)
    musicnow.append(music)
    test1 = entireNum.get('href')
    url = 'https://www.youtube.com'+test1
    with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']

    driver.quit()
    
    return music, URL


def play(ctx, musicnow, song_queue, user, musictitle, app):
    global vc
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    URL = song_queue[0]
    del user[0]
    del musictitle[0]
    del song_queue[0]
    vc = get(app.voice_clients, guild=ctx.guild)
    if not vc.is_playing():
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx, musicnow, user, song_queue, musictitle)) 

def play_next(ctx, musicnow, user, song_queue, musictitle):
    if len(musicnow) - len(user) >= 2:
        for i in range(len(musicnow) - len(user) - 1):
            del musicnow[0]
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if len(user) >= 1:
        if not vc.is_playing():
            del musicnow[0]
            URL = song_queue[0]
            del user[0]
            del musictitle[0]
            del song_queue[0]
            vc.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS), after=lambda e: play_next(ctx, musicnow, song_queue, user, musictitle))


async def come(message):
    try:
        global vc
        vc = await message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(message.author.voice.channel)
        except:
            await message.channel.send("채널에 유저가 접속해있지 않네요.")


async def 나가(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send("이미 그 채널에 속해있지 않아요.")


async def URL재생(message, url):
    try:
        global vc
        vc = await message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(message.author.voice.channel)
        except:
            await message.channel.send("채널에 유저가 접속해있지 않네요.")


    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await message.channel.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + url + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    else:
        await message.channel.send("노래가 이미 재생되고 있습니다!")


async def 재생(message, msg, musicnow, user, musictitle, song_queue):

    global vc

    try:
        global vc
        vc = await message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(message.author.voice.channel)
        except:
            await message.channel.send("채널에 유저가 접속해있지 않네요.")


    if not vc.is_playing():
        waiting_message = await message.channel.send(embed = discord.Embed(title= "노래 재생 시도", description = "현재 " + msg + "을(를) 재생 시도중", color = 0x00ff00))
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromedriver_dir = "/Users/junho/Documents/python-project/chromedriver"
        driver = webdriver.Chrome(chromedriver_dir, options=options)
        driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()

        musicnow.insert(0, entireText)
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await waiting_message.edit(embed = discord.Embed(title= "노래 재생", description = "현재 " + musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after = lambda e: play_next(message, musicnow, song_queue, user, musictitle))
    else:
        user.append(msg)
        result, URLTEST = title(msg, musictitle, musicnow)
        song_queue.append(URLTEST)
        await message.channel.send("이미 노래가 재생 중이라" + result + "을(를) 대기열로 추가시켰어요!")


async def 멜론차트(message):
    if not vc.is_playing():
        
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromedriver_dir = "/Users/junho/Documents/python-project/chromedriver"
        driver = webdriver.Chrome(chromedriver_dir, options=options)
        driver.get("https://www.youtube.com/results?search_query=멜론차트")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await message.channel.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await message.channel.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")


async def 일시정지(message, musicnow):
    if vc.is_playing():
        vc.pause()
        await message.channel.send(embed = discord.Embed(title= "일시정지", description = musicnow[0] + "을(를) 일시정지 했습니다.", color = 0x00ff00))
    else:
        await message.channel.send("지금 노래가 재생되지 않네요.")


async def 다시재생(message, musicnow):
    try:
        vc.resume()
    except:
         await message.channel.send("지금 노래가 재생되지 않네요.")
    else:
         await message.channel.send(embed = discord.Embed(title= "다시재생", description = musicnow[0]  + "을(를) 다시 재생했습니다.", color = 0x00ff00))


async def 노래끄기(message, musicnow):
    if vc.is_playing():
        vc.stop()
        await message.channel.send(embed = discord.Embed(title= "노래끄기", description = musicnow[0]  + "을(를) 종료했습니다.", color = 0x00ff00))
    else:
        await message.channel.send("지금 노래가 재생되지 않네요.")


async def 지금노래(message, musicnow):
    if not vc.is_playing():
        await message.channel.send("지금은 노래가 재생되지 않네요..")
    else:
        await message.channel.send(embed = discord.Embed(title = "지금노래", description = "현재" + musicnow[0] + "을(를) 재생하고 있습니다.", color= 0x00ff00))


async def 대기열추가(message, msg, user, musictitle, musicnow, song_queue):

    user.append(msg)
    result, URLTEST = title(msg, musictitle, musicnow)
    song_queue.append(URLTEST)
    await message.channel.send(result + "를 재생목록에 추가했어요!")


async def 대기열삭제(message, number, musicnow, user, musictitle, song_queue):
    try:
        ex = len(musicnow) - len(user)
        del user[int(number) - 1]
        del musictitle[int(number) - 1]
        del song_queue[int(number)-1]
        del musicnow[int(number)-1+ex]
            
        await message.channel.send("대기열이 정상적으로 삭제되었습니다.")
    except:
        if len(list) == 0:
            await message.channel.send("대기열에 노래가 없어 삭제할 수 없어요!")
        else:
            if len(list) < int(number):
                await message.channel.send("숫자의 범위가 목록개수를 벗어났습니다!")
            else:
                await message.channel.send("숫자를 입력해주세요!")


async def 목록(message, musictitle):
    if len(musictitle) == 0:
        await message.channel.send("아직 아무노래도 등록하지 않았어요.")
    else:
        global Text
        Text = ""
        for i in range(len(musictitle)):
            Text = Text + "\n" + str(i + 1) + ". " + str(musictitle[i])
            
        await message.channel.send(embed = discord.Embed(title= "노래목록", description = Text.strip(), color = 0x00ff00))


async def 목록초기화(message, musicnow, user, musictitle, song_queue):
    try:
        ex = len(musicnow) - len(user)
        del user[:]
        del musictitle[:]
        del song_queue[:]
        while True:
            try:
                del musicnow[ex]
            except:
                break
        await message.channel.send(embed = discord.Embed(title= "목록초기화", description = """목록이 정상적으로 초기화되었습니다. 이제 노래를 등록해볼까요?""", color = 0x00ff00))
    except:
        await message.channel.send("아직 아무노래도 등록하지 않았어요.")


async def 목록재생(message, user, musicnow, song_queue, musictitle, app):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    if len(user) == 0:
        await message.channel.send("아직 아무노래도 등록하지 않았어요.")
    else:
        if len(musicnow) - len(user) >= 1:
            for i in range(len(musicnow) - len(user)):
                del musicnow[0]
        if not vc.is_playing():
            play(message, song_queue, user, musictitle, app)
        else:
            await message.channel.send("노래가 이미 재생되고 있어요!")


async def 가사(message, title1):
    url = f"https://www.google.com/search?q={title1}+가사"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    lyrics = soup.find_all('div', class_="BNeawe tAd8D AP7Wnd")
    await sendff(message,f"가사 : {title1}", lyrics[-2].string,"green")

async def sendff(message, titlef, descriptionf, colorf):
    if (colorf == "red"):
        return await message.channel.send(embed = discord.Embed(title= titlef, description = descriptionf, color = 0xff0000))
    elif (colorf == "green"):
        return await message.channel.send(embed = discord.Embed(title= titlef, description = descriptionf, color = 0x00ff00))
    elif (colorf == "blue"):
        return await message.channel.send(embed = discord.Embed(title= titlef, description = descriptionf, color = 0x0000ff))