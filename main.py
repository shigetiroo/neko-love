import discord, os, json, datetime
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime
from discord_components.client import DiscordComponents
from discord_components import *
now = datetime.now()
intents = discord.Intents().all()
intents.members = True

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)
PREFIX=config["prefix_settings"]["prefix"]      # The Prefix for the Bot, change it in config.json
STATUS1=config["status1"]                       # Rich Presence Status 1, you can add or delete as many of these as shown below, just add them in config.json aswell
STATUS2=config["status2"]                       # Same here
TOKEN = config["token"]                         # The Token from your Bot, add it in config.json
if config["prefix_settings"]["use_space"] == True: # If in config.json use_space is set to true, this is the called function
    prefix = PREFIX + ' '


client = commands.Bot(command_prefix = PREFIX, help_command = None, intents = intents)

status = cycle([STATUS1,STATUS2]) # Funktion for cycling the Rich Presence Statuses

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.", delete_after=5) # If the command is nonexistend, the Bot will send a message and delete it after 5 Seconds

@client.event
async def on_ready():
    with open('./config.json', 'r') as cjson:
        config = json.load(cjson)
    PREFIXX=config["prefix_settings"]["prefix"]
    change_status.start()
    current_time = now.strftime("%H:%M:%S")
    print('-----------------------------------\nLogged in as: {0.user}'.format(client),f'\nPrefix => {PREFIXX}', '\nLogged in at', current_time, '\nID of the Client =', client.user.id,f'\nConnected to {len(client.guilds)} servers!', '\n------------------------------------') # Printing some Info about the Bot in your Console
    DiscordComponents(client)
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(next(status))) # Function called for cycling the Rich Presence
    #await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name=str(len(client.guilds)) + ' Servers.')) # Remove the hashtag in front to just display on how many Servers the Bot is currently on (Also add a hashtag in front of the other client.change function above) 

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(next(status))) # Function to change the Rich Presence Statuses

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
client.run(TOKEN)