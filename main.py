mytitle = "Bad Server Cloner V2 - Developed By Odqin Hope.#3890"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = 'Your Account ID'
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.BLACK}


────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
██████╗░░█████╗░██████╗░  ░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗  ██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗
██████╦╝███████║██║░░██║  ╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝
██╔══██╗██╔══██║██║░░██║  ░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗
██████╦╝██║░░██║██████╔╝  ██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░  ╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░  ██╗░░░██╗██████╗░░░░░█████╗░
██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗  ██║░░░██║╚════██╗░░░██╔══██╗
██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝  ╚██╗░██╔╝░░███╔═╝░░░██║░░██║
██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗  ░╚████╔╝░██╔══╝░░░░░██║░░██║
╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║  ░░╚██╔╝░░███████╗██╗╚█████╔╝
░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝╚═╝░╚════╝░
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
{Style.RESET_ALL}
                                                            {Fore.RED}Developed By Bad.{Style.RESET_ALL}
        """)
token = input(f'💥 Please Enter Your Token 💥:\n >')
guild_s = input('📀 Please Enter Server Id You Want To Copy 📀:\n >')
guild = input('💿 Please Enter Server Id Where You Want To Paste 💿:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Bad Start Clone The Server...")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}




██████╗░░█████╗░███╗░░██╗███████╗  ██╗
██╔══██╗██╔══██╗████╗░██║██╔════╝  ██║
██║░░██║██║░░██║██╔██╗██║█████╗░░  ██║
██║░░██║██║░░██║██║╚████║██╔══╝░░  ╚═╝ 
██████╔╝╚█████╔╝██║░╚███║███████╗  ██╗  
╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝  ╚═╝  
                █▄▄ █▄█   █▄▄ ▄▀█ █▀▄ ░
                █▄█ ░█░   █▄█ █▀█ █▄▀ ▄
  

    {Style.RESET_ALL}""")
    time.sleep(2)

client.run(token, bot=False)
