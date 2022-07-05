from discord import Status, Game
from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands.errors import MissingRequiredArgument
from discord.ext.commands.errors import CommandNotFound
from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")

bot = commands.Bot(".")


@bot.event
async def on_ready():
    game = Game('Type ".commands"!')

    await bot.change_presence(status=Status.online, activity=game)

    print("I'm Codez and I'm ready!")


@bot.event
async def on_command_error(ctx: Context, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.reply("Please make sure to send all arguments!")
    elif isinstance(error, CommandNotFound):
        await ctx.reply("This command doesn't exist!")
    else:
        raise error

bot.load_extension("commands.commands")
bot.load_extension("commands.execute")
bot.load_extension("commands.languages")
bot.load_extension("commands.usage")


bot.run(getenv("TOKEN"))
