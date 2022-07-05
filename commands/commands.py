from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands import Cog, Bot


class Commands(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Send a list of all my commands")
    async def commands(self, ctx: Context):
        description_arg = ".commands\
            \n.execute\
            \n.help\
            \n.languages\
            \n.usage"

        embed_arg = Embed(
            title="My commands",
            description=description_arg,
            color=255
        ).set_author(
            name=ctx.bot.user.name,
            icon_url=ctx.bot.user.avatar_url
        )

        await ctx.send(embed=embed_arg)


def setup(bot: Bot):
    bot.add_cog(Commands(bot))
