from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Bot


@commands.hybrid_command(
    with_app_command=True, description="Send my supported languages"
)
async def languages(ctx: Context):
    embed_arg = Embed(
        title="My supported languages",
        description=", ".join(languages.avaliables),
        color=255,
    ).set_author(name=ctx.me.name, icon_url=ctx.me.avatar)

    await ctx.send(embed=embed_arg)


with open("./utils/supported_languages.txt") as file:
    languages.avaliables = file.read().split("\n")


async def setup(bot: Bot):
    bot.add_command(languages)
