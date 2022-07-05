from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands import Cog, Bot


class Languages(Cog):
    languages = []

    def __init__(self, bot):
        file = open("./supported_languages.txt")

        self.languages = file.read().split("\n")

        file.close()

        self.bot = bot

    @commands.command(help="Send my supported languages")
    async def languages(self, ctx: Context):
        embed_arg = Embed(
            title="My supported languages",
            description=", ".join(self.languages),
            color=255
        ).set_author(
            name=ctx.bot.user.name,
            icon_url=ctx.bot.user.avatar_url
        )

        await ctx.send(embed=embed_arg)


def setup(bot: Bot):
    bot.add_cog(Languages(bot))
