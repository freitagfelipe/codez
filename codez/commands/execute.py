from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands import Bot
from pyston import PystonClient, File


class Reason(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


async def execute_code(arguments: dict[str, str]) -> str:
    output = await execute_code.PYSTON.execute(
        arguments["language"], [File(arguments["code"])], stdin=arguments["inputs"]
    )

    if output.success:
        return output.run_stage.output

    if output.compile_stage and output.compile_stage.output:
        return output.compile_stage.output

    return output.run_stage.output


def format_code(arguments: list) -> dict[str, str]:
    args: list[str] = []

    match arguments:
        case [_, *content]:
            args = content

    count = sum(1 if "```" in arg else 0 for arg in args)

    if count == 0:
        raise Reason('Wrong command usage! See ".usage"!')
    elif count > 1:
        raise Reason('Make sure to do not insert more than two "```"! See ".usage".')

    index = args.index("```", 0)

    code, inputs = args[:index], args[index + 1 :]

    if inputs == []:
        inputs = ""

    if code == [] or code.count("") == len(code):
        raise Reason('You need to insert a code to execute! See ".usage".')

    return {"code": "\n".join(code), "inputs": "\n".join(inputs)}


@commands.command()
async def execute(ctx: Context, language: str, *, execution: str):
    if "```" in language:
        await ctx.send('Incorrect usage of execute command! See ".usage".')

        return

    try:
        arguments: dict[str, str] = format_code(execution.split("\n"))
        arguments["language"] = language.lower()

        if not arguments["language"] in execute.LANGUAGES:
            raise Reason(
                "Unsupported language! Use the languages command for a list of my supported languages."
            )

        arguments["output"] = await execute_code(arguments)
        arguments["end"] = "---Your output finish here!---"
        arguments["inputs"] = (
            arguments["inputs"].split("\n") if arguments["inputs"] else None
        )

        description_arg = "The language is: {language}\n\nYour code:\n```{language}\n{code}\n```\nYour input: \n```{inputs}```\nYour output:\n```\n{output}{end}```".format(
            **arguments
        )

        embed = Embed(
            title="Here is your output!", description=description_arg, color=255
        ).set_author(name=ctx.me.name, icon_url=ctx.me.avatar)

        await ctx.send(embed=embed)
    except IndexError:
        await ctx.send("Not enough arguments! See .usage command.")
    except Reason as error:
        await ctx.send(error)
    except Exception as error:
        print(error)

        await ctx.send("Something went wrong. Please try again later!")


with open("./utils/supported_languages.txt") as file:
    execute.LANGUAGES = file.read().split("\n")

execute_code.PYSTON = PystonClient()


async def setup(bot: Bot):
    bot.add_command(execute)
