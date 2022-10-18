import asyncio
import os
import dotenv
import discord
from codez import setup
from discord.ext import commands

dotenv.load_dotenv()


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="?", intents=intents, help_command=None)

        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()

        if not self.synced:
            await self.tree.sync()

            self.synced = True

        print(f"We have logged in as {self.user}.")
        print("I'm CodeZ and I'm ready!")


bot = Bot()


async def main():
    async with bot:
        await setup.configure(bot)
        await bot.start(os.environ["TOKEN"])


asyncio.run(main())
