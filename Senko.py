# Work with Python 3.6
import discord
from discord.ext import commands
from webserver import keep_alive
import os
import asyncio
import random
from time import gmtime, strftime

bot = commands.Bot(command_prefix = "s$")
bot.remove_command('help')

  
#SERIOUS GUILD COMMANDS

bot.serious_guilds = [688534403260874873]

@bot.command(name='guildIsSerious')
async def guildIsSerious(ctx):
  if not(ctx.guild.id in bot.serious_guilds):
    bot.serious_guilds.append(ctx.guild.id)
    record_stats("guild was changed to serious", ctx)
    await ctx.send("I will behave in this server.")
  else:
    record_stats("guild attempted and failed to be changed to serious (already serious)", ctx)
    await ctx.send("Guild is already serious!")

@bot.command(name='guildIsNotSerious')
async def guildIsNotSerious(ctx):
  if ctx.guild.id in bot.serious_guilds:
    bot.serious_guilds.remove(ctx.guild.id)
    await ctx.send("Tehehe")
    record_stats("guild changed from serious to non serious", ctx)
  else:
    await ctx.send("This server is already not a serious server!")
    record_stats("guild attempted and failed to change from serious to non serious (already non serious)", ctx)

@bot.command(name='getSeriousGuilds')
async def getSeriousGuilds(ctx):
  await ctx.send(bot.serious_guilds)
  record_stats("getSeriousGuilds", ctx)

#DAD COMMANDS

bot.dad_guilds = []

@bot.command(name='guildHasDad')
async def guildHasDad(ctx):
  if not(ctx.guild.id in bot.dad_guilds):
    bot.dad_guilds.append(ctx.guild.id)
    record_stats("guild has dad", ctx)
    await ctx.send("DadBot activated.")
  else:
    record_stats("guild attempted and failed to have dad (already has dad)", ctx)
    await ctx.send("DadBot already on!")

@bot.command(name='guildHasNoDad')
async def guildHasNoDad(ctx):
  if ctx.guild.id in bot.dad_guilds:
    bot.dad_guilds.remove(ctx.guild.id)
    await ctx.send("Your dad left you")
    record_stats("guild changed from dad to no dad", ctx)

  else:
    await ctx.send("This server already has no dad!")
    record_stats("guild attempted and failed to change from dad to not dad (already non dad)", ctx)

@bot.command(name='getDadGuilds')
async def getDadGuilds(ctx):
  await ctx.send(bot.dad_guilds)
  record_stats("getDadGuilds", ctx)

@bot.command(name='dad_joke')
async def dad_joke(ctx):
  if ctx.guild.id in bot.dad_guilds:
    dad_responses = ["Why was the stadium so cool? Because it was filled with fans!", "Why can't you hear a pterodactyl using the bathroom? Because the 'P' was silent!", "My dad was chopping onions. Onions was a good dog.", "What do you call a fish with no eyes? A fsh!", "What happened to the Italian chef? He pasta way!", "They ask me, why don't I tell egg jokes? Because they always get cracked up!", "Why was the mathbook always depressed? Because his parents were divorced and his grades were falling due to the stress and neither of his parents cared about him so he spiraled into a never-ending self-pity party, in which he could never return from. Just kidding! Because it's filled with problems!", "Someone asked to call their parents on my phone, but now it's broken. They really didn't need to stand on it to make the call!", "Did you hear about the guy who invented the knock-knock joke? He won the 'no-bell' prize!", "A family of elephants walk into a bar. What do they take? A lot of space!", "If a child refuses to sleep during nap time, are they guilty of resisting a rest?", "What sound does a plane make when it crashes? Boeing!", "I got into a fight with a guy who hit me with a bat. I didn't know these animals hurt that much!", "É pave ou pa cume?"]
    num = random.randint(0,len(dad_responses)-1)
    await ctx.channel.send(dad_responses[num])
    record_stats("dad joke called", ctx)
  else:
    record_stats("dad joke attempted and failed: no dad", ctx)


#CENSORED GUILD COMMANDS

bot.censored_guilds = []

