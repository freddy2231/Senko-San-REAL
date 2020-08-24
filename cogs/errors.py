import discord
from discord.ext import commands
import traceback

class COGNAME(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded COGNAME cog!")

    async def on_command_error(self, ctx, error):
        embed = discord.Embed(title='Error', color='#FF0000')
        if isinstance(error, commands.CommandNotFound):
            embed.description("Oh dear! Seems like this command doesn't exist, try using s$help.")
        elif isinstance(error, commands.BadArgument):
            embed.description("Oh dear! Seems like you used this command wrongly.")
        elif isinstance(error, commands.BotMissingPermissions):
            embed.description("Oh dear! Seems like I don't have permissions to do this command.")
        elif isinstance(error, commands.MissingPermissions):
            embed.description('Oh dear! You do not have permissions to use this command.')
        else:
            try:
                0/0 # just trying to cause an error
            except Exception as error:
                return await ctx.send(traceback.format_exc())
    
def setup(client):
    client.add_cog(COGNAME(client))