import discord, json
from discord.ext import commands
from bot import getembed
class Afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def afk(self, ctx):
        await ctx.message.delete()
        args = ctx.message.content.split()
        afkdata = json.loads(open("data/afk.json","r").read())
        if afkdata['enabled'] == True:
            text = "You already have AFK Enabled!"
            try:
                await ctx.send(embed=getembed(text), delete_after=30)
            except:
                await ctx.send(text)
        else:
            if len(args) <= 1:
                text = f"I will set your AFK status as the default message: `{afkdata['default_message']}`"
            else:
                text = f"I will set your AFK status as the custom message: `{' '.join(args[1:])}`"
                afkdata['custom_message'] = f"AFK:\n\n`{' '.join(args[1:])}`"
            try:
                await ctx.send(embed=getembed(text), delete_after=30)
            except:
                await ctx.send(text)
            afkdata['enabled'] = True
        open("data/afk.json","w+").write(json.dumps(afkdata, indent=4, sort_keys=True))
def setup(bot):
    bot.add_cog(Afk(bot))