@bot.command(name='guildIsCensored')
async def guildIsCensored(ctx):
  if not(ctx.guild.id in bot.censored_guilds):
    bot.censored_guilds.append(ctx.guild.id)
    await ctx.send("I will censor this server.")
    record_stats("guild changed to censored", ctx)

  else:
    await ctx.send("Guild is already censored!")
    record_stats("guild attempted and failed to change to censored (already censored)", ctx)

@bot.command(name='guildIsNotCensored')
async def guildIsNotCensored(ctx):
  if ctx.guild.id in bot.censored_guilds:
    bot.censored_guilds.remove(ctx.guild.id)
    await ctx.send("Tehehe")
    record_stats("guild changed from censored to non censored", ctx)

  else:
    await ctx.send("This server is already not censored!")
    record_stats("guild attempted and failed to change from censored to non censored (already non censored)", ctx)

@bot.command(name='getCensoredGuilds')
async def getCensoredGuilds(ctx):
  await ctx.send(bot.censored_guilds)
  record_stats("getCensoredGuilds", ctx)

#BRUH DETECTOR COMMANDS

bot.bruh_guilds = [688534403260874873]

@bot.command(name='guildIsNotBruh')
async def guildIsBruh(ctx):
  if not(ctx.guild.id in bot.bruh_guilds):
    bot.bruh_guilds.append(ctx.guild.id)
    await ctx.send("I will not detect bruh moments in this server.")
    record_stats("guild changed to not bruh", ctx)
  else:
    await ctx.send("Guild already does not detect bruh moments!")
    record_stats("guild attempted and failed to change to not bruh (already not bruh)", ctx)

@bot.command(name='guildIsBruh')
async def guildIsNotBruh(ctx):
  if (ctx.guild.id in bot.bruh_guilds):
    bot.bruh_guilds.remove(ctx.guild.id)
    await ctx.send("Tehehe")
    record_stats("guild changed to bruh", ctx)
  else:
    await ctx.send("I already do not detect bruh moments on this server!")
    record_stats("guild attempted and failed to change to bruh (already bruh)", ctx)

@bot.command(name='getBruhGuilds')
async def getBruhGuilds(ctx):
  await ctx.send(bot.bruh_guilds)
  record_stats("getBruhGuilds", ctx)


#COMMANDS

@bot.command(name='hello')
async def hello(ctx):
  await ctx.channel.send("Hello there, {0}".format(ctx.author.mention))
  record_stats("s$hello", ctx)

@bot.command(name='spank')
async def spank(ctx):
  serious = False
  if ctx.guild.id in bot.serious_guilds:
    record_stats("s$spank failed: guild was serious", ctx)
    serious = True
  if not serious:
    await ctx.channel.send("Uhnnn, why would you spank me, Master? Did I do anything wrong?")
    record_stats("s$spank", ctx)

@bot.command(name="how_many_guilds")
async def how_many_guilds(ctx):
  await ctx.channel.send(len(bot.guilds))
  
@bot.command(name='dance')
async def dance(ctx):
  serious = False
  if ctx.guild.id in bot.serious_guilds:
    serious = True
    record_stats("s$dance failed: guild was seriouss", ctx)
  if not serious:
    danceGIF = discord.File("sDance.gif")
    await ctx.channel.send(file=danceGIF)
    record_stats("s$dance", ctx)

@bot.command(name='pat')
async def pat(ctx):
  patGIF = discord.File("sPAT.gif")
  await ctx.channel.send(file=patGIF)
  record_stats("s$pat", ctx)

bot.the_hated = []
@bot.command(name='hate')
async def hate(ctx, person:discord.Member):
  serious = False
  if ctx.guild.id in bot.serious_guilds:
    serious = True
    record_stats("s$hate failed: guild was serious", ctx)
  if not serious:
    if not(person in bot.the_hated):
      bot.the_hated.append(person)
      await ctx.send("Added!")
      record_stats("s$hate: added user", ctx)
      return
    else: 
      await ctx.channel.send("That person is already on the list!")
      record_stats("s$hate failed: user already added", ctx)
  else:
      pass
    

