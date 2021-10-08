import discord
from dotenv import load_dotenv
from os import getenv
from commands import command
from commands import run

load_dotenv(".env")

class MyClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(activity = discord.Game(name = "Type .command"))

        print("I'm ready!")
    
    async def on_message(self, message):
        if(not(message.author.bot)):
            if(message.content.startswith(".run")):
                await run.run(message, self)
            elif(message.content.startswith(".command")):
                await command.command(message, self)
    
client = MyClient()

client.run(getenv("TOKEN"))