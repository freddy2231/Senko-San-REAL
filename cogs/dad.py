import discord
from discord.ext import commands
import json
from time import gmtime, strftime
import random

dad = json.load(open('dad_guilds.json', 'r'))

def true_dad(guild):
    lol = json.load(open('dad_guilds.json', 'r'))
    lol[f"{guild}"]=True
    json.dump(lol, open('dad_guilds.json', 'r'),sort_keys=True,indent=4)

def false_dad(guild):
    huh = open('dad_guilds.json', 'r')

    if guild in huh:
        huh[guild] = False
    json.dump(huh, open('dad_guilds.json', 'r'),sort_keys=True,indent=4)







class dadcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded dadcog cog!")

    async def on_message(self, message):
        if not message.guild.id in dad:
            pass
        else:
            ea = False
            if message.guild.id in dad:
                ea = True
            dad_message = message.content.lower().replace("i'm ", "im ").replace("i’m ", "im ")
            if ea:
                if "im " in dad_message:
                    dad_message = dad_message[(dad_message.index("im ")):]
                    dad_message = dad_message.replace("im ", "")
                    await message.channel.send("Hi {0}, I'm dad!".format(dad_message))
                    
        self.bot.process_commands(message)
    #commands code starts here V

    #commands code ends here ^

    @commands.command(name='guildHasDad')
    async def guildHasDad(self, ctx):
        if not ctx.guild.id in dad:
            true_dad(ctx.guild.id)
            
            await ctx.send("Dadbot activated.")
        else:
            
            await ctx.send("Dadbot already on!")

    @commands.command(name='guildHasNoDad')
    async def guildHasNoDad(self, ctx):
        if ctx.guild.id in dad:
            false_dad(ctx.guild.id)
            await ctx.send("Your dad left you")
            

        else:
            await ctx.send("This server already has no dad!")
            

    @commands.command(name='getDadGuilds')
    async def getDadGuilds(self, ctx):
        if ctx.author.id == 219987389135716364 or 597420184122294272 or 361143836598337546:
            await ctx.send(dad)
            

    @commands.command(name='dad_joke')
    async def dad_joke(self, ctx):
        if ctx.guild.id in dad:
            dad_responses = ["Why was the stadium so cool? Because it was filled with fans!", "Why can't you hear a pterodactyl using the bathroom? Because the 'P' was silent!", "My dad was chopping onions. Onions was a good dog.", "What do you call a fish with no eyes? A fsh!", "What happened to the Italian chef? He pasta way!", "They ask me, why don't I tell egg jokes? Because they always get cracked up!", "Why was the mathbook always depressed? Because his parents were divorced and his grades were falling due to the stress and neither of his parents cared about him so he spiraled into a never-ending self-pity party, in which he could never return from. Just kidding! Because it's filled with problems!", "Someone asked to call their parents on my phone, but now it's broken. They really didn't need to stand on it to make the call!", "Did you hear about the guy who invented the knock-knock joke? He won the 'no-bell' prize!", "A family of elephants walk into a bar. What do they take? A lot of space!", "If a child refuses to sleep during nap time, are they guilty of resisting a rest?", "What sound does a plane make when it crashes? Boeing!", "I got into a fight with a guy who hit me with a bat. I didn't know these animals hurt that much!", "É pave ou pa cume?"]
            num = random.randint(0,len(dad_responses)-1)
            await ctx.channel.send(dad_responses[num])
            
        else:
            await ctx.send('Server does not have dad')

def setup(bot):
    bot.add_cog(dadcog(bot))