@bot.command(name='hate_remove')
async def hate_remove(ctx, person:discord.Member):
  serious = False
  if ctx.guild.id in bot.serious_guilds:
    serious = True
    record_stats("s$hate_remove failed: guild was serious", ctx)
  if not serious:
    if (person in bot.the_hated):
      bot.the_hated.remove(person)
      await ctx.send("Removed!")
      record_stats("s$hate: user was removed", ctx)
      return
    else: 
      await ctx.channel.send("That person isn't hated (yet...)")
      record_stats("s$hate_removed failed: not added on list", ctx)
  else:
      pass

@bot.command(name='hate_list')
async def hate_list(ctx):
  serious = False
  if ctx.guild.id in bot.serious_guilds:
    serious = True
    record_stats("s$hate_list failed: guild was serious", ctx)
  if not serious:
    await ctx.send(bot.the_hated)
    record_stats("s$hate_list", ctx)
  else:
    pass

bot.number = 691010171828437025
@bot.command(name='love')
async def love(ctx, *, personM:discord.Member):
  #print("break 1")
  serious = False
  if ctx.guild.id in bot.serious_guilds:
    #print("break 2")
    serious = True
    record_stats("s$love failed: guild was serious", ctx)
  if not serious:
    #print("break 3")
    loveGIF = discord.File("senkoLove.gif")
    for register in bot.the_hated:
      if personM in bot.the_hated:
        #print("break 4")
        loveGIF = discord.File("sMAD.gif")
        await ctx.channel.send(f"Shut up, {personM.mention} does not deserve love", file=loveGIF)
        record_stats("s$love: user doesn't deserve love", ctx)
        return

    if personM.id == bot.number:
      #print("break 5")
      loveGIF = discord.File("sLove.gif")
      await ctx.channel.send(f"I love you too, {ctx.author.mention}", file=loveGIF)
      record_stats("s$love: love senko", ctx)
      return

    elif personM.id == ctx.author.id:
      #print("break 6")
      loveGIF == discord.File("senkoLove.gif")
      await ctx.channel.send(f"You must love yourself a lot, {personM.mention}", file=loveGIF)
      record_stats("s$love: user loved themselves", ctx)

    else:
      #print("break 7")
      loveGIF = discord.File("senkoLove.gif")
      await ctx.channel.send(f"{ctx.author.mention} loves you, {personM.mention}", file=loveGIF)
      record_stats("s$love: user loved other user", ctx)
  else:
    pass

@bot.command(name="fluff")
async def fluff(ctx):
  serious = False
  if ctx.guild.id in bot.serious_guilds:
    serious = True
    record_stats("s$fluff failed: guild was serious", ctx)
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
    record_stats("s$fluff", ctx)

@bot.command(name="hug")
async def hug(ctx):
  serious = False
  if ctx.guild.id in bot.serious_guilds:
    serious = True
    record_stats("s$hug failed: guild was serious", ctx)
  if not serious:
      hugGIF = discord.File("sHug.gif")
      await ctx.channel.send(file=hugGIF)
      record_stats("s$hug", ctx)

@bot.command(name="protecc")
async def protecc(ctx):
  serious = False
  if ctx.guild.id in bot.serious_guilds:
    serious = True
    record_stats("s$protecc failed: guild was serious", ctx)
  if not serious:
      protecc = discord.File("sJOJO.png")
      await ctx.channel.send("No bullying allowed!", file=protecc)
      record_stats("s$protecc", ctx)

#Invites
@bot.command(name="bot_invite")
async def bot_invite(ctx):
  invite_embed = discord.Embed(title='Invite Link!', description="A link to invite Senko to your server!", url="https://discord.com/oauth2/authorize?client_id=691010171828437025&permissions=8&scope=bot" )
  await ctx.channel.send(embed=invite_embed)
  record_stats("bot invite link called", ctx)

@bot.command(name="discord_invite")
async def discord_invite(ctx):
  discordinvite_embed = discord.Embed(title='Invite Link!', url="https://discord.gg/dtNdafD", description='A link to the discord server dedicated to Senko, Senko\'s Playground!')
  await ctx.channel.send(embed=discordinvite_embed)
  record_stats("discord invite link called", ctx)
    
