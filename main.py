import disnake
from disnake.ext import commands, tasks
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
#here are the things that we import

token = os.getenv("token")
#here you import your bot token from .env
bot = commands.InteractionBot(intents=disnake.Intents.all())
#don't forget to active all intents on the discord dev portal too


activities = [
    lambda: disnake.Activity(type=disnake.ActivityType.playing, name="/ping"), #put whatever you like
    lambda: disnake.Activity(type=disnake.ActivityType.watching, name=f"{len(bot.guilds)} servers") #to get how many servers your bot in
]


@bot.event
async def on_ready():
    change_activity.start()
    print(f"Logged in as {bot.user}")
    #print when your bot gets active

@tasks.loop(minutes=30)
async def change_activity():
    for activity_generator in activities:
        activity = activity_generator()
        await bot.change_presence(activity=activity)
        print(f"Updated activity: {activity.type.name} - {activity.name}")
        await asyncio.sleep(30 * 60)
        #updates bot activity after every 30 minutes
        
cog_modules = [
    "dog", "ping", "uptime"
]


for module in cog_modules:
    try:
        bot.load_extension(f"cogs.{module}")
    except Exception as e:
        print(f"Error : {e}")
#loads your cogs

bot.run(token)
