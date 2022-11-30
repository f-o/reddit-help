import discord
import requests

# instantiate a discord client
client = discord.Client()

@client.event
async def on_ready():
    print(f'You have logged in as {client}')

# called whether there is a message in the chat
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
        
    # if the message starts with "!crypto"
    if message.content.startswith('!price'):

        # Generating the URL with the id parameter
        coingecko = 'https://api.coingecko.com/api/v3/simple/price?ids=kuma-inu&vs_currencies=usd'

        # getting data from coingecko
        r = requests.get(url=coingecko)

        # converting data to json
        data = r.json()

        # Store the price in a variable
        price = data['kuma-inu']['usd']

        # Convert the scientific notation to a float with 12 decimal places
        price = format(price, '.12f')

        # sending the price to the chat
        await message.channel.send(f'The price is: {price} USD')

BOT_TOKEN = 'Token'
client.run(BOT_TOKEN)