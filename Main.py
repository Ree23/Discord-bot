import discord
from discord.ext import commands

extensions = (
    "cogs.Watchafaboulas"
)
Human_Boi = commands.Bot(command_prefix=("*"))


def main():
    @Human_Boi.event
    async def on_ready():
        print("logged in as {},id = {}".format(Human_Boi.user.name, Human_Boi.user.name))
        print("Users Connected {}.".format(str(len(set(Human_Boi.get_all_members())))))

    for extension in extensions:
        try:
            Human_Boi.load_extension(extension)
        except Exception as e:
            print('Failed to load extension: {}\n{}'.format(extension, e))
        else:
            print('Successfully loaded extension: ({})'.format(extension))
        Human_Boi.run("""put token here""")


if __name__ == '__main__':
    main()
