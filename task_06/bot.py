import discord 
import scraper
import os 
from discord.ext import commands
import csv
from dotenv import load_dotenv 



load_dotenv()
token = os.getenv("SECRET_KEY")
Client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#bot is getting ready
@Client.event
async def on_ready():
    print("The bot is ready for use")
    print("------------")




   



  

    
@Client.event
async def on_message(message):

  if message.content.startswith("!help"):
    await message.channel.send(scraper.intro())

  if message.content.startswith("!livescore"):

    
    

 



    with open("score.csv","a",newline="") as file:
          writer = csv.writer(file)
          
          writer.writerow((scraper.check().split("\n")))
         
    await message.channel.send(scraper.check())
    

  
  if message.content.startswith("!csv"):
    
    




    await message.channel.send(file = discord.File("score.csv"))


          


        
Client.run(token)