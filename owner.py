from discord.ext import commands
import discord
import json
import random
import os
import asyncio
class OwnerOnly(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=["gd"])
    @commands.is_owner() 
    async def get_data(self,ctx,doc_name:str,doc_type:str):
      if doc_type=="json":
        with open(f"{doc_name}.json","r")as f:
          pp=json.load(f)
      else:
        with open(f"{doc_name}.{doc_type}","r")as f:
          pp=f.read()
      await ctx.send(f"```{doc_type}\n{pp}\n```")
    @commands.command()
    @commands.is_owner() 
    async def getbugdata(self,ctx,bug_id:int):
      rndclr=random.choice([discord.Colour.red().value,discord.Colour.dark_grey().value])
      with open("bugreports.json","r") as f:
        idk=json.load(f)
    
     
      if str(bug_id) in idk.keys() :
        embed= discord.Embed(color=rndclr)

        embed.add_field(name="Bug ID", value=bug_id,inline=False)
        embed.add_field(name="Bug", value=idk[str(bug_id)]['bug'],inline=False)
        id=idk[str(bug_id)]['reporter']
        user = self.bot.get_user(id)
    
        if user is None:  # Maybe the user isn't cached?
                   user = await self.bot.fetch_user(id)
        
        embed.add_field(name="Bug Reporter", value=user.mention,inline=False)
        if idk[str(bug_id)]['status']=="\🙈 Unseen":   
          idk[str(bug_id)]['status']="\🐵 Seen, In Progress"

          with open("bugreports.json","w")as f:
            json.dump(idk,f,indent=4)
        embed.add_field(name="Status", value=idk[str(bug_id)]['status'],inline=False)
        await ctx.reply(embed=embed,mention_author=False)
      else:
        embed= discord.Embed(description="No case with that ID found!",color=rndclr)
        await ctx.reply(embed=embed,mention_author=False)
    
    @commands.command()
    @commands.is_owner()
    async def setstatus(self,ctx,bug_id:int):
      rndclr=random.choice([discord.Colour.red().value,discord.Colour.dark_grey().value])
      with open("bugreports.json","r") as f:
        idk=json.load(f)
    
     
      if str(bug_id) in idk.keys() :
        msg=await ctx.reply("Available statuses:\n🟢-> Accepted\n🔴->Declined\n🔧->Fixed\n🟡->Testing")
        await msg.add_reaction("🟢") 
        await msg.add_reaction("🟡") 
        await msg.add_reaction("🔴") 
        await msg.add_reaction("🔧")
        
        check=lambda r,  u: u == ctx.author and msg and str(r.emoji) in "🟢🟡🔴🔧"

        reaction, user = await self.bot.wait_for("reaction_add", check=check) 
        print("phase1 done")
        await msg.clear_reaction(emoji="🟢") 
        await msg.clear_reaction(emoji="🟡") 
        await msg.clear_reaction(emoji="🔴") 
        await msg.clear_reaction(emoji="🔧")
        if str(reaction.emoji)=="🟢":
          status="Accepted"
          await msg.edit(content=f"Do you want to set this bug as {status}?\nBug: **{idk[str(bug_id)]['bug']}**\nBug Id: {bug_id}")
          await msg.add_reaction("✅")  
          await msg.add_reaction("❎")
          check=lambda r,  u: u == ctx.author and msg and str(r.emoji) in "✅❎"
          reaction, user = await self.bot.wait_for("reaction_add", check=check)
          if str(reaction.emoji)=="✅":
            idk[str(bug_id)]['status']="\🟢 Accepted!"
            with open("bugreports.json","w") as f:
                json.dump(idk,f,indent=4)
            await msg.edit(content="Successful!!")
            id=idk[str(bug_id)]['reporter']
            user = self.bot.get_user(id)
    
            if user is None:  # Maybe the user isn't cached?
                   user = await self.bot.fetch_user(id)
            await user.send(f"A bug subitted by you({idk[str(bug_id)]['bug']}) has just been accepted by the developer!\nWe thank you for your cooperation and for lending your interest in this project!")
        elif  str(reaction.emoji)=="🟡":
            status="Testing"
            await msg.edit(content=f"Do you want to set this bug as {status}?\nBug: **{idk[str(bug_id)]['bug']} **\nBug Id: {bug_id}")
            await msg.add_reaction("✅")  
            await msg.add_reaction("❎")
            check=lambda r,  u: u == ctx.author and msg and str (r.emoji) in "✅❎"
            reaction, user = await self.bot.wait_for("reaction_add",   check=check)
            if str(reaction.emoji)=="✅":
              idk[str(bug_id)]['status']="\🟡 Testing!"
              with open("bugreports.json","w") as f:
                  json.dump(idk,f,indent=4)
              await msg.edit(content="Successful!!")
              id=idk[str(bug_id)]['reporter']
              user = self.bot.get_user(id)

              if user is None:  # Maybe the user isn't cached?
                     user = await self.bot.fetch_user(id)
              await user.send(f"A bug subitted by you({idk[str  (bug_id)]['bug']}) is being tested by the developer!\nWe thank you for your cooperation and for lending your interest in this project!")
        elif  str(reaction.emoji)=="🔴":
            status="Declined"
            await msg.edit(content=f"Do you want to set this bug as {status}?\nBug: **{idk[str(bug_id)]['bug']}**\nBug Id: {bug_id}")
            await msg.add_reaction("✅")  
            await msg.add_reaction("❎")
            check=lambda r,  u: u == ctx.author and msg and str (r.emoji) in "✅❎"
            reaction, user = await self.bot.wait_for("reaction_add",   check=check)
            if str(reaction.emoji)=="✅":
              idk[str(bug_id)]['status']="\🔴 Declined!"
              with open("bugreports.json","w") as f:
                  json.dump(idk,f,indent=4)
              await msg.edit(content="Successful!!")
              id=idk[str(bug_id)]['reporter']
              user = self.bot.get_user(id)

              if user is None:  # Maybe the user isn't cached?
                     user = await self.bot.fetch_user(id)
              await user.send(f"A bug subitted by you({idk[str(bug_id)]['bug']}) has been declined by the developer! This could be caused if you sent a joke report, or, if the bug has already been patched!\nWe thank you for your cooperation and for lending your interest in this project!")
        elif  str(reaction.emoji)=="🔧":
            status="Fixed"
            print("Phase 2")
            await msg.edit(content=f"Do you want to set this bug as {status}?\nBug: **{idk[str(bug_id)]['bug']}**\nBug Id: {bug_id}")
            await msg.add_reaction("✅")  
            await msg.add_reaction("❎")
            check=lambda r,  u: u == ctx.author and msg and str (r.emoji) in "✅❎"
            reaction, user = await self.bot.wait_for("reaction_add",   check=check)
            if str(reaction.emoji)=="✅":
              print("Phase 3")
              idk[str(bug_id)]['status']="\🔧 Fixed!"
              with open("bugreports.json","w") as f:
                  json.dump(idk,f,indent=4)
              await msg.edit(content="Successful!!")
              id=idk[str(bug_id)]['reporter']
              user = self.bot.get_user(id)

              if user is None:  # Maybe the user isn't cached?
                     user = await self.bot.fetch_user(id)
              await user.send(f"A bug subitted by you({idk[str(bug_id)]['bug']}) has been fixed the developer!\nWe thank you for your cooperation and for lending your interest in this project!")
        else:
            await msg.edit(content="Aborted!")
        await msg.delete()
        await ctx.message.delete()
    @commands.command()
    @commands.is_owner() 
    async def msg (self,ctx,*, msg:str):
      #await bot.owner.send("starting...")
      print("kjbevkbvj")
      with open("ann_chan.json","r")as f:
        pre=json.load(f)
      for guild in self.bot.guilds:
          
          try:
            for i in pre[str(guild.id)]:  
              id=i
              channel=self.bot.get_channel(id)
              await channel.send(f"> {msg}\nThanking you,\nThe AntiScam team\n*PS: To get back to the developer, please send a friend request to `Iced Dev#7379`*")
          except discord.Forbidden:
            print("no lol")
          except KeyError:
            try:
              await guild.owner.send(f"Hi {guild.owner.name}! Hope you are well in these trying times... The developer has left a message for you, here it is:\n> {msg}\nThanking you,\nThe AntiScam team\n*PS: To get back to the developer, please send a friend request to `Iced Dev#7379`*\nAlso, please use `a!linkannouncementchannel` to link a channel where I can post these updates! ")
            except discord.Forbidden:
              print("lol no")
          await asyncio.sleep(2)
    @commands.command()
    @commands.is_owner() 
    async def wipe (self,ctx,reason:str):
      wipe={}
      with open ("channel backup.json","r") as f:
        backup=json.load(f)
      with open('channel.json', 'w') as f:
              json.dump(wipe, f, indent=4)
    
      await asyncio.sleep(20)
      with open('channel.json', 'w') as f:
              json.dump(backup, f, indent=4)
    @commands.command()
    @commands.is_owner()
    async def ggl(self,ctx):
     for gg in self.bot.guilds:
     
       await ctx.author.send(f"{gg} {gg.owner}")
def setup(bot):
    bot.add_cog(OwnerOnly(bot))