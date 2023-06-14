
import requests
from urllib.parse import urlparse
import pandas as pd
import discord
import re
from sklearn.tree import DecisionTreeClassifier
import os
from keep_awake import keep_alive
import urllib
# from urllib.requests import urlopen
from discord.ext import commands
from discord.ext.tasks import loop
import datetime
import time
import writescam
import random
import json
from flask import Flask
from get_action import get_action
from get_channel import get_channel

intents = discord.Intents.default()
intents.members = True
class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()
    
    
    async def send_bot_help(self, mapping):
        e=discord.Embed(title="AntiScam Commands",colour = rndclr)
        for cog in mapping:
          list=[f"`{command.name}`" for command in mapping[cog]]
          nicerlist='\n '.join(list)
          
          if cog != None:  
            e.add_field(name=cog.qualified_name, value=nicerlist)
          else:
            e.add_field(name="None", value=nicerlist)
          e.set_footer(text=f"Try a!help <command> to get info on a specific command!")
        await self.get_destination().send(embed=e)
        #return await super().send_bot_help(mapping)
    async def send_cog_help(self, cog):
        e=discord.Embed(title="AntiScam Commands",description=f"Relevant to \"{cog.qualified_name}\"",colour = rndclr)
        list=[f"`{command.name}`" for command in cog.get_commands()]
        nicerlist='\n '.join(list)
        e.add_field(name=cog.qualified_name, value=nicerlist)
        e.set_footer(text=f"Try a!help <command> to get info on a specific command!")
        await self.get_destination().send(embed=e)
    async def send_group_help(self, group):
        e=discord.Embed(title="AntiScam Commands",description=f"Relevant to \"{group.qualified_name}\"",colour = rndclr)
        list=[f"`{command.name}`" for index, command in enumerate(group.commands)]
        nicerlist='\n '.join(list)
        e.add_field(name=f"{group.qualified_name}",value=nicerlist)
        e.set_footer(text=f"Try a!help <command> to get info on a specific command!")
        await self.get_destination().send(embed=e)
    async def send_command_help(self, command):
        e=discord.Embed(title="AntiScam Commands",description=f"Relevant to \"{command.name}\"",colour = rndclr)
        #print(command.clean_params)
        tuple_list = list(command.clean_params.items())
        stuff=""
        for i in tuple_list:  
          keyvalue=i[0]
          stuff+=f"`{keyvalue}`\n"
        
        e.add_field(name=f"{command.name}",value=f"{command.help}")
        #e.add_field(name="Usage",value=command.usage,inline=False)
        #print(",".join(command.aliases))
        #print(command.aliases)
        if len(command.aliases)!=0:  
          e.add_field(name="Aliases",value=",".join(command.aliases),inline=False)
        else :
          e.add_field(name="Aliases",value="No Aliases Found!",inline=False)
        if len(stuff)!=0:

          e.add_field(name="Required Arguments",value=stuff,inline=False)
        else:
          e.add_field(name="Required Arguments",value="None",inline=False)
        e.add_field(name="Command Checks [BETA]",value=command.checks,inline=False)
        e.set_footer(text=f"Path: {command.cog_name} > {command.name}")
        await self.get_destination().send(embed=e)
    async def send_error_message(self, error):
        e=discord.Embed(title="AntiScam Commands",description=f"Error!",colour =0xFF7000)
        list_of_commands=list(map(lambda m:m.name, filter(lambda m: m.name.startswith((str(error).split('"')[1][0])), bot.commands)))
      
        shit=""
      ###print(bot.commands)
        for i in list_of_commands:
          shit+=f"`{i}`\n"
        if len(shit) !=0:  
          e.add_field(name=f"{error}",value=f"{len(list_of_commands)} alternatives found\nDid you mean:\n{shit}")
        else:
          e.add_field(name=f"{error}",value=f"No command suggestions found!")
        await self.get_destination().send(embed=e)
    
bot = commands.Bot(command_prefix=commands.when_mentioned_or('a!'),case_insensitive=True,intents=intents,strip_after_prefix=True,help_command=CustomHelpCommand(),description="ooga booga")
initial_extensions=['utils','misc','customisation','owner']

