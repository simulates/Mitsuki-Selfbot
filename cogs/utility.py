from aiohttp import client
import discord, json, requests, emoji, urllib, asyncio, aiohttp, base64, codecs, random, sys, colorama, re
from discord import user
from cogs import aryi
from discord.ext import commands
from aiohttp import ClientSession
from bot import getembed
from PIL import Image
from colorama import Fore

def getav(url, user):
    return discord.Embed(title='Avatar', color=0x2f3136).set_image(url=url).set_footer(text=user)    
config = json.loads(open('data/config.json','r').read())

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['fm','firstmsg'])
    async def firstmessage(self, ctx):
        await ctx.message.delete()
        msg = None
        async for message in ctx.message.channel.history(limit=1,oldest_first=True):
            msg = message
        text = f"https://discord.com/channels/@me/{msg.channel.id}/{msg.id}"
        try:
            await ctx.send(embed=getembed(f"[Click here]({text})"),delete_after=30)
        except:
            await ctx.send(text)

    @commands.command(aliases=['p','purge'])
    async def d(self,ctx):
        args = ctx.message.content.split()
        if len(args) == 1:
            async for message in ctx.channel.history(limit=9999999999999999999999).filter(lambda m: m.author == ctx.message.author):
                try:
                    await message.delete()
                except:
                    continue
        else:
            if not args[1].isdigit():
                await ctx.message.delete()
                if args[1] == "images":
                    async for message in ctx.channel.history(limit=9999999999999999999999).filter(lambda m: len(m.attachments) > 0):
                        try:
                            await message.delete()
                        except:
                            continue
                elif args[1] == "embeds":
                    async for message in ctx.channel.history(limit=9999999999999999999999).filter(lambda m: len(m.embeds) > 0):
                        try:
                            await message.delete()
                        except:
                            continue
                elif args[1] == "help":
                    text = f"""
**Invalid Parse Of Arguments**
`{args[0]}` 
`{args[0]}` **[number]**
`{args[0]}` **images**
`{args[0]}` **embeds**
`{args[0]}` **help**
"""
                    try:
                        await ctx.send(embed=getembed(text),delete_after=30)
                    except:
                        await ctx.send(f">>> {text}")
                else:
                    text = "{} is not a valid number.".format(args[1])
                    try:
                        await ctx.send(embed=getembed(text),delete_after=30)
                    except:
                        await ctx.send(text)
            else:
                counter=0
                async for message in ctx.channel.history(limit=9999999999999999999999).filter(lambda m: m.author == ctx.message.author):
                    try:
                        await message.delete()
                    except:
                        continue
                    counter+=1
                    if counter == int(args[1])+1:
                        break

    @commands.command(aliases=['asciispam'])
    async def spamascii(self, ctx):
        await ctx.message.delete()
        times = ctx.message.content.split()
        if len(times) == 1:
            text = f"""
**Invalid Parse Of Arguments**

`{times[0]}` **[number]**
"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            if not times[1].isdigit():
                embed = getembed(f"**{times[1]}** is not a valid number lol")
                return await ctx.send(embed=embed)
            times = int(times[1])
            for x in range(times):
                await ctx.send(aryi.asciigen(1999),delete_after=10)

    @commands.command(aliases=['sendascii'])
    async def ascii(self, ctx, *, text):
        await ctx.message.delete()
        r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
        if len('```'+r+'```') > 2000:
            return
        await ctx.send(f"```{r}```")

    @commands.command(aliases=['del'])
    async def delete(self, ctx):
        await ctx.message.delete()
        args = ctx.message.content.split()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

`{args[0]}` **[userID]**
"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            if not args[1].isdigit():
                embed = getembed(f"**{args[1]}** is not a valid number lol")
                return await ctx.send(embed=embed)
            user = await self.bot.fetch_user(int(args[1]))
            if user == None:
                return await ctx.send(embed=getembed(f"User ID **{args[1]}** is invalid."))
            async for message in user.history(limit=999999999999999999999999999999999999999999).filter(lambda m: m.author == ctx.message.author):
                try:
                    await message.delete()
                except:
                    continue

    @commands.command()
    async def spam(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        if len(args) == 1 or len(args) == 2:
            text = f"""
**Invalid Parse Of Arguments**

