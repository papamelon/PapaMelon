import discord

from discord.ext import commands

import asyncio

import schoolInfo

import re 

import nest_asyncio


nest_asyncio.apply()


hue = 0

gy = ''

yue = ''

async def th(yue):
    print_end : str = "\n\n\n\n\n"
    school_data: dict = await schoolInfo.search(yue)
    # print(school_data, end=print_end)
    # 학교를 검색하는 구문입니다.

    meal_data: dict = await schoolInfo.meal(
        ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
        SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"],
    )

    # gy = re.findall(('[가-힣]+'),str(meal_data))
    # print(gy)
    all =[]
    test = len(meal_data)

    i = 0

    all.append(meal_data[0]['SCHUL_NM'])
    while(i<test):
      all.append(meal_data[i]['MMEAL_SC_NM'])
      all.append(meal_data[i]['DDISH_NM'])
      i += 1
    ki = ('\n'.join(all))
    return ki


async def eat(message,text):

    msg = await message.channel.send(embed = discord.Embed(title = text+ "을(를)을 검색중..", color = 0x0000ff))

    try:
        loop = asyncio.get_event_loop()
        index1 = loop.run_until_complete(th(text))
        await msg.edit(embed = discord.Embed(title= "급식", description = str(index1).replace(")",")\n"), color = 0x00ff00))
    except:
         await msg.edit(embed = discord.Embed(title="학교이름이 정확하지 않아요! 다시 검색해 주세요!", color = 0xff0000))


async def sendff(message, titlef, descriptionf, colorf):
    if (colorf == "red"):
        return await message.channel.send(embed = discord.Embed(title= titlef, description = descriptionf, color = 0xff0000))
    elif (colorf == "green"):
        return await message.channel.send(embed = discord.Embed(title= titlef, description = descriptionf, color = 0x00ff00))
    elif (colorf == "blue"):
        return await message.channel.send(embed = discord.Embed(title= titlef, description = descriptionf, color = 0x0000ff))