import discord
import os
from discord.ext import commands
import requests
import random
from music_cog import music_cog




# bot_logic in original

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

kask = ["kask","kaskım","Kaskımı","kaskını","kaskini","kaskin"]

def sifre_olusturucu(sifre_uzunlugu):
    ogeler = "+-/*!&$#?=@<>"
    sifre = ""

    for i in range(sifre_uzunlugu):
        sifre += random.choice(ogeler)

    return sifre

def cumle():

    cumlesec = random.randint(1,5)

    if cumlesec == 1:
        return "KASKIMI GERİ VER"
    
    elif cumlesec == 2:
        return "BİSİKLET KASKI O NE KADAR DEĞERLİ BİLİYOR MUSUN?"
    
    elif cumlesec == 3:
        return "KASKIMI GERİ VERİR MİSİN?"
    
    elif cumlesec == 4:
        return "KIRMA!"
    
    elif cumlesec == 5:
        return "KASKIMI ZORLA ALIYORSUNUZ ŞUAN"



def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)


def yazi_tura():
    para = random.randint(0, 5)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command('mem')
async def mem(ctx):
    randomMem = random.choice(os.listdir('img'))
    with open(f"img/{randomMem}" , "rb") as f:
        pic = discord.File(f)

    await ctx.send(file=pic)    


def getDogImg():
    url = 'https://random.dog/woof.json'
    response = requests.get(url)
    data = response.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    dogImg = getDogImg()
    await ctx.send(dogImg)

@bot.listen()
async def on_message(message):
    if message.author != bot.user:
        content = message.content.lower()  
        for kelime in kask:
            if kelime in content:
                response = cumle()
                await message.channel.send(response)
                
                randomMem = random.choice(os.listdir('img'))
                with open(f"img/{randomMem}" , "rb") as f:
                    pic = discord.File(f)
                
                await message.channel.send(file=pic)
                break


              


    
            

            


        



@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')



@bot.command()
async def sans(ctx):
    await ctx.send("kaybeden biber yer 🌶️ "+yazi_tura())
    
    bot.add_cog(music_cog(bot))

    







    

bot.run("MTE1MzM3NjE1MDI5MTIxODQ4Mw.G1Gxsi.xkdWZKgctztbTfCZIBRpuKiAhFUUFfXfSv1nNk")