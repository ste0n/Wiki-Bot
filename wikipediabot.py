import discord
from email import message
from email.headerregistry import DateHeader
from http import server
from multiprocessing.connection import Client
from webbrowser import get


import time
import discord.utils
import wikipedia
h =[6]
def lensentence(k):
    h[0]=k

class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
     
    async def on_message(self, message):

        if message.author.bot:
            
            return
        if message.content == "wiki$help":
            await message.channel.send("wikilen={number of sentences}")
            await message.channel.send("wikilan={language}")
            await message.channel.send("wiki${word}")


        if message.content.startswith("wikilen="):
            try:
                  argss = message.content.split('=')
                  sen = int(argss)
                  lensentence(sen)
            except:
                return
        if message.content.startswith("wikilan="):
            try:
                  argss = message.content.split('=')
                  lan = str(argss)
                  wikipedia.set_lang(lan)
                  
            except:
                await message.channel.send("Type it right!")
                return
        if message.content.startswith("wiki$"):
            
            args = message.content.split('$')
            search = str(args[1])
            try:
                
    
                
                wikicontent = wikipedia.summary(search, sentences=h[0])
                

                await message.channel.send(f"Here is the wiki item for({search}):")
                await message.channel.send(wikicontent)
            
            except:
                
                await message.channel.send("Type it right!")
                    
                return       
               
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run("Token")



