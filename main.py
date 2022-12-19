import discord
import test
from discord.ext import commands
 
intent = discord.Intents.default()
intent.message_content = True

app = commands.Bot(command_prefix='/', intents=intent)
 
@app.event
async def on_ready():
    print('Done!')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def hello(ctx):
    await test.hello(ctx)

app.run("MTA1NDE4NDI2OTEwMDA5NzY5OA.G6Sfut.NYfm2a1JfGQX5PSstmjyrSp-6VFcWnIcW7N55w")