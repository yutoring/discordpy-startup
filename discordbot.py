from discord.ext import commands
import os
import datetime
import traceback
from discord.ext import tasks

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

dateTimeList = [
'17:30'
]

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ready')

# 指定時間に走る処理
async def SendMessage():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')    
    
    

@tasks.loop(seconds=30)
async def time_check():
    sleepTime = 0
    # 現在の時刻
    now = datetime.now().strftime('%Y/%m/%d %H:%M')
    if now in dateTimeList :
        print(now)
        await SendMessage('asd')
        #該当時間だった場合は２重に投稿しないよう３０秒余計に待機
        await asyncio.sleep(30)



@Client.event

async def time_check
await SendMessage('asdasd')
 
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


    
#ループ処理
time_check.start()

bot.run(token)
