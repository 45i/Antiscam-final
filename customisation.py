from discord.ext import commands
import discord
import json
import random
import asyncio
class Customisation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["aa"])
    @commands.has_permissions(administrator=True)
    async def addaction(self,ctx,action:str):
           """Add ban/kick action to the bot. Only called when a scam occurs"""
           if "ban" in action.lower():
             karma="ban"
             with open('action.json', 'r') as f:
              prefixes = json.load(f)
             prefixes[str(ctx.guild.id)] = karma
             with open('action.json', 'w') as f:
              json.dump(prefixes, f, indent=4)

           elif "kick" in action.lower():
             karma="kick" 
             with open('action.json', 'r') as f:
              prefixes = json.load(f)
             prefixes[str(ctx.guild.id)] = karma
             with open('action.json', 'w') as f:
              json.dump(prefixes, f, indent=4)
           else:
             if action[0].lower()=="b" or len(action)==3:
               await ctx.reply("That isn't a valid action!\nDid you mean: `ban`?")
               karma="ban"
             else:
             
               if action[0].lower()=="k":
                 await ctx.reply("That isn't a valid action!\nDid you mean: `kick`?")
                 karma="kick"
               else:
                 await ctx.reply("That isn't a valid action!\nAvailable actions are: \n > `kick`\n> `ban`")
                 karma="None\nArgument was wrong!!"


           await ctx.reply(f"Added action `{karma}`!")
             
    @commands.command(aliases=["lc"])
    @commands.has_permissions(manage_channels=True)
    async def linkchannel(self,ctx,*,channel:discord.TextChannel):
         """Link a channel to the bot. Only called when a scam occurs to log the scam in a set channel/multiple channels"""
         id=channel.id
         with open('channel.json', 'r') as f:
             prefixes = json.load(f)
         try:
              gg=prefixes[str(ctx.guild.id)]
              channel=self.bot.get_channel(id)
              if id not in gg:
               try:
                await channel.send(content="This is a test message...",delete_after=1)
                msg=await ctx.reply(f"This will action will add {channel.mention} to my database!\nReact with ✔ to update the information or with ❌ to let it be")
               except discord.Forbidden:
                msg=await ctx.reply(f"This will action will add {channel.mention} to my database!\nNote: **I Don't have `send_messages` perms in this channel!**\nReact with ✔ to update the information or with ❌ to let it be")
               await msg.add_reaction("✔")
               await msg.add_reaction("❌")
               check=lambda r, u: u == ctx.author and str(r.emoji) in "✔❌"
               reaction, user = await self.bot.wait_for("reaction_add", check=check)
               if str(reaction.emoji)=="❌":
                await msg.edit(content="Update skipped...", delete_after=10)
                await msg.clear_reaction("❌")
                await msg.clear_reaction("✔")

               elif str(reaction.emoji)=="✔":
                id = 831154220723339324
                user = self.bot.get_user(id)
    
                if user is None:  # Maybe the user isn't cached?
                  user = await self.bot.fetch_user(id)
    
                needthisshit=prefixes[str(ctx.guild.id)]
                # need_back=needthisshit
                needthisshit.append(channel.id)
                # pre_back=prefixes

                prefixes[str(ctx.guild.id)] = needthisshit

                with open('channel.json', 'w') as f:
                 json.dump(prefixes, f, indent=4)



                with open("channel backup.json","w") as f:
                    json.dump(prefixes, f, indent=4)

                await msg.edit(content=f"Updated database to include **{channel.mention}**(`{id}`)!",
                delete_after=10)

                await msg.clear_reaction("❌")
                await msg.clear_reaction("✔")
                await channel.send("I'll log scams here!")


              else:
                await ctx.reply("That channel is already linked!")

         except KeyError:
           karma =[id]
           prefixes[str(ctx.guild.id)] = karma
           with open('channel.json', 'w') as f:
             json.dump(prefixes, f, indent=4)
           channel=self.bot.get_channel(id)
           await ctx.reply(f"Added channel {channel.mention} with id `{id}`!")
    @commands.command(aliases=["lac"])
    @commands.has_permissions(administrator=True)
    async def linkannouncementchannel(self,ctx, channel:discord.TextChannel):
         """Currently WIP, will be updated when done"""
         id=channel.id
         with open('ann_chan.json', 'r') as f:
             prefixes = json.load(f)
         try:
              gg=prefixes[str(ctx.guild.id)]
              channel=self.bot.get_channel(id)
              if id not in gg:
               try:
                await channel.send(content="This is a test message...",delete_after=1)
                msg=await ctx.reply(f"This will action will add {channel.mention} to my database!\nReact with ✔ to update the information or with ❌ to let it be")
               except discord.Forbidden:
                msg=await ctx.reply(f"This will action will add {channel.mention} to my database!\nNote: **I Don't have `send_messages` perms in this channel!**\nReact with ✔ to update the information or with ❌ to let it be")
               await msg.add_reaction("✔")
               await msg.add_reaction("❌")
               check=lambda r, u: u == ctx.author and str(r.emoji) in "✔❌"
               reaction, user = await self.bot.wait_for("reaction_add", check=check)
               if str(reaction.emoji)=="❌":
                await msg.edit(content="Update skipped...", delete_after=10)
                await msg.clear_reaction("❌")
                await msg.clear_reaction("✔")

               elif str(reaction.emoji)=="✔":
                id = 831154220723339324
                user = self.bot.get_user(id)
    
                if user is None:  # Maybe the user isn't cached?
                  user = await self.bot.fetch_user(id)
    
                needthisshit=prefixes[str(ctx.guild.id)]
                # need_back=needthisshit
                needthisshit.append(channel.id)
                # pre_back=prefixes

                prefixes[str(ctx.guild.id)] = needthisshit

                with open('ann_chan.json', 'w') as f:
                 json.dump(prefixes, f, indent=4)





                await msg.edit(content=f"Updated database to include **{channel.mention}**(`{id}`)!",
                delete_after=10)

                await msg.clear_reaction("❌")
                await msg.clear_reaction("✔")
                await channel.send("I'll log scams here!")


              else:
                await ctx.reply("That channel is already linked!")

         except KeyError:
           karma =[id]
           prefixes[str(ctx.guild.id)] = karma
           with open('ann_chan.json', 'w') as f:
             json.dump(prefixes, f, indent=4)
           channel=self.bot.get_channel(id)
           await ctx.reply(f"Added channel {channel.mention} with id `{id}`!")
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def settings (self,ctx,module:str=None,state:bool=None):
     """Change server settings! This is a VERY dangerous command as it WILL alter the performance of the bot based on the settings you have chosen!"""
     rndclr=random.choice([discord.Colour.red().value,discord.Colour.dark_grey().value])
     if module==None and state==None: 
      embed=discord.Embed(color=rndclr)
    
      try:
        with open("serversettings.json","r")as f:
          uhh=json.load(f)
        settings=uhh[str(ctx.guild.id)]
        print(settings)
        caselogging=settings['caselogging']
        caserecording=settings['caserecording']
        takeaction=settings['takeaction']
        privacymode=settings['privacymode']
        err=settings['errorlogging']
        if caselogging==True:
          caselogging="\✅"
        if caserecording==True:
          caserecording="\✅"  
        if takeaction==True:
          takeaction="\✅"  
        if privacymode==True:
          privacymode="\✅"  
        if err==True:
          err="\✅"
        if caselogging==False:
          caselogging="\❎"  
        if caserecording==False:
          caserecording="\❎"  
        if takeaction==False:
          takeaction="\❎"  
        if privacymode==False:
          privacymode="\❎"  
        if err==False:
          err="\❎"
        embed.add_field(name="Case Logging",value=f"Toggles Case Logging for each scam detected\nCase Logging is where the bot will log cases to the linked channels or to the owner(if no linked channels exist)... This setting changes that.\nUse `a!settings caselogging <state(True or False)>`\nCurrent State: {caselogging}",inline=False)
        embed.add_field(name="Case Recording",value=f"Toggles Case Recording for each scam detected\nCase Recording is where the bot will record cases to the DataBase which can be then accessed by the `getcaseinfo`, `serverdata`, and the `editcaseaction` commands... This setting changes that.\nUse `a!settings caserecording <state(True or False)>`\nCurrent State: {caserecording}",inline=False)
        embed.add_field(name="Take Action",value=f"Toggles Taking Action against violators(**This is not recommended as this will not kick or ban violators!**)\nUse `a!settings takeaction <state(True or False)>`\nCurrent State: {takeaction}",inline=False)
        embed.add_field(name="Privacy Mode",value=f"Toggles Privacy Mode for this server(**This is not recommended as this will stop logging scams in our support server! Don't worry, it's only visible to the devs and is only used to test the bot's response time and accuracy!**)\nUse `a!settings privacymode <state(True or False)>`\nCurrent State: {privacymode}",inline=False)
        embed.add_field(name="Error Logging",value=f"Toggles Error Logging for this server(**This is not recommended as this will stop logging errors when they occur [For Example: _`403` Errors_]!**)\nUse `a!settings errorlogging <state(True or False)>`\nCurrent State: {err}",inline=False)
      except KeyError:
        settings={}
        settings['caselogging']=True
        settings['caserecording']=True
        settings['takeaction']=True
        settings['privacymode']=False
        settings['errorlogging']=False
        with open("serversettings.json","r") as f:  
          settingsh=json.load(f)
        settingsh[str(ctx.guild.id)]=settings
        with open("serversettings.json","w") as f:
          json.dump(settingsh,f,indent=4)
        embed.add_field(name="Case Logging",value=f"Toggles Case Logging for each scam detected\nCase Logging is where the bot will log cases to the linked channels or to the owner(if no linked channels exist)... This setting changes that.\nUse `a!settings caselogging <state(True or False)>`\nCurrent State: \✅",inline=False)
        embed.add_field(name="Case Recording",value=f"Toggles Case Recording for each scam detected\nCase Recording is where the bot will record cases to the DataBase which can be then accessed by the `getcaseinfo`, `serverdata`, and the `editcaseaction` commands... This setting changes that.\nUse `a!settings caserecording <state(True or False)>`\nCurrent State: \✅",inline=False)
        embed.add_field(name="Take Action",value=f"Toggles Taking Action against violators(**This is not recommended as this will not kick or ban violators!**)\nUse `a!settings takeaction <state(True or False)>`\nCurrent State: \✅",inline=False)
        embed.add_field(name="Privacy Mode",value=f"Toggles Privacy Mode for this server(**This is not recommended as this will stop logging scams in our support server! Don't worry, it's only visible to the devs and is only used to test the bot's response time and accuracy!**)\nUse `a!settings privacymode <state(True or False)>`\nCurrent State: \❎",inline=False)
        embed.add_field(name="Error Logging",value=f"Toggles Error Logging for this server(**This is not recommended as this will stop logging errors when they occur [For Example: _`403` Errors_]!**)\nUse `a!settings errorlogging <state(True or False)>`\nCurrent State: \❎",inline=False)
      await ctx.reply(embed=embed)
     elif module!=None and state==None:
        with open("serversettings.json","r")as f:
          uhh=json.load(f)
        try:
          settings=uhh[str(ctx.guild.id)]
          if module.lower()=="caselogging":
            if settings['caselogging']==True:
             settings['caselogging']=False
             bb="Turned CaseLogging **OFF**"
            else:
              settings['caselogging']=True
              bb="Turned CaseLogging **ON**"
          elif module.lower()=="caserecording":
            if settings['caserecording']==True:
              settings['caserecording']=False
              bb="<:notrecording:920715329984933909> Turned CaseRecording **OFF**"
            else:
              settings['caserecording']=True
              bb="<:recording:920713742604455967> Turned CaseRecording **ON**"
          elif module.lower()=="takeaction":
            if settings['takeaction']==True:
              settings['takeaction']=False
              bb="<:nottakingaction:920719953781456898> Turned TakeAction **OFF**"
            else:
              settings['takeaction']=True
              bb="<:takingaction:920719954968445057> Turned TakeAction **ON**"
          elif module.lower()=="privacymode":
            if settings['privacymode']==True:
               settings['privacymode']=False
               bb="<:notincognito:920605377840680960> Turned PrivacyMode **OFF**"
            else:
              settings['privacymode']=True
              bb="<:incognito:920605376997650433> Turned PrivacyMode **ON**"
          elif module.lower()=="errorlogging":
            if settings['errorlogging']==True:
             settings['errorlogging']=False
             bb="Turned Error Logging **OFF**"
            else:
              settings['errorlogging']=True
              bb="Turned Error Logging **ON**"
          else:
            bb="<:notnicetho:920712378151231508> Sorry that's not a setting!\nYou may choose from the following options:\n> **CaseLogging**\n> **CaseRecording**\n> **TakeAction**\n> **Privacymode**\nRun `a!settings` to get detailed info about what each one of these actions do!"
          settingsh={}
          settingsh[str(ctx.guild.id)]=settings
          with open("serversettings.json","w")as f:
            json.dump(settingsh, f, indent=4)

        except KeyError:
          settings={}
          with open("serversettings.json","r") as f:
            settingsh=json.load(f)

          settings['caselogging']=True
          settings['caserecording']=True
          settings['takeaction']=False
          settings['privacymode']=False
          settings['errorlogging']=False
          if module.lower()=="caselogging":
            if settings['caselogging']==True:
             settings['caselogging']=False
             bb="Turned CaseLogging **OFF**"
            else:
              settings['caselogging']=True
              bb="Turned CaseLogging **ON**"
          elif module.lower()=="caserecording":
            if settings['caserecording']==True:
              settings['caserecording']=False
              bb="<:notrecording:920715329984933909> Turned CaseRecording **OFF**"
            else:
              settings['caserecording']=True
              bb="<:recording:920713742604455967> Turned CaseRecording **ON**"
          elif module.lower()=="takeaction":
            if settings['takeaction']==True:
              settings['takeaction']=False
              bb="<:nottakingaction:920719953781456898> Turned TakeAction **OFF**"
            else:
              settings['takeaction']=True
              bb="<:takingaction:920719954968445057> Turned TakeAction **ON**"
          elif module.lower()=="privacymode":
            if settings['privacymode']==True:
               settings['privacymode']=False
               bb="<:notincognito:920605377840680960> Turned PrivacyMode **OFF**"
            else:
              settings['privacymode']=True
              bb="<:incognito:920605376997650433> Turned PrivacyMode **ON**"
          elif module.lower()=="errorlogging":
            if settings['errorlogging']==True:
             settings['errorlogging']=False
             bb="Turned Error Logging **OFF**"
            else:
              settings['errorlogging']=True
              bb="Turned Error Logging **ON**"
          else:
            bb="<:notnicetho:920712378151231508> Sorry that's not a setting!\nYou may choose from the following options:\n> **CaseLogging**\n> **CaseRecording**\n> **TakeAction**\n> **Privacymode**\nRun `a!settings` to get detailed info about what each one of these actions do!"
          settingsh[str(ctx.guild.id)]=settings
          with open("serversettings.json","w")as f:
            json.dump(settingsh, f, indent=4)
        await ctx.reply(bb)
     elif module!=None and state!=None:
        with open("serversettings.json","r")as f:
          uhh=json.load(f)
        try:
          settings=uhh[str(ctx.guild.id)]
          if module.lower()=="caselogging":
            if state!=True:
             settings['caselogging']=False
             bb="Turned CaseLogging **OFF**"
            else:
              settings['caselogging']=True
              bb=" Turned CaseLogging **ON**"
          elif module.lower()=="caserecording":
            if state!=True:
              settings['caserecording']=False
              bb="<:notrecording:920715329984933909> Turned CaseRecording **OFF**"
            else:
              settings['caserecording']=True
              bb="<:recording:920713742604455967> Turned CaseRecording **ON**"
          elif module.lower()=="takeaction":
            if state!=True:
              settings['takeaction']=False
              bb="<:recording:920713742604455967> Turned TakeAction **OFF**"
            else:
              settings['takeaction']=True
              bb="<:takingaction:920719954968445057> Turned TakeAction **ON**"
          elif module.lower()=="privacymode":
            if state!=True:
               settings['privacymode']=False
               bb="<:notincognito:920605377840680960> Turned PrivacyMode **OFF**"
            else:
              settings['privacymode']=True
              bb="<:incognito:920605376997650433> Turned PrivacyMode **ON**"
          elif module.lower()=="errorlogging":
            if state!=True:
             settings['errorlogging']=False
             bb="Turned Error Logging **OFF**"
            else:
              settings['errorlogging']=True
              bb="Turned Error Logging **ON**"
          else:
            bb="<:notnicetho:920712378151231508> Sorry that's not a setting!\nYou may choose from the following options:\n> **CaseLogging**\n> **CaseRecording**\n> **TakeAction**\n> **Privacymode**\nRun `a!settings` to get detailed info about what each one of these actions do!"
          settingsh={}
          settingsh[str(ctx.guild.id)]=settings
          with open("serversettings.json","w")as f:
            json.dump(settingsh, f, indent=4)

        except KeyError:
          settings={}
          with open("serversettings.json","r") as f:
            settingsh=json.load(f)

          settings['caselogging']=True
          settings['caserecording']=True
          settings['takeaction']=False
          settings['privacymode']=False
          settings['errorlogging']=False
          if module.lower()=="caselogging":
            if state!=True:
             settings['caselogging']=False
             bb="Turned CaseLogging **OFF**"
            else:
              settings['caselogging']=True
              bb="Turned CaseLogging **ON**"
          elif module.lower()=="caserecording":
            if state!=True:
              settings['caserecording']=False
              bb="<:notrecording:920715329984933909> Turned CaseRecording **OFF**"
            else:
              settings['caserecording']=True
              bb="<:recording:920713742604455967> Turned CaseRecording **ON**"
          elif module.lower()=="takeaction":
            if state!=True:
              settings['takeaction']=False
              bb="<:nottakingaction:920719953781456898> Turned TakeAction **OFF**"
            else:
              settings['takeaction']=True
              bb="<:takingaction:920719954968445057> Turned TakeAction **ON**"
          elif module.lower()=="privacymode":
            if state!=True:
               settings['privacymode']=False
               bb="<:notincognito:920605377840680960> Turned PrivacyMode **OFF**"
            else:
              settings['privacymode']=True
              bb="<:incognito:920605376997650433> Turned PrivacyMode **ON**"
          elif module.lower()=="errorlogging":
            if state!=True:
             settings['errorlogging']=False
             bb="Turned Error Logging **OFF**"
            else:
              settings['errorlogging']=True
              bb="Turned Error Logging **ON**"
          else:
            bb="<:notnicetho:920712378151231508> Sorry that's not a setting!\nYou may choose from the following options:\n> **CaseLogging**\n> **CaseRecording**\n> **TakeAction**\n> **Privacymode**\n> **Error Logging**\nRun `a!settings` to get detailed info about what each one of these actions do!"
          settingsh[str(ctx.guild.id)]=settings
          with open("serversettings.json","w")as f:
            json.dump(settingsh, f, indent=4)
        await ctx.reply(bb)
    @commands.command(aliases=["uc"])
    @commands.has_permissions(administrator=True)
    async def unlinkchannel(self,ctx,channel:discord.TextChannel=None):
      """Unlink a logging channel or every logging channel from the bot"""
      index=channel
      with open('channel.json', 'r') as f:
            prefixes = json.load(f)
            #(prefixes) 
            #("heehoo")
      
      
      try:
          gg=prefixes[str(ctx.guild.id)]
          i=1
      except KeyError:
          ex=await ctx.reply("There is no linked channel in this server  ¯\_(ツ)_/¯")
          i=0
      
      if i==1and index==None :
        channel=self.bot.get_channel(gg[0])
        
        ex=await ctx.reply(f"This will unlink all the linked channels(in this server) from my database...\nTo Unlink a specific channel, mention it(For example say, `a!unlinkchannel` {channel.mention})\n Continue?")  
        await ex.add_reaction("❌")
        await ex.add_reaction("✔")
        check=lambda r, u: u == ctx.author and str(r.emoji) in "✔❌"
        reaction, user = await self.bot.wait_for("reaction_add", check=check)
        if str(reaction.emoji)=="✔":  
          await ex.edit(content=f"Removing channels ")
          prefixes.pop(str(ctx.guild.id))
          await ex.edit(content=f"Removed channels")
          with open('channel.json', 'w') as f:
            json.dump(prefixes, f, indent=4)  
          with open('channel backup.json', 'w') as f:
              json.dump(prefixes, f, indent=4)  
          await ex.edit(content=f"Database Successfully updated!")
        else:
          await ex.edit(content="Removal Aborted...")
        await ex.clear_reaction("✔")
        await ex.clear_reaction("❌")
        await asyncio.sleep(5)
        await ex.delete()
      elif i==1 and index!=None:
        if index.id in gg:  
          att=gg.index(index.id)
          gg.pop(att)
          channel=self.bot.get_channel(index.id)
          ex=await ctx.reply(f"This will unlink {channel.mention} from my   database...\n Continue?")  
          await ex.add_reaction("❌")
          await ex.add_reaction("✔")
          check=lambda r, u: u == ctx.author and str(r.emoji) in "✔❌"
          reaction, user = await self.bot.wait_for("reaction_add", check=check)
          if str(reaction.emoji)=="✔":  
            await ex.edit(content=f"Removing channel {channel.mention}")
            if len(gg)!=0:  
              prefixes[str(ctx.guild.id)]=gg
            else:
              prefixes.pop(str(ctx.guild.id))
            await ex.edit(content=f"Removed channel {channel.mention}")
            with open('channel.json', 'w') as f:
              json.dump(prefixes, f, indent=4)
            with open('channel backup.json', 'w') as f:
              json.dump(prefixes, f, indent=4)    
            await ex.edit(content=f"Database Successfully updated!")
          else:
            await ex.edit(content="Removal Aborted...")
          await ex.clear_reaction("✔")
          await ex.clear_reaction("❌")
          await asyncio.sleep(5)
          await ex.delete()
        else:
          ex=await ctx.reply("That channel isn't linked in this server  ¯\_(ツ)_/¯")
          await asyncio.sleep(5)
          await ex.delete()
      else:
        await asyncio.sleep(5)
        await ex.delete() 
def setup(bot):
    bot.add_cog(Customisation(bot))