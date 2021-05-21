import discord, json
from discord import embeds
from discord.ext import commands
from bot import getembed

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def prefix(self, ctx):
        await ctx.message.delete()
        config = json.loads(open("data/config.json","r").read())
        commands = ctx.message.content.rsplit(config['prefix'])[1].split()
        if len(commands) == 1:
            text = f"""
**Invalid Parse Of Arguments**

{config['prefix']}prefix ``[new_prefix]``"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            config['prefix'] = commands[1]
            open('data/config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))
            text = f"Your **prefix** was changed, your new **prefix** is **{commands[1]}**"
            try:
                await ctx.send(embed=embeds,delete_after=30)
            except:
                await ctx.send(f">>> {text}")

    @commands.command()
    async def nitrosniper(self, ctx):
        config = json.loads(open("data/config.json","r").read())
        await ctx.message.delete()
        if config['Snipers']['NitroSniper'] == True:
            config['Snipers']['NitroSniper'] = False
            text = "```Nitro Sniper has been disabled.```"
        elif config['Snipers']['NitroSniper'] == False:
            config['Snipers']['NitroSniper'] = True
            text = "```Nitro Sniper has been enabled.```"
        else:
            config['Snipers']['NitroSniper'] = True
            text = "```Nitro Sniper has been enabled.```"
        open('data/config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))
        embed = getembed(text)
        try:
            await ctx.send(embed=embed,delete_after=30)
        except:
            await ctx.send(f">>> {text}")

    @commands.command()
    async def slotbotsniper(self, ctx):
        config = json.loads(open("data/config.json","r").read())
        await ctx.message.delete()
        if config['Snipers']['SlotbotSniper']['snipe'] == True:
            config['Snipers']['SlotbotSniper']['snipe'] = False
            text = "```Slotbot sniper has been disabled.```"
        elif config['Snipers']['SlotbotSniper']['snipe'] == False:
            config['Snipers']['SlotbotSniper']['snipe'] = True
            text = "```Slotbot sniper has been enabled.```"
        else:
            config['Snipers']['SlotbotSniper']['snipe'] = True
            text = "```Slotbot sniper has been enabled.```"
        open('data/config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))
        embed = getembed(text)
        try:
            await ctx.send(embed=embed,delete_after=30)
        except:
            await ctx.send(f">>> {text}")

    @commands.command()
    async def polluxsniper(self, ctx):
        config = json.loads(open("data/config.json","r").read())
        await ctx.message.delete()
        if config['Snipers']['PolluxSniper']['snipe'] == True:
            config['Snipers']['PolluxSniper']['snipe'] = False
            text = "```Pollux sniper has been disabled.```"
        elif config['Snipers']['PolluxSniper']['snipe'] == False:
            config['Snipers']['PolluxSniper']['snipe'] = True
            text = "```PolluxSniper sniper has been enabled.```"
        else:
            config['Snipers']['PolluxSniper']['snipe'] = True
            text = "```Pollux sniper has been enabled.```"
        open('data/config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))
        embed = getembed(text)
        try:
            await ctx.send(embed=embed,delete_after=30)
        except:
            await ctx.send(f">>> {text}")

    

def setup(bot):
    bot.add_cog(Config(bot))