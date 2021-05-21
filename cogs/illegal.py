import discord, json, requests, emoji, base64 ,hashlib ,string ,random ,io ,typing ,aiohttp
from cogs import aryi
from colorama import Fore
from discord.ext import commands
from datetime import datetime
from bot import getembed

config = json.loads(open("data/config.json","r").read())
token = config['token']

def logitem(text):
    	print(f"    {c.EC}-> {c.LR}{text}{c.EC}")





class Illegal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def earrape(self, ctx):
        await ctx.message.delete()
        works = True
        config = json.loads(open('data/config.json','r').read())
        args = ctx.message.content.split()
        inv = f"""
**Invalid Parse of Arguments**

{config['prefix']}earrape **VoiceCallID** **YoutubeURL**"""
        if len(args) == 1 or len(args) == 2:
            works = False
            embed = getembed(inv)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {inv}")
        elif len(args) == 3:
            if not args[1].isdigit():
                embed = getembed(inv)
                try:
                    return await ctx.send(embed=embed,delete_after=30)
                except:
                    return await ctx.send(f">>> {inv}")
            vc = self.bot.get_channel(int(args[1]))
            if vc == None:
                text = "The ID is invalid"
                embed = getembed(text)
                try:
                    await ctx.send(embed=embed,delete_after=30)
                except:
                    await ctx.send(f">>> {text}")
                works = False
            if works == True:
                vc = await vc.connect()
                try:
                    song = await aryi.YTDLSource.from_url(args[2], stream=True)
                    vc.play(song)
                    vc.source = discord.PCMVolumeTransformer(vc.source)
                    vc.source.volume = 10.0
                    text = "```I have connected to the Voice Call and I am playing the URL.```"
                except Exception as e:
                    text = f"```Error Occured: {e}```"
                    await vc.disconnect()
                embed = getembed(text)
                try:
                    await ctx.send(embed=embed,delete_after=30)
                except:
                    await ctx.send(f">>> {text}")

    @commands.command(aliases=["validate"])
    async def check(self, ctx):
        await ctx.message.delete()
        args = ctx.message.content.split()
        config = json.loads(open('data/config.json','r').read())
        if len(args) == 1:
            text = f"""
**Invalid Parse of Arguments**

{config['prefix']}check **token**"""
        else:
            headers = {'authorization' : args[1]}
            src = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers, timeout=10)
            if src.status_code == 403 or src.status_code == 401:
                text = f"Token **{args[1]}** was invalid."
            else:
                friends = requests.get("https://canary.discordapp.com/api/v6/users/@me/relationships", headers=headers, timeout=10).json()
                servers = requests.get('https://canary.discordapp.com/api/v6/users/@me/guilds', headers=headers, timeout=10).json()
                dm_channels = requests.get('https://canary.discordapp.com/api/v6/users/@me/channels', headers=headers, timeout=10).json()
                billing = requests.get('https://discord.com/api/v8/users/@me/billing/payment-sources',headers=headers).json()
                response = src.json()
                text=f"""```
`Token:` **{args[1]}**
`Name:` **{response['username']}#{response['discriminator']}**
`ID:` **{response['id']}**
`Email:` **{response['email']}**
`Phone:` **{response['phone']}**
`Language:` **{response['locale']}**
`Servers:` **{len(servers)}**
`Friends:` **{len(friends)}**
`DM Channels:` **{len(dm_channels)}**
--------------------Billing--------------------
{billing}
```"""
        try:
            await ctx.send(embed=getembed(text),delete_after=30)
        except:
            await ctx.send(f">>> {text}")

    @commands.command()
    async def disable(self, ctx):
        await ctx.message.delete()
        args = ctx.message.content.split()
        config = json.loads(open('data/config.json','r').read())
        if len(args) == 1:
            inv = f"""
**Invalid Parse of Arguments**

{config['prefix']}earrape **VoiceCallID** **YoutubeURL**"""
            embed = getembed(inv)
            try:
                await ctx.send(embed=embed)
            except:
                await ctx.send(f">>> {inv}")
        else:
            text = f"""
**Disabler**

I am currently disabling the token **{args[1]}**
            """
            try:
                await ctx.send(embed=getembed(text),delete_after=30)
            except:
                await ctx.send(f">>> {text}")
            while True:
                src = requests.get('https://canary.discordapp.com/api/v6/users/@me/guilds', headers={'authorization' : args[1]}, timeout=10)
                if src.status_code == 401 or src.status_code == 403:
                    text = "I have disabled/phonelocked the token"
                    try:
                        await ctx.send(embed=getembed(text),delete_after=30)
                    except:
                        await ctx.send(f">>> {text}")
                    break
                else:
                    pass
    
    @commands.command()
    async def socials(self, ctx): # b '\xfc'
        await ctx.message.delete()
        em = discord.Embed()
        if config['Socials']['name']:
            em.add_field(name="𝖓𝖆𝖒𝖊", value=f"`{config['Socials']['name']}`", inline=False)
        if config['Socials']['aliases']:
            em.add_field(name="𝖆𝖑𝖎𝖆𝖘𝖊𝖘", value=f"`{config['Socials']['aliases']}`", inline=False)
        if config['Socials']['age']:
            em.add_field(name="𝖆𝖌𝖊", value=f"`{config['Socials']['age']}`", inline=False)
        if config['Socials']['location']:
            em.add_field(name="𝖑𝖔𝖈𝖆𝖙𝖎𝖔𝖓", value=f"`{config['Socials']['location']}`", inline=False)
        if config['Socials']['discord']:
            em.add_field(name="𝖉𝖎𝖘𝖈𝖔𝖗𝖉", value=f"`{config['Socials']['discord']}`", inline=False)
        if config['Socials']['github']:
            em.add_field(name="𝖌𝖎𝖙𝖍𝖚𝖇", value=f"`{config['Socials']['github']}`", inline=False)
        if config['Socials']['telegram']:
            em.add_field(name="𝖙𝖊𝖑𝖊𝖌𝖗𝖆𝖒", value=f"`{config['Socials']['telegram']}`", inline=False)
        if config['Socials']['snapchat']:
            em.add_field(name="𝖘𝖓𝖆𝖕𝖈𝖍𝖆𝖙", value=f"`{config['Socials']['snapchat']}`", inline=False)
        if config['Socials']['soundcloud']:
            em.add_field(name="𝖘𝖔𝖚𝖓𝖉𝖈𝖑𝖔𝖚𝖉", value=f"`{config['Socials']['soundcloud']}`", inline=False)
        em.set_image(url=ctx.message.author.avatar_url)
        em.set_footer(text="⋆  mitsuki.tech  ⋆")
        em.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=em, delete_after=30)

    @commands.command()
    async def whois(self, ctx, *, user: discord.User = None): 
        await ctx.message.delete()
        if user is None:
            user = ctx.author      
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        return await ctx.send(embed=em, delete_after=30)
    
    @commands.command(aliases=['cn'])
    async def changenick(self, ctx, member: discord.Member, *, nick): 
        await ctx.message.delete()
        num = 0
        msg = await ctx.send(content=f"Changed their nickname {num} times.")
        while True:
            await member.edit(nick=nick)
            num +=1
            await msg.edit(content=f"Changed their nickname {num} times.")
            member.nick = nick

    @commands.command(name="serverinfo", description="Show information of the command server.", usage="")
    async def serverinfo(self, ctx):
        guild = ctx.message.guild
        try:
            embed = discord.Embed(title=f"‍ {guild.name}'s information")
            embed.add_field(name=" Server ID", value=f"```{guild.id}```", inline=True)
            embed.add_field(name=" Server Name", value=f"```{guild.name}```", inline=True)
            embed.add_field(name=" Server Owner", value=f"```{guild.owner}```", inline=True)
            embed.add_field(name=" Created At", value="```" + str(guild.created_at.strftime("%d %B, %Y")) + "```", inline=True)
            embed.set_thumbnail(url=guild.icon_url)
            embed.set_footer(text=f"{guild.name}")
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=30)
        except discord.HTTPException:
            createdAt = guild.created_at.strftime("%d %B, %Y")
            await ctx.send(f"** {user.name}'s information**\nID: {guild.id}\nName: {guild.name}\nOwner: {guild.owner}\nCreated At: {createdAt}")
    
    @commands.command()
    async def selfbotcheck(self, ctx):
        await ctx.message.delete()
        await ctx.send("🎉 **GIVEAWAY** 🎉")
 
    @commands.command(aliases=['search'])
    async def lookup(self, ctx):
        args = ctx.message.content.split()
        config = json.loads(open('data/config.json','r').read())
        ApiKey = config['leakcheck-key']
        await ctx.message.delete()
        if len(args) < 3:
            text = f"""
**Invalid Parse Of Arguments**

{config['prefix']}``search`` **[email/login] [term]**"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            container = discord.Embed(title="Database Lookup", color=0xffcece)
            container.set_footer(text="Made by connor")
            searchType = args[1]
            searchTerm = str(args[2])
            try:
                r = requests.post(f"https://leakcheck.net/api/?key={ApiKey}&check={searchTerm}&type={searchType}")
                searchRequest = r.json()
                if searchRequest['success'] == True:
                    if len(searchRequest['result']) > 2000:
                        container.add_field(name="Error:", value="Results too large for embed", inline=False)
                    else:
                        if searchRequest['success'] == True:
                            for i in range(int(searchRequest['found'])):
                                try:
                                    line =(str(searchRequest['result'][i]['line']))
                                    source = (str(searchRequest['result'][i]['sources']))
                                    last_breach = (str(searchRequest['result'][i]['last_breach']))
                                    if not last_breach == "":  
                                        container.add_field(name="⠀", value=f"Info: **{line}**\nSource: **{source}**\nLast Breach: **{last_breach}**", inline=False)
                                    if not source == "":  
                                        container.add_field(name="⠀", value=f"Info: **{line}**\n", inline=False)
                                    else: 
                                        container.add_field(name="⠀", value=f"Info: **{line}**\nSources: **{source}**", inline=False)
                                except:
                                    await ctx.send("Error")
                                i += 1
                elif searchRequest['success'] == False:
                    container.add_field(name="Term:", value=searchTerm, inline=False)
                    container.add_field(name="Success:", value=searchRequest['success'], inline=False)
                    container.add_field(name="Error", value=searchRequest['error'], inline=False)
                await ctx.send(embed=container, delete_after=30)
            except:
                pass

    @commands.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
    async def geoip(self, ctx, *, ipaddr: str = '1.3.3.7'): # b'\xfc'
        await ctx.message.delete()
        r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
        geo = r.json()
        em = discord.Embed()
        fields = [
            {'name': 'IP', 'value': geo['query']},
            {'name': 'ipType', 'value': geo['ipType']},
            {'name': 'Country', 'value': geo['country']},
            {'name': 'City', 'value': geo['city']},
            {'name': 'Continent', 'value': geo['continent']},
            {'name': 'Country', 'value': geo['country']},
            {'name': 'IPName', 'value': geo['ipName']},
            {'name': 'ISP', 'value': geo['isp']},
            {'name': 'Latitute', 'value': geo['lat']},
            {'name': 'Longitude', 'value': geo['lon']},
            {'name': 'Org', 'value': geo['org']},
            {'name': 'Region', 'value': geo['region']},
            {'name': 'Status', 'value': geo['status']},
        ]
        for field in fields:
            if field['value']:
                em.add_field(name=field['name'], value=field['value'], inline=True)
        return await ctx.send(embed=em, delete_after=30)

    @commands.command(aliases=['ping', 'webping'])
    async def pingweb(self, ctx, website = None): # b'\xfc'
        await ctx.message.delete()
        if website is None: 
            pass
        else:
            try:
                r = requests.get(website).status_code
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)
            if r == 404:
                await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=3)
            else:
                await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=3)       

    @commands.command()
    async def masschannels(self, ctx, name="mitsuki"):
        await ctx.message.delete()
        for _i in range (250):
            try:
                await ctx.guild.create_text_channel(name=name)
            except:
                return

    @commands.command()
    async def deletechannels(self, ctx):
        await ctx.message.delete()
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
            except:
                return  

def setup(bot):
    bot.add_cog(Illegal(bot))