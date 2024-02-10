import discord 
import scraper
import csv
import os 
from dotenv import load_dotenv


load_dotenv()
token = os.getenv("TOKEN")


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("bot is runnning!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("!hello"):
        await message.channel.send(scraper.intro())

    if message.content.startswith("!livescore"):
        await message.channel.send(scraper.check())
        with open("score.csv","a") as score:
            write = csv.writer(score)
            contents = []
            for j in scraper.check().split("\n"):
                contents.append(j)
                
                
            write.writerow(contents)

            
    if message.content.startswith("!csv"):
        await message.channel.send(file= discord.File("score.csv"))




client.run(token)




