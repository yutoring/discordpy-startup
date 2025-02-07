from discord.ext import commands
import tasks
from datetime import datetime
import os
import traceback


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


# 接続に必要なオブジェクトを生成
client = discord.Client()

#投稿する日時
dateTimeList = [
'2019/11/19 18:09',
'2019/11/19 18:15',
'2019/11/19 18:20',
]

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ready')

# 指定時間に走る処理
async def SendMessage():
    channel = get_channel(ctx)
    await channel.send('時間だよ')

# 30秒に一回ループ
@tasks.loop(seconds=30)
async def time_check():
    sleepTime = 0
    # 現在の時刻
    now = datetime.now().strftime('%Y/%m/%d %H:%M')
    if now in dateTimeList :
        print(now)
        await SendMessage()
        #該当時間だった場合は２重に投稿しないよう３０秒余計に待機
        await asyncio.sleep(30)

        
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


#ループ処理
time_check.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)
bot.run(token)
