# Work with Python 3.6
import discord
from discord.ext import commands
from webserver import keep_alive 
import os
import asyncio 
import random
import time

os.environ['TZ'] = 'US/Eastern'
time.tzset()

print("Please wait for me")


prefix = "s$"
bot = commands.Bot(command_prefix = prefix)
bot.remove_command('help')

bot.playing_music = False
bot.playing_music_chn = None
bot.playing_music_name = ''
bot.playing_music_stop = False

bot.yonas = bot.get_user(320383406330347520)

senko_san_op = "Senko_San_OP.mp3"
senko_san_end = "Senko_San_END.mp3"

@bot.command(name='flip')
async def flip(ctx):
  await ctx.send(random.choice(["Heads!", "Tails!"]))

@bot.command(name='spam')
async def spam(ctx, name:discord.Member, *times):
  if len(times) == 0:
    num = 3
  else:
    num = int(times[0])
  if num>10:
    num=10
  for i in range(0, num):
    await ctx.send(name.mention)

@bot.command(name='daniel')
async def daniel(ctx, *times):
  if len(times) == 0:
    num = 3
  else:
    num = int(times[0])
  if num > 10:
    num = 10
  for i in range(0, num):
    await ctx.send("#DanielIsOverParty")




#@bot.command(name='play') 
#async def play(ctx, *arg):
#  if len(arg) == 0:
#    await ctx.channel.send("Choose a song.")
#  if "weeb" in arg[0]:
#    channel = ctx.message.author.voice.channel
#    await channel.connect()
#    await ctx.channel.send("-play https://www.youtube.com/watch?v=VU2ft6BFezs&t=430s&ab_channel=%E1%83%A6AkoMusic%E1%83%A6")
#    await ctx.voice_client.disconnect()

bot.games = ["Overwatch", "CS:GO", "League Of Legends", "Valorant", "Smash", "Rainbow", "COD", "Fortnite", "Rocket League", "Minecraft", "Fifa", "Madden", "NBA"]
bot.open_games = []
class Queue:
  def __init__(self, game, first_gamer ):
    self.game = game
    self.first_gamer = first_gamer
    self.gamers = []
  def add_gamer(self, gamer):
    self.gamers.append(f"{gamer}")
  def remove_gamer(self, gamer):
    for g in self.gamers:
      if g == str(gamer):
        self.gamers.remove(f"{gamer}")
def join_queue(game, gamer):
  if game in bot.open_games:
    game.add_gamer(gamer)
  else:
    create_queue(game, gamer)
def create_queue(game, gamer):
  new = Queue(game, gamer)
  bot.open_games.append(new)
  join_queue(new, gamer)
def leave_queue(game, gamer):
  for g in bot.open_games:
    if game == g.game:
      g.remove_gamer(gamer)
def remove_queue(game):
  for g in bot.open_games:
    if game == g.game:
     bot.open_games.remove(g)

@bot.command(name="queue")
async def queue(ctx,*arg):
  real_channel = ctx.message.channel
  gold = discord.Color.gold()
  if len(arg) == 0:
    await ctx.send("Please use the command as follows:\n\ns$queue <create, join, remove, or leave> <game>")
  if "create" in arg[0]:
    for item in bot.games:
      if item in arg[1]:
        create_queue(arg[1], ctx.author)
        queue_embed = discord.Embed(title=f"{item} LFG", description=f"{ctx.message.author}", color=gold)
  elif "join" in arg[0]:
    for item in bot.open_games:
      if item.game == arg[1]:
        for g in item.gamers:
          if g == str(ctx.message.author):
            await ctx.send("You are already in that queue!")
            return
        item.add_gamer(ctx.message.author)
        des = "\n".join(item.gamers)
        queue_embed = discord.Embed(title=f"{item.game} LFG", description=f"{des}", color=gold)
  elif "remove" in arg[0]:
    for item in bot.open_games:
      if item.game == arg[1]:
        remove_queue(item.game)
        queue_embed = discord.Embed(title=f"{item.game} LFG - REMOVED", color=gold)
  elif "leave" in arg[0]:
    for item in bot.open_games:
      if item.game == arg[1]:
        leave_queue(item.game, ctx.message.author)
        des = "\n".join(item.gamers)
        queue_embed = discord.Embed(title=f"{item.game} LFG", description=f"{des}", color=gold)
  await ctx.channel.purge(bulk=True)
  await ctx.send(embed=queue_embed)



