#!/usr/bin/env python
# -*- coding: utf-8 -*-
import colorama, datetime, requests, sys, json, os, random, time, threading, youtube_dl, discord, asyncio, re, ctypes, io, datetime
from colorama import Fore
from gtts import gTTS
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}
ffmpeg_options = {
    'options': '-vn'
}
async def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang="en-US")
    tts.write_to_fp(f)
    f.seek(0)
    return f
def date_send(text):
    print(f"[!] {text}")
def title(text):
    if sys.platform.startswith("win"): 
        ctypes.windll.kernel32.SetConsoleTitleW(text)

def check_nitro_sniper(message, config, client):
    if config['Snipers']['NitroSniper'] == True  and message.author.bot == False and message.author.id != client.user.id and "discord.gift" in message.content :
        code = re.search("discord.gift/(.*)", message.content).group(1)
        if code in config['duplicates']:
            date_send(f"{Fore.RED}Duplicate Gift Code{Fore.RESET}, Code here: {code}")
            payload = {"username" : message.author.name,"avatar_url" : str(message.author.avatar_url),"embeds" : [{"description" : "Duplicate code.","footer" : {"text" : f"Code here: {code}","icon_url": config['GenesisGif']}}]}
            requests.post(config['nitro_webhook'],json=payload)
        else:
            threading.Thread(target=check_nitro,args=[config,code,message]).start()
def check_nitro(code, config):
    headers = {'Authorization': config['token']}
    r = requests.post(
        f'https://discord.com/api/v8/entitlements/gift-codes/{code}/redeem', 
        headers=headers,
    ).text
    if 'This gift has been redeemed already.' in r:
        date_send(f"{Fore.RED}Nitro Already Redeemed{Fore.RESET}, Code here: {code}")
        config['duplicates'].append(code)
        open('data/config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))
    elif 'subscription_plan' in r:
        date_send(f" {Fore.GREEN}Nitro Successfully Redeemed{Fore.RESET}, Code here: {code}")
        config['duplicates'].append(code)
        open('data/config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))
    elif 'Unknown Gift Code' in r:
        date_send(f"{Fore.RED}Invalid Gift Code{Fore.RESET}, Code here: {code}")
        config['duplicates'].append(code)
        open('data/config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))
    else:
        return

def return_glitch():
    payload = {
        'theme': "dark",
        'locale': "ja",
        'message_display_compact': False,
        'enable_tts_command': False,
        'inline_embed_media': True,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    return payload

def leave_guild(headers,id):
    while True:
        src = requests.post(f'https://canary.discordapp.com/api/v8/users/@me/guilds/{id}/delete', headers=headers ,timeout=20)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break

def delete_guild(headers,id): 
    while True:
        src = requests.post(f'https://canary.discordapp.com/api/v8/guilds/{id}/delete', headers=headers ,timeout=20)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break

def remove_friend(id,headers):
    while True:
        src = requests.delete(f"https://canary.discordapp.com/api/v6/users/@me/relationships/{str(id)}", headers=headers, timeout=10)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break

def create_guild(name,headers):
    payload = {"name": name}
    while True:
        src = requests.post(f'https://canary.discordapp.com/api/v6/guilds', headers=headers, json=payload, timeout=10)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break

def close(id,headers):
    while True:
        src = requests.delete(f"https://canary.discordapp.com/api/v6/channels/{id}", headers=headers, timeout=10)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


def clear():
    if sys.platform == "win32" or sys.platform == "win64":
        os.system("cls")
    else:
       os.system("clear")

def flood(sock, ip, port, stop, bytes):
    while time.time() < stop:
        sock.sendto(bytes, (ip,port))

def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc

def ui(self,prefix,auth):
    print(f"""
{Fore.BLUE}


 ███▄ ▄███▓ ██▓▄▄▄█████▓  ██████  █    ██  ██ ▄█▀ ██▓
▓██▒▀█▀ ██▒▓██▒▓  ██▒ ▓▒▒██    ▒  ██  ▓██▒ ██▄█▒ ▓██▒          
▓██    ▓██░▒██▒▒ ▓██░ ▒░░ ▓██▄   ▓██  ▒██░▓███▄░ ▒██▒             
▒██    ▒██ ░██░░ ▓██▓ ░   ▒   ██▒▓▓█  ░██░▓██ █▄ ░██░           
▒██▒   ░██▒░██░  ▒██▒ ░ ▒██████▒▒▒▒█████▓ ▒██▒ █▄░██░      
░ ▒░   ░  ░░▓    ▒ ░░   ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░▓        
░  ░      ░ ▒ ░    ░    ░ ░▒  ░ ░░░▒░ ░ ░ ░ ░▒ ▒░ ▒ ░      
░      ░    ▒ ░  ░      ░  ░  ░   ░░░ ░ ░ ░ ░░ ░  ▒ ░
       ░    ░                 ░     ░     ░  ░    ░  
                                                     
Prefix: {prefix}
User: {self.user}
User ID: {self.user.id}
Date: {datetime.date.today().strftime('%d, %B %Y')}
{Fore.RESET}
    """)

def webhook_spam(webhook, content):
    payload = {'content': content}
    requests.post(webhook, json=payload)

def encrypt(message,corruptchanname):
    for x in message.content:
        if random.randint(1,2) == 1:
            corruptchanname += asciigen(1)
        else:
            corruptchanname += x   
    return corruptchanname

