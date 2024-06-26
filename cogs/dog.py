import disnake
from disnake.ext import commands
import requests

class DogCommand(commands.Cog):
    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot
        
    @commands.slash_command(description="get a random pic of dog")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dog(self, inter: disnake.ApplicationCommandInteraction):
     await ctx.response.defer()


     url = "https://random.dog/woof.json"
     response = requests.get(url)

     if response.status_code == 200:
         data = response.json() 
         image = data['url']
         await inter.edit_original_response(image) #send a random image or gif of a dog
     else:
         await inter.edit_original_response(f"Error: {response.status_code} {response.text}")
         
    

def setup(bot: commands.InteractionBot):
    bot.add_cog(DogCommand(bot))