#SERIOUS GUILD COMMANDS


@bot.command(name='getSeriousGuilds')
async def getSeriousGuilds(ctx):
  with open("serious.txt", "r") as b:
    bruh = b.read()
    await ctx.send(bruh)

#DAD COMMANDS

bot.dad_guilds = []

@bot.command(name='getDadGuilds')
async def getDadGuilds(ctx):
  with open("dadbot.txt", "r") as b:
    bruh = b.read()
    await ctx.send(bruh)

@bot.command(name='dad_joke')
async def dad_joke(ctx):
  with open("dadbot.txt", "r") as d:
    dad = d.read()
    if str(ctx.guild.id) in dad:
      dad_responses = ["Why was the stadium so cool? Because it was filled with fans!", "Why can't you hear a pterodactyl using the bathroom? Because the 'P' was silent!", "My dad was chopping onions. Onions was a good dog.", "What do you call a fish with no eyes? A fsh!", "What happened to the Italian chef? He pasta way!", "They ask me, why don't I tell egg jokes? Because they always get cracked up!", "Why was the mathbook always depressed? Because his parents were divorced and his grades were falling due to the stress and neither of his parents cared about him so he spiraled into a never-ending self-pity party, in which he could never return from. Just kidding! Because it's filled with problems!", "Someone asked to call their parents on my phone, but now it's broken. They really didn't need to stand on it to make the call!", "Did you hear about the guy who invented the knock-knock joke? He won the 'no-bell' prize!", "A family of elephants walk into a bar. What do they take? A lot of space!", "If a child refuses to sleep during nap time, are they guilty of resisting a rest?", "What sound does a plane make when it crashes? Boeing!", "I got into a fight with a guy who hit me with a bat. I didn't know these animals hurt that much!", "É pave ou pa cume?"]
      num = random.randint(0,len(dad_responses)-1)
      await ctx.channel.send(dad_responses[num])


#CENSORED GUILD COMMANDS


@bot.command(name='getCensoredGuilds')
async def getCensoredGuilds(ctx):
  with open("censor.txt", "r") as b:
    bruh = b.read()
    await ctx.send(bruh)

#TOGGLE COMMANDS

@bot.command(name="toggle")
async def toggle(ctx, *arg):
  if len(arg) == 0:
    await ctx.channel.send("Please type a passive activity to toggle.")
  elif arg[0] == "bruh":
    with open("not_bruh.txt", "r+") as b:
      bruh = b.read()
      if not(str(ctx.guild.id) in bruh):
        b.write(str(ctx.guild.id) + "\n")
        await ctx.send("I will not detect bruh moments in this server.")
      elif (str(ctx.guild.id) in bruh):
        bruh = bruh.replace(str(ctx.guild.id), "")
        b.truncate(0)
        b.write(bruh)
        await ctx.send("Tehehe")
  elif arg[0] == "censor":
    with open("censor.txt", "r+") as c:
      censor = c.read()
      if not(str(ctx.guild.id) in censor):
        c.write(str(ctx.guild.id) + "\n")
        await ctx.send("I will censor this server.")
      elif str(ctx.guild.id) in censor:
        censor = censor.replace(str(ctx.guild.id), "")
        c.truncate(0)
        c.write(censor)
        await ctx.send("Tehehe")
  elif arg[0] == "serious":
    with open("serious.txt", "r+") as s:
      serious = s.read()
      if not(str(ctx.guild.id) in serious):
        s.write(str(ctx.guild.id) + "\n")
        await ctx.send("I will behave in this server.")
      elif str(ctx.guild.id) in serious:
        serious = serious.replace(str(ctx.guild.id), "")
        s.truncate(0)
        s.write(serious)
        await ctx.send("Tehehe")
  elif arg[0] == "dadbot":
    with open("dadbot.txt", "r+") as d:
      dadbot = d.read()
      if not(str(ctx.guild.id) in dadbot):
        d.write(str(ctx.guild.id) + "\n")
        await ctx.send("DadBot activated.")
      elif str(ctx.guild.id) in dadbot:
        dadbot = dadbot.replace(str(ctx.guild.id), "")
        d.truncate(0)
        d.write(dadbot)
        await ctx.send("Your dad left you.")
  else:
    await ctx.channel.send("That is not a function! Try \"s$toggle bruh\", \"s$toggle censor\", \"s$toggle dadbot\", or \"s$toggle serious\" to toggle a function!")
    
