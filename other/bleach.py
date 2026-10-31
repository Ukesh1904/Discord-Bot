import discord 
from discord.ext import commands
import random
import os
import json 

bleach = commands.Bot(command_prefix = ',', intents=discord.Intents.all())

token = ""

collected_characters = {}

bleach_characters = {
    "Ichigo Kurosaki": {"power": "\nPower = 9000","url": "https://media1.tenor.com/m/7GgfegR83eIAAAAC/ichigo-kurosaki-final-getsuga-tenshou.gif", "rank": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Unicode_0x0041.svg/800px-Unicode_0x0041.svg.png"},
    "Rukia Kuchiki": {"power": "\nPower = 8000","url": "https://media1.tenor.com/m/GGFgGQAePWcAAAAd/rukia.gif", "rank": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/IPA_Unicode_0x0073.svg/800px-IPA_Unicode_0x0073.svg.png"},
    "Renji Abarai": {"power": "\nPower = 7000","url": "https://media1.tenor.com/m/-U4YwqBf0jkAAAAC/bleach-bleach2022.gif", "rank": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Unicode_0x0041.svg/800px-Unicode_0x0041.svg.png"},
    "Byakuya Kuchiki": {"power": "\nPower = 6000","url": "https://media1.tenor.com/m/jHmFV_uPfgEAAAAC/byakuya-blood-war.gif", "rank": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Unicode_0x0041.svg/800px-Unicode_0x0041.svg.png"},
    "Toshiro Hitsugaya": {"power": "\nPower = 5000","url": "https://media1.tenor.com/m/2Hu-_L-yopAAAAAC/toshirohitsugaya-bleach.gif", "rank": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Unicode_0x0041.svg/800px-Unicode_0x0041.svg.png"},
    # "Kenpachi Zaraki": "https://vignette.wikia.nocookie.net/bleach/images/5/5b/KenpachiZaraki.png/revision/latest/scale-to-width-down/340?cb=20170731000233",
    # "Grimmjow Jaegerjaquez": "https://vignette.wikia.nocookie.net/bleach/images/3/34/GrimmjowJaegerjaquez_art.png/revision/latest/scale-to-width-down/340?cb=20130128191728",
    # "Ulquiorra Cifer": "https://vignette.wikia.nocookie.net/bleach/images/5/51/Ulquiorra_manga.jpg/revision/latest/scale-to-width-down/340?cb=20100524224257",
    # "Orihime Inoue": "https://vignette.wikia.nocookie.net/bleach/images/2/2e/Orihime_Inoue_character_image.png/revision/latest/scale-to-width-down/340?cb=20170722200017",
    # "Yoruichi Shihouin": "https://vignette.wikia.nocookie.net/bleach/images/c/c7/Yoruichi_new_outfit.png/revision/latest/scale-to-width-down/340?cb=20200628152233",
    "Sosuke Aizen": {"power": "\nPower = 10000","url": "https://media1.tenor.com/m/DBbblZDY3D4AAAAC/sosuke-aizen-bleach.gif", "rank": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/IPA_Unicode_0x0073.svg/800px-IPA_Unicode_0x0073.svg.png"},
    "Sosuke Aizen": {"power": "\nPower = 10000","url": "https://media1.tenor.com/m/DBbblZDY3D4AAAAC/sosuke-aizen-bleach.gif", "rank": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/IPA_Unicode_0x0073.svg/800px-IPA_Unicode_0x0073.svg.png"},
    # "Uryu Ishida": "https://vignette.wikia.nocookie.net/bleach/images/f/f8/Uryu_Ishida_Bankai.png/revision/latest/scale-to-width-down/340?cb=20201010123139",
    "Kisuke Urahara": {"power": "\nPower = 6000","url": "https://media1.tenor.com/m/ZdIVT_MdkA4AAAAC/kisuke.gif", "rank": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/IPA_Unicode_0x0073.svg/800px-IPA_Unicode_0x0073.svg.png"}
}

rolls_counter={}

max_rolls = 5

 
@bleach.event
async def on_ready():
    print("Bleach is ready to play game.")
    print("-----------------------------")
    

@bleach.command()
async def roll(ctx):
     if ctx.author.id in rolls_counter and rolls_counter[ctx.author.id] >= max_rolls:
        await ctx.send("You've reached the maximum number of rolls.")
     else:
        character = random.choice(list(bleach_characters.keys()))
        power = bleach_characters[character]["power"]
        image_url = bleach_characters[character]["url"]
        rank_url = bleach_characters[character]["rank"]
        msg = discord.Embed(title=f'{character}',description=power,color=discord.Color.random())
        msg.set_image(url=image_url)
        msg.set_thumbnail(url=rank_url)
        # await ctx.send(f'You rolled: {character}')
        # await ctx.send(image_url)
        await ctx.send(embed=msg)
        
        rolls_counter[ctx.author.id] = rolls_counter.__annotations__get(ctx.author.id, 0) + 1
        
         # Auto collect character
        if ctx.author.id not in collected_characters:
            collected_characters[ctx.author.id] = []
        collected_characters[ctx.author.id].append(character)
        
# Command to show collected character
@bleach.command()
async def collection(ctx):
    if ctx.author.id in collected_characters:
        collection_list = collected_characters[ctx.author.id]
        await ctx.send(f'{ctx.author.name}\'s Collection:')
        for character in collection_list:
            await ctx.send(character)
    else:
        await ctx.send('You haven\'t collected any characters yet.')
        

bleach.run(token)