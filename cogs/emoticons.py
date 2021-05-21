import discord, requests, pyfiglet
from discord.ext import commands 

class emoticons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["emojis", "listemojis", "listemotes", "emotes"])
    async def listemoticons(self, ctx):
        await ctx.message.delete()
        text = "fuckyou, lenny, what, bear, worried, ak47, awp, lmg, sword, love, goodnight, smile"
        await ctx.send(text)

    @commands.command()
    async def fuckyou(self, ctx):
        await ctx.message.delete()
        middle = '╭∩╮(･◡･)╭∩╮'
        await ctx.send(middle)

    @commands.command()
    async def lenny(self, ctx):
        await ctx.message.delete()
        lenny = '( ͡° ͜ʖ ͡°)'
        await ctx.send(lenny)

    @commands.command()
    async def what(self, ctx):
        await ctx.message.delete()
        what = '( ʘ̆ ╭͜ʖ╮ ʘ̆ )'
        await ctx.send(what)

    @commands.command()
    async def bear(self, ctx):
        await ctx.message.delete()
        bear = 'ʕ •ᴥ•ʔ'
        await ctx.send(bear)

    @commands.command()
    async def worried(self, ctx):
        await ctx.message.delete()
        worried = '(´･ _･｀)'
        await ctx.send(worried)

    @commands.command()
    async def ak47(self, ctx):
        await ctx.message.delete()
        ak = '︻╦╤─'
        await ctx.send(ak)

    @commands.command()
    async def awp(self, ctx):
        await ctx.message.delete()
        awp = '︻デ═一'
        await ctx.send(awp)

    @commands.command()
    async def lmg(self, ctx):
        await ctx.message.delete()
        lmg = '︻╦̵̵͇̿̿̿̿╤──'
        await ctx.send(lmg)

    @commands.command()
    async def sword(self, ctx):
        await ctx.message.delete()
        sword = 'ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>'
        await ctx.send(sword)

    @commands.command()
    async def love(self, ctx):
        await ctx.message.delete()
        love = '(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥'
        await ctx.send(love)

    @commands.command(aliases=["gn"])
    async def goodnight(self, ctx):
        await ctx.message.delete()
        night = '✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩'
        await ctx.send(night)

    @commands.command()
    async def smile(self, ctx):
        await ctx.message.delete()
        smile = '˙ ͜ʟ˙'
        await ctx.send(smile)



def setup(bot):
    bot.add_cog(emoticons(bot))