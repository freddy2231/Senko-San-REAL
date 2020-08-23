import discord
from discord.ext import commands
from time import strftime, gmtime
import json 


bruh = open('bruh.json', 'r')

def bruh_t(id):
    p = json.load(open('bruh.json', 'r'))
    p[f"{id}"]=True
    json.dump(p, open('bruh.json', 'r'),sort_keys=True,indent=4)

def bruh_f(id):
    p = json.load(open('bruh.json', 'r'))
    p[f"{id}"]=False
    json.dump(p, open('bruh.json', 'r'),sort_keys=True,indent=4)

    



class bruhcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded bruh cog!")

    async def on_message(self, message):
        bruhs = False
        if message.guild.id in bruh:
            bruhs = True
        if not bruhs:
            if  "bruh" in message.content.lower():
                if not ("s$guildIsBruh" in message.content or "s$guildIsNotBruh" in message.content or "s$getBruhGuilds" in message.content):
                    bruhImg=discord.File('bruh.jpg')
                    await message.channel.send(f"That's quite a bruh moment {message.author.mention}!", file=bruhImg)    
        self.bot.process_commands(message)
    #commands code starts here V

    


    @commands.command(name='guildIsNotBruh')
    async def guildIsBruh(self, ctx):
        if not(ctx.guild.id in bruh):
            bruh_t(ctx.guild.id)
            await ctx.send("I will detect bruh moments in this server.")
            
        else:
            await ctx.send("Guild already does detect bruh moments!")
            

    @commands.command(name='guildIsBruh')
    async def guildIsNotBruh(self, ctx):
        if (ctx.guild.id in bruh):
            bruh_f(ctx.guild.id)
            await ctx.send("Tehehe")
            
        else:
            await ctx.send("I already do not detect bruh moments on this server!")
            

    @commands.command(name='getBruhGuilds')
    async def getBruhGuilds(self, ctx):
        if ctx.author.id == 219987389135716364 or 597420184122294272 or 361143836598337546:
            await ctx.send(bruh)
        else:
            await ctx.send('No permissions')



def setup(bot):
    bot.add_cog(bruhcog(bot))