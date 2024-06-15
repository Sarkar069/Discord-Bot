import disnake
from disnake.ext import commands
import asyncio
import os
import requests
from dotenv import load_dotenv
load_dotenv()

Api_key = os.getenv('Ninja_API')

class DogCommand(commands.Cog):
    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot
        
    @commands.slash_command(description="get a random pic of dog")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dog(self, ctx: disnake.ApplicationCommandInteraction):
     await ctx.response.defer()

     await asyncio.sleep(3)

     url = "https://random.dog/woof.json"
     response = requests.get(url)

     if response.status_code == 200:
         data = response.json() 
         image = data['url']
         await ctx.edit_original_response(image)
     else:
         await ctx.edit_original_response(f"Error: {response.status_code} {response.text}")
         
    
    @commands.slash_command(description="get a random meme")
    async def meme(ctx : disnake.ApplicationCommandInteraction):
     await ctx.response.defer()
     await asyncio.sleep(3)

     url = "https://memes.cyclic.app/api"

     response = requests.get(url)

     if response.status_code == 200:
          data = response.json()
          image = data['url']
          embed = disnake.Embed(color=disnake.Colour.dark_blue())
          embed.set_image(url=image)
          embed.set_footer(text="Subreddit : memes")
          await ctx.edit_original_response(embed=embed)
          
     else:
         await ctx.send("Error: Unable to fetch memes.")

def setup(bot: commands.InteractionBot):
    bot.add_cog(DogCommand(bot))
