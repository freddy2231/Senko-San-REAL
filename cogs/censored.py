import discord
from discord.ext import commands
import json 
from time import strftime, gmtime

def write_t(id):
    p = json.load(open('censored_guilds.json', 'r'))

    p[f"{id}"]=True

    json.dump(p, open('censored_guild.json', 'r'),sort_keys=True,indent=4)

def write_f(id):
    p = json.load(open('censored_guilds.json', 'r'))

    p[f"{id}"]=False

    json.dump(p, open('censored_guild.json', 'r'),sort_keys=True,indent=4)

censor = json.load(open('censored_guild.json', 'r'))



class censored(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded censor cog')

    async def on_message(self, message): 
        if message.author == self.bot.user:
            return
            #so the bot doesn't respond to itself
        bad_words = {}
        bad_words[0] = "fuck"
        bad_words[1] = "faggot"
        bad_words[2] = "nigger"
        bad_words[3] = "shit"
        bad_words[4] = "cunt"
        bad_words[5] = "bitch"
        bad_words[6] = "retard"
        bad_words[7] = "arnold"
        bad_words[8] = "asshole" 

        censored = False
        if message.guild.id in censor:
            censored = True
            if censored:
                for word in bad_words:
                    if bad_words[word] in message.content.lower():
                        await message.delete()
                        await message.channel.send("That's really funny bud.")
        self.bot.process_commands(message)

    @commands.command(name='guildIsCensored')
    async def guildIsCensored(self, ctx):
        if not(ctx.guild.id in censor):
            write_t(ctx.guild.id)
            await ctx.send("I will censor this server.")
            

        else:
            await ctx.send("Guild is already censored!")
            

    @commands.command(name='guildIsNotCensored')
    async def guildIsNotCensored(self, ctx):
        if ctx.guild.id in censor:
            write_f(ctx.guild.id)
            await ctx.send("Tehehe")
            

        else:
            await ctx.send("This server is already not censored!")
            

    @commands.command(name='getCensoredGuilds')
    async def getCensoredGuilds(self, ctx):
        if ctx.author.id == 219987389135716364 or 597420184122294272 or 361143836598337546:
            await ctx.send(censor)
            
        else:
            await ctx.send('No permissions')

def setup(bot):
    bot.add_cog(censored(bot))