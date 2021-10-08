import discord

async def command(message, self):
    embed = discord.Embed(
        title = "I only have one command other than the one you just used!",
        description = "You can use this command as follows!",
        color = 255
    ).set_author(name = self.user.name, icon_url = self.user.avatar_url).set_image(url = "https://raw.githubusercontent.com/freitagfelipe/codez/main/medias/usageExample.png")

    return await message.channel.send(embed = embed)