import discord, json, datetime, requests, random, asyncio, aiohttp
from bs4 import BeautifulSoup as bs4
from discord.ext import commands
from bot import getembed
import translators as ts

def action_embed(url):
    em = discord.Embed(color=0x2f3136)   
    em.set_image(url=url)
    return em

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

class Interactive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def anal(self, ctx):
        await ctx.message.delete()
        url = requests.get("https://nekos.life/api/v2/img/anal").json()['url']
        embed = action_embed(url)
        try:
            await ctx.send(embed=embed, delete_after=30)
        except:
            await ctx.send(f">>> **Unable to send embeds here lOl**")

    @commands.command()
    async def hentai(self, ctx):
        await ctx.message.delete()
        url = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif").json()['url']
        embed = action_embed(url)
        try:
            await ctx.send(embed=embed, delete_after=30)
        except:
            await ctx.send(f">>> **Unable to send embeds here lOl**")

    @commands.command()
    async def boobs(self, ctx):
        await ctx.message.delete()
        url = requests.get("https://nekos.life/api/v2/img/boobs").json()['url']
        embed = action_embed(url)
        try:
            await ctx.send(embed=embed, delete_after=30)
        except:
            await ctx.send(f">>> **Unable to send embeds here lOl**")

    @commands.command()
    async def bj(self, ctx):
        await ctx.message.delete()
        url = requests.get("https://nekos.life/api/v2/img/bj").json()['url']
        embed = action_embed(url)
        try:
            await ctx.send(embed=embed, delete_after=30)
        except:
            await ctx.send(f">>> **Unable to send embeds here lOl**")

    @commands.command()
    async def tits(self, ctx):
        await ctx.message.delete()
        url = requests.get("https://nekos.life/api/v2/img/tits").json()['url']
        embed = action_embed(url)
        try:
            await ctx.send(embed=embed, delete_after=30)
        except:
            await ctx.send(f">>> **Unable to send embeds here lOl**")

    @commands.command()
    async def cuddle(self, ctx):
        await ctx.message.delete()
        config = json.loads(open("data/config.json","r").read())
        if len(ctx.message.mentions) == 0:
            text = f"""
**Invalid Parse Of Arguments**

`{config['prefix']}cuddle` **[@user]**
"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed, delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            url = requests.get("https://nekos.life/api/v2/img/cuddle").json()['url']
            embed = action_embed(url)
            embed.set_footer(text=f"{self.bot.user} just cuddled {ctx.message.mentions[0].name}")
            try:
                await ctx.send(embed=embed, delete_after=30)
            except:
                await ctx.send(f">>> **Unable to send embeds here lOl**")

    @commands.command()
    async def hug(self, ctx):
        config = json.loads(open("data/config.json","r").read())
        await ctx.message.delete()
        if len(ctx.message.mentions) == 0:
            text = f"""
**Invalid Parse Of Arguments**

`{config['prefix']}hug` **[@user]**
"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed, delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            url = requests.get("https://nekos.life/api/v2/img/hug").json()['url']
            embed = action_embed(url)
            embed.set_footer(text=f"{self.bot.user} just hugged {ctx.message.mentions[0].name}")
            try:
                await ctx.send(embed=embed, delete_after=30)
            except:
                await ctx.send(f">>> **Unable to send embeds here lOl**")

    @commands.command()
    async def kiss(self, ctx):
        await ctx.message.delete()
        config = json.loads(open("data/config.json","r").read())
        if len(ctx.message.mentions) == 0:
            text = f"""
**Invalid Parse Of Arguments**

`{config['prefix']}kiss` **[@user]**
"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed, delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            url = requests.get("https://nekos.life/api/v2/img/kiss").json()['url']
            embed = action_embed(url)
            embed.set_footer(text=f"{self.bot.user} just kissed {ctx.message.mentions[0].name}")
            try:
                await ctx.send(embed=embed, delete_after=30)
            except:
                await ctx.send(f">>> **Unable to send embeds here lOl**")
                
    @commands.command()
    async def slap(self, ctx):
        await ctx.message.delete()
        config = json.loads(open("data/config.json","r").read())
        if len(ctx.message.mentions) == 0:
            text = f"""
**Invalid Parse Of Arguments**

