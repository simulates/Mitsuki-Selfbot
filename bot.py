#!/usr/bin/env python
# -*- coding: utf-8 -*-
import discord, json, datetime, colorama, time, sys, os, requests, random, threading, ctypes, re, asyncio, emoji, importlib_metadata, getpass
from colorama import Fore
from discord.ext import commands
from cogs import aryi


colorama.init()
startup_extensions = ['cogs.afk','cogs.status','cogs.sniping','cogs.interactive','cogs.configuration','cogs.utility','cogs.imaging','cogs.illegal','cogs.crypto', 'cogs.emoticons', 'cogs.math']
config = json.loads(open("data/config.json","r").read())

token = config['token']

def getembed(text):
    embed = discord.Embed(
        description=text,
        color=0x2f3136
    )
    return embed

def get_prefix(client, message):
    return json.loads(open("data/config.json","r").read())['prefix']
client = commands.Bot(command_prefix=get_prefix,help_command=None,self_bot=True)
if not os.path.exists("files"):
    os.mkdir("files")
    os.mkdir("files/DMChannels")
    os.mkdir("files/GroupChannels")
    os.mkdir("files/Servers")
if config['token'] == "" or config['token'] == "token here":
    print(f"Token isn't in the config.json...")
    time.sleep(5)
    sys.exit()
if config['prefix'] == "" or config['prefix'] == "prefix here":
    print(f"Prefix isn't in the config.json...")
    time.sleep(5)
    sys.exit()
aryi.title("Mitsuki Selfbot open sourced")

start = datetime.datetime.now()

def start_up():
    username = getpass.getuser()
    filepath = os.path.dirname(os.path.realpath(__file__))
    startup = r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.format(username)
    if os.path.exists(startup):
        with open(startup + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(f"""
cd {str(filepath).split()[:-1]}
python {__file__}""")

@client.event
async def on_connect():
    userID = client.user.id

    aryi.clear()
    aryi.ui(client,json.loads(open('data/config.json','r').read())['prefix'],config['token'])
    aryi.date_send(f"{Fore.BLUE}Slotbot Sniper: {Fore.WHITE}{config['Snipers']['SlotbotSniper']['snipe']}{Fore.RESET}")
    aryi.date_send(f"{Fore.BLUE}Pollux Sniper: {Fore.WHITE}{config['Snipers']['PolluxSniper']['snipe']}{Fore.RESET}")
    aryi.date_send(f"{Fore.BLUE}Giveaway Sniper: {Fore.WHITE}{config['Snipers']['GiveawaySniper']['snipe']}{Fore.RESET}")
    aryi.date_send(f"{Fore.BLUE}Nitro Sniper: {Fore.WHITE}{config['Snipers']['NitroSniper']}{Fore.RESET}")
    print("===============================================")


@client.event
async def on_message(message):
    afkdata = json.loads(open("data/afk.json","r").read())
    if afkdata['enabled'] == True and message.guild == None:
        if message.author.id == client.user.id:
            if message.content != afkdata['custom_message'] and message.content != afkdata['default_message']:
                await message.edit(content=f"I see you are not AFK anymore, let me disable that for you. Also, whoever he sent this to and has not seen the message before it was edited, here it is:\n\n{message.content}")
                afkdata['enabled'] = False
                afkdata['ids'] = []
                afkdata['custom_message'] = ""
                open("data/afk.json","w+").write(json.dumps(afkdata,indent=4,sort_keys=True))
        else:
            if message.channel.id in afkdata['ids']:
                return
            if afkdata['custom_message'] != "":
                await message.channel.send(afkdata['custom_message'])
            else:
                await message.channel.send(afkdata['default_message'])
            afkdata['ids'].append(message.channel.id)
            open("data/afk.json","w+").write(json.dumps(afkdata,indent=4,sort_keys=True))
    await client.process_commands(message)
    config = json.loads(open("data/config.json","r").read())
    if config['Snipers']['NitroSniper'] == True  and message.author.bot == False and message.author.id != client.user.id and "discord.gift" in message.content :
        code = re.search("discord.gift/(.*)", message.content).group(1).split()[0]
        if code in config['duplicates']:
            aryi.date_send(f"{Fore.RED}Duplicate Gift Code{Fore.RESET}, Code here: {code}")
        else:
            threading.Thread(target=aryi.check_nitro, args=[code, config]).start()
    if message.content.startswith("Someone just dropped") and message.author.id == config['Snipers']['SlotbotSniper']['id'] and config['Snipers']['SlotbotSniper']['snipe'] == "True":
        try:
            await message.channel.send("~grab",delete_after=10)
            aryi.date_send(f"Attempted to snipe slotbot || Channel: [{message.channel.name}] || Server: [{message.guild.name}]")
        except:
            pass
    if 'Type `pick` for a chance to claim it!' in message.content and message.author.id == config['Snipers']['PolluxSniper']['id'] and config['Snipers']['PolluxSniper']['snipe'] == "True":
        try:
            await message.channel.send("pick")
            aryi.date_send(f"Attempted to snipe pollux || Channel: [{message.channel.name}] || Server: [{message.guild.name}]")
        except:
            pass
    if message.content == "prefix" and message.author.id == client.user.id:
        text = f"```your prefix is {config['prefix']}```"
        embed = discord.Embed(description=text)
        try:
            await message.edit(content="",embed=embed,delete_after=30) 
        except:
            await message.channel.send(text)

async def status_cycle():
    await client.wait_until_ready()
    while True:
        config = json.loads(open("data/config.json","r").read())
        if config['stream-cycle'] == False:
            return
        for status in config['statuses']:
            headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
            requests.patch("https://discord.com/api/v8/users/@me/settings",headers=headers,json={"custom_status":{"text":status['state']}})
            await asyncio.sleep(status["delay"])


@client.command(aliases=["cmds"])
async def help(ctx):
    await ctx.message.delete()
    config = json.loads(open("data/config.json","r").read())
    embed = discord.Embed(
        color=0x2f3136,
        timestamp=ctx.message.created_at,
        description=f"**Prefix**: `{config['prefix']}`"
    ) 
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    embed.set_author(name="sin",icon_url=ctx.message.author.avatar_url)
    commands_count = 0
    cogs_count = 0
    for cog in client.cogs:
        if cog == "Sniping":
            pass
        else:
            cogs_count += 1
            text = ""
            for command in client.get_cog(cog).walk_commands():
                commands_count += 1
                text += "`{}` ".format(command)
            embed.add_field(name=cog,value=text,inline=True)
    embed.set_footer(text=f"{cogs_count} Cogs | {commands_count} Commands",icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed,delete_after=30)
if __name__ == "__main__":
    for file in os.listdir("cogs"):
        if file.endswith(".py") and not file.startswith("__") and not "aryi" in file:
            client.load_extension(f"cogs.{file[:-3]}")
    client.loop.create_task(status_cycle())
    client.run(token,bot=False,reconnect=True)
