# Work with Python 3.6
import discord
from discord.ext import commands
from webserver import keep_alive
import os
import random

bot = commands.Bot(command_prefix = "s$")
bot.remove_command('help')

  
#SERIOUS GUILD COMMANDS

bot.serious_guilds = [688534403260874873]

@bot.command(name='guildIsSerious')
async def guildIsSerious(ctx):
    if not(ctx.guild.id in bot.serious_guilds):
        bot.serious_guilds.append(ctx.guild.id)
        print("guild was changed to serious", ctx.author.name,  ctx.guild.id, ctx.guild.name)
        await ctx.send("I will behave in this server.")
    else:
        print("guild attempted and failed to be changed to serious (already serious)", ctx.author.name,  ctx.guild.id, ctx.guild.name)
        await ctx.send("Guild is already serious!")

@bot.command(name='guildIsNotSerious')
async def guildIsNotSerious(ctx):
    if ctx.guild.id in bot.serious_guilds:
        bot.serious_guilds.remove(ctx.guild.id)
        await ctx.send("Tehehe")
        print("guild changed from serious to non serious", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    else:
        await ctx.send("This server is already not a serious server!")
        print("guild attempted and failed to change from serious to non serious (already non serious)", ctx.author.name,  ctx.guild.id, ctx.guild.name)

@bot.command(name='getSeriousGuilds')
async def getSeriousGuilds(ctx):
    await ctx.send(bot.serious_guilds)
    print("getSeriousGuilds", ctx.author.name,  ctx.guild.id, ctx.guild.name)

#DAD COMMANDS

bot.dad_guilds = []

@bot.command(name='guildHasDad')
async def guildHasDad(ctx):
    if not(ctx.guild.id in bot.dad_guilds):
        bot.dad_guilds.append(ctx.guild.id)
        print("guild has dad", ctx.author.name,  ctx.guild.id, ctx.guild.name)
        await ctx.send("DadBot activated.")
    else:
        print("guild attempted and failed to have dad (already has dad)", ctx.author.name,  ctx.guild.id, ctx.guild.name)
        await ctx.send("DadBot already on!")

@bot.command(name='guildHasNoDad')
async def guildHasNoDad(ctx):
    if ctx.guild.id in bot.dad_guilds:
        bot.dad_guilds.remove(ctx.guild.id)
        await ctx.send("Your dad left you")
        print("guild changed from dad to no dad", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    else:
        await ctx.send("This server already has  no dad!")
        print("guild attempted and failed to change from dad to not dad (already non dad)", ctx.author.name,  ctx.guild.id, ctx.guild.name)

@bot.command(name='getDadGuilds')
async def getDadGuilds(ctx):
    await ctx.send(bot.dad_guilds)
    print("getDadGuilds", ctx.author.name,  ctx.guild.id, ctx.guild.name)

#CENSORED GUILD COMMANDS

bot.censored_guilds = []

@bot.command(name='guildIsCensored')
async def guildIsCensored(ctx):
    if not(ctx.guild.id in bot.censored_guilds):
        bot.censored_guilds.append(ctx.guild.id)
        await ctx.send("I will censor this server.")
        print("guild changed to censored", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    else:
        await ctx.send("Guild is already censored!")
        print("guild attempted and failed to change to censored (already censored)", ctx.author.name,  ctx.guild.id, ctx.guild.name)

@bot.command(name='guildIsNotCensored')
async def guildIsNotCensored(ctx):
    if ctx.guild.id in bot.censored_guilds:
        bot.censored_guilds.remove(ctx.guild.id)
        await ctx.send("Tehehe")
        print("guild changed from censored to non censored", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    else:
        await ctx.send("This server is already not censored!")
        print("guild attempted and failed to change from censored to non censored (already non censored)", ctx.author.name,  ctx.guild.id, ctx.guild.name)

@bot.command(name='getCensoredGuilds')
async def getCensoredGuilds(ctx):
    await ctx.send(bot.censored_guilds)
    print("getCensoredGuilds", ctx.author.name,  ctx.guild.id, ctx.guild.name)

#BRUH DETECTOR COMMANDS

bot.bruh_guilds = [688534403260874873]

@bot.command(name='guildIsNotBruh')
async def guildIsBruh(ctx):
    if not(ctx.guild.id in bot.bruh_guilds):
        bot.bruh_guilds.append(ctx.guild.id)
        await ctx.send("I will not detect bruh moments in this server.")
        print("guild changed to not bruh", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    else:
        await ctx.send("Guild already does not detect bruh moments!")
        print("guild attempted and failed to change to not bruh (already not bruh)", ctx.author.name,  ctx.guild.id, ctx.guild.name)

@bot.command(name='guildIsBruh')
async def guildIsNotBruh(ctx):
    if (ctx.guild.id in bot.bruh_guilds):
        bot.bruh_guilds.remove(ctx.guild.id)
        await ctx.send("Tehehe")
        print("guild changed to bruh", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    else:
        await ctx.send("I already do not detect bruh moments on this server!")
        print("guild attempted and failed to change to bruh (already bruh)", ctx.author.name,  ctx.guild.id, ctx.guild.name)

@bot.command(name='getBruhGuilds')
async def getBruhGuilds(ctx):
    await ctx.send(bot.bruh_guilds)
    print("getBruhGuilds", ctx.author.name,  ctx.guild.id, ctx.guild.name)

#COMMANDS

@bot.command(name='hello')
async def hello(ctx):
    await ctx.channel.send("Hello there, {0}".format(ctx.author.mention))
    print("s$hello", ctx.author.name,  ctx.guild.id, ctx.guild.name)

@bot.command(name='spank')
async def spank(ctx):
    serious = False
    if ctx.guild.id in bot.serious_guilds:
        print("s$spank failed: guild was serious", ctx.author.name,  ctx.guild.id, ctx.guild.name)
        serious = True
    if not serious:
        await ctx.channel.send("Uhnnn, why would you spank me, Master? Did I do anything wrong?")
        print("s$spank", ctx.author.name,  ctx.guild.id, ctx.guild.name)

@bot.command(name='dance')
async def dance(ctx):
    serious = False
    if ctx.guild.id in bot.serious_guilds:
        serious = True
        print("s$dance failed: guild was serious", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    if not serious:
        danceGIF = discord.File("sDance.gif")
        await ctx.channel.send(file=danceGIF)
        print("s$dance", ctx.author.name,  ctx.guild.id, ctx.guild.name)

@bot.command(name='pat')
async def pat(ctx):
    patGIF = discord.File("sPAT.gif")
    await ctx.channel.send(file=patGIF)
    print("s$pat", ctx.author.name,  ctx.guild.id, ctx.guild.name)

bot.the_hated = []
@bot.command(name='hate')
async def hate(ctx, person:discord.Member):
    serious = False
    if ctx.guild.id in bot.serious_guilds:
        serious = True
        print("s$hate failed: guild was serious", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    if not serious:
        if not(person in bot.the_hated):
            bot.the_hated.append(person)
            await ctx.send("Added!")
            print("s$hate: added user", ctx.author.name,  ctx.guild.id, ctx.guild.name)
            return
        else: 
            await ctx.channel.send("That person is already on the list!")
            print("s$hate failed: user already added", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    else:
        pass
    

@bot.command(name='hate_remove')
async def hate_remove(ctx, person:discord.Member):
    serious = False
    if ctx.guild.id in bot.serious_guilds:
        serious = True
        print("s$hate_remove failed: guild was serious", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    if not serious:
        if (person in bot.the_hated):
            bot.the_hated.remove(person)
            await ctx.send("Removed!")
            print("s$hate: user was removed", ctx.author.name,  ctx.guild.id, ctx.guild.name)
            return
        else: 
            await ctx.channel.send("That person isn't hated (yet...)")
            print("s$hate_removed failed: not added on list", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    else:
        pass

@bot.command(name='hate_list')
async def hate_list(ctx):
    serious = False
    if ctx.guild.id in bot.serious_guilds:
        serious = True
        print("s$hate_list failed: guild was serious", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    if not serious:
        await ctx.send(bot.the_hated)
        print("s$hate_list", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    else:
        pass

bot.number = 691010171828437025
@bot.command(name='love')
async def love(ctx, *, personM:discord.Member):
    serious = False
    if ctx.guild.id in bot.serious_guilds:
        serious = True
        print("s$love failed: guild was serious", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    if not serious:
        loveGIF = discord.File("senkoLove.gif")
        for register in bot.the_hated:
            if personM in bot.the_hated:
                loveGIF = discord.File("sMAD.gif")
                await ctx.channel.send(f"Shut the fuck up, {personM.mention} does not deserve love", file=loveGIF)
                print("s$love: user doesn't deserve love", ctx.author.name,  ctx.guild.id, ctx.guild.name)
                return

        if personM.id == bot.number:
            loveGIF = discord.File("sLove.gif")
            await ctx.channel.send(f"I love you too, {ctx.author.mention}", file=loveGIF)
            print("s$love: love senko", ctx.author.name,  ctx.guild.id, ctx.guild.name)

        elif personM.id == ctx.author.id:
            loveGIF == discord.File("senkoLove.gif")
            await ctx.channel.send(f"You must love yourself a lot, {personM.mention}", file=loveGIF)
            print("s$love: user loved themselves", ctx.author.name,  ctx.guild.id, ctx.guild.name)

        else:
            loveGIF = discord.File("senkoLove.gif")
            await ctx.channel.send(f"{ctx.author.mention} loves you, {personM.mention}", file=loveGIF)
            print("s$love: user loved other user", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    else:
        pass

@bot.command(name="fluff")
async def fluff(ctx):
    serious = False
    if ctx.guild.id in bot.serious_guilds:
        serious = True
        print("s$fluff failed: guild was serious", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    if not serious:
        gifnum = random.randint(0,2)
        if gifnum == 0:
            fluffy = discord.File("sFluff1.png")
            await ctx.channel.send(file=fluffy)
        if gifnum == 1:
            fluffy = discord.File("sFluff3.jpg")
            await ctx.channel.send(file=fluffy)
        if gifnum == 2:
            fluffy = discord.File("sFluff4.jpg")
            await ctx.channel.send(file=fluffy)
        print("s$fluff", ctx.author.name,  ctx.guild.id, ctx.guild.name)

@bot.command(name='hug')
async def hug(ctx):
    serious = False
    if ctx.guild.id in bot.serious_guilds:
        serious = True
        print("s$hug failed: guild was serious", ctx.author.name,  ctx.guild.id, ctx.guild.name)
    if not serious:
        hugGIF = discord.File("sHug.gif")
        await ctx.channel.send(file=hugGIF)
        print("s$hug", ctx.author.name,  ctx.guild.id, ctx.guild.name)

    
#HELP
        
@bot.command(name='help')
async def help(ctx):
    gold = discord.Colour.gold()
    helper = discord.Embed(title='Senko-san', description='wh-what would you like to do with me uwu\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!', colour=gold)
    commands = {}
    #Command help
    commands['s$hello'] = "Returns a greeting and mention"
    #commands['s$remind <game> <day> <time>'] = "Sets a reminder for a game"
    commands['s$love @user'] = "Send some love to another user, or, if they're hated, send some hate ( •̀ᴗ•́ )و ̑̑. If you want some love yourself, try s$love @Senko-San"
    commands['s$hate @user'] = "Add a user to the hate list"
    commands['s$hate_remove @user'] = "Remove a user from the hate list"
    commands['s$pat'] = "Pat Senko!"
    commands['s$hug'] = "Hug Senko!"
    commands['s$fluff'] = "Fluff Senko!"
    commands['s$dance'] = "Let Senko dance!"
    commands['s$guildIsNotBruh'] = "Senko will no longer detect bruh moments in this server"
    commands['s$guildIsBruh'] = "Senko will detect bruh moments in this server (default)"
    commands['s$guildHasNoDad'] = "Senko will no longer be a dad (default)"
    commands['s$guildHasDad'] = "Senko will become a dad"
    commands['s$guildIsSerious'] = "Senko will not use love/hate features and other things"
    commands['s$guildIsNotSerious'] = "Senko will use the above features (default)"
    commands['s$guildIsCensored'] = "Senko will censor bad words"
    commands['s$guildIsNotCensored'] = "Senko will not censor bad words (default)"

    commands['Passive Commands:'] = "_______________________________________________________________________________________"

    #Passive help
    commands['"Bruh Detector"'] = "Detects bruh moments. (Triggers when someone says 'bruh' "
    commands['"DadBot"'] = "It's our dad"
    commands['"Censor"'] = "Censors bad words"
    commands['"Senko"'] = "Just say, 'Hello/Hi Senko, I'm home!' or 'Just came back from work.' or 'I had a long day'. Then respond if she says she made dinner, asking 'What's for dinner?' or tell her how your day went!"
    

    for command, description in commands.items():
        helper.add_field(name=command,value=(description + "\n"), inline=False)
    await ctx.channel.send(embed = helper)
    print("s$help", ctx.author.name,  ctx.guild.id, ctx.guild.name)

#ON_MESSAGE COMMANDS

@bot.event
async def on_message(message): 
    if message.author == bot.user:
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

    censor = False
    if message.guild.id in bot.censored_guilds:
        censor = True
    if censor:
        for word in bad_words:
            if bad_words[word] in message.content.lower():
                print("word has been censored")
                await message.delete()
                await message.channel.send("That's really funny bud.")
                print("message deleted: bad word", message.author.name, message.guild.id, message.guild.name)
    if message.content.lower().startswith("k$"):
        print("tried to use k$", message.author.name, message.guild.id, message.guild.name)
        await message.channel.send("My master changed the command prefix used to summon me. Try typing 's$' before your command!")
        #for updated command
        
    bruh = False
    if message.guild.id in bot.bruh_guilds:
        bruh = True
    if not bruh:
        if  "bruh" in message.content.lower():
            if not ("s$guildIsBruh" in message.content or "s$guildIsNotBruh" in message.content or "s$getBruhGuilds" in message.content):
                bruhImg=discord.File('bruh.jpg')
                await message.channel.send(f"That's quite a bruh moment {message.author.mention}!", file=bruhImg)
                print("bruh moment detected", message.author.name, message.guild.id, message.guild.name)
                
                #bruh detector, sends msg and file

    serious = False
    if message.guild.id in bot.serious_guilds:
        serious = True
    if not serious:
        if ("i love you senko" in message.content.lower()) or ("i love you senkosan" in message.content.lower()):
            await message.channel.send(f"I love you too, {message.author.mention}")
            print("user said i love you senko,senko replied", message.author.name, message.guild.id, message.guild.name)
    else:
        pass

    
    dad = False
    if message.guild.id in bot.dad_guilds:
      dad = True
    if dad:
      if ("i'm" in message.content.lower()) or ("i’m" in message.content.lower() or ("im" in message.content.lower())):
          msg = message.content
          if "i’m" in msg.lower():
              if not("i’m" in msg):
              #if it has a capital somewhere in "i'm" which would prevent the bot
              #from replacing the "i'm"
                  if "I’m" in msg:
                      msg = msg.replace("I’m", "i’m")
                  if "I’M" in msg:
                      msg = msg.replace("I’M", "i’m")
                  if "i’M" in msg:
                      msg = msg.replace("i’M", "i’m")
              msg = msg[(msg.index("i’m")):]
              msg = msg.replace("i’m", "")
              await message.channel.send("Hi{0}, I'm dad!".format(msg))
              print("dad bot used", message.author.name, message.guild.id, message.guild.name)
          elif "i'm" in msg.lower():
              if not("i'm" in msg):
                  if "I'm" in msg:
                      msg = msg.replace("I'm", "i'm")
                  if "I'M" in msg:
                      msg = msg.replace("I'M", "i'm")
                  if "i'M" in msg:
                      msg = msg.replace("i'M", "i'm")
              msg = msg[(msg.index("i'm")):]
              msg = msg.replace("i'm", "")
              await message.channel.send("Hi{0}, I'm dad!".format(msg))
              print("dad bot used", message.author.name, message.guild.id, message.guild.name)
          elif (" im " in msg.lower())  or (msg.lower().startswith("im ")):
              if (not ("im" in msg)) or (not (msg.startswith("im"))):
                  if "Im" in msg:
                      msg = msg.replace("Im", "im")
                  if "IM" in msg:
                      msg = msg.replace("IM", "im")
                  if "iM" in msg:
                      msg = msg.replace("iM", "im")
                  if msg.startswith("Im"):
                      msg = "im" + msg[1:]
                  if msg.startswith("iM"):
                      msg = "im" + msg[1:]
                  if msg.startswith("IM"):
                      msg = "im" + msg[1:]
              msg = msg[(msg.index("im")):]
              msg = msg.replace("im", "")
              await message.channel.send("Hi{0}, I'm dad!".format(msg))
              print("dad bot used", message.author.name, message.guild.id, message.guild.name)


    clean_message = message.content.replace("'", "").lower().replace("’", "").replace(",","")

    responses = ["Welcome home dear!", "I've been waiting for you! Dinner's ready to eat!", "How was your day at work?"]

    true_channel = message.channel
    true_author = message.author
    if ("hi senko im home" in clean_message) or ("hello senko im home" in clean_message) or ("just came back from work" in clean_message) or ("i had a long day" in clean_message):

      num = random.randint(0,2)
      home = discord.File("sHome.png")
      await message.channel.send(responses[num],file=home)
      print("conversation began with senko", message.author.name, message.guild.id, message.guild.name)
      def check1(message):
        return message.author == true_author and message.channel == true_channel and "whats for dinner" in message.content.lower().replace("'", "").replace("’", "").replace(",","")
      def check2good(message):
        return message.author == true_author and message.channel == true_channel and ("good" in message.content.lower() or "great" in message.content.lower() or "super" in message.content.lower() or "amazing" in message.content.lower())
      def check2bad(message):
        return message.author == true_author and message.channel == true_channel and ("bad" in message.content.lower() or "horrible" in message.content.lower() or "sad" in message.content.lower())

      if num == 1:
          await bot.wait_for('message', check=check1)
          food = discord.File("sFood.jpg")
          await message.channel.send(f"Your favorite!",file=food)
      if num == 2:
        await bot.wait_for('message', check=check2good)
        await message.channel.send("That's great! Now come let me pamper you!")
      if num == 2:
        await bot.wait_for('message', check=check2bad)
        fluff = discord.File("senko6.png")
        await message.channel.send("Aww...that's okay. I'll let you fluff my tail to make you feel better",file=fluff)
        
        

      
      

    await bot.process_commands(message)


@bot.event
async def on_ready():
    status = discord.Game("type s$help for a list of commands!")
    await bot.change_presence(status=discord.Status.online, activity=status)
    print('\nLogged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
keep_alive()
bot.run(os.environ.get("TOKEN"))
