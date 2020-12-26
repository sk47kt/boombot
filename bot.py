import discord
import pyupbit
import time
import os
xrpprice = pyupbit.get_current_price("KRW-XRP")
df = pyupbit.get_ohlcv("KRW-XRP", count=3)
sung=str(round(xrpprice/304,3))
baek=str(round(xrpprice/350,3))
client = discord.Client()
channel = client.get_channel(791857271776477184)
@client.event
async def on_ready():
    print(f'{client.user} 에 로그인하였습니다!')
    

@client.event
async def on_message(message):
    if message.content.startswith('리플'):
      await message.channel.send('현재가 : {0}'.format(xrpprice))
      await message.channel.send('최근3일가격{0}'.format(df))
      if (350/xrpprice)<1:
          await message.channel.send('백종인[350] 수익률{0}%'.format(baek[2:4]))
      else:
          await message.channel.send('백종인[350] 손실율{0}%'.format(baek[2:4]))
      if (304/xrpprice)<1:
          await message.channel.send('정성민[304] 수익률{0}%'.format(sung[2:4]))
      else:
          await message.channel.send('정성민[304] 손실율{0}%'.format(sung[2:4]))
      time.sleep(1800)
client.run(os.environ['token'])
