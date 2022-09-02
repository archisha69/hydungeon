import discord, time
from discord.ext import commands

client = commands.Bot(command_prefix=".", case_insensitive=True)
oid = 705462972415213588

@client.event
async def on_ready(): print("o"); await client.change_presence(activity=discord.Game(name=".help", timestamps={"start": time.time()}))

@client.command()
async def load(ctx, *, arg1):
    if ctx.author.id == oid:
        try: client.load_extension(f'cogs.{arg1}'); await ctx.send("Loaded Cog"); print(f"[Cog] {ctx.author} loaded cog."); return
        except Exception as e: await ctx.send(e); print(f"[Cog] An unexpected error has occurred: {e}")

@client.command()
async def unload(ctx, *, arg1):
    if ctx.author.id == oid:
        try: client.unload_extension(f'cogs.{arg1}'); await ctx.send("Unloaded Cog"); print(f"[Cog] {ctx.author} unloaded cog."); return
        except Exception as e: await ctx.send(e); print(f"[Cog] An unexpected error has occurred: {e}")

@client.command()
async def reload(ctx, *, arg1):
    if ctx.author.id == oid:
        try: client.unload_extension(f'cogs.{arg1}'); client.load_extension(f'cogs.{arg1}'); await ctx.send("Reloaded Cog"); print(f"[log] {ctx.author} reloaded cog."); return
        except Exception as e: await ctx.send(e); print(f"[Cog] An unexpected error has occurred: {e}")
    
client.load_extension("cogs.dungeon")
client.load_extension("cogs.e")
client.run("imagine thinking i forgor the token here :skull:")



#6274772069207573652061726368
