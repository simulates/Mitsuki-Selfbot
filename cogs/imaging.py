import discord, json, requests
from discord.ext import commands
from requests.api import request
from bot import getembed 

def action_embed(url):
    em = discord.Embed(color=0x2f3136)   
    em.set_image(url=url)
    return em

def getimageembed(url):
    return discord.Embed(color=0x2f3136).set_image(url=url)

class Imaging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api = "http://192.99.253.209:8000/api/"

    @commands.command()
    async def abort(self, ctx):
        await ctx.message.delete()
        user = self.bot.user.avatar_url
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0].avatar_url
        link = self.api + "aborted?avatar1=" + str(user)
        try:
            await ctx.send(embed=getimageembed(link),delete_after=30)
        except:
            await ctx.send(link)
            
    @commands.command()
    async def magik(self, ctx):
        await ctx.message.delete()
        user = self.bot.user.avatar_url
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0].avatar_url
        link = self.api + "magik?avatar1=" + str(user)
        try:
            await ctx.send(embed=getimageembed(link),delete_after=30)
        except:
            await ctx.send(link)

    @commands.command()
    async def trigger(self, ctx):
        await ctx.message.delete()
        user = self.bot.user.avatar_url
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0].avatar_url
        link = self.api + "trigger?avatar1=" + str(user)
        try:
            await ctx.send(embed=getimageembed(link),delete_after=30)
        except:
            await ctx.send(link)

    @commands.command()
    async def salty(self, ctx):
        await ctx.message.delete()
        user = self.bot.user.avatar_url
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0].avatar_url
        link = self.api + "salty?avatar1=" + str(user)
        try:
            await ctx.send(embed=getimageembed(link),delete_after=30)
        except:
            await ctx.send(link)

    @commands.command()
    async def roblox(self, ctx):
        await ctx.message.delete()
        user = self.bot.user.avatar_url
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0].avatar_url
        link = self.api + "roblox?avatar1=" + str(user)
        try:
            await ctx.send(embed=getimageembed(link),delete_after=30)
        except:
            await ctx.send(link)

    @commands.command()
    async def rip(self, ctx):
        await ctx.message.delete()
        user = self.bot.user.avatar_url
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0].avatar_url
        link = self.api + "rip?avatar1=" + str(user)
        try:
            await ctx.send(embed=getimageembed(link),delete_after=30)
        except:
            await ctx.send(link)

    @commands.command()
    async def satan(self, ctx):
        await ctx.message.delete()
        user = self.bot.user.avatar_url
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0].avatar_url
        link = self.api + "satan?avatar1=" + str(user)
        try:
            await ctx.send(embed=getimageembed(link),delete_after=30)
        except:
            await ctx.send(link)

    @commands.command()
    async def sickban(self, ctx):
        await ctx.message.delete()
        user = self.bot.user.avatar_url
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0].avatar_url
        link = self.api + "sickban?avatar1=" + str(user)
        try:
            await ctx.send(embed=getimageembed(link),delete_after=30)
        except:
            await ctx.send(link)

    @commands.command()
    async def trash(self, ctx):
        await ctx.message.delete()
        user = self.bot.user.avatar_url
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0].avatar_url
        link = self.api + "trash?avatar1=" + str(user)
        try:
            await ctx.send(embed=getimageembed(link),delete_after=30)
        except:
            await ctx.send(link)

    @commands.command()
    async def ugly(self, ctx):
        await ctx.message.delete()
        user = self.bot.user.avatar_url
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0].avatar_url
        link = self.api + "ugly?avatar1=" + str(user)
        try:
            await ctx.send(embed=getimageembed(link),delete_after=30)
        except:
            await ctx.send(link)

    @commands.command()
    async def warp(self, ctx):
        await ctx.message.delete()
        user = self.bot.user.avatar_url
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0].avatar_url
        link = self.api + "warp?avatar1=" + str(user)
        try:
            await ctx.send(embed=getimageembed(link),delete_after=30)
        except:
            await ctx.send(link)   

    @commands.command()
    async def deepfry(self, ctx):
        await ctx.message.delete()
        user = self.bot.user.avatar_url
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0].avatar_url
        link = self.api + "deepfry?avatar1=" + str(user)
        try:
            await ctx.send(embed=getimageembed(link),delete_after=30)
        except:
            await ctx.send(link)

    @commands.command()
    async def bed(self, ctx):
        await ctx.message.delete()
        user = self.bot.user.avatar_url
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0].avatar_url
        link = self.api + "bed?avatar1=" + str(user)
        try:
            await ctx.send(embed=getimageembed(link),delete_after=30)
        except:
            await ctx.send(link)

    @commands.command()
    async def dog(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/img/dog").json()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name="Random Dog." , icon_url="https://www.centralnewyorkinjurylawyer.com/files/2015/06/dog.jpg") 
        embed.set_image(url=str(r["link"]))
        await ctx.send(embed=embed)    

def setup(bot):
    bot.add_cog(Imaging(bot))
