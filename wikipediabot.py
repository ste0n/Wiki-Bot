import asyncio
import discord
from email import message
from email.headerregistry import DateHeader
from http import server
from multiprocessing.connection import Client
from webbrowser import get
import datetime
import time
import discord.utils
import wikipedia
sentencel =6


from discord import Member

client = discord.Client()
@client.event
async def on_ready():
    print('Bot logged in as user: {}'.format(client.user.name))



@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("wiki$lengh="):
        try:
            
            argss = message.content.split('=')
            sentencel = int(argss)

        except KeyError:
            return


    if message.content.startswith("wiki$"):
        args = message.content.split('$')
        search = str(args[1])
        try:
            wikicontent = wikipedia.summary(search, sentences=sentencel)
            await message.channel.send(f"Here is the wiki item for({search}):")
            await message.channel.send(wikicontent)
        except KeyError:
            return














client.run('TOKEN')
