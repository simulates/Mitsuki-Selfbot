import discord, json, requests, emoji
from cogs import aryi
from discord.ext import commands
class Sniping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        config = json.loads(open('data/config.json','r').read())
        if payload.emoji.name == emoji.emojize(config['Snipers']['GiveawaySniper']['emoji'],use_aliases=True) and config['Snipers']['GiveawaySniper']['snipe'] == "True" and payload.event_type == "REACTION_ADD" and payload.user_id == config['Snipers']['GiveawaySniper']['id']:
            channel = self.bot.get_channel(payload.channel_id)
            if channel == None:
                aryi.date_send(f"Unable to snipe this giveaway || Channel: {payload.channel_id} || Server: {payload.guild_id}")
            else:
                message = await channel.fetch_message(payload.message_id)
                if message != None:
                    await message.add_reaction(emoji.emojize(config['Snipers']['GiveawaySniper']['emoji'],use_aliases=True))
                    aryi.date_send(f"Sniped a giveaway || Channel: {channel.name} || Server: {channel.guild.name}")
                    payload = {"username" : message.author.name,"avatar_url" : str(message.author.avatar_url),"embeds" : [{"title" : "Sniped Giveaway","description" : f"Channel: <#{message.channel.id}>","footer" : {"text" : f"Server: {message.guild.name}","icon_url": config['GenesisGif']}}]}
                    requests.post(config['sniping_webhook'],json=payload)

def setup(bot):
    bot.add_cog(Sniping(bot))