#HELP
@bot.command(name='help')
async def help(ctx):
  record_stats("s$help", ctx)
  commands = {}
  gold = discord.Colour.gold()
  #print("break 1")
  helper = discord.Embed(title='Senko-san', description='wh-what would you like to do with me uwu\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!', colour=gold)
  #Command help
  commands['s$hello'] = "Returns a greeting and mention"
  commands['s$love @user'] = "Send some love to another user, or, if they're hated, send some hate ( •̀ᴗ•́ )و ̑̑. If you want some love yourself, try s$love @Senko-San"
  commands['s$hate @user'] = "Add a user to the hate list"
  commands['s$hate_remove @user'] = "Remove a user from the hate list"
  commands['s$pat'] = "Pat Senko!"
  commands['s$hug'] = "Hug Senko!"
  commands['s$fluff'] = "Fluff Senko!"
  commands['s$dance'] = "Let Senko dance!"
  commands['s$bot_invite'] = "Link for you to add Senko to your server!"
  commands['s$discord_invite'] = "Link for you to join the Discord!"

  commands['Passive Activity:'] = "___________"

  commands['"Bruh Detector"'] = "Detects bruh moments. (\"s$help_bruh\" for more info! )"
  commands['"DadBot"'] = "Will respond to certain messages. (\"s$help_dadbot\" for more info!) "
  commands['"Censor"'] = "Censors bad words. (\"s$help_censor\" for more info!)"
  commands['"Senko"'] = "Your personal Senko! (\"s$help_senko\" for more info!)"
  commands['"Serious"'] = "Serious mode limits commands Senko will respond to. (\"s$help_serious\" for more info!)"
  #print("break 2")
  for command, description in commands.items():
    helper.add_field(name=command,value=(description + "\n"), inline=False)
    #print("break 3")
  #print("break 4")
  await ctx.channel.send(embed = helper)

@bot.command(name='help_dadbot')
async def help_dadbot(ctx):
    record_stats("s$help", ctx)
    commands = {}
    gold = discord.Colour.gold()

    helper = discord.Embed(title='DadBot', description='Your own personal DadBot! (Disclaimer: will not replace your biological dad, but it will try!\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!', colour=gold)
    commands['s$dad_joke'] = "Senko tells a dad joke!"
    commands['s$guildHasNoDad'] = "Senko will no longer be a dad (default)"
    commands['s$guildHasDad'] = "Senko will become a dad"
    commands['DadBot (Passive Activity'] = "If Senko is a Dad, she (he?) will respond to messages like this:\nUser: Wow, I'm really tired\nSenko-san: Hi really tired, I'm dad!"
    for command, description in commands.items():
        helper.add_field(name=command,value=(description + "\n"), inline=False)
    await ctx.channel.send(embed = helper)

@bot.command(name="help_senko")
async def help_senko(ctx):
    commands = {}
    gold = discord.Colour.gold()
    helper = discord.Embed(title='Senko-san', description='Your very own senko interactions!\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!', colour=gold)
    commands['Senko-san'] = "Senko will respond to many different trigger phrases. Some of them allow you to reply back, after which she will reply once more."
    commands['"Hello/Hi Senko, I\'m home!", "I had a long day", or "Just came back from work"'] = "Senko will respond with one of three responses. You can then ask her what's for dinner, or tell her how your day went using simple descriptors."
    commands['"Good morning Senko!"'] = "Senko will respond with one of three responses. You can then ask her what's for breakfast, or tell her how your sleep was using simple descriptors."
    commands['"Good night Senko!"'] = "Senko will respond with one of three responses."
    
    for command, description in commands.items():
        helper.add_field(name=command,value=(description + "\n"), inline=False)
    await ctx.channel.send(embed = helper)
