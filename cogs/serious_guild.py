import discord
from discord.ext import commands
import json
import asyncio
# json made by @sponk
from time import gmtime, strftime

def record_stats(message, ctx):
    the_time = strftime("%a, %d %b %Y %X -0400", gmtime())
    with open("message_stats.txt", "a") as f:
	    f.write(f"Time: {the_time}, Guild: {ctx.guild}, User: {ctx.author}, Message: {message}\n")

def true_serious(guild):
    js = {
        f"{guild}": True
    }
    with open('guild_serious.json', 'a') as outwrite:
        json.dump(js, outwrite)

#function writes guild serious as false
def false_serious(guild):
    breh = open('guild_serious.json', 'w')

    if guild in breh:
        breh[guild] = False

    json.dump(breh, open('guild_serious.json', 'r'),sort_keys=True,indent=4)

serious = json.load(open('guild_serious.json', 'r'))

class serious_guilds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded serious_guilds cog!")

    async def on_message(self, message):
        seriouss = False
        if message.guild.id in serious:
            seriouss = True
        if not seriouss:
            if ("i love you senko" in message.content.lower()) or ("i love you senkosan" in message.content.lower()):
                await message.channel.send(f"I love you too, {message.author.mention}")
                record_stats("user said i love you senko,senko replied", message)
        else:
            pass    

    

    #commands code starts here V
    @commands.command(name='guildIsSerious')
    async def guildIsSerious(self, ctx):
    
        if not(ctx.guild.id in serious):
            
            true_serious(ctx.guild.id)
            record_stats("guild was changed to serious", ctx)
            await ctx.send("I will behave in this server.")
        else:
            record_stats("guild attempted and failed to be changed to serious (already serious)", ctx)
            await ctx.send("Guild is already serious!")

    @commands.command(name='guildIsNotSerious')
    async def guildIsNotSerious(self, ctx):
    
        if ctx.guild.id in serious:
            false_serious(ctx.guild.id)
            await ctx.send("Tehehe")
            record_stats("guild changed from serious to non serious", ctx)
        else:
            await ctx.send("This server is already not a serious server!")
            record_stats("guild attempted and failed to change from serious to non serious (already non serious)", ctx)

    @commands.command(name='getSeriousGuilds')
    async def getSeriousGuilds(self, ctx):
        if ctx.author.id == 219987389135716364 or 597420184122294272 or 361143836598337546:

        
            await ctx.send(serious)
            record_stats("getSeriousGuilds", ctx)
        else:
            await ctx.send("You don't have permissions to do this command")


    #commands code ends here ^
def setup(client):
    client.add_cog(serious_guilds(client))