from discord.ext import commands

class Watchafaboulas:
    def __init__(self, Human_Boi):
        self.Human_Boi = Human_Boi

    @commands.command(name='ping',
                      description="A command that will send the bot's latency.")
    async def ping(self, ctx):
        # ping
        await ctx.send(f"{self.Human_Boi.latency * 1000} ms of delay.')


def setup(Human_Boi):
    Human_Boi.add_cog(Watchafaboulas(Human_Boi))
