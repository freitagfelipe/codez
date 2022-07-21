from discord import Status, Game
from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands.errors import MissingRequiredArgument
from discord.ext.commands.errors import CommandNotFound
from dotenv import load_dotenv
from os import getenv, listdir

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
        await ctx.reply("This command doesn't exist! Type .commands or .help to see all my commands!")
    else:
        raise error

for file in listdir("./commands/"):
    if file.endswith(".py"):
        bot.load_extension(f'commands.{file[:-3]}')

bot.run(getenv("TOKEN"))