app = Flask(__name__)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
@bot.event
async def on_ready():
  print("running rn")  
  
  # try:
  #   update_stats.start()
  # except RuntimeError:
  #   await bot.change_presence(status=discord.Status.idle,
  #                                 activity=discord.Activity(type=discord.ActivityType.playing,
  #                                 name="Runtime Errors >:("))
  await bot.change_presence(status=discord.Status.dnd)
  #("started...")
  global rndclr
  rndclr=random.choice([discord.Colour.red().value,discord.Colour.dark_grey().value])
  global startTime
  startTime = time.time()
  global dat
  dat=datetime.datetime.now()
  global start
  start=False


  #await channel.send("Locked and loaded! Let's Go!")
  ####print("lol")
  start=True
  # for guild in bot.guilds:
  #   for member in guild.members:
  #     if str(member).split("#")[0].lower()=="hypersquad events":
  #       await member.ban(reason="Discord Impersonation Scam")
  #     #(str(member))

  # await bot.change_presence(status=discord.Status.idle,
  #                                 activity=discord.Activity(type=discord.ActivityType.playing,
  #                                 name="Bot Starting Up..."))

# @loop(minutes=1)
# async def update_stats():
#     """This function runs every 30 minutes to automatically update your server count."""
#     try:
#         await bot.topggpy.post_guild_count()
#         #print(f"Posted server count ({bot.topggpy.guild_count})")
#     except Exception as e:
#         #print(f"Failed to post server count\n{e.__class__.__name__}: {e}")

@loop(seconds=10)
async def stat():

  try:
    await bot.change_presence(status=discord.Status.dnd,
                                  activity=discord.Activity(type=discord.ActivityType.watching,
                                                            name=f"for scams in {len(bot.guilds)} servers - {round(bot.latency * 1000)}ms"))
  except OverflowError:
      await bot.change_presence(status=discord.Status.invisible,
                                  activity=discord.Activity(type=discord.ActivityType.playing,
                                  name="Overflow Errors >:("))

  reactions=["👌🏼","👍🏼","✅","☑","✔","⏱"]
  global rhombus
  rhombus=str(random.choice(reactions))

