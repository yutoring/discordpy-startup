from discord.ext import commands, tasks
from datetime import datetime
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

target_channel_id = 325988737572012033

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    
@tasks.loop(hours=24)
async def called_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await ctx.send("Test man is testing")

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Eyyy B0sss!")



    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')



called_once_a_day.start()
bot.run(token)
