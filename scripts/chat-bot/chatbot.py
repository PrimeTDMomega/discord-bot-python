import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as', client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    welcome_message = f'Welcome to the server, {member.mention}!'
    await member.guild.default_channel.send(welcome_message)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the permission to use this command.')
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('Missing required argument.')

client.run('YOUR_BOT_TOKEN')