#BRUH DETECTOR COMMANDS 

@bot.command(name='getBruhGuilds')
async def getBruhGuilds(ctx):
  with open("not_bruh.txt", "r") as b:
    bruh = b.read()
    await ctx.send(bruh)


#COMMANDS
@bot.command(name="entry")
async def entry(ctx, *, entry):
  d1 = time.strftime("%m/%d/%Y", time.localtime())
  entry_embed = discord.Embed(title=f"Date: {str(d1)}", description=entry, color=discord.Color.gold())
  await ctx.message.delete()
  await ctx.send(embed=entry_embed)


async def playMusic(context, music):

    # grab the user who sent the command
    user=context.message.author

    voice_channel=context.message.author.voice
    channel=None

    if bot.playing_music == True and bot.playing_music_name != music:
        await context.channel.send(user.mention + ' i currently singing other music in \'' + bot.playing_music_chn + '\'')
        return
    # only play music if user is in a voice channel
    if voice_channel!= None and bot.playing_music == False:
        # grab user's voice channel
        channel=voice_channel.channel.name

        bot.playing_music = True
        bot.playing_music_chn = channel
        bot.playing_music_name = music
        bot.playing_music_stop = False

        await context.channel.send('Senko San is singing in \'' + channel + '\' come to me')
        
        vc = context.author.voice
        if vc:
            vc = await vc.channel.connect()

        #await asyncio.sleep(15)

        vc.play(discord.FFmpegPCMAudio(music))

        while vc.is_playing():
            if bot.playing_music_stop == True:
                await context.channel.send("Ok")
                break
            await asyncio.sleep(.1)  #Sleep while playing music

        await vc.disconnect()
        bot.playing_music = False
        bot.playing_music_name = None
        bot.playing_music_name = ''
        bot.playing_music_stop = False

    elif bot.playing_music == True:
        if voice_channel != None and voice_channel.channel.name == bot.playing_music_chn:
            await context.channel.send(user.mention + ' you already in the channel')
        else:
            await context.channel.send(user.mention + ' can you enter the \'' + bot.playing_music_chn + '\' channel please because i currently singing there')
    else:
        await context.channel.send(user.mention + ' can you enter the voice channel please if you want me singing for you')

@bot.command(name='sing')
async def sing(ctx, *arg):  # Singing  intro command
    if len(arg) == 0:
        await ctx.channel.send("Usage:")
        await ctx.channel.send(prefix + "sing [intro | end | stop | status]")
    elif arg[0].lower() == 'intro':
        await playMusic(ctx, senko_san_op)

    elif arg[0].lower() == 'end':
        await playMusic(ctx, senko_san_end)

    elif arg[0].lower() == 'stop':
        if bot.playing_music == False:
            await ctx.channel.send("Currently i'm not singing")
            return
        bot.playing_music_stop = True

    elif arg[0].lower() == 'status':
        await ctx.channel.send('Status:')
        if bot.playing_music == False:
            await ctx.channel.send("Currently i'm not singing")
            return
        await ctx.channel.send('Voice Channel: ' + bot.playing_music_chn)
        await ctx.channel.send('Join the channel if you like me singing for you')

    else:
        await ctx.channel.send("No such subcommands")
        await ctx.channel.send("Usage:")
        await ctx.channel.send(prefix + "sing [intro | end | stop | status]")

