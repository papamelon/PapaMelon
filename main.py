import discord
import test
from discord.ext import commands
import TOKEN
 
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

app.run(TOKEN.DISCORD_BOT_TOKEN)