@bot.command(name="help_censor")
async def help_censor(ctx):
    commands = {}
    gold = discord.Colour.gold()
    helper = discord.Embed(title='Censor Ability', description='Senko will censor bad words on your server!\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!', colour=gold)
    commands['s$guildIsCensored'] = "Senko will censor bad words"
    commands['s$guildIsNotCensored'] = "Senko will not censor bad words (default)"
    commands['Censor (Passive Activity)'] = "If Senko sees a message with a bad word in it, she will delete the message. **NOTE**: Senko must be a moderator in your server for this ability to work."
    for command, description in commands.items():
        helper.add_field(name=command,value=(description + "\n"), inline=False)
    await ctx.channel.send(embed = helper)

@bot.command(name="help_serious")
async def help_serious(ctx):
    commands = {}
    gold = discord.Colour.gold()
    helper = discord.Embed(title='Serious Passive', description='When you turn the Serious passive on, Senko will not respond to much of her commands.\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!', colour=gold)
    commands['s$guildIsSerious'] = "Senko will not use love/hate, pat, hug, etc etc commands."
    commands['s$guildIsNotSerious'] = "Senko will use the above features (default)"
    commands['Serious (Passive Activity)'] = "Senko will not respond most of her commands when serious. This is so that if Senko migrates to a more serious role in certain servers, she will be a better fit for that role."
    for command, description in commands.items():
        helper.add_field(name=command,value=(description + "\n"), inline=False)
    await ctx.channel.send(embed = helper)

