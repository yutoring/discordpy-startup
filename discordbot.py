from discord.ext import commands
import os
import datetime
import traceback
import tasks

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

dateTimeList = [
'17:25'
]

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


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
