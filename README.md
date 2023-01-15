This is a branch for another person to check out, if your here to learn to make a discord bot ignore this, go [here](https://github.com/PrimeTDMomega/discord-bot-python/).
If you dont want re-structure ↓↓↓↓↓↓
```
import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

total_trades = 0
winning_trades = 0
losing_trades = 0
total_profit = 0
contract_cost = 75

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    global total_trades, winning_trades, losing_trades, total_profit, contract_cost
    if "BTO" in message.content:
        total_trades += 1
        # Extract the contract cost from the message
        cost_index = message.content.index("@")
        if cost_index != -1:
            contract_cost = float(message.content[cost_index + 1:])
        # Subtract the contract cost
        total_profit -= contract_cost
        await message.channel.send(f'You just bought an option contract for ${contract_cost}. Your current profit is ${total_profit}.')
    elif "STC" in message.content:
        total_trades += 1
        cost_index = message.content.index("@")
        if cost_index != -1:
            sell_cost = float(message.content[cost_index + 1:])
            if sell_cost > contract_cost:
                winning_trades += 1
                total_profit += sell_cost - contract_cost
                await message.channel.send(f'Congratulations, you just made a winning trade! You sold an option contract for ${sell_cost}. Your current profit is ${total_profit}.')
            else:
                losing_trades += 1
                total_profit += sell_cost - contract_cost
                await message.channel.send(f'Sorry, you just lost a trade. You sold an option contract for ${sell_cost}. Your current profit is ${total_profit}.')
    elif message.content == '!stats':
        await message.channel.send(f'Total trades: {total_trades} \n Winning trades: {winning_trades} \n Losing trades: {losing_trades} \n Total profit: ${total_profit}')

client.run('YOUR_TOKEN_HERE')
```