@bot.command(name='hello')
async def hello(ctx):
  await ctx.channel.send("Hello there, {0}".format(ctx.author.mention))

@bot.command(name='spank')
async def spank(ctx):
  serious = False
  with open("serious.txt", "r") as s:
    seriousR = s.read()
    if str(ctx.guild.id) in seriousR:
      serious = True
  if not serious:
    await ctx.channel.send("Uhnnn, why would you spank me, Master? Did I do anything wrong?")

@bot.command(name="guilds")
async def guilds(ctx):
  await ctx.channel.send(len(bot.guilds))
  
@bot.command(name='dance')
async def dance(ctx):
  serious = False
  with open("serious.txt", "r") as s:
    seriousR = s.read()
    if str(ctx.guild.id) in seriousR:
      serious = True
  if not serious:
    danceGIF = discord.File("pics_n_gifs/sDance.gif")
    await ctx.channel.send(file=danceGIF)

@bot.command(name='pat')
async def pat(ctx):
  patGIF = discord.File("pics_n_gifs/sPAT.gif")
  await ctx.channel.send(file=patGIF)

bot.the_hated = []
@bot.command(name='hate')
async def hate(ctx, person:discord.Member):
  serious = False
  with open("serious.txt", "r") as s:
    seriousR = s.read()
    if str(ctx.guild.id) in seriousR:
      serious = True
  if not serious:
    if not(person in bot.the_hated):
      bot.the_hated.append(person)
      await ctx.send("Added!")
      return
    else: 
      await ctx.channel.send("That person is already on the list!")
  else:
      pass
    

@bot.command(name='hate_remove')
async def hate_remove(ctx, person:discord.Member):
  serious = False
  with open("serious.txt", "r") as s:
    seriousR = s.read()
    if str(ctx.guild.id) in seriousR:
      serious = True
  if not serious:
    if (person in bot.the_hated):
      bot.the_hated.remove(person)
      await ctx.send("Removed!")
      return
    else: 
      await ctx.channel.send("That person isn't hated (yet...)")
  else:
      pass

@bot.command(name='hate_list')
async def hate_list(ctx):
  serious = False
  with open("serious.txt", "r") as s:
    seriousR = s.read()
    if str(ctx.guild.id) in seriousR:
      serious = True
  if not serious:
    await ctx.send(bot.the_hated)
  else:
    pass

bot.number = 691010171828437025
@bot.command(name='love')
async def love(ctx, *, personM:discord.Member):
  serious = False
  with open("serious.txt", "r") as s:
    seriousR = s.read()
    if str(ctx.guild.id) in seriousR:
      serious = True
  if not serious:
    loveGIF = discord.File("pics_n_gifs/senkoLove.gif")
    for unused_variable_for_no_reason_lmao in bot.the_hated:
      if personM in bot.the_hated:
        loveGIF = discord.File("pics_n_gifs/sMAD.gif")
        await ctx.channel.send(f"Shut up, {personM.mention} does not deserve love", file=loveGIF)
        return

    if personM.id == bot.number:
      loveGIF = discord.File("pics_n_gifs/sLove.gif")
      await ctx.channel.send(f"I love you too, {ctx.author.mention}", file=loveGIF)
      return

    elif personM.id == ctx.author.id:
      loveGIF == discord.File("pics_n_gifs/senkoLove.gif")
      await ctx.channel.send(f"You must love yourself a lot, {personM.mention}", file=loveGIF)

    else:
      loveGIF = discord.File("pics_n_gifs/senkoLove.gif")
      await ctx.channel.send(f"{ctx.author.mention} loves you, {personM.mention}", file=loveGIF)
  else:
    pass