@bot.command(name="help_bruh")
async def help_bruh(ctx):
    commands = {}
    gold = discord.Colour.gold()
    helper = discord.Embed(title='Bruh Detector', description='The Bruh Detector will detect bruh moments when enabled.\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!', colour=gold)
    commands['s$guildIsNotBruh'] = "Senko will no longer detect bruh moments in this server"
    commands['s$guildIsBruh'] = "Senko will detect bruh moments in this server (default)"
    commands['Bruh Detector'] = "Senko will respond anytime someone says \"bruh\" when the Bruh Detector is enabled."
    for command, description in commands.items():
      helper.add_field(name=command,value=(description + "\n"), inline=False)
    await ctx.channel.send(embed = helper)
    

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
                await message.delete()
                await message.channel.send("That's really funny bud.")
                record_stats("message deleted: bad word", message)
        
    bruh = False
    if message.guild.id in bot.bruh_guilds:
        bruh = True
    if not bruh:
        if  "bruh" in message.content.lower():
            if not ("s$guildIsBruh" in message.content or "s$guildIsNotBruh" in message.content or "s$getBruhGuilds" in message.content):
                bruhImg=discord.File('bruh.jpg')
                await message.channel.send(f"That's quite a bruh moment {message.author.mention}!", file=bruhImg)
                record_stats("bruh moment detected", message)
                
                #bruh detector, sends msg and file

    serious = False
    if message.guild.id in bot.serious_guilds:
        serious = True
    if not serious:
        if ("i love you senko" in message.content.lower()) or ("i love you senkosan" in message.content.lower()):
            await message.channel.send(f"I love you too, {message.author.mention}")
            record_stats("user said i love you senko,senko replied", message)
    else:
        pass

    
    dad = False
    if message.guild.id in bot.dad_guilds:
      dad = True
    dad_message = message.content.lower().replace("i'm ", "im ").replace("i’m ", "im ")
    if dad:
      if "im " in dad_message:
            dad_message = dad_message[(dad_message.index("im ")):]
            dad_message = dad_message.replace("im ", "")
            await message.channel.send("Hi {0}, I'm dad!".format(dad_message))
            record_stats("dad bot used", message)

    clean_message = message.content.replace("'", "").lower().replace("’", "").replace(",","")

    responses = ["Welcome home dear!", "I've been waiting for you! Dinner's ready to eat!", "How was your day at work?"]

    true_channel = message.channel
    true_author = message.author
    if ("hi senko im home" in clean_message) or ("hello senko im home" in clean_message) or ("just came back from work" in clean_message) or ("i had a long day" in clean_message):
      num = random.randint(0,2)
      home = discord.File("sHome.png")
      await message.channel.send(responses[num],file=home)
      record_stats("conversation began with senko", message)
      def check1(message):
        return message.author == true_author and message.channel == true_channel and "whats for dinner" in message.content.lower().replace("'", "").replace("’", "").replace(",","")
      def check2good(message):
        return message.author == true_author and message.channel == true_channel and ("good" in message.content.lower() or "great" in message.content.lower() or "super" in message.content.lower() or "amazing" in message.content.lower())
      def check2bad(message):
        return message.author == true_author and message.channel == true_channel and ("bad" in message.content.lower() or "horrible" in message.content.lower() or "sad" in message.content.lower())

      if num == 1:
        try:
          await bot.wait_for('message', check=check1, timeout=60.0)
        except asyncio.TimeoutError:
          return
        food = discord.File("sFood.jpg")
        await message.channel.send(f"Your favorite!",file=food)
      if num == 2:
        try:
          await bot.wait_for('message', check=check2good, timeout=60.0)
        except asyncio.TimeoutError:
          return
        await message.channel.send("That's great! Now come let me pamper you!")
      if num == 2:
        try:
          await bot.wait_for('message', check=check2bad, timeout=60.0)
        except asyncio.TimeoutError:
          return
        fluff = discord.File("senko6.png")
        await message.channel.send("Aww...that's okay. I'll let you fluff my tail to make you feel better",file=fluff)
        
    goodnight_responses = ["Thanks for all your hard work today. Good night, and sweet dreams!", "I fluffed your futon outside so it feels and smells like the sun! Sleep well!", "Good night, dear!"]
    if "good night senko" in message.content.lower().replace(",",""):
      num = random.randint(0,2)
      sleep = discord.File("sSleep.jpg")
      await message.channel.send(goodnight_responses[num],file=sleep)
      record_stats("senko said good night", message)

    goodmorning_responses = ["Good morning!", "Good morning, dear. Breakfast is ready!", "Good morning! How was your sleep?"]
    if "good morning senko" in message.content.lower().replace(",",""):
      
      def check1morning(message):
        return true_author == message.author and true_channel == message.channel and ("whats for breakfast" in message.content.lower().replace("'","").replace("’", "").replace(",",""))
      def check2morning_good(message):
        return message.author == true_author and message.channel == true_channel and ("good" in message.content.lower() or "great" in message.content.lower() or "super" in message.content.lower() or "amazing" in message.content.lower())
      def check2morning_bad(message):
        return message.author == true_author and message.channel == true_channel and ("bad" in message.content.lower() or "horrible" in message.content.lower() or "sad" in message.content.lower() or "cry" in message.content.lower())
      num = random.randint(0,2)
      morning = discord.File("sMorning.jpg")
      await message.channel.send(goodmorning_responses[num],file=morning)
      if num == 1:
        try:
          await bot.wait_for('message', check=check1morning, timeout=60.0)
        except asyncio.TimeoutError:
          return
        breakfast = discord.File("sBreakfast.gif")
        await message.channel.send("I made something special for you!", file=breakfast)
      if num == 2:
        try:
          await bot.wait_for('message', check=check2morning_good, timeout=60.0)
        except asyncio.TimeoutError:
          return
        await message.channel.send("That's great! I've got your clothes ready for work!")
      if num ==2:
        try:
          await bot.wait_for('message', check=check2morning_bad, timeout=60.0)
        except asyncio.TimeoutError:
          return
        await message.channel.send("Aw, that's okay. Maybe some breakfast could cheer you up!")
      record_stats("senko said good morning", message)

    await bot.process_commands(message)

def record_stats(message, ctx):
  the_time = strftime("%a, %d %b %Y %X -0400", gmtime())
  with open("message_stats.txt", "a") as f:
	  f.write(f"Time: {the_time}, Guild: {ctx.guild}, User: {ctx.author}, Message: {message}\n")

@bot.event
async def on_ready():
    status = discord.Game("type s$help for a list of commands!")
    await bot.change_presence(status=discord.Status.online, activity=status)
    print('\nLogged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print("Number of guilds: " + str(len(bot.guilds)))
    
keep_alive()
bot.run(os.environ.get("TOKEN"))