@bot.event #needs to be reworked:(
async def on_message(message):
 try:
  strt=start
 except NameError:
   strt=False
 if strt==True:
  type_scam="Undefined..."
  mentions = [str(m) for m in message.mentions]

  if str(bot.user) in list(mentions):
            text = str(message.content).split()
            if len(text) == 1:

              with open('channel.json', 'r') as f:
                prefixes = json.load(f)
              with open('action.json','r') as f:
                action=json.load(f)


              try:
                gg=prefixes[str(message.guild.id)]
                stringthing=""
                i=0
                for ch in gg:
                  channel=bot.get_channel(ch)
                  if i!=len(gg)-1:
                    stringthing+=f"{channel.mention} "
                  else:
                    stringthing+=f"{channel.mention}"

                  i+=1
                goth=f"I will log scams in {stringthing.replace(' ',', ')}"

              except KeyError:
                goth=f"I will send logged scams to the owner of this server for there is no linked channel! Use `a!linkchannel` to link one!"
              try:
                gg=action[str(message.guild.id)]
                b=f"I will {gg} scammers in this server!"
              except KeyError:
                b=f"I will ban scammers in this server as there is no custom action set up! Use `a!addaction <action>` to set up a custom action. If no action is set up, I will ban the violator!"

              await message.reply(f"My prefix in this server is `a!`!\n{goth}\n{b}")
  startTime = time.time()
  type_scam="undefined..."
  hits=[]
  chicka=message.content
  lol=chicka

  urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',message.content.lower())
  # for url in urls:
  #   if is_safe_url(url)==True:
  #     score+=0.1
  #   else:
  #     score+=0.37
  with open("cache.json","r") as f:
    cache=json.load(f)
  cachelist=cache['helpme']
  score=0
  req= requests.get("https://raw.githubusercontent.com/45i/Frequent-Scams/Main/Malicious%20Websites/raw-links.txt")
  resp=req.text;
  lista=str(resp).splitlines()
  if message.content not in cachelist:
    do=1
  else:
    do=3
  for l in urls:
    
      gucci=urlparse(l).netloc
      if gucci in lista:
        do=2
  if len(urls)==0:
    do=4
  if do==1:
    global model
    model  = DecisionTreeClassifier()
    if "nitro" in message.content.lower().replace('.',' ').replace('?',' ') .replace('!',' ').replace(',',' ').replace(';',' ').replace(':',' ').replace ('-',' ').replace('_',' ').replace('(',' ').replace(')',' ').replace('{',' ')  .replace('}',' ').replace('[',' ').replace(']',' ').replace("'",' ').replace  ('"',' ').split():
      # s=""
      # h=""
      hits.append("nitro")


      if "scam" not in message.content.lower():
        score+=0.0027
      else:
        score += 0.0025
      type_scam="Discord Nitro Scam"
    if "@everyone" in message.content.lower() or"@here" in message.content.lower():
      score+=0.003
    if "free" in message.content.lower() :
      hits.append("free")
      if "scam" not in message.content.lower():
        score+=0.003
      else:
        score += 0.0025

      type_scam="Discord Nitro Scam"
    
    if "vbuck" in message.content.lower() :
      hits.append("vbuck")
      if "scam" not in message.content.lower():
        score+=0.003
      else:
        score += 0.0025
    if "robux" in message.content.lower() :

      if "scam" not in message.content.lower():
        score+=0.003
      else:
        score += 0.0025
      hits.append("robux")
      type_scam="ROBUX scam"

    if "steam" in message.content.lower() :
      hits.append("steam")
      if "scam" not in message.content.lower() :
        score+=0.0035

    scorus=0
    for j in urls:


     try:

      
      
      ####print(j)
      ####print("bit.ly" in j)
        # if "bit.ly" in j or "bit.do" in j:

        #   scorus+=0.77
      try:
        resp = urllib.request.urlopen(j)
        final_url = resp.geturl()
        response_code = resp.getcode()
        if response_code == 302:
    # redirected so this may a short url
          response = requests.get(final_url)
        else:
    # this is not a short url  
          response = requests.get(j)
      except urllib.error.HTTPError:
        if message.author.bot==False   and message.author!=bot.user:  
          
            try:
              with open("serversettings.json","r")as f:
                settings=json.load(f)['errorlogging']
              if settings==True:
                await message.reply(f"We got a 403 Error Meaning this webpage({j}) may not exist, or is empty",delete_after=10)
              else:
                pass
            except KeyError:
              pass
            
        response = requests.get(j)
        # final_url != original_url if redirected
      except urllib.error.URLError:
        if message.author.bot==False   and message.author!=bot.user:
            
            try:  
              with open("serversettings.json","r")as f:
                  settings=json.load(f)['errorlogging']
              if settings==True:
                await message.reply(f"We got a URLError Meaning this webpage({j}) may not exist",delete_after=10)
              else:
                pass
            except KeyError:
              pass

          
        response = requests.get(j)
      ##print(response.text)
      if "404 - Not Found" not in response.text and message.author.bot==False   and message.author!=bot.user:
        

        

          if "nitro" in str(response.text).lower().replace('.',' ').replace('?',' ') .replace('!',' ').replace(',',' ').replace(';',' ').replace(':',' ') .replace('-',' ').replace('_',' ').replace('(',' ').replace(')',' ') .replace('{',' ').replace('}',' ').replace('[',' ').replace(']',' ') .replace("'",' ').replace('"',' ').split():
      # s=""
      # h=""



            if "scam" not in str(response.text).lower():
              scorus+=0.57
            else:
              scorus += 0.25


          if "free" in str(response.text).lower() :
            if "nitro" in str(response.text).lower().replace('.',' ').replace('?',' ') .replace('!',' ').replace(',',' ').replace(';',' ').replace(':',' ') .replace('-',' ').replace('_',' ').replace('(',' ').replace(')',' ') .replace('{',' ').replace('}',' ').replace('[',' ').replace(']',' ') .replace("'",' ').replace('"',' ').split():
              scorus+=0.6
            if "scam" not in str(response.text).lower():
              scorus+=0.007
              type_scam="Discord Nitro Scam"
            else:
              scorus += 0.0025



          if "vbuck" in str(response.text).lower() :

            if "scam" not in str(response.text).lower():
              scorus+=0.3
              type_scam="VBuck Scam"
            else:
              scorus += 0.25
          if "robux" in str(response.text).lower() :

            if "scam" not in str(response.text).lower():
              scorus+=0.3
              type_scam="Robux Scam"
            else:
              scorus += 0.25

          if "steam" in str(response.text).lower() :

            if "scam" not in str(response.text).lower() :
              scorus+=0.1
          if "air drop" in str(response.text).lower() or "air-drop" in str(response.text).lower()   or   "airdrop" in str(response.text).lower():

            if "scam" not in str(response.text).lower():

              scorus+=0.005


          if "leaving this" in   str(response.text).lower() and "game" in str(response.text).lower  ():

            scorus+=0.055
            if "trade offer" in str(response.text).lower():
              scorus+=0.03
            else:
              scorus += 0.025
          if "skin" in str(response.text).lower() :
            if "swapper" in str(response.text).lower() or "switcher" in str(response.text).lower()or"changer" in str(response.text).lower():
              scorus+=0.075
              type_scam="Skin Switcher Scam\nThis type of action(switching/swapping skins) is illegal/against game ToS and can lead to an account ban!"
            if "custom skin" in str(response.text).lower():
              scorus+=0.0075
              type_scam="Skin Switcher Scam\nThis type of action(switching/swapping skins) is illegal/against game ToS and can lead to an account ban!"
          if "csgo"in str(response.text).lower() or "cs:go" in str(response.text).lower():

            scorus+=0.035
            if "trade offer" in str(response.text).lower():
              scorus+=0.015
            else:
              scorus += 0.005
          if str(j).lower()=="https://discord.com/nitro" or str(j).lower()=="https://discord.gg/" or str(j).lower()  =="https://discord.com/nitro/"  or "tenor.com"in str(j).lower()or   "giphy.com"in str(j).lower() or"steamcommunity.com" in str(j).lower()or"store.steampowered.com" in str(j).lower():
            scorus=0
        ####print(meta)
      else:
        if message.author.bot==False and message.author!=bot.user:
         
          try:  
            with open("serversettings.json","r")as f:
                settings=json.load(f)['errorlogging']
            if settings==True:
              await message.reply(f"We got a 404 Error from this website(||{j}||), meaning it may not exist, or is trying to hide information. We don't trust such websites!")
            else:
              pass
          except KeyError:
           pass
         
          #scorus+=0.5
     except requests.ConnectionError:
        if message.author.bot==False and message.author!=bot.user:
          
            try:
              with open("serversettings.json","r")as f:
                settings=json.load(f)['errorlogging']
              if settings==True:
                await message.reply(f"We got a ConnectionError meaning this website(|| {j}||) may not exist!")
            except KeyError:
              pass
          
        scorus=score
    ###print(scorus)

    if score>=0.2:
      score+=scorus
    else:
      score=scorus

    if "air drop" in message.content.lower() or "air-drop" in   message.content.lower() or  "airdrop" in message.content.lower():
      hits.append("airdrop")
      if "scam" not in message.content.lower():

          score+=0.005


    if "leaving this" in   message.content.lower() and "game" in  message.content.lower():

      score+=0.0055
      if "trade offer" in message.content.lower():
        score+=0.003
      else:
        score += 0.0025
      if len(type_scam)!=0:
        type_scam+=", Steam Scam"
      else:
        type_scam+="Steam Scam"
    if "csgo"in message.content.lower() or "cs:go" in message.content.lower():

      score+=0.0035
      if "trade offer" in message.content.lower():
        score+=0.0015
      else:
        score += 0.005
      if len(type_scam)!=0:
        type_scam+=", Steam Scam"
      else:
        type_scam+="Steam Scam"
    if len(urls)==0:
      score=0
  elif do==2:
    score=1
    scorus=1
    type_scam="Undefined...\nOne or more links in this message have appeared in our database of scam links!\nVisit [Here](https://raw.githubusercontent.com/45i/Frequent-Scams/Main/Malicious%20Websites/raw-links.txt) for more info!"
  elif do==3:
    score=1
    scorus=1
    type_scam="Undefined...\nThis exact message has appeared in the past and has automatically been cached!"
  if do != 4:   
    scam_data= pd.read_csv('scam.csv')
    X=scam_data.drop(columns=['text','is_scam']) #input dataset(text)
    y= scam_data['is_scam'] #output dataset(is_scam)

    bruh=""
    for i in urls: #not required
      bruh+=i+"\n" #it really isn't



    if len(urls)==0:
      score=0
    try:  
      model.fit(X,y)
    except NameError:
      model = DecisionTreeClassifier()
      model.fit(X,y)
    well=model.predict([[score]])
    ##print(f"{well} <- {message.content}")
    v=""
    ble=""
    exception="None"
    #print(well[0])
    if well[0]==1 and message.author!=bot.user and message.author.bot ==False:
      try:
        await message.delete()
        crack="Message Removed!"
      except discord.NotFound:
        crack="I tried removing the message but it might have already been removed..."
      except discord.Forbidden:
        crack="I don't have `manage messages` permission in this server!"

      with open("serversettings.json","r")as f:
          settings=json.load(f)
      try:
        if settings[str(message.guild.id)]['takeaction']==True:
          doit=True
        else:
          doit=False
      except KeyError:
        doit=True
      except AttributeError:
        doit=True  

      try:
        try:
          action= "none"
          if await get_action(message.guild.id) != "B":
            gg=await get_action(message.guild.id)
            ###print(gg)
            if  gg.lower()=="ban" and doit==True:
              await message.author.ban(reason=type_scam)
              action="ban"
              v="<:ban:920602343354032179> Violator was **banned**(Custom Action)!"
              ble="Scam removed, Message deleted! Moderator, please review this action and unban violator if required..."
              exception="None"
            elif gg.lower()=="kick" and doit==True:
              action="kick"
              v="<:kick:920601767245385768> Violator was **kicked**(Custom Action)!"
              await message.author.kick(reason=type_scam)
              ble="Scam removed, Message deleted! Moderator, please review this action..."
              exception="None"
            else:
              v="Server has TakeAction turned **OFF**"
              ble="No action taken"
          else:
            if doit==True and await get_action(message.guild.id)!="kick":
              await message.author.ban(reason=type_scam)
              v="<:ban:920602343354032179> Violator was banned(default action)\nrun `a!addaction <ban/kick> `!"
              ble="Scam removed, Message deleted! Moderator, please review this action and unban violator if required..."
              action="ban"
              exception="None"
            elif await get_action(message.guild.id)=="kick":
              action="kick"
              v="<:kick:920601767245385768> Violator was **kicked**(Custom Action)!"
              await message.author.kick(reason=type_scam)
              ble="Scam removed, Message deleted! Moderator, please review this action..."
              exception="None"
            else:
              v="Server has TakeAction turned **OFF**"
              ble="No action taken"

        except KeyError:
              await message.author.ban(reason=type_scam)
              v="<:ban:920602343354032179> Violator was banned(default action)\nrun `a!addaction <ban/kick> `!"
              ble="Scam removed, Message deleted! Moderator, please review this action and unban violator if required..."
              action="ban"
              exception="None"
      except Exception as e:
        ble="An Exception has occurred!"
        action="exception"
        exception=str(e)
        v=f"Heres the exception *as caught by the Handler*:\n```py\n{e}\n```"

      bb=bruh[0:len(bruh)-1]


      embed=discord.Embed(title=ble,description=v,colour=rndclr)

      if len(message.mentions)>0:
        roles = message.mentions
        roless = [role.mention for role in roles]
        roles=', '.join(roless)
      else:
        roles="None"
      if len(message.content)<=1024:
        for l in urls:
          lol.replace(l,f"`{l}`")
          embed.add_field(name="Message",value=f"||{lol}||")
      else:
        embed.add_field(name="Message",value=f"Message longer than 1024 characters...")
      embed.add_field(name="Type",value=type_scam)
      embed.add_field(name=f"Mentions", value=f"{roles}", inline=False)
      embed.add_field(name="URLs in message",value=f"||{bb.replace(')','')}||",inline=False)


      with open("case.json","r") as f:
        case_id=json.load(f)
      ###print(case_id)
      case_id['help']=str(int(case_id['help'])+1)
      with open("case.json","w") as f:
        json.dump(case_id,f,indent=4)
      info=[]

      info.append(action)
      try:  
        info.append(message.author.id)
      except:
        info.append(927059943935324211)
      info.append(lol)
      try:  
        info.append(message.channel.id)
      except:
        info.append(930136065690439781)
      try:  
        info.append(message.guild.id)
      except:
        info.append(909397210960126032)
      info.append(exception)
      with open("cases.json","r") as f:
        caseinfo=json.load(f)
      caseinfo[case_id['help']]=info
      with open("serversettings.json","r")as f:
        setting=json.load(f)
      try:
        if setting[str(message.guild.id)]['caserecording']==True:
          doit=True
        else:
          doit=False
      except KeyError:
        doit=True

      if doit==True:
        with open("cases.json","w") as f:
          json.dump(caseinfo,f,indent=4)

      embed.add_field(name="Violator",value=message.author.mention)
      embed.add_field(name="Case ID",value=case_id['help'])
      embed.add_field(name="Channel",value=message.channel.mention)
      uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
      embed.add_field(name="Acted upon in",value=uptime.split(':')[len(uptime.split(':'))-1]+" seconds")


      embed.add_field(name="Hits",value=hits,inline=False)
      embed.add_field(name="Warning!",value="Do not click on any of the links!",inline=False)
      embed.add_field(name="ScareScore Information",value=f"ScareScore: {score}\nScarePercent: {round((score/1)*100)}%",inline=False)
      embed.add_field(name="METAScore Information",value=f"METAScore: {scorus}\nMETAPercent: {round((scorus/1)*100)}%",inline=False)
      channel = bot.get_channel([debugchannelid])
      embed.timestamp = datetime.datetime.now()
      embed.set_footer(text="Even redirect and shortened URLs work too btw 😜")
      with open("serversettings.json","r")as f:
        setting=json.load(f)
      try:
        if setting[str(message.guild.id)]['privacymode']==True:
          doit=True
        else:
          doit=False
      except KeyError:
        doit=True
      if doit==True:
        await channel.send(embed=embed, content=f"Scam detected in {message.guild}" )

      with open("caselists.json","r") as f:
        prefixes=json.load(f)
      with open("serversettings.json","r")as f:
        setting=json.load(f)
      try:
        if setting[str(message.guild.id)]['caserecording']==True:
          doit=True
        else:
          doit=False
      except KeyError:
        doit=True
      id=case_id['help']
      try:
          if doit==True:
            gg=prefixes[str(message.guild.id)]


            if id not in gg:


              ff = 831154220723339324
              user = bot.get_user(ff)

              if user is None:  # Maybe the user isn't cached?
                user = await bot.fetch_user(ff)

              needthisshit=prefixes[str(message.guild.id)]
              # need_back=needthisshit
              needthisshit.append(case_id['help'])
              # pre_back=prefixes

              prefixes[str(message.guild.id)] = needthisshit

              with open('caselists.json', 'w') as f:
               json.dump(prefixes, f, indent=4)
          else:
            await message.channel.send(f"<:notnicetho:909790003863883877> Case not recorded! CaseInfo and CaseActions have been disabled for this case with id {id}")

      except KeyError:
         karma =[id]
         prefixes[str(message.guild.id)] = karma
         with open('caselists.json', 'w') as f:
           json.dump(prefixes, f, indent=4)
      with open ("serversettings.json","r")as f:
          settings=json.load(f)
      try:
        if settings[str(message.guild.id)]['caselogging']==True:
          doit=True
        else:
          doit = False
      except KeyError:
        doit=True

      try:

        if await get_channel(message.guild.id) != "no channel found" and doit==True:
          gg=await get_channel(message.guild.id)
          for ggg in gg:
            channel=bot.get_channel(int(ggg))
            try:
              edit=await channel.send(embed=embed)
            except Exception as e:
              try:
                try:
                  await message.channel.send(f"Couldn't log message in {channel.mention}!\nError: ```py\n{e}\n```")
                except discord.Forbidden:
                  pass
              except AttributeError:
                try:
                  await message.channel.send(f"Couldn't log message in {channel}!\nError: ```py\n{e}\n```")
                except discord.Forbidden:
                  pass
            if len(message.content)>1024:
              try:
                await channel.send(content=f"Message: \n{message.content}")
              except discord.Forbidden:
                  pass
        elif settings[str(message.guild.id)]['caselogging']==True and await get_channel(message.guild.id) == "no channel found":
          try:  
            await message.channel.send(f"No custom channel found, please use `a!linkchannel` to link it. Sending the message to the owner({message.guild.owner})")
          except discord.Forbidden:
                  pass
          try  :
            edit=await message.guild.owner.send(embed=embed, content="Please use `a!linkchannel` to link a channel for me to send the messages in")
            if len(message.content)>1024:
              await message.guild.owner.send(content=f"Message: \n{message.content}")
          except discord.Forbidden:
            edit=await message.channel.send(embed=embed, content="Please use `a!linkchannel` to link a channel for me to send the messages in... Couldn't send log to owner as I'm forbidden from doing so:(\n **Owner, please note that this compromises the server security!**")
            if len(message.content)>1024:
              await message.channel.send(content=f"Message: \n{message.content}")
        else:
          await message.channel.send("<:notnicetho:909790003863883877> Server has CaseLogging turned **OFF**")
      except KeyError:
        if doit==True:


          try:  
            await message.channel.send(f"No custom channel found, please use `a!linkchannel` to link it. Sending the message to the owner({message.guild.owner})")
          except: pass
          try  :
            edit=await message.guild.owner.send(embed=embed, content="Please use `a!linkchannel` to link a channel for me to send the messages in")
            if len(message.content)>1024:
              await message.guild.owner.send(content=f"Message: \n{message.content}")
          except discord.Forbidden:
            edit=await message.channel.send(embed=embed, content="Please use `a!linkchannel` to link a channel for me to send the messages in... Couldn't send log to owner as I'm forbidden from doing so:(\n **Owner, please note that this compromises the server security!**")
            if len(message.content)>1024:
              await message.channel.send(content=f"Message: \n{message.content}")
        else:
           await message.channel.send("<:notnicetho:909790003863883877> Server has CaseLogging turned **OFF**")

      try:
        await message.author.send(message.content,delete_after=10)
      except:
        print("no lol")
      try:
        await message.delete()
      except discord.NotFound:
        await edit.edit(content=crack, embed=embed)
      except discord.Forbidden:
        await edit.edit(content=crack, embed=embed)

      #scam(scam=message.content)

      score =0








    field_names = ['text','is_scam','danger_score']
    chuckycheese =message.content
    for mention in message.mentions:
        chuckycheese=str(chuckycheese).replace(str(mention),"")
    row_dict = {'text': chuckycheese.replace(",",""),'is_scam': well[0],'danger_score':score}
    #if random.randint(-100,100)==0:
      #writescam.append_dict_as_row('scam.csv', row_dict, field_names)
    score =0
    if do==True and  well[0]==1 and message.author!=bot.user and message.author.bot ==False:
      cachelist.append(message.content)
      cache["helpme"]=cachelist
      with open("cache.json","w")as f:
        json.dump(cache, f, indent=4)
    with open("serversettings.json","r")as f:
          settings=json.load(f)
    ban=0
    kick=0
    ex=0
    no=0
    for guild in bot.guilds:

     member=guild.get_member(message.author.id)
     if guild.get_member(message.author.id) is not None and well[0]==1 and message.author.bot==False   and message.author!=bot.user:
      try:
        if settings[str(guild.id)]['takeaction']==True:
          doit=True
        else:
          doit=False
      except KeyError:
        doit=True

      try:
        try:
          action= "none"
          if await get_action(guild.id) != "B":
            gg=await get_action(guild.id)
            ###print(gg)
            if  gg.lower()=="ban" and doit==True:
              await member.ban()
              action="ban"
              ggi=True
              ban+=1
              v="<:bonked:909103788470722581> Violator was **banned**(Custom Action)!"
              ble="Scam removed, Message deleted! Moderator, please review this action and unban violator if required..."

              exception="None"
            elif gg.lower()=="kick" and doit==True:
              action="kick"
              ggi=True
              kick+=1
              v="<:kick:908746838906142770> Violator was **kicked**(Custom Action)!"
              await member.kick()
              ble="Scam removed, Message deleted! Moderator, please review this action..."
              exception="None"
            else:
              ggi=False
              no+=1
              v="Server has TakeAction turned **OFF**"
              ble="No action taken"
          else:
            if doit==True and await get_action(guild.id)!="kick":
              ggi=True
              ban+=1
              await member.ban()
              v="<:bonked:909103788470722581> Violator was banned(default action)\nrun `a!addaction <ban/kick> `!"
              ble="Scam removed, Message deleted! Moderator, please review this action and unban violator if required..."
              action="ban"
              exception="None"
            elif await get_action(guild.id)=="kick":
              kick+=1
              action="kick"
              v="<:kick:908746838906142770> Violator was **kicked**(Custom Action)!"
              await member.kick()
              ble="Scam removed, Message deleted! Moderator, please review this action..."
              exception="None"
            else:
              no+=1
              v="Server has TakeAction turned **OFF**"
              ble="No action taken"

        except KeyError:
              ban+=1
              await member.ban()
              v="<:bonked:909103788470722581> Violator was banned(default action)\nrun `a!addaction <ban/kick> `!"
              ble="Scam removed, Message deleted! Moderator, please review this action and unban violator if required..."
              action="ban"
              exception="None"

      except Exception as e:
        ble="An Exception has occurred!"
        action="exception"
        exception=str(e)
        ex+=1
        v=f"Heres the exception *as caught by the Handler*:\n```py\n{e}\n```"

    if guild.get_member(message.author.id) is not None and well[0]==1 and message.author.bot==False   and message.author!=bot.user:
      try:
        await message.channel.send(f"{message.author.mention} was network-removed on {ban+kick} servers!\nBanned in {ban} servers\nKicked in {kick} servers\nNo Actions were taken in {no} servers\nException occurred in {ex} servers!")
        ban=0
        kick=0
        ex=0
        no=0
      except UnboundLocalError:
        wee=0
 await bot.process_commands(message)


