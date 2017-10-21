from discord.ext import commands


class Watchafaboulas:
    def __init__(self, Human_Boi):
        self.Human_Boi = Human_Boi


    @commands.command(name= "ping")
    async def ping(self, ctx):
        await ctx.send("pong")
def setup(Human_Boi):
    Human_Boi.add_cog(Watchafaboulas(Human_Boi))