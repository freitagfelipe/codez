from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Bot


@commands.hybrid_command(
    with_app_command=True, description="Send a list of all my commands"
)
async def commands(ctx: Context):
    commands = [
        "commands(has slash version) - send a list of all my commands",
        "execute - executes a given code",
        "languages(has slash version) - send my supported languages",
        "usage(has slash version) - send an image that teaches you how to use the execute command",
    ]

    embed_arg = Embed(
        title="My commands", description="\n".join(commands), color=255
    ).set_author(name=ctx.me.name, icon_url=ctx.me.avatar)

    await ctx.reply(embed=embed_arg)


async def setup(bot: Bot):
    bot.add_command(commands)