@bot.event
async def on_guild_channel_delete(channel):
  with open('channel.json', 'r') as f:
         prefixes = json.load(f)

  try:
    if channel.id in prefixes[str(channel.guild.id)]:
      gg=prefixes[str(channel.guild.id)]
      att=gg.index(channel.id)
      gg.pop(att)
      ###print(gg)
      if len(gg)!=0:
          prefixes[str(channel.guild.id)]=gg
      else:
          prefixes.pop(str(channel.guild.id))
      with open('channel.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
      with open('channel backup.json', 'w') as f:
          json.dump(prefixes, f, indent=4)
  except KeyError:
    pass



@bot.event
async def on_command_error(ctx, error):
    i=False
    if isinstance(error, commands.MissingPermissions):
      try:
        await ctx.reply(f"```py\n{error}\n```Executed in: {ctx.message.channel.mention}, by {ctx.author}")
      except:
        await ctx.send(f"```py\n{error}\n```Executed in: {ctx.message.channel}, by {ctx.author}")
        
        
    # elif isinstance(error, commands.UserInputError):
    #     embed = discord.Embed(colour =rndclr)
    #     embed.set_author(name='Input error')
    #     embed.add_field(name='Something about your input was wrong.. just wrong... check your input and try again...',value='...')
    #     embed.set_footer(text ='Imagine getting a error msg lol')
    #     await ctx.reply(embed=embed)
    elif isinstance(error,commands.MissingRequiredArgument):
        embed = discord.Embed(colour = rndclr)
        embed.set_author(name='Missing arguement')
        embed.add_field(name='You forgot to add an arguement',value=f"`{error}` ")
        embed.set_footer(text ='Beep Bop Boop Beep?')
        await ctx.reply(embed=embed)
    elif isinstance(error,commands.BadArgument):
        embed = discord.Embed(colour = rndclr)
        embed.set_author(name='Bad Argument')
        embed.add_field(name='That\'s not the right one',value=f"{error}")
        embed.set_footer(text ='Beep Bop Boop Beep?')
        await ctx.reply(embed=embed)
    elif isinstance(error,commands.BotMissingPermissions):

            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_author(name='Missing Bot perms')
            embed.add_field(name='AntiScam is missing the required permissions for the command to work, give it the proper perms',value=f'{error}')
            embed.set_footer(text ='Did you forget to add the bot some perms?')
            await ctx.reply(embed=embed)
    elif isinstance(error,commands.NotOwner):


        embed = discord.Embed(colour = rndclr)
        embed.set_author(name='Why just why...')
        embed.add_field(name='You did a bot dev only command and thought it could work?',value='Haha Noob')
        embed.set_footer(text ='Why did you think you could do that?')
        await ctx.reply(embed=embed)
    elif isinstance(error,commands.CommandNotFound):
      list_of_commands=list(map(lambda m:m.name, filter(lambda m: m.name.startswith((str(error).split('"')[1][0])), bot.commands)))
      embed=discord.Embed(colour=rndclr,description="No such command found!")
      shit=""
      ###print(bot.commands)
      for i in list_of_commands:
        shit+=f"`{i}`\n"
      if len(shit)!=0:
          embed.add_field(name="Did You Mean?",value=shit)
      try:  
        await ctx.reply(embed=embed,delete_after=10)
      except:
        await ctx.send(embed=embed,delete_after=10)
    else:
      try:
        await ctx.reply(f"```py\n{error}\n```")
      except:
        await ctx.send(f"```py\n{error}\n```")




@bot.event
async def on_guild_join(guild):
  channel = bot.get_channel([channelid])
  embed=discord.Embed(description=f"Joined guild! {guild}",colour=discord.Colour.green())
  await guild.owner.send("Hi!\nThank you for choosing AntiScam!\nPlease note that the bot is still being actively developed under the hood...\nPlease familiarise yourself with a few of the important customised settings for your server, provided by AntiScam.\nWhen a scam is detected, the bot is to send a log to all the linked channels. If none exist then it will send the log to the owner. To link a channel use `a!linkchannel`\nThe bot bans violators(people who send scams) by default. But you can change this by running `a!addaction`. Available options are `ban`, and `kick`\nFor more information try running the help command at `a!help`\nWe would also recommend joining our support server here: \nhttps://discord.gg/FghqFerGsj")

  await channel.send(embed=embed)

keep_alive()
bot.run( os.environ['token'])

