import os
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Bot


@commands.hybrid_command(with_app_command=True)
async def usage(ctx: Context):
    url_arg = os.environ["CONTENT_URL"]

    embed_arg = (
        Embed(title="How to use execute command", color=255)
        .set_author(name=ctx.me.name, icon_url=ctx.me.avatar)
        .set_image(url=url_arg)
    )

    await ctx.reply(embed=embed_arg)


async def setup(bot: Bot):
    bot.add_command(usage)
