import os


async def configure(bot):
    for file in os.listdir("./codez/commands"):
        if file.endswith(".py"):
            await bot.load_extension(f"codez.commands.{file[:-3]}")
