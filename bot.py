import discord
import pyupbit
import time
import os
xrpprice = pyupbit.get_current_price("KRW-XRP")
df = pyupbit.get_ohlcv("KRW-XRP", count=3)
sung_p=str(round(xrpprice/304,3))
baek_p=str(round(xrpprice/350,3))
sung_m=str(round(1-(xrpprice/304),3))
baek_m=str(round(1-(xrpprice/354),3))
client = discord.Client()
channel = client.get_channel(791857271776477184)
@client.event
async def on_ready():
    print(f'{client.user} 에 로그인하였습니다!')
    await bot.change_presence(activity=discord.Streaming(name = '빅샥', url='https://www.youtube.com/watch?v=3M_5oYU-IsU'))
    
@client.event
async def on_message(message):
    if message.content.startswith('리플'):
      await message.channel.send('현재가 : {0}'.format(xrpprice))
      await message.channel.send('최근3일가격{0}'.format(df))
      if (350/xrpprice)<1:
        await message.channel.send('백종인[350] 수익{0}%'.format(baek_p[2:4]))
      else:
        await message.channel.send('백종인[350] 손실{0}%'.format(baek_m[2:4]))
      if (304/xrpprice)<1:
        await message.channel.send('정성민[304] 수익{0}%'.format(sung_p[2:4]))
      else:
        await message.channel.send('정성민[304] 손실{0}%'.format(sung_m[2:4]))
      time.sleep(1800)
client.run(os.environ['token'])
