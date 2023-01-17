from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Bot


@commands.hybrid_command(with_app_command=True)
async def commands(ctx: Context):
    commands = [
        "(?/) about - sends informations about the bot",
        "(?/) commands - sends a list of all my commands",
        "(??) execute - executes a given code",
        "(?/) languages - sends my supported languages",
        "(?/) usage - sends an image that teaches you how to use the execute command",
        '\nIf the "?" is present in the command description that means you can execute the command like ?<command>',
        'If the "/" is present in the command description that means you can execute the command like /<command>',
    ]

    embed_arg = Embed(
        title="My commands", description="\n".join(commands), color=255
    ).set_author(name=ctx.me.name, icon_url=ctx.me.avatar)

    await ctx.reply(embed=embed_arg)


async def setup(bot: Bot):
    bot.add_command(commands)
