from discord.ext import commands
import discord
import json
import random
import os
import requests
class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=["whois","userinfo"])
    async def info(self,ctx, *, user: discord.Member = None):
      """Get information about a user"""
      if not user:
          user = ctx.author

          embed = discord.Embed(title=f"{user.name}",
                                description=f"Server: {user.guild}",
                                color=user.color.value)
      else:
          embed = discord.Embed(title=f"{user.name}",
                                description=f"Server: {user.guild}",
                                color=user.color.value)
      # Add author, thumbnail, fields, and footer to the embed
      if ".gif" in str(user.avatar_url):
          embed.set_author(name=f"Data From Discord",
                           icon_url=ctx.author.avatar_url)
      else:
          embed.set_author(name=f"Data From Discord", icon_url=user.avatar_url)
      embed.add_field(name=f"Nickname",
                      value=f"{user.display_name}",
                      inline=False)
      name_split = str(user).split()
      i = 0
      discrim = ""
      seg = ""
      while i < len(name_split):
          seg = name_split[i]
          if "#" in seg:
              discrim = seg
          i += 1

      embed.add_field(name=f"ID", value=f"{user.id}", inline=False)
      embed.add_field(name=f"Discriminator", value=f"{user.discriminator}", inline=False)
      embed.add_field(name=f"Color", value=user.color, inline=False)
      req=requests.get(f"https://showcase.api.linx.twenty57.net/UnixTime/tounix?date={str (user.joined_at).replace(' ','%20')}")
      res=req.json()

      embed.add_field(name=f"Joined At", value=f"<t:{res}:R>", inline=False)
      req=requests.get(f"https://showcase.api.linx.twenty57.net/UnixTime/tounix?date={str (user.created_at).replace(' ','%20')}")
      res=req.json()

      embed.add_field(name=f"Created At",
                      value=f"<t:{res}:R>",
                      inline=False)
      embed.add_field(name=f"IsPending", value=f"{user.pending}", inline=False)

      roles = user.roles
      roles = [role.mention for role in roles]
      embed.add_field(name=f"Roles", value=f"{', '.join(roles)}", inline=False)
      embed.add_field(name=f"Top Role", value=f"{user.top_role}", inline=False)
      embed.add_field(name=f"Channel Permissions ", value=f"{user.permissions_in(ctx.channel)}", inline=False)
      embed.add_field(name=f"Guild Permissions", value=f"{user.guild_permissions}", inline=False)
      print(user.avatar_url)

      if ".gif" in str(user.avatar_url):

          embed.add_field(
              name="Epilepsy Trigger hidden",
              value=
              "User avatar is a .gif file and may trigger epilepsy. It has been hidden",
              inline=False)

      else:

          embed.set_image(url=f"{user.avatar_url}")

      embed.add_field(name=f"Is {user.display_name} an administrator?",
                      value=user.guild_permissions.administrator,
                      inline=True)
      embed.add_field(name=f"Can {user.display_name} kick members?",
                      value=user.guild_permissions.kick_members,
                      inline=True)
      embed.add_field(name=f"Can {user.display_name} ban members?",
                      value=user.guild_permissions.ban_members,
                      inline=True)
      embed.add_field(name=f"Is {user.display_name} a bot?",
                      value=user.bot,
                      inline=True)
      embed.add_field(name=f"Is {user.display_name} a Discord System User?",
                      value=user.system,
                      inline=True)

      embed.set_footer(text="Information requested by: {}".format(
          ctx.author.display_name, ctx.author.avatar_url),
          icon_url=ctx.author.avatar_url)

      #### Useful ctx variables ####
      ## User's display name in the server
      ctx.author.display_name

      ## User's avatar URL
      ctx.author.avatar_url
      await ctx.send(embed=embed)
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def getcaseinfo(self,ctx,case_id:int):
     """For MODS only! Use this command to get information on a case. Requires the CaseID ofcourse""" 
     rndclr=random.choice([discord.Colour.red().value,discord.Colour.dark_grey().value])
     with open("cases.json","r") as f:
        idk=json.load(f)
    
     if idk[str(case_id)][4] == ctx.guild.id:
      if str(case_id) in idk.keys() :
        embed= discord.Embed(color=rndclr)

        embed.add_field(name="Case ID", value=case_id,inline=False)
        embed.add_field(name="Message Content", value=idk[str(case_id)][2],inline=False)
        id=idk[str(case_id)][1]
        user = self.bot.get_user(id)
    
        if user is None:  # Maybe the user isn't cached?
                   user = await self.bot.fetch_user(id)
        channel=self.bot.get_channel(idk[str(case_id)][3])
        guild=self.bot.get_guild(idk[str(case_id)][4])
        embed.add_field(name="Message Author", value=user.mention,inline=False)
        embed.add_field(name="Channel In Which Message Was Sent", value=channel.mention,inline=False)
        embed.add_field(name="Guild Message Was Sent", value=guild,inline=False)
        embed.add_field(name="Action Taken", value=idk[str(case_id)][0],inline=False)

        if idk[str(case_id)][5]:  
          embed.add_field(name="Exception", value=idk[str(case_id)][5],inline=False)
        else:
          embed.add_field(name="Exception", value="None",inline=False)
        await ctx.reply(embed=embed,mention_author=False)
      else:
        embed= discord.Embed(description="No case with that ID found!",color=rndclr)
        await ctx.reply(embed=embed,mention_author=False)
     else:
        embed= discord.Embed(description="This case is not from this server!",color=rndclr)
        await ctx.reply(embed=embed,mention_author=False)
    @commands.command()
    async def report(self,ctx,*,bug:str):
      with open("bug.txt","r") as f:
          case_id=int(f.read())
    ##print(case_id)
      
      
      info={}

      info['bug']=(bug)
      info['reporter']=(ctx.author.id)
      info['status']= "\🙈 Unseen"
      
      with open("bugreports.json","r") as f:
        caseinfo=json.load(f)
      message=await ctx.reply(f"Your report will be sent as:\n> {bug}\nProceed?")
      await message.add_reaction("✅")
      await message.add_reaction("❎")
      check=lambda r,  u: u == ctx.author and message and str(r.emoji) in "✅❎"
      reaction, user = await self.bot.wait_for("reaction_add", check=check)
      if str(reaction.emoji)=="✅":
        caseinfo[case_id]=info
        with open("bugreports.json","w") as f:
          json.dump(caseinfo,f,indent=4)
        try:  
          await message.clear_reaction(emoji="❎")
          await message.clear_reaction(emoji='✅')
        except Exception as e :
          await message.reply(f"Couldn't clear reactions :(\n```py\n{e}\n```")
        await message.edit(content="Thank you for sending a report! The developer may get back to you if required!",delete_after=10)
        channel = self.bot.get_channel(912740836201087046)
        await channel.send(embed=discord.Embed(description=f"New Bug Report!\n> {bug}\nReported By: {ctx.author.mention}({ctx.author})\nStatus: \🙈 Unseen\nBug Id: {case_id}"))
        case_id=str(int(case_id)+1)
        with open("bug.txt","w") as f:
          f.write(case_id)
      else:
        await message.clear_reaction(emoji="❎")
        await message.clear_reaction(emoji='✅')
        await message.edit(content="Aborted!",delete_after=10)
      

    @commands.command()
    async def ping (self,ctx):
        """Get the bot's latency"""
        rndclr=random.choice([discord.Colour.red().value,discord.Colour.dark_grey().value])
        # i=0
        #bb=dat
        dot=["...","..","."]
        message=await ctx.send(f"Pinging"+random.choice(dot))
        #req=requests.get(f"https://showcase.api.linx.twenty57.net/UnixTime/tounix?date={str(bb).replace(' ','%20')}")
        #res=req.json()
        global uptime
        #uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        embed=discord.Embed(title="Ping",colour=rndclr)
        embed.add_field(name="Latency", value=f"{round(self.bot.latency * 1000)}ms")
        # embed.add_field(name="Uptime", value=uptime)
        # embed.add_field(name="Uptime Approximation", value=f"<t:{res}:R>")

        embed.set_footer(text=f"{self.bot.user}")

        try:
          await message.edit(embed=embed,content="Pong!")
        except discord.HTTPException:
        #   await ctx.send("Current uptime: " + uptime)
          await ctx.send("Latency: " + f"{round(self.bot.latency * 1000)}ms")
    @commands.command()
    async def stats(self,ctx):
      """Get bot stats\nPreviously known as a!botinfo"""
      rndclr=random.choice([discord.Colour.red().value,discord.Colour.dark_grey().value])
      guild=self.bot.guilds
      members_set = set()
      for guild in guild:
          for member in guild.members:
            members_set.add(member)
      members = len(members_set)
      #Create a variable that contains all the servers
      activeServers = self.bot.guilds
      #Create a variable to store amount of members per server
      sum = 0
      #Loop through the servers, get all members and add them up
      #uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
      for s in activeServers:
            sum += len(s.members)
  
      import psutil
  
      # Getting loadover15 minutes
      load1, load5, load15 = psutil.getloadavg()
  
      cpu_usage = (load15/os.cpu_count()) * 100
      # Getting all memory using os.popen()
      total_memory, used_memory, free_memory = map(
      int, os.popen('free -t -m').readlines()[-1].split()[1:])
  
      
      e=discord.Embed(color=rndclr,title="Bot Stats")
      if len(self.bot.guilds)%10==0:
        gru=f"Milestone Reached! <:cool:920602032262508594>: {len(self.bot.guilds)} servers!" 
      elif len(self.bot.guilds)==69or len(self.bot.guilds)==420 or len(self.bot.guilds)==1337:
             gru=f"Hehe **{len(self.bot.guilds)}** servers"
      else:
        gru=f"**{len(self.bot.guilds)}** servers!"
      e.add_field(name="Servers", value=gru)
      e.add_field(name="Members", value=sum)
      e.add_field(name="Hosting Service", value="Replit")
      e.add_field(name="Latency", value=f"{round(self.bot.latency * 1000)}ms")
      #e.add_field(name="Uptime", value=uptime)
      e.add_field(name="ML Algorithm Provider", value=f"[SciKit Learn](https://scikit-learn.org)")
      e.add_field(name="ML Algorithm", value=f"[Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html?highlight=decisiontree#sklearn.tree.DecisionTreeClassifier)")
      e.add_field(name="Language",value="Python")
      e.add_field(name="Hardware",value=f"`CPU USAGE: {cpu_usage}%\nRAM USAGE: { round((used_memory/total_memory) * 100, 2)}%`",inline=False)
      id = 886309422526259231
      user = self.bot.get_user(id)
      
      e.set_thumbnail(url="https://top.gg/api/widget/886309422526259231.svg")
      with open('channel.json', 'r') as f:
            prefixes = json.load(f)
      try:  
        gg=prefixes[str(ctx.guild.id)]
        stringthing=""
        i=0
        for ch in gg:  
          channel=self.bot.get_channel(ch)
          if i!=len(gg)-1:   
            stringthing+=f"{channel.mention} "
          else:
            stringthing+=f"{channel.mention}"
          i+=1
        e.add_field(name="Linked Channel in this server",value=f"{stringthing.replace(' ',', ')}\nUse `a!serverdata` to get more data about this server")
      except KeyError:
         e.add_field(name="Linked Channel in this server",value="None found...\nuse `a!linkchannel` to link one!\nTry `a!serverdata` to get more data recorded from this server")
      if user is None:  # Maybe the user isn't cached?
                    user = await self.bot.fetch_user(id)
      #e.add_field(name="Top Role",value=self.bot.user.top_role)
      e.add_field(name=f"Reaction reponses | ONLY APPLICABLE TO {str(ctx.author).split('#')[0].upper()}", value=f"React with 📥 to get my invite link\nIf you love my services, please consider voting for me on Top.gg. Simply react with 🗳",inline=False)#damn
  
      e.set_footer(text=f"Developed solely by Iced Dev#7379 ")
      message=await ctx.reply(content="> Check out our curated list of scam links we have collected: https://github.com/45i/Frequent-Scams",embed=e,mention_author=False)
      await message.add_reaction("📥")
      await message.add_reaction("🗳")
  
      emb=discord.Embed(title="Did you love the bot?",colour=rndclr)
      emb.add_field(name="If so, please Vote it on Top.gg!",value="Click [**Here**](https://top.gg/bot/886309422526259231/vote)!")
      # pop=requests.get(f"https://top.gg/api/self.bots/886309422526259231/votes")
      # pp=pop.json()
      #print(pp)
      yy="Developed Solely by Iced Dev#7379 | Don't forget to write a review!"
      # if pp["voted"]==0 and "voted" in pp:
      #   yy="You have voted for me 0 times in this month :("
      # elif pp["error"]=="Unauthorized" and "voted" not in pp:
      #     yy="Developed Solely by Iced Dev#7379"
      # else:
      #   yy=f"You have voted for me {pp['voted']} times in this month! :)"
      emb.set_footer(text=yy)
  
      check=lambda r,u: u == ctx.author and message and str(r.emoji) in "📥🗳📧"
      reaction, user = await self.bot.wait_for("reaction_add", check=check)
      if str(reaction.emoji) == "📥":
        emb=discord.Embed(description="Click **[Here](https://discord.com/api/oauth2/authorize?client_id=886309422526259231&permissions=268495879&scope=bot)** to invite the standard version, or **[here](https://discord.com/oauth2/authorize?client_id=842588036675928094&permissions=92164&scope=bot)** to invite the BETA version")
        mssage=await user.send(embed=emb)
        em=discord.Embed(title="Invite sent", description=f"Check your DMs or click [**Here**]({mssage.jump_url})")
  
        await message.edit(embed=em)
  
        await message.clear_reaction(emoji="📥")
        await message.clear_reaction(emoji='🗳')
  
  
  
      if str(reaction.emoji) == "🗳":
        await message.edit(embed=emb)
        await message.clear_reaction(emoji="📥")
        await message.clear_reaction(emoji='🗳')
    
    @commands.command()
    async def serverdata(self,ctx):
      """Get a summary of all the data we have collected from this server"""
      rndclr=random.choice([discord.Colour.red().value,discord.Colour.dark_grey().value])
      guild=ctx.guild.id
      with open("action.json","r")as f:
        action=json.load(f)
      with open("ann_chan.json","r")as f:
        ann=json.load(f)
      with open("caselists.json","r")as f:
        cases=json.load(f)
      with open("channel.json","r")as f:
        channels=json.load(f)
      i=0
      stringthing=""
      casestr=""
      annstr=""
      actionstr=""
      try:  
        gg=channels[str(ctx.guild.id)]
        for ch in gg:  
          channel=self.bot.get_channel(ch)
          if i!=len(gg)-1:   
            stringthing+=f"{channel.mention}, "
          else:
            stringthing+=f"{channel.mention}"
          i+=1
      except KeyError:

        stringthing="None found...\nuse `a!linkchannel` to link one!"
      i=0
      try:  
        casesh=cases[str(ctx.guild.id)]
        for ch in casesh:  

          if i!=len(casesh)-1:   
            casestr+=f"{ch}, "
          else:
            casestr+=f"{ch}"
          i+=1
      except KeyError:
        casestr="No cases recorded in this server! Yay! <:cool:907253652996116480>"
      i=0
      # for ch in ann:  
      #     channel=self.bot.get_channel(ch)
      #     if i!=len(ann)-1:   
      #       stringthing+=f"{channel.mention}, "
      #     else:
      #       stringthing+=f"{channel.mention}"
      #     i+=1
      # i=0

      try:
                    gg=action[str(ctx.guild.id)]
                    actionstr=f"I will {gg} scammers in this server!"
      except KeyError:
                    actionstr=f"I will ban scammers in this server as there is no custom action set up! Use `a!addaction <action>` to set up a custom action. If no action is set up, I will ban the violator!"

      i=0
      embed=discord.Embed(color=rndclr)
      embed.add_field(name="Linked Channels",value=stringthing,inline=False)
      embed.add_field(name="Recorded Cases",value=casestr,inline=False)
      embed.add_field(name="Linked Action",value=actionstr,inline=False)
      embed.set_footer(text="Use `a!settings` to tweak certain settings specific to this server")
      await ctx.reply(embed=embed)

  
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def editcaseaction(self,ctx, case_id:int):
      """For MODS only! Use this command to edit the action taken for a crtain case"""
      rndclr=random.choice([discord.Colour.red().value,discord.Colour.dark_grey().value])
      with open("cases.json","r") as f:
        idk=json.load(f)
      #print(idk.keys())
      #print(idk[str(case_id)])

      if idk[str(case_id)][4] == ctx.guild.id: 
       if str(case_id) in idk.keys():
        embed= discord.Embed(color=rndclr)

        if idk[str(case_id)][0] =="ban":
          mseg=await ctx.reply("Based on the action taken for this case, the available action is to unban the violator...\nProceed?")
          await mseg.add_reaction("✅")
          await mseg.add_reaction("❌")
          check=lambda r, u: u == ctx.author and str(r.emoji) in "✅❌"
          reaction, usr = await self.bot.wait_for("reaction_add", check=check)  
          if str(reaction.emoji)=="✅":
            await mseg.clear_reaction("✅")
            await mseg.clear_reaction("❌")
            id=idk[str(case_id)][1]
            user = self.bot.get_user(id)

            if user is None:  # Maybe the user isn't cached?
                   user = await self.bot.fetch_user(id)

            await mseg.edit(content="Unban Requested",embed=None,mention_author=False)
            await ctx.guild.unban(user)
            await mseg.edit(content="Unban Successful!",embed=None,mention_author=False,delete_after=10)
            idk[str(case_id)][0]=f"**Original Action**: Ban\n*Violator was unbanned by {ctx.author.mention}*"
            with open("cases.json","w") as f:
                  json.dump(idk, f, indent=4)
          else:
            await mseg.edit(content="Unban Cancelled",embed=None,mention_author=False,delete_after=10)
        # elif idk[str(case_id)][0] =="mute":

        #     id=idk[str(case_id)][1]
        #     user = self.bot.get_user(int(id))

        #     if user != None and user in ctx.guild.members:  # Maybe the user isn't cached?

        #       mseg=await ctx.reply("Based on the action taken for this case, the available action is to unmute the violator...\nProceed?")
        #       await mseg.add_reaction("✅")
        #       await mseg.add_reaction("❌")
        #       check=lambda r, u: u == ctx.author and str(r.emoji) in "✅❌"
        #       reaction, usr = await self.bot.wait_for("reaction_add", check=check)  
        #       if str(reaction.emoji)=="✅":
        #         await mseg.clear_reaction("✅")
        #         await mseg.clear_reaction("❌")        
        #         await mseg.edit(content="Unmute Requested",embed=None,mention_author=False)
        #         with open("m_role.json","r")as f:
        #           roles=json.load(f)
        #         print(roles[str(ctx.guild.id)])
        #         for role in roles[str(ctx.guild.id)]:  
        #           print(role)
        #           mutedRole = discord.utils.get(ctx.guild.roles, name=str(role))
        #           await user.remove_roles(mutedRole)
        #         await mseg.edit(content="Unmute Successful!",embed=None,mention_author=False,delete_after=10)
        #         idk[str(case_id)][0]=f"**Original Action**: Mute\n*Violator was unmuted by {ctx.author.mention}*"
        #         with open("cases.json","w") as f:
        #           json.dump(idk, f, indent=4)
        #       else:
        #         await mseg.edit(content="Unmute Cancelled",embed=None,mention_author=False,delete_after=10)
        #     else:
        #       await mseg.edit(content="User isn't present in this server!",embed=None,mention_author=False,delete_after=10)

        elif "unbanned" in idk[str(case_id)][0]:
          await ctx.reply("Violator was already unbanned!")
        else:
          await ctx.reply("No relevant action found!")
      else:

        embed= discord.Embed(description="This case is not from this server!",color=rndclr)
        await ctx.reply(embed=embed,mention_author=False)

  
def setup(bot):
    bot.add_cog(Utilities(bot))