@bot.command(name="fluff")
async def fluff(ctx):
  serious = False
  with open("serious.txt", "r") as s:
    seriousR = s.read()
    if str(ctx.guild.id) in seriousR:
      serious = True
  if not serious:
    gifnum = random.randint(0,2)
    if gifnum == 0:
      fluffy = discord.File("pics_n_gifs/sFluff1.png")
      await ctx.channel.send(file=fluffy)
    if gifnum == 1:
      fluffy = discord.File("pics_n_gifs/sFluff3.jpg")
      await ctx.channel.send(file=fluffy)
    if gifnum == 2:
      fluffy = discord.File("pics_n_gifs/sFluff4.jpg")
      await ctx.channel.send(file=fluffy)

@bot.command(name="hug")
async def hug(ctx):
  serious = False
  with open("serious.txt", "r") as s:
    seriousR = s.read()
    if str(ctx.guild.id) in seriousR:
      serious = True
  if not serious:
      hugGIF = discord.File("pics_n_gifs/sHug.gif")
      await ctx.channel.send(file=hugGIF)

@bot.command(name="protecc")
async def protecc(ctx):
  serious = False
  with open("serious.txt", "r") as s:
    seriousR = s.read()
    if str(ctx.guild.id) in seriousR:
      serious = True
  if not serious:
      protecc = discord.File("pics_n_gifs/sJOJO.png")
      await ctx.channel.send("No bullying allowed!", file=protecc)

@bot.command(name="patreon")
async def patreon(ctx):
  patreon = discord.Embed(title='Support our Patreon!', description='A link to the patreon of Senko\'s developers. Your donation helps keep us doing what we\'re doing. Thank you for any and all support.', url='https://www.patreon.com/senkosanbot', color=discord.Color.gold())
  await ctx.channel.send(embed=patreon)

@bot.command(name="devs")
async def devs(ctx):
  dev_embed = discord.Embed(title='Developers:', description="\n1. freddy2231#6891\n2. Fox#3211\n3. sponk#1228\n\nThis project initiated by freddy2231#6891", color=discord.Color.gold())
  await ctx.channel.send(embed=dev_embed)

@bot.command(name='dashboard')
async def dashboard(ctx):
  dashboard = discord.Embed(title="Dashboard", description="Here you can view toggles for each passive.\n__________", color=discord.Color.gold())

  on = "\U0001F7E2"

  off = "\U0001F534"

  switch = {}
  with open("not_bruh.txt", "r") as b:
    bruh = b.read()
    if not str(ctx.guild.id) in bruh:
      switch[" Bruh Detector: "] = f"{on}"
    else:
      switch[" Bruh Detector: "] = f"{off}"
  with open("serious.txt", "r") as b:
    serious = b.read()
    if str(ctx.guild.id) in serious:
      switch[" Serious:              "] = f"{on}"
    else:
      switch[" Serious:              "] = f"{off}"

  with open("censor.txt", "r") as b:
    censor = b.read()
    if str(ctx.guild.id) in censor:
      switch[" Censor:               "] = f"{on}"
    else:
      switch[" Censor:               "] = f"{off}"
  
  with open("dadbot.txt", "r") as b:
    dad = b.read()
    if str(ctx.guild.id) in dad:
      switch[" DadBot:              "] = f"{on}"
    else:
      switch[" DadBot:              "] = f"{off}"
  
  for name, toggle in switch.items():
    dashboard.add_field(name=name + "   " + toggle, value="_______________", inline=False)
  
  await ctx.channel.send(embed=dashboard)
  
  
#Invites
@bot.command(name="bot_invite")
async def bot_invite(ctx):
  invite_embed = discord.Embed(title='Invite Link!', description="A link to invite Senko to your server!", url="https://discord.com/oauth2/authorize?client_id=691010171828437025&permissions=8&scope=bot", color=discord.Color.gold() )
  await ctx.channel.send(embed=invite_embed)

@bot.command(name="discord_invite")
async def discord_invite(ctx):
  discordinvite_embed = discord.Embed(title='Invite Link!', url="https://discord.gg/dtNdafD", description='A link to the discord server dedicated to Senko, Senko\'s Playground!', color=discord.Color.gold())
  await ctx.channel.send(embed=discordinvite_embed)
    