`{args[0]}` **[number]** **[message]**
            """
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            if not args[1].isdigit():
                embed = getembed(f"**{args[1]}** is not a valid number lol")
                return await ctx.send(embed=embed,delete_after=30)
            for x in range(int(args[1])):
                await ctx.send(" ".join(args[2:]))

    @commands.command(aliases=['hide'])
    async def encrypt(self, ctx):
        await ctx.message.delete()
        args = ctx.message.content.split()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

`{args[0]}` **[number]**
            """
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            counter = 0
            async for message in ctx.channel.history(limit=999999999999999).filter(lambda m: m.author == ctx.message.author):
                text=''
                await message.edit(content=aryi.encrypt(message,text))
                counter += 1
                if counter == int(args[1]):
                    break
                    
    @commands.command(aliases=['avatar', 'pfp'])
    async def av(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        embed = None
        if len(ctx.message.mentions) == 0:
            if len(args) == 1:
                embed = getav(ctx.message.author.avatar_url, ctx.author)
            else:
                if not args[1].isdigit():
                    embed = getembed(f"**{args[1]}** is not a valid number lol")
                    return await ctx.send(embed=embed,delete_after=30)
                user = self.bot.get_user(int(args[1]))
                if user == None:
                    return await ctx.send(embed=getembed(f"User ID **{args[1]}** is invalid."))
                embed = getav(user.avatar_url, user)
        else:
            embed = getav(ctx.message.mentions[0].avatar_url, ctx.message.mentions[0])
        await ctx.send(embed=embed,delete_after=30)

    @commands.command(aliases=['b64'])
    async def base64(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

`{args[0]}` **[encode/decode]** **[message]**
            """
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        string = " ".join(args[2:])
        if args[1] == "encode":
            decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
            encoded_stuff = str(decoded_stuff)
            encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
            await ctx.send(encoded_stuff) 
        elif args[1] == "decode":
            decoded_stuff = base64.b64decode(string)
            decoded_stuff = str(decoded_stuff, 'utf-8')
            await ctx.send(decoded_stuff)
        else:
            await ctx.send("Error")

    @commands.command(aliases=['gping'])
    async def ghostping(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

{config['prefix']}ghostping @``[user]``"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")

    @commands.command(aliases=['randomss'])
    async def randomscreenshot(self, ctx): # b'\xfc'
        await ctx.message.delete()
        string = "https://prnt.sc/"
        dicts = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range (6):
            add = random.choice(dicts)
            string +=add
        await ctx.send(string)


    @commands.command(aliases=['capetester'])
    async def capetest(self, ctx): # b'\xfc'
        args = ctx.message.content.split()
        await ctx.message.delete()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

`{args[0]}` **[slim/classic]** **[username]** **[cape]**
            """
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else: 
            modelType = str(args[1])
            username = str(args[2])
            cape = str(args[3])
            getSkinHash = requests.post(f"https://www.faav.tk/v1/namemc/skinhash?username={username}")
            skinhash = getSkinHash.json()
            skinhash = skinhash['skinhash']
            if cape == '2011':
                capeHash = '9349fa25c64ae935'
            elif cape == '2016':
                capeHash = '1981aad373fa9754'
            capeTestURL = f"https://www.faav.tk/minecraft-cape-tester/cape-test/?model={modelType}&skinhash={skinhash}&capehash={capeHash}"
            em = discord.Embed(title='Cape Test')
            em.set_image(url=capeTestURL)
            print(capeTestURL)
            await ctx.send(capeTestURL)
            await ctx.send(embed=em, delete_after=30)
            



    @commands.command(aliases=['mcl', 'mc-lookup', 'mc'])
    async def mclookup(self, ctx): # b'\xfc'
        args = ctx.message.content.split()
        await ctx.message.delete()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

`{args[0]}` **[username]**
            """
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else: 
            username = str(args[1])
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://api.ashcon.app/mojang/v2/user/"+username) as r:
                    res = await r.json()
                    try:
                        uuid = res['uuid'] # getuuid
                        try:
                            capeInfo = res['textures']['cape']['url'] #get cape
                        except KeyError:
                            capeInfo = "User has no cape" #no cape
                        async with aiohttp.ClientSession() as css:
                            async with css.get(f"https://api.namemc.com/profile/{uuid}/friends") as ra:
                                result = await ra.json()
                                friends = 0
                                for friend in result:
                                    friends+=1
                        usernames = ""
                        history = ""
                        date_changed = ""
                        i=0
                        skin_url = res['textures']['skin']['url'] #get skin
                        for each in res['username_history']:
                            i=i+1
                            if i>1:
                                history = f"[{str(i)}] **{(each['username'])} ** - {(each['changed_at'][0:4])}/{(each['changed_at'][5:7])}/{(each['changed_at'][8:10])} at {(each['changed_at'][11:19])}\n{history}" # date formatting
                        history = f"{history}[1] **{str(res['username_history'][0]['username'])}**\n`Total name changes:` **{str(i-1)}**\n`NameMC Friends:` **{friends}**\n" # compile history
                        em = discord.Embed(title=username, url=f"https://namemc.com/{username}")
                        em.add_field(name="`UUID:`", value=f"*{uuid}*", inline=False)
                        em.add_field(name="`Name History:`", value=history, inline=False)
                        '''socialsRequest = requests.get(f"https://api.snaz.in/v2/namemc/profile/{uuid}")
                        socialsResult = socialsRequest.json()
                        print(socialsRequest.json)
                        for each in socialsResult:
                            if each['claimed']:
                                em.add_field(name="`Claimed:`", value=f"*{each['claimed']}*", inline=False)
                                em.add_field(name="`Location:`", value=f"*{each['location']['name']}*", inline=False)
                                if not each['accounts']['title'] == 'Discord':
                                    em.add_field(name=f"`{each['accounts']}:`", value=f"{each['accounts']['url']}", inline=False)
                                else:
                                    em.add_field(name=f"`{each['accounts']}:`", value=f"**{each['accounts']['content']}**", inline=False)'''
                        try:
                            capeInfo = res['textures']['cape']['url']
                            #2016
                            if capeInfo == "http://textures.minecraft.net/texture/e7dfea16dc83c97df01a12fabbd1216359c0cd0ea42f9999b6e97c584963e980":
                                capeInfo="https://render.namemc.com/skin/3d/body.png?skin=12b92a9206470fe2&cape=1981aad373fa9754&theta=150&width=140&height=280"
                            #2015
                            if capeInfo == "http://textures.minecraft.net/texture/b0cc08840700447322d953a02b965f1d65a13a603bf64b17c803c21446fe1635":
                                capeInfo="https://render.namemc.com/skin/3d/body.png?skin=12b92a9206470fe2&cape=72ee2cfcefbfc081&theta=150&width=140&height=280"
                            #2013
                            if capeInfo == "http://textures.minecraft.net/texture/153b1a0dfcbae953cdeb6f2c2bf6bf79943239b1372780da44bcbb29273131da":
                                capeInfo="https://render.namemc.com/skin/3d/body.png?skin=12b92a9206470fe2&cape=0e4cc75a5f8a886d&theta=150&width=140&height=280"
                            #2012
                            if capeInfo == "http://textures.minecraft.net/texture/a2e8d97ec79100e90a75d369d1b3ba81273c4f82bc1b737e934eed4a854be1b6":
                                capeInfo="https://render.namemc.com/skin/3d/body.png?skin=12b92a9206470fe2&cape=ebc798c3f7eca2a3&theta=150&width=140&height=280"
                            #2011
                            if capeInfo == "http://textures.minecraft.net/texture/953cac8b779fe41383e675ee2b86071a71658f2180f56fbce8aa315ea70e2ed6":
                                capeInfo="https://render.namemc.com/skin/3d/body.png?skin=12b92a9206470fe2&cape=9349fa25c64ae935&theta=150&width=140&height=280"
                            em.set_thumbnail(url=capeInfo)
                        except KeyError:
                            ofCape = requests.get(f"https://capes.kqzz.me/croppedcape/{res['username']}")
                            if ofCape.status_code == 200:
                               em.set_thumbnail(url=f"https://capes.kqzz.me/croppedcape/{res['username']}?scale=10")
                        em.set_image(url=f"https://visage.surgeplay.com/full/512/{uuid}.png")
                        em.set_footer(text=f"https://namemc.com/{username} | Made by connor")
                        if len(em) > 1024:
                            await ctx.send(f"Embed would be too large, **{username}** has ``{str(i)}`` namechanges. However you may view them at https://namemc.com/{username}/")
                        else:
                            await ctx.send(embed=em,delete_after=30)
                    except KeyError:
                            text = f"{username} is not currently on an account."
                            embed = getembed(text)
                            try:
                                await ctx.send(embed=embed,delete_after=30)
                            except:
                                await ctx.send(f">>> {text}")


    @commands.command(aliases=['rates'])
    async def exchangerates(self, ctx): # b'\xfc'
        convertApiKey = "e08e888ee7d71fd7661e"
        args = ctx.message.content.split()
        await ctx.message.delete()
        if len(args) == 1 or len(args) == 2:
            text = f"""
**Invalid Parse Of Arguments**

`{args[0]}` **[convert from]** **[convert to]**
            """
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else: 
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://free.currconv.com/api/v7/convert?q="+args[1]+"_"+args[2]+"&compact=ultra&apiKey="+convertApiKey) as r:
                    res = await r.json()
                    em = discord.Embed(title="Currency exchange")
                    em.add_field(name="`Exchange rate:`",value=f"The current exchange rate of 1 **{args[1]}** to **{args[2]}** is ``"+str(res.get(args[1]+"_"+args[2]))+"``",inline=False)
                    await ctx.send(embed=em)

    bumpstatus = "off"
    @commands.command(aliases=['autobump', 'bumpauto'])
    async def bump(self, ctx, bumpingyuh=None):
        global bumpstatus 
        if bumpingyuh == None:
            if bumpstatus == "off":
                bumpstatus = "on"
            elif bumpstatus == "on":
                bumpstatus = "off"
        else:
            if bumpingyuh.lower() == "off":
                bumpstatus = "off"
            if bumpingyuh.lower() == "on":
                bumpstatus = "on"
            if bumpingyuh.lower() == "true":
                bumpstatus = "on"
            if bumpingyuh.lower() == "false":
                bumpstatus = "off"
        await ctx.send(f"`Autobump status : {bumpstatus}`",delete_after=3)
        while bumpstatus=="on":
            await ctx.send("!d bump")
            await asyncio.sleep(7201)

    @commands.command()
    async def guildav(self, ctx):
        await ctx.message.delete()
        em = discord.Embed(title=ctx.guild.name)
        em.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=em)

    @commands.command()
    async def poll(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

`{args[0]}` **[question]**
            """
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            args.pop(0)
            question = ' '.join(args)
            emoji1 = '✅'
            emoji2 = '❌'
            question = await ctx.send(f'{question}')
            await question.add_reaction(emoji1)
            await question.add_reaction(emoji2)
    
    @commands.command(aliases=["info"])
    async def stats(self,ctx):
        await ctx.message.delete()
        config = json.loads(open('data/config.json','r').read())
        text = f"""
`Ping:` **{round(self.bot.latency * 1000, 1)}ms**
`DM Logging:` **{config['Logging']['StoreDMFiles']}**
`GC Logging:` **{config['Logging']['StoreGCFiles']}**
`Server Logging:` **{config['Logging']['StoreGuildFiles']}**
`Attachment Logging:` **{config['Logging']['LogAttachments']}**
`Slotbot Sniper:` **{config['Snipers']['SlotbotSniper']['snipe']}**
`Pollux Sniper:` **{config['Snipers']['PolluxSniper']['snipe']}**
`Nitro Sniper:` **{config['Snipers']['NitroSniper']}**
`OS Platform:` **{sys.platform}**
`Python Version:` **{sys.version}**
"""
        embed = getembed(text)
        try:
            await ctx.send(embed=embed)
        except:
            await ctx.send(f">>> {text}")
    
    @commands.command()
    async def tts(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        buff = await aryi.do_tts(" ".join(args[1:]))
        await ctx.send(file=discord.File(buff, "speech.wav"))

    @commands.command(aliases=['ud'])
    async def urban(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        config = json.loads(open('data/config.json','r').read())
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

{config['prefix']}urban ``[term]``"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            args.pop(0)
            search = ' '.join(args)
            number = 1
            if " | " in search:
                search, number = search.rsplit(" | ", 1)
            r= requests.get("http://api.urbandictionary.com/v0/define", params={"term": search})
            r = r.json()
            if not r["list"]:
                await ctx.send(f"{config['prefix']}{search} couldn't be found on Urban Dictionary.")
            else:
                try:
                    top_result = r["list"][int(number) - 1]
                    embed = discord.Embed(title=top_result["word"], description=top_result["definition"], url=top_result["permalink"])
                    if top_result["example"]:
                        embed.add_field(name="Example:", value=top_result["example"])
                    embed.set_author(name=top_result["author"],
                                    icon_url="https://lh5.ggpht.com/oJ67p2f1o35dzQQ9fVMdGRtA7jKQdxUFSQ7vYstyqTp-Xh-H5BAN4T5_abmev3kz55GH=w300")
                    if len(r['list']) > 1:
                        number = str(int(number)+1)
                        embed.set_footer(text=f"{len(r['list'])} results were found. To see a different result, use {config['prefix']}ud {search} | {number}.")
                    await ctx.send("", embed=embed, delete_after=30)
                except IndexError:
                    await ctx.send("Error")

    @commands.command(aliases=['markasread', 'read'])
    async def readall(self, ctx):
        await ctx.message.delete()
        for guild in self.bot.guilds:
            try:
                await guild.ack()
                await asyncio.sleep(0.3)
            except:
                pass

    @commands.command()
    async def covid(self, ctx):
        await ctx.message.delete()
        url = "https://api.covidtracking.com/v1/us/current.json"

        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                positive = f"{r[0]['positive']}"
                negative = f"{r[0]['negative']}"
                pending = f"{r[0]['pending']}"
                hospitalized = f"{r[0]['hospitalizedCumulative']}"
                inicu = f"{r[0]['inIcuCumulative']}"
                deaths = f"{r[0]['death']}"

        embed = discord.Embed(title="USA Covid-19 Stats")
        embed.add_field(name="Confirmed", value=positive)
        embed.add_field(name="Negative", value=negative)
        embed.add_field(name="Pending", value=pending)
        embed.add_field(name="Hospitalized", value=hospitalized)
        embed.add_field(name="In ICU", value=inicu)
        embed.add_field(name="Total Deaths", value=deaths)
        embed.set_thumbnail(url="https://images.squarespace-cdn.com/content/v1/5c4085e585ede1f50f94a4b9/1581018457505-JM3FO6WMFN9BGP3IOE8D/ke17ZwdGBToddI8pDm48kL5hQm_JZO5i_9Equza1B-57gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1URbcWFoTofQNHE0Fe4ADwtkYw2N2aveJw6FaFCcRrQmU3WUfc_ZsVm9Mi1E6FasEnQ/2019-nCoV-CDC-23312_without_background.png")

        await ctx.send(embed=embed)

    @commands.command()
    async def fnshop(self, ctx):
        await ctx.message.delete()
        url = "https://api.nitestats.com/v1/shop/image"

        embed = discord.Embed(title="Fortnite Shop")
        embed.set_image(url=url)
    
        await ctx.send(embed=embed)

    @commands.command()
    async def yesno(self, ctx):
        await ctx.message.delete()
        url = "https://yesno.wtf/api"

        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                yesno = f"{r['answer']}"
                gif = f"{r['image']}"
            embed = discord.Embed(title=yesno)
            embed.set_image(url=gif)
            await ctx.send(embed=embed)

    @commands.command(aliases=['dc'])
    async def disconnect(self, ctx, member: discord.Member): 
        await ctx.message.delete()
        print(f"trying to disconnect {str(member)}")
        await member.move_to(self.bot.get_channel("1"))

    @commands.command()
    async def nick(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

{config['prefix']}nick ``[nickname]``"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            args.pop(0)
            nickname = ' '.join(args)
            embed = discord.Embed(color=0x0000)
            embed.set_author(name="Nickname")
            embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
            try:
                await ctx.author.edit(nick=nickname)
                text = f"Nickname set to `{nickname}`."
            except discord.HTTPException:
                text = f"Missing permissions to change nickname."
            await ctx.send(embed=getembed(text), delete_after=30)

def setup(bot):
    bot.add_cog(Utility(bot))