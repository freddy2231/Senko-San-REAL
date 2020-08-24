# Work with Python 3.6
import discord
from discord.ext import commands
#from webserver import keep_alive  Because this will not run in repl again
import os
import asyncio
import random
from time import gmtime, strftime
# json made by sponk
import json 


prefix = "s$"

print("Please wait for me")

bot = commands.Bot(command_prefix = prefix)
for fileName in os.listdir('./cogs'):
    if fileName.endswith('.py'):
        bot.load_extension(f"cogs.{fileName[:-3]}")

# this function saves guild's id into a json file and writes true







bot.remove_command('help')


#SERIOUS GUILD COMMANDS
@bot.command()

async def load(ctx, cogname):
  if ctx.author.id == 219987389135716364 or 597420184122294272 or 361143836598337546:
    bot.load_extension(f"cogs.{cogname}")
    await ctx.send(f"Loaded {cogname}!")
  else:
    await ctx.send('You cannot do this command')

@bot.command()

async def unload(ctx, cogname):
  if ctx.author.id == 219987389135716364 or 597420184122294272 or 361143836598337546:
    bot.unload_extension(f"cogs.{cogname}")
    await ctx.send(f"Unloaded {cogname}!")
  else:
    await ctx.send('You cannot do this command')

@bot.command()

async def reload(ctx, cogname):
  if ctx.author.id == 219987389135716364 or 597420184122294272 or 361143836598337546:
    bot.reload_extension(f"cogs.{cogname}")
    await ctx.send(f"Reloaded {cogname}!")
  else:
    await ctx.send('You cannot do this command')
# variable easy access




#DAD COMMANDS





#BRUH DETECTOR COMMANDS

 #688534403260874873] this will not portable for us to test




#COMMANDS





@bot.command(name="how_many_guilds")
async def how_many_guilds(ctx):
  if ctx.author.id == 219987389135716364 or 597420184122294272 or 361143836598337546:
    await ctx.channel.send(len(bot.guilds))
  else:
    await ctx.send("You don't have permissions to do this")
  


#@bot.command(name="sing")
#async def sing(ctx):
#  user = ctx.message.author
#  voice_channel = user.voice.voice_channel
#  channel = None
  # only play music if user is in a voice channel
#  if voice_channel != None:
#      channel = voice_channel.name
#      await bot.say('User is in channel: '+ channel)
#      vc = await bot.join_voice_channel(voice_channel)
#      player = vc.create_ffmpeg_player('vuvuzela.mp3', after=lambda: print('done'))
#      player.start()
#      while not player.is_done():
#          await asyncio.sleep(1)
#      player.stop()
#      await vc.disconnect()
#  else:
#      await bot.say('User is not in a channel.')


#Invites
@bot.command(name="bot_invite")
async def bot_invite(ctx):
  invite_embed = discord.Embed(title='Invite Link!', description="A link to invite Senko to your server!", url="https://discord.com/oauth2/authorize?bot_id=691010171828437025&permissions=8&scope=bot" )
  await ctx.channel.send(embed=invite_embed)
  

@bot.command(name="discord_invite")
async def discord_invite(ctx):
  discordinvite_embed = discord.Embed(title='Invite Link!', url="https://discord.gg/dtNdafD", description='A link to the discord server dedicated to Senko, Senko\'s Playground!')
  await ctx.channel.send(embed=discordinvite_embed)
  
#HELP
@bot.command(name='help')
async def help(ctx):
  
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


        
    
                
                
                #bruh detector, sends msg and file

    

@bot.event  
async def on_message(message):

  clean_message = message.content.replace("'", "").lower().replace("’", "").replace(",","")

  responses = ["Welcome home dear!", "I've been waiting for you! Dinner's ready to eat!", "How was your day at work?"]

  true_channel = message.channel
  true_author = message.author
  if ("hi senko im home" in clean_message) or ("hello senko im home" in clean_message) or ("just came back from work" in clean_message) or ("i had a long day" in clean_message):
    num = random.randint(0,2)
    home = discord.File("sHome.png")
    await message.channel.send(responses[num],file=home)
    
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
      

    await bot.process_commands(message)



@bot.event
async def on_ready():
    status = discord.Game("type s$help for a list of commands!")
    await bot.change_presence(status=discord.Status.online, activity=status)
    print('\nLogged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print("Number of guilds: " + str(len(bot.guilds)))
 #I know the first content of guilds is the bot user id this automate adding itself when ready instead keep changing code
    

#keep_alive()  also not run in repl again
if not os.environ.get("TOKEN") == None:
    bot.run(os.environ.get("TOKEN"))
else:
    print("Error: TOKEN enviroment variable not set")
