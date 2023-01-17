from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Bot


@commands.hybrid_command(with_app_command=True)
async def about(ctx: Context):
    embed_arg = Embed(
        title="About",
        description="Created by: [Felipe Freitag](https://github.com/freitagfelipe)",
        color=255,
    ).set_author(name=ctx.me.name, icon_url=ctx.me.avatar)

    await ctx.reply(embed=embed_arg)


async def setup(bot: Bot):
    bot.add_command(about)
