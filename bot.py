import discord
from discord.ext import commands
import os

# Bot Prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# List of cogs to load, you might have more based on your project structure
initial_extensions = ['cogs.game', 'cogs.management', 'cogs.community']

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I can't find that command. Try !help for a list of commands.")
    else:
        raise error

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', e)

    bot.run('YOUR_TOKEN_HERE')