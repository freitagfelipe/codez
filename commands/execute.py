from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands import Cog, Bot
from pyston import PystonClient, File


class Execute(Cog):
    PISTON = PystonClient()
    languages = []

    def __init__(self, bot):
        file = open("./supported_languages.txt")

        self.languages = file.read().split("\n")

        file.close()

        self.bot = bot

    async def execute_code(self, arguments: dict[str, str]) -> str:
        output = await self.PISTON.execute(
            arguments["language"],
            [File(arguments["code"])],
            stdin=arguments["inputs"]
        )

        if output.success:
            return output.run_stage.output

        if output.compile_stage and output.compile_stage.output:
            return output.compile_stage.output

        return output.run_stage.output

    def format_code(self, arguments: list) -> dict[str, str]:
        args: list[str] = []

        match arguments:
            case [_, *code]:
                args = code

        index = args.index("```")

        code, inputs = args[:index], args[index + 1:]

        if inputs == []:
            inputs = ""

        return {"code": "\n".join(code), "inputs": "\n".join(inputs)}

    @commands.command(help="Execute a code")
    async def execute(self, ctx: Context, language: str, *, execution: str):
        if "```" in language:
            await ctx.send('Incorrect usage of execute command! See ".usage".')

            return

        try:
            arguments: dict[str, str] = self.format_code(execution.split("\n"))
            arguments["language"] = language.lower()

            if not arguments["language"] in self.languages:
                raise Exception("Unsupported language!\
                    See .languages for a list of my supported languages.")

            arguments["output"] = await self.execute_code(arguments)
            arguments["end"] = "---Your output finish here!---"
            arguments["inputs"] = arguments["inputs"] or None

            description_arg = "The language is: {language}\n\n\
                Your code:\n```{language}\n{code}```\n\
                Your input: ```{inputs}```\nYour output:\n\
                ```\n{output}{end}```".format(**arguments)

            embed = Embed(
                title="Here is your output!",
                description=description_arg,
                color=255
            ).set_author(
                name=ctx.bot.user.name,
                icon_url=ctx.bot.user.avatar_url
            )

            await ctx.send(embed=embed)
        except IndexError:
            await ctx.send(
                "Not enough arguments! See .usage command."
            )
        except Exception as error:
            await ctx.send(error)


def setup(bot: Bot):
    bot.add_cog(Execute(bot))
