import disnake
from disnake.ext import commands, tasks
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

token = os.getenv("TOKEN")

bot = commands.InteractionBot(intents=disnake.Intents.all())

activities = [
    lambda: disnake.Activity(type=disnake.ActivityType.playing, name="Mysteries Of Universe 🌌"),
    lambda: disnake.Activity(type=disnake.ActivityType.watching, name=f"{len(bot.guilds)} servers")
]

@bot.event
async def on_ready():
    change_activity.start()
    print(f"Logged in as {bot.user}")

@tasks.loop(minutes=30)
async def change_activity():
    for activity_generator in activities:
        activity = activity_generator()
        await bot.change_presence(activity=activity)
        print(f"Updated activity: {activity.type.name} - {activity.name}")
        await asyncio.sleep(30 * 60)
        
        
cog_modules = [
    "apod", "astro", "deepspace", "eq", "google", "horo", "image",
    "isro", "mars", "ping", "planet","uptime"
]


for module in cog_modules:
    try:
        bot.load_extension(f"cogs.{module}")
    except Exception as e:
        print(f"Error : {e}")


bot.run(token)
