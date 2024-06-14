import disnake
from disnake.ext import commands
import asyncio


bot = commands.InteractionBot(intents=disnake.Intents.all())
url = "https://cdn.discordapp.com/attachments/1101410251061866590/1139508274367045632/bot_logo.png"

class PingCommand(commands.Cog):

    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot

    @commands.slash_command(description="Get the bot's current websocket latency.")
    @commands.guild_only()
    async def ping(self, ctx: disnake.ApplicationCommandInteraction):
        await ctx.response.defer(ephemeral=True)
        await asyncio.sleep(3)
        embed = disnake.Embed(title=f" Pong..! 🏓 `{round(self.bot.latency * 1000)}` ms", color=disnake.Colour.purple())
        embed.set_author(name="Stellar Enigma", icon_url=url)
        await ctx.edit_original_response(embed=embed)
        
        

    
        


def setup(bot: commands.InteractionBot):
    bot.add_cog(PingCommand(bot))