#HELP
@bot.command(name='help')
async def help(ctx, *arg):
    commands = {}
    gold = discord.Colour.gold()
    if len(arg) == 0:
        helper = discord.Embed(title='Senko-san', description='wh-what would you like to do with me uwu\n\nFounder: @freddy2231#6891\nType \"s$devs\" to learn more about the developers.\n\n\"s$discord_invite\" to join the discord!\nSupport the creators on the patreon with \"s$patreon\"!\n\n\"s$help commands\" for a list of commands!"', colour=gold)
    elif arg[0].lower() == "commands":
        helper = discord.Embed(title="Commands", description="Senko has many commands for you to try!\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!", color = discord.Color.gold())
        commands['s$hello'] = "Returns a greeting and mention"
        commands['s$love @user'] = "Send some love to another user, or, if they're hated, send some hate ( •̀ᴗ•́ )و ̑̑. If you want some love yourself, try s$love @Senko-San"
        commands['s$hate @user'] = "Add a user to the hate list"
        commands['s$hate_remove @user'] = "Remove a user from the hate list"
        commands['s$pat'] = "Pat Senko!"
        commands['s$hug'] = "Hug Senko!"
        commands['s$fluff'] = "Fluff Senko!"
        commands['s$dance'] = "Let Senko dance!"
        commands['s$sing'] = "Senko will sing (\"s$help sing\" for more info)"
        commands['s$bot_invite'] = "Link for you to add Senko to your server!"
        commands['s$discord_invite'] = "Link for you to join the Discord!"
        commands['s$devs'] = "Info about the developers of this project."
        commands['s$queue <action> <game>'] = "Create or join a Looking-for-Group queue! WARNING: FOR USE ONLY IN LOOKING-FOR-GROUP CHANNELS. \"s$help queue\" for more information."
        commands['Passive Activity'] = "Use \"s$help passive\" for info about the passive activities."
        commands['s$toggle <passive>'] = "Toggle any passive activity. Keywords are: 'dadbot', 'censor', 'serious', and 'bruh'"
    elif arg[0].lower() == "passive":
        helper = discord.Embed(title='Senko-san', description='wh-what would you like to do with me uwu\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!', colour=gold)
        commands['s$dashboard'] = "View toggles to each passive."
        commands['"Bruh Detector"'] = "Detects bruh moments. (\"s$help bruh\" for more info! )"
        commands['"DadBot"'] = "Will respond to certain messages. (\"s$help dadbot\" for more info!) "
        commands['"Censor"'] = "Censors bad words. (\"s$help censor\" for more info!)"
        commands['"Senko"'] = "Your personal Senko! (\"s$help senko\" for more info!)"
        commands['"Serious"'] = "Serious mode limits commands Senko will respond to. (\"s$help serious\" for more info!)"
    elif arg[0].lower() == "sing":
        helper = discord.Embed(title="Sing Commands", description="Senko will sing for you!\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!", color = gold)
        commands['s$sing'] = "Senko will sing either the opening or ending of the Sewayaki Kitsune no-Senko-san anime!"
        commands['s$sing intro'] = "Senko will sing the intro song."
        commands['s$sing end'] = "Senko will sing the ending song."
        commands['s$sing stop'] = "Senko will stop singing."
        commands['s$sing status'] = "Senko will tell you if she is singing or not."
    elif arg[0].lower() == "bruh":
        helper = discord.Embed(title='Bruh Detector', description='The Bruh Detector will detect bruh moments when enabled.\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!', colour=gold)
        commands['s$toggle bruh'] = "Turn Bruh Detector on or off."
        commands['Bruh Detector'] = "Senko will respond anytime someone says \"bruh\" when the Bruh Detector is enabled."
    elif arg[0].lower() == "dadbot":
        helper = discord.Embed(title='DadBot', description='Your own personal DadBot! (Disclaimer: will not replace your biological dad, but it will try!)\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!', colour=gold)
        commands['s$dad_joke'] = "Senko tells a dad joke!"
        commands['s$toggle dadbot'] = "Toggle dadbot on or off."
        commands['DadBot (Passive Activity)'] = "If Senko is a Dad, she (he?) will respond to messages like this:\nUser: Wow, I'm really tired\nSenko-san: Hi really tired, I'm dad!"        
    elif arg[0].lower() == "senko":
        helper = discord.Embed(title='Senko-san', description='Your very own senko interactions!\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!', colour=gold)
        commands['Senko-san'] = "Senko will respond to many different trigger phrases. Some of them allow you to reply back, after which she will reply once more."
        commands['"Hello/Hi/Hey Senko, I\'m home!", "I had a long day", or "Just came back from work"'] = "Senko will respond with one of three responses. You can then ask her what's for dinner, or tell her how your day went using simple descriptors."
        commands['"Good morning Senko!"'] = "Senko will respond with one of three responses. You can then ask her what's for breakfast, or tell her how your sleep was using simple descriptors."
        commands['"Good night Senko!"'] = "Senko will respond with one of three responses."
        commands['"Hi/Hello/Hey Senko"'] = "Senko will greet you."
        commands['"Thank you/Thanks Senko"'] = "Thank Senko for all her affection!"
    elif arg[0].lower() == "censor":
        helper = discord.Embed(title='Censor Ability', description='Senko will censor bad words on your server!\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!', colour=gold)
        commands['s$toggle censor'] = "Toggle censor on or off."
        commands['Censor (Passive Activity)'] = "If Senko sees a message with a bad word in it, she will delete the message. **NOTE**: Senko must be a moderator in your server for this ability to work."
    elif arg[0].lower() == "serious":
        helper = discord.Embed(title='Serious Passive', description='When you turn the Serious passive on, Senko will not respond to much of her commands.\n\nDeveloper: @freddy2231#6891\nDM me on discord for questions, or a link to join the discord!', colour=gold)
        commands['s$toggle serious'] = "Toggle serious mode on or off."
        commands['Serious (Passive Activity)'] = "Senko will not respond most of her commands when serious. This is so that if Senko migrates to a more serious role in certain servers, she will be a better fit for that role."
    else:
        await ctx.channel.send("No such command. Use \"s$help\" for more help for s$help command")
        return
    for command, description in commands.items():
        helper.add_field(name=command, value=(description + "\n"), inline=False)
    await ctx.channel.send(embed=helper)

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
  bad_words[8] = "asshole" 
  bad_words[9] = "nigga"

  with open("censor.txt", "r") as c:
    censorR = c.read()
    censor = False
    if str(message.guild.id) in censorR:
        censor = True
  if censor:
      for word in bad_words:
          if bad_words[word] in message.content.lower():
              await message.delete()
              await message.channel.send("That's really funny bud.")

  with open("not_bruh.txt") as b:
    bruhR = b.read()    
    bruh = False
    if str(message.guild.id) in bruhR:
        bruh = True
  if not bruh:
      if  "bruh" in message.content.lower():
          if not ("s$toggle bruh" in message.content or "s$getBruhGuilds" in message.content or "s$help bruh" in message.content):
              bruhImg=discord.File('pics_n_gifs/bruh.jpg')
              await message.channel.send(f"That's quite a bruh moment {message.author.mention}!", file=bruhImg)              
              #bruh detector, sends msg and file

  serious = False
  with open("serious.txt", "r") as s:
    seriousR = s.read()
    if str(message.guild.id) in seriousR:
      serious = True
  if not serious:
      if ("i love you" in message.content.lower()) and ("senko" in message.content.lower()):
          await message.channel.send(f"I love you too, {message.author.mention}")
  else:
      pass

  
  dad = False
  with open("dadbot.txt", "r") as s:
    dadR = s.read()
    if str(message.guild.id) in dadR:
      dad = True
  dad_message = message.content.lower().replace("i'm ", "im ").replace("i’m ", "im ")
  if dad:
    if "im " in dad_message:
          dad_message = dad_message[(dad_message.index("im ")):]
          dad_message = dad_message.replace("im ", "")
          await message.channel.send("Hi {0}, I'm dad!".format(dad_message))

  clean_message = message.content.replace("'", "").lower().replace("’", "").replace(",","")


  good_msgs = ["good", "great", "super", "amazing"]

  bad_msgs = ["bad", "horrible", "sad", "cry"]

  responses = ["Welcome home dear!", "I've been waiting for you! Dinner's ready to eat!", "How was your day at work?"]
  goodnight_responses = ["Thanks for all your hard work today. Good night, and sweet dreams!", "I fluffed your futon outside so it feels and smells like the sun! Sleep well!", "Good night, dear!"]
  goodmorning_responses = ["Good morning!", "Good morning, dear. Breakfast is ready!", "Good morning! How was your sleep?"]

  def check(message):
    return true_author == message.author and true_channel == message.channel
  
  true_channel = message.channel

  true_author = message.author
  
  if ("hi senko im home" in clean_message) or ("hey senko im home" in clean_message) or ("hello senko im home" in clean_message) or ("just came back from work" in clean_message) or ("i had a long day" in clean_message):
    num = random.randint(0,2)
    home = discord.File("pics_n_gifs/sHome.png")
    await message.channel.send(responses[num],file=home)

    return_message = await bot.wait_for('message', check=check)

    if num == 1 and ("whats for dinner" in return_message.content.lower().replace("'", "").replace("’", "").replace(",","")):
      food = discord.File("pics_n_gifs/sFood.jpg")
      await message.channel.send(f"Your favorite!",file=food)
      return
    if num == 2:
      for msg in good_msgs:
        if msg in return_message.content.lower():
          await message.channel.send("That's great! Now come let me pamper you!")
          return
      for msg in bad_msgs:
        if msg in return_message.content.lower():
          fluff = discord.File("pics_n_gifs/senko6.png")
          await message.channel.send("Aww...that's okay. I'll let you fluff my tail to make you feel better",file=fluff)
          return

  if not serious:
    if "good night senko" in message.content.lower().replace(",",""):
      num = random.randint(0,2)
      sleep = discord.File("pics_n_gifs/sSleep.jpg")
      await message.channel.send(goodnight_responses[num],file=sleep)

    if "good morning senko" in message.content.lower().replace(",",""):

      num = random.randint(0,2)
      morning = discord.File("pics_n_gifs/sMorning.jpg")

      await message.channel.send(goodmorning_responses[num],file=morning)

      return_message = await bot.wait_for('message', check=check)

      if num == 1 and ("whats for breakfast" in return_message.content.lower().replace("'","").replace("’", "").replace(",","")):
        breakfast = discord.File("pics_n_gifs/sBreakfast.gif")
        await message.channel.send("I made something special for you!", file=breakfast)
        return
      if num == 2:
        for msg in good_msgs:
          if msg in return_message.content.lower():
            await message.channel.send("That's great! I've got your clothes ready for work!")
            return
        for msg in bad_msgs:
          if msg in return_message.content.lower():
            await message.channel.send("Aw, that's okay. Maybe some breakfast could cheer you up!")
            return
    

  if (("hi " in message.content.lower()) or ("hey " in message.content.lower()) or ("hello " in message.content.lower())) and ("senko" in message.content.lower() and not("im home" in message.content.lower().replace("'","")) and not("i love you" in message.content.lower())):
    await message.channel.send(f"Hello, {message.author.mention}!")
  if ("thank you" in message.content.lower()) and ("senko" in message.content.lower()):
    await message.channel.send(f"You're welcome, {message.author.mention}!") 
  if ("die" in message.content.lower()) and ("senko" in message.content.lower()):
    mad = discord.File("pics_n_gifs/sMAD.gif")
    await message.channel.send("That's not very nice...", file=mad)
  await bot.process_commands(message)

@bot.event
async def on_ready():
    status = discord.Game("s$help to get started!")
    await bot.change_presence(status=discord.Status.online, activity=status)
    channel = bot.get_channel(745429102063779902)
    await channel.send("Senko-san, at your service!")
    print('\nLogged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print("Number of guilds: " + str(len(bot.guilds)))


keep_alive()
bot.run(os.environ.get("TOKEN"))
