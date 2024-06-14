import disnake
import uptime
import datetime
import time
import psutil
import asyncio
from disnake.ext import commands

url = "https://cdn.discordapp.com/attachments/1101410251061866590/1139508274367045632/bot_logo.png"

ram_usage = psutil.virtual_memory().percent
ram_usage_str = f"{ram_usage}%"

process = psutil.Process()
memory_usage = process.memory_info().rss / 1024 ** 2  #
memory_usage_str = f"{memory_usage:.2f} MB"

cpu_usage = psutil.cpu_percent(interval=1)
cpu_usage_str = f"{cpu_usage}%"

bot = commands.InteractionBot()

mem_stats = psutil.virtual_memory()
available_memory = mem_stats.available / 1024 ** 2






class Uptime(commands.Cog):
    def __init__(self, bot : commands.InteractionBot):
        self.bot = bot
        

        
    global startTime 
    startTime = time.time()


   

    @commands.slash_command(description="info about bot stats")
    @commands.guild_only()
    async def stats(self, ctx: disnake.ApplicationCommandInteraction):
     await ctx.response.defer(ephemeral=True)
     await asyncio.sleep(3)
     
     uptime_seconds = int(round(time.time() - startTime))
     uptime_timedelta = datetime.timedelta(seconds=uptime_seconds)
     days, seconds = uptime_timedelta.days, uptime_timedelta.seconds
     hours = seconds // 3600
     minutes = (seconds % 3600) // 60
     seconds = seconds % 60
     uptime_string = f"{days}d {hours}h {minutes}m {seconds}s"
     embed = disnake.Embed(
        title="Stellar Enigma",
        description=None,
        color=disnake.Colour.purple(),
    )
    
     embed.set_thumbnail(url=url)
     embed.add_field(name="➠ CPU Usage", value=cpu_usage_str, inline=False)
     embed.add_field(name="➠ Memory Usage", value=memory_usage_str, inline=False)
     embed.add_field(name="➠ Ram Usage", value=ram_usage_str, inline=False)
     embed.add_field(name="➠ Server Count", value=len(ctx.bot.guilds), inline=False)
     embed.add_field(name="➠ Avilable  Memory", value=f"{available_memory:.2f} MB",inline=False)
     embed.add_field(name="➠ Library", value="[Disnake.py](https://guide.disnake.dev/)", inline=False)
     embed.add_field(name="➠ Uptime", value=f"```{uptime_string}```", inline=False)


     
     embed.set_footer(text="@ Sarkar#8622", icon_url=None)
     await ctx.edit_original_response(embed=embed)
 
   


def setup(bot : commands.InteractionBot):
    bot.add_cog(Uptime(bot)) 
    