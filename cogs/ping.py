import disnake
from disnake.ext import commands


bot = commands.InteractionBot(intents=disnake.Intents.all())
url = "" #put here your bot logo URL

# this is very necessary for cog
class PingCommand(commands.Cog):

    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot

    @commands.slash_command(description="Get the bot's current websocket latency.")
    @commands.guild_only()
    async def ping(self, ctx: disnake.ApplicationCommandInteraction):
        await ctx.response.defer(ephemeral=True) # if true only who ran the command can see the message bot send
        embed = disnake.Embed(title=f" Pong..! 🏓 `{round(self.bot.latency * 1000)}` ms", color=disnake.Colour.purple())
        embed.set_author(name="Your Bot name", icon_url=url)
        await ctx.edit_original_response(embed=embed)
        
        

    
        


def setup(bot: commands.InteractionBot):
    bot.add_cog(PingCommand(bot))

# adds your cog to bot
