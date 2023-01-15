import discord
import config
from trading_commands import on_message, on_ready

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

total_trades = 0
winning_trades = 0
losing_trades = 0
total_profit = 0

@client.event
async def on_ready():
    await on_ready()
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    await on_message(message)

client.run('YOUR_TOKEN_HERE')
