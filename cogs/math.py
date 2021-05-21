import discord, json, requests, emoji, urllib
from cogs import aryi
from discord.ext import commands
from bot import getembed

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

`{args[0]}` **[num1]** **[num2]**
            """
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            result = str(int(args[1])+int(args[2]))
            embed = discord.Embed(description="The sum of "+args[1]+" and "+args[2]+" is "+result)
            await ctx.send(embed=embed)

    @commands.command()
    async def subtract(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

`{args[0]}` **[num1]** **[num2]**
            """
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            result = str(int(args[1])-int(args[2]))
            embed = discord.Embed(description="The subtraction of "+args[2]+" from "+args[1]+" is "+result)
            await ctx.send(embed=embed)

    @commands.command()
    async def divide(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

`{args[0]}` **[num1]** **[num2]**
            """
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            result = str(int(args[1])/int(args[2]))
            embed = discord.Embed(description="The division of "+args[1]+" by "+args[2]+" is "+result)
            await ctx.send(embed=embed)

    @commands.command()
    async def multiply(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

`{args[0]}` **[num1]** **[num2]**
            """
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            result = str(int(args[1])*int(args[2]))
            embed = discord.Embed(description="The multiplication of "+args[1]+" * "+args[2]+" is "+result)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Math(bot))