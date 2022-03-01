from tkinter import Misc
from discord.ext import commands
import discord
import json
import random
import asyncio
class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def faq(self,ctx):
      """Get FAQ for the bot ig?"""
      rndclr=random.choice([discord.Colour.red().value,discord.Colour.dark_grey().value])
      """FAQ for the bot"""
      e=discord.Embed(title="Frequently Asked Questions",colour=rndclr)
      e.add_field(name="Is AntiScam a paid service?",value="No. AntiScam is not and never wil be, a paid service.",inline=False)
      e.add_field(name="How does AntiScam work?",value='AntiScam generates a counter and increments it based on how much it "gets scared". ',inline=False)

      e.add_field(name="Will AntiScam randomly delete my messages?",value="Chances are next to none! The algorithm has been tested uncountable number of times and perfected upon, so a false positive is an extremely rare scenario. Nonetheless, if anything of the sort occurs, you will recieve a preview of your message for 10 seconds to review the message for potenitally harmful links that may have set off the trigger.",inline=False)
      e.set_footer(text="For more info, use a!botinfo")
      ed=await ctx.reply(embed=e,mention_author=False)
      await asyncio.sleep(10)
      e.set_footer(text="The questions were asked by no one, mind you")
      await ed.edit(embed=e)
    @commands.command()
    async def vote(self,ctx):  
      """Vote the bot on Top.gg!"""
      e=discord.Embed()
      e.add_field(name="Vote for me!",value="Click [**Here**](https://top.gg/bot/886309422526259231/vote)!!")
      await ctx.reply(embed=e)
def setup(bot):
    bot.add_cog(Miscellaneous(bot))