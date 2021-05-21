import discord, json, datetime, asyncio
from discord.ext import commands
from bot import getembed, status_cycle


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["play"])
    async def playing(self, ctx):
        await ctx.message.delete()
        args = ctx.message.content.split()
        config = json.loads(open('data/config.json','r').read())
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

{config['prefix']}playing ``[STATUS]``"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name=" ".join(args[1:]), details=" ".join(args[1:])))
            
    @commands.command(aliases=['listen'])
    async def listening(self, ctx):
        await ctx.message.delete()
        config = json.loads(open('data/config.json','r').read())
        args = ctx.message.content.split()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

{config['prefix']}listening ``[STATUS]``"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=" ".join(args[1:]),details=" ".join(args[1:])))

    @commands.command(aliases=['watch'])
    async def watching(self, ctx):
        await ctx.message.delete()
        config = json.loads(open('data/config.json','r').read())
        args = ctx.message.content.split()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

{config['prefix']}watching ``[STATUS]``"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=" ".join(args[1:]),details=" ".join(args[1:])))

    @commands.command(aliases=['compete'])
    async def competing(self, ctx):
        await ctx.message.delete()
        config = json.loads(open('data/config.json','r').read())
        args = ctx.message.content.split()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

{config['prefix']}competing ``[STATUS]``"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            await self.bot.change_presence(activity=discord.Activity(type=5,name=" ".join(args[1:]),details=" ".join(args[1:])))

    @commands.command(aliases=['stream'])
    async def streaming(self, ctx):
        await ctx.message.delete()
        args = ctx.message.content.split()
        config = json.loads(open('data/config.json','r').read())
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

{config['prefix']}streaming ``[STATUS]``"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            await self.bot.change_presence(activity=discord.Streaming(name=" ".join(args[1:]),url=config['twitchURL']))

    @commands.command(aliases=['cycle'])
    async def cyclestatus(self, ctx):
        await ctx.message.delete()
        config = json.loads(open('data/config.json','r').read())
        streamCycle = config['stream-cycle']
        if streamCycle == True:
            config['stream-cycle'] = False
        elif streamCycle == False:
            config['stream-cycle'] = True
        await ctx.send(embed=getembed("Stream cycle is now: **"+str(config['stream-cycle'])+"**"), delete_after=30)
        open('data/config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))

    @commands.command()
    async def addstatus(self, ctx):
        await ctx.message.delete()
        args = ctx.message.content.split()
        config = json.loads(open('data/config.json','r').read())
        if len(args) < 3 or not args[1].isdigit():
            text = f"""
**Invalid Parse Of Arguments**

{config['prefix']}addstatus **[DELAY]** **[status]**"""
        else:
            config['statuses'].append({
                "delay" : int(args[1]),
                "state" : " ".join(args[2:])
            })
            text = f"I have added your `custom status` as **{' '.join(args[2:])}** with `delay` **{args[1]}** seconds"
            open('data/config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))
        try:
            await ctx.send(embed=getembed(text),delete_after=30)
        except:
            await ctx.send(f">>> {text}")
def setup(bot):
    bot.add_cog(Status(bot))