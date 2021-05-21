#!/usr/bin/env python
# -*- coding: utf-8 -*-
import discord, pyfiglet, requests, json
from discord.ext import commands as commands 
from bot import getembed

class crypto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def crypto(self, ctx):
        args = ctx.message.content.split()
        config = json.loads(open("data/config.json","r").read())
        await ctx.message.delete()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

``{config['prefix']}crypto`` **[type]**

To view a list of types, use ``{config['prefix']}listcrypto``"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            cryptoType = str(args[1])
            if cryptoType == "BTC" or "ETH" or "XMR" or "XRP" or "DOGE" or "LINK" or "ATOM" or "COMP" or "LTC" or "BCH" or "DOT":
                r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+cryptoType+"&tsyms=USD,EUR,GBP")
                kekistan = r.json()
                gbp = kekistan['GBP']
                eur = kekistan['EUR']
                usd = kekistan['USD']
                embedic = discord.Embed(description=f'GBP: `£{str(gbp)}`\nEUR: `€{str(eur)}`\nUSD: `${str(usd)}`')
                if cryptoType == "BTC":
                    iconURL = "https://cdn.discordapp.com/attachments/813459313153671178/820118046073028638/bitcoin-225079_960_720.png"
                elif cryptoType == "ETH":
                    iconURL = "https://cdn.freebiesupply.com/logos/large/2x/ethereum-1-logo-png-transparent.png"
                elif cryptoType == "XMR":
                    iconURL = "https://cdn.freebiesupply.com/logos/large/2x/monero-logo-png-transparent.png"
                elif cryptoType == "XRP":
                    iconURL = "https://cdn.freebiesupply.com/logos/large/2x/ripple-2-logo-png-transparent.png"
                elif cryptoType == "DOGE":
                    iconURL = "https://cdn.coindoo.com/2019/10/dogecoin-logo.png"
                elif cryptoType == "LINK":
                    iconURL = "https://s2.coinmarketcap.com/static/img/coins/64x64/1975.png"
                elif cryptoType == "ATOM":
                    iconURL = "https://s2.coinmarketcap.com/static/img/coins/64x64/3794.png"
                elif cryptoType == "COMP":
                    iconURL = "https://s2.coinmarketcap.com/static/img/coins/64x64/5692.png"
                elif cryptoType == "LTC":
                    iconURL ="https://s2.coinmarketcap.com/static/img/coins/64x64/2.png"
                elif cryptoType == "BCH":
                    iconURL = "https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png"
                elif cryptoType == "DOT":
                    iconURL = "https://s2.coinmarketcap.com/static/img/coins/64x64/6636.png"
                embedic.set_author(name=cryptoType, icon_url=iconURL)
                await ctx.send(embed=embedic)
            else:
                await ctx.send("Incorrect crypto entered. Use listcrypto for a list of cryptocurrencies you can check")

    @commands.command()
    async def listcrypto(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(description="The cryptocurrencies that you are able to check are `BTC`, `ETH`, `XMR`, `XRP`, `DOGE`, `LINK`, `ATOM`, `COMP`, `LTC`, `BCH`, `DOT`")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(crypto(bot))