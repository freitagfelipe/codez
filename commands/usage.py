from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands import Cog, Bot
from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")


class Usage(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Send a how to use execute command image")
    async def usage(self, ctx: Context):
        url_arg = getenv("CONTENT_URL")

        embed_arg = Embed(
            title="How to use execute command",
            color=255
        ).set_author(
            name=ctx.bot.user.name,
            icon_url=ctx.bot.user.avatar_url
        ).set_image(
            url=url_arg
        )

        await ctx.send(embed=embed_arg)


def setup(bot: Bot):
    bot.add_cog(Usage(bot))