`{config['prefix']}slap` **[@user]**
"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed, delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            url = requests.get("https://nekos.life/api/v2/img/slap").json()['url']
            embed = action_embed(url)
            embed.set_footer(text=f"{self.bot.user} just slapped {ctx.message.mentions[0].name}")
            try:
                await ctx.send(embed=embed, delete_after=30)
            except:
                await ctx.send(f">>> **Unable to send embeds here lOl**")
    
    @commands.command()
    async def cat(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/img/cat").json()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name="Random Cat.", icon_url="https://cdn.discordapp.com/attachments/796868392095186976/810566027637162034/zeenode_cat.png") 
        embed.set_image(url=str(r["link"]))
        await ctx.send(embed=embed, delete_after=30)  

    @commands.command(aliases=["tran", "tr"]) 
    async def translate(self, ctx, *args):
        await asyncio.sleep(0.05)
        await ctx.message.delete()
        args = ' '.join(args).split(" ", 2)
        try:
            if args[0] != "auto" and args[1] != "auto":
                msg = ts.google(args[2], from_language=args[0], to_language=args[1])
            elif args[0] == "auto" and args[1] != "auto":
                msg = ts.google(args[2], to_language=args[1])
            elif args[0] != "auto" and args[1] == "auto":
                msg = ts.google(args[2], from_language=args[1])
            else:
                msg = ts.google(args[2])
            await asyncio.sleep(0.3)
            await ctx.send(msg)
        except:
            print("Error")
    
    @commands.command(aliases=['qrcode'])
    async def qr(self, ctx, *, text):
        text = text.replace(" ","%20")
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(color=0x000000)
        embed.set_image(url=f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={text}")
        await ctx.message.edit(content="",embed=embed,delete_after=30)

    @commands.command(aliases=['8ball'])
    async def _ball(self, ctx, *, question):
        await ctx.message.delete()
        responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'There is a good chance'
        ]
        answer = random.choice(responses)
        embed = discord.Embed()
        embed.add_field(name="Question", value=question, inline=False)
        embed.add_field(name="Answer", value=answer, inline=False)
        embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
        embed.set_footer(text=datetime.datetime.now())
        await ctx.send(embed=embed, delete_after=30)      

    @commands.command(aliases=['slots', 'bet'])
    async def slot(self, ctx): # b'\xfc'
        await ctx.message.delete()
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
        if (a == b == c):
            await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}), delete_after=30)
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}), delete_after=30)
        else:
            await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}), delete_after=30)
    
    @commands.command()
    async def joke(self, ctx):  # b'\xfc'
        await ctx.message.delete()
        headers = {
            "Accept": "application/json"
        }
        async with aiohttp.ClientSession()as session:
            async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
                r = await req.json()
        await ctx.send(r["joke"], delete_after=30)

    @commands.command()
    async def topic(self, ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get('https://www.conversationstarters.com/generator.php').content
        soup = bs4(r, 'html.parser')
        topic = soup.find(id="random").text
        await ctx.send(topic, delete_after=30)

    @commands.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
    async def wyr(self, ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
        soup = bs4(r, 'html.parser')
        qa = soup.find(id='qa').text
        qor = soup.find(id='qor').text
        qb = soup.find(id='qb').text
        em = discord.Embed(description=f'Would you rather?\n\n{qa}?\n{qor}\n{qb}')
        await ctx.send(embed=em, delete_after=30)

    @commands.command()
    async def trumptweet(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        config = json.loads(open('data/config.json','r').read())
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

{config['prefix']}trumptweet ``[text]``"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            args.pop(0)
            msg = ' '.join(args)
            r= requests.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={msg}")
            r = r.json()
            embed = discord.Embed(color=0x0000)
            embed.set_author(name="Trump Tweet." , icon_url="https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg") 
            embed.set_image(url=str(r["message"]))
            await ctx.send(embed=embed, delete_after=30)    

    @commands.command()
    async def tweet(self, ctx):
        args = ctx.message.content.split()
        await ctx.message.delete()
        config = json.loads(open('data/config.json','r').read())
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

{config['prefix']}tweet  ``[username]`` ``[text]``"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            args.pop(0)
            username = args[0]
            args.pop(0)
            msg = ' '.join(args)
            r = requests.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={msg}")
            r = r.json()
            embed = discord.Embed(color=0x0000)
            embed.set_author(name="Tweet." , icon_url="https://icons.iconarchive.com/icons/dakirby309/windows-8-metro/256/Web-Twitter-alt-2-Metro-icon.png") 
            embed.set_image(url=str(r["message"]))
            await ctx.send(embed=embed, delete_after=30)
   
    @commands.command()
    async def blowjob(self, ctx):
        await ctx.message.delete()
        args = ctx.message.content.split()
        config = json.loads(open('data/config.json','r').read())
        if len(ctx.message.mentions) == 0:
            text = f"""
**Invalid Parse Of Arguments**
`{config['prefix']}blowjob` **[@user]**"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed, delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
                url = requests.get("https://nekos.life/api/v2/img/blowjob").json()['url']
                embed = action_embed(url)
                embed.set_footer(text=f"{self.bot.user} just blew {ctx.message.mentions[0].name}")
                try:
                    await ctx.send(embed=embed, delete_after=30)
                except:
                    await ctx.send(f">>> **Unable to send embeds here lOl**")
def setup(bot):
    bot.add_cog(Interactive(bot))