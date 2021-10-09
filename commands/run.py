import discord
from pyston import PystonClient, File

piston = PystonClient()

async def executeCode(arguments):
    output = await piston.execute(arguments["Language"], [File(arguments["Code"])], stdin = "\n".join(arguments["Inputs"]) if arguments["Inputs"] else "")
    output = output.raw_json["run"]["output"] if output.success == True else output.raw_json["compile"]["stderr"]

    return output

def separateString(message):
    message = message.split("```")
    message.pop(0)
    inputs = message.pop()
    message = message[0].split("\n")
    language = message.pop(0)
    code = "\n".join(message)

    if (inputs == ""):
        inputs = None
    else:
        inputs = inputs.split("\n")
        inputs.pop(0)

    return {"Language": language, "Code": code, "Inputs": inputs}

async def run(message, self):
    try:
        arguments = separateString(message.content)
        arguments["Output"] = await executeCode(arguments)

        embed = discord.Embed(
            title = "Here is your output!",
            description = "The language is: {Language}\n\nYour code:\n```{Language}\n{Code}```\nYour input: ```{Inputs}```\nYour output:\n```\n{Output}---Your output finish here!---```".format(**arguments),
            color = 255
        ).set_author(name = self.user.name, icon_url = self.user.avatar_url)

        return await message.channel.send(embed = embed)
    except:
        return await message.channel.send('Some error occurred! Please try again! If you have some doubt about how to use .run you can type ".command"!')