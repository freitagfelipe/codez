# [CodeZ](http://gg.gg/codez-bot)

- This is a Discord Bot that serves as a compilation and interpretation method inside Discord Chat. It receives your code as a chat text and does the compilation/interpretation of it, delivering the correspondent output.

## How CodeZ was made

- CodeZ is written in Python, using [Discord.py](https://discordpy.readthedocs.io/en/stable/) lib to communicate with Discord API and other libs like:
    - [Pyston](https://github.com/ffaanngg/pyston)
    - [Dotenv](https://pypi.org/project/python-dotenv/)

## How to host

1. Go in [Discord applications](https://discord.com/developers/applications).
2. Create a new application with send messages permission and save the bot token.
3. Download this repository.
4. In your repository folder open a terminal and type pip install -r requirements.txt
5. Create a .env file and paste it inside:
    1. TOKEN=<YOUR-DISCORD-BOT-TOKEN>
6. Create a [Heroku](https://heroku.com) account.
7. Create a new app in Heroku.
8. Deploy this repository using Github or Heroku CLI.
9. Set the bot token in Heroku's eviroment variables.

**Don't share your keys with anyone!**

## Commands help

#### .command
- Description: explain how to use .run
- Usage: .command

#### .run
- Description: 
- Usage:
    1. If you don't have inputs:
        .run
        ```language
            //your code
        ```
    2. If you have inputs:
        .run
        ```language
            //your code
        ```
        Input1
        Input2
        ...
        InputN