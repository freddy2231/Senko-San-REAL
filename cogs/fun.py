import json
import discord
from discord.ext import commands
from time import gmtime, strftime
import random



def hate_true(id):
    js = json.load(open('hated.json', 'r'))
    js[f"{id}"]=True
    json.dump(js, open('i.json', 'r'),sort_keys=True,indent=4)


def hate_false(id):
    hi = json.load(open('hated.json', 'w'))

    if id in hi:
        hi[id] = False
    json.dump(hi, open('hated.json', 'r'),sort_keys=True,indent=4)

serious = json.load(open('guild_serious', 'r'))

hate = json.load(open('hated.json', 'r'))

msg = 'This server is serious'

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded fun cog')

    @commands.command(name='dance')
    async def dance(self, ctx):
        
        if ctx.guild.id in serious:
            await ctx.send('This server is serious!')
            
        if not serious:
            danceGIF = discord.File("sDance.gif")
            await ctx.channel.send(file=danceGIF)
            

    @commands.command(name='pat')
    async def pat(self, ctx):
        if ctx.guild.id in serious:
            await ctx.send(msg)

        else:
            patGIF = discord.File("sPAT.gif")
            await ctx.channel.send(file=patGIF)
            
        

    
    @commands.command(name='hate')
    async def hate(self, ctx, person:discord.Member):
    
        if ctx.guild.id in serious:
            await ctx.send(msg)
            
        if not ctx.guild.id in serious:
            if not(person in hate):
                hate_true(person)
                await ctx.send("Added!")
                
                return
            else: 
                await ctx.channel.send("That person is already on the list!")
                
        else:
            pass
        

    @commands.command(name='hate_remove')
    async def hate_remove(self, ctx, person:discord.Member):
    
        if ctx.guild.id in serious:
            await ctx.send(msg)
            
        if not serious:
            if (person in hate):
                hate_false(person)
                await ctx.send("Removed!")
                
                return
            else: 
                await ctx.channel.send("That person isn't hated (yet...)")
                
        else:
            pass

    @commands.command(name='hate_list')
    async def hate_list(self, ctx):
        if ctx.author.id == 219987389135716364 or 597420184122294272 or 361143836598337546:
            
            await ctx.send(hate)
            
        else:
            pass

    
    @commands.command(name='love')
    async def love(self, ctx, *, personM:discord.Member):
    #print("break 1")
    
        if ctx.guild.id in serious:
            #print("break 2")
            await ctx.send(msg)
            
        if not ctx.guild.id in serious:
            #print("break 3")
            loveGIF = discord.File("senkoLove.gif")
            
            if personM in hate:
                    #print("break 4")
                loveGIF = discord.File("sMAD.gif")
                await ctx.channel.send(f"Shut up, {personM.mention} does not deserve love", file=loveGIF)
                
                return

            if personM.id == 691010171828437025:
            #print("break 5")
                loveGIF = discord.File("sLove.gif")
                await ctx.channel.send(f"I love you too, {ctx.author.mention}", file=loveGIF)
                
                return

            elif personM.id == ctx.author.id:
            #print("break 6")
                loveGIF == discord.File("senkoLove.gif")
                await ctx.channel.send(f"You must love yourself a lot, {personM.mention}", file=loveGIF)
                

            else:
            #print("break 7")
                loveGIF = discord.File("senkoLove.gif")
                await ctx.channel.send(f"{ctx.author.mention} loves you, {personM.mention}", file=loveGIF)
                
        else:
            pass

    @commands.command(name="fluff")
    async def fluff(self, ctx):
    
        if ctx.guild.id in serious:
            
            await ctx.send('This server is serious!')
        if not ctx.guild.id in serious:
            gifnum = random.randint(0,2)
            if gifnum == 0:
                fluffy = discord.File("sFluff1.png")
                await ctx.channel.send(file=fluffy)
            elif gifnum == 1:
                fluffy = discord.File("sFluff3.jpg")
                await ctx.channel.send(file=fluffy)
            if gifnum == 2:
                fluffy = discord.File("sFluff4.jpg")
                await ctx.channel.send(file=fluffy)
                

    @commands.command(name="hug")
    async def hug(self, ctx):
    
        if ctx.guild.id in serious:
            await ctx.send('Server is serious')
            
        if not ctx.guild.id in serious:
            hugGIF = discord.File("sHug.gif")
            await ctx.channel.send(file=hugGIF)
            

    @commands.command(name="protecc")
    async def protecc(self, ctx):
    
        if ctx.guild.id in serious:
            await ctx.send('Server is serious')
            
        if not ctx.guild.id in serious:
            protecc = discord.File("sJOJO.png")
            await ctx.channel.send("No bullying allowed!", file=protecc)
            
    

    @commands.command(name='hello')
    async def hello(self, ctx):
        await ctx.channel.send("Hello there, {0}".format(ctx.author.mention))
        

    @commands.command(name='spank')
    async def spank(self, ctx):
        
        if ctx.guild.id in serious:
            await ctx.send('Server is serious')
        if not ctx.guild.id in serious:
            await ctx.channel.send("Uhnnn, why would you spank me, Master? Did I do anything wrong?")
            

def setup(bot):
    bot.add_cog(fun(bot))