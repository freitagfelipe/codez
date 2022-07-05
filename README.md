# [CodeZ](http://gg.gg/codez-bot)

- This is a Discord Bot that serves as a compilation and interpretation method inside Discord Chat. It receives your code as a chat text and does the compilation/interpretation of it, delivering the correspondent output.

## How CodeZ was made

- CodeZ is written in Python, using [Discord.py](https://discordpy.readthedocs.io/en/stable/) lib to communicate with Discord API and other libs like:
    - [Pyston](https://github.com/ffaanngg/pyston)
    - [Dotenv](https://pypi.org/project/python-dotenv/)

#### .commands
- Description: send a list of all my commands
- Usage: .commands

#### .execute
- Description: execute a code
- Usage: see .usage for more information about this command

#### .help
- Description: send a message with help about my commands
- Usage: .help or .help <command\>

#### .languages
- Description: send my supported languages
- Usage: .languages

#### .usage
- Description: send a how to use execute png
- Usage: .usage