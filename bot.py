import discord
import pyupbit
import time
client = discord.Client()
channel = client.get_channel(791857271776477184)
xrpprice = pyupbit.get_current_price("KRW-XRP")
df = pyupbit.get_ohlcv("KRW-XRP", count=3)
sung=str(round(xrpprice/304,3))
baek=str(round(xrpprice/350,3))
@client.event
async def on_ready():
    print(f'{client.user} 에 로그인하였습니다!')

@client.event
async def on_message(message):
    if message.content.startswith('리플'):
      while True:
        await message.channel.send('현재가 : {0}'.format(xrpprice))
        await message.channel.send('최근3일가격{0}'.format(df))
        await message.channel.send('백종인[350] 수익률{0}%'.format(baek[2:4]))
        await message.channel.send('정성민[304] 수익률{0}%'.format(sung[2:4]))
        time.sleep(120)
client.run('NzkxODUyMzkxMTAzNDYzNDY1.X-VMAQ.IUGjQ5Bok5vdrPo7f0deb_8_F4M')
