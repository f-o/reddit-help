from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests


def price(update: Update, context: CallbackContext) -> None:

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
    update.message.reply_text(f'The price is: {price} USD')


updater = Updater('TOKEN HERE')

updater.dispatcher.add_handler(CommandHandler('price', price))

updater.start_polling()
updater.idle()