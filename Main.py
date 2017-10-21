import discord
from discord.ext import commands

extension = (
    'cogs.Watchafaboulas'
)

Human_Boi = commands.Bot(command_prefix='*')

def main():
    @Human_Boi.event
    async def on_ready():
        print(f'\nLogged in as {Human_Boi.user.name} (ID: {Human_boi.user.id})')
        print(f'Connected to {str(len(set(lambdabot.get_all_members())))} users')
        print(f'Version: {discord.__version__}')
        print('-' * 20)
    
    for extension in extensions:
        try:
            Human_Boi.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension: {extension}\n{e}')
        else:
            print(f'Successfully loaded extension: {extension}')

        Human_Boi.run(token)


if __name__ == '__main__':
    main()
