import os
import logging
from dotenv import load_dotenv
from telebot import TeleBot, types

# Load environment variables from .env file
load_dotenv()

# Get the API token from the environment variable
TOKEN = os.getenv('TELEGRAM_API_KEY')

# Check if the TOKEN is available
if not TOKEN:
    raise ValueError("No API Key found. Please set the TELEGRAM_API_KEY environment variable.")

# Initialize the bot with the token
BOT = TeleBot(TOKEN)

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

logger.info('Bot is starting...')

# Handler for the /start command and "start bot" message
@BOT.message_handler(commands=['start'])
@BOT.message_handler(func=lambda message: message.text.lower() == 'start bot')
def start(message):
    # Set the bot's command list
    BOT.set_my_commands([
        types.BotCommand("/start", "Start the bot"),
    ])

    # Create a reply keyboard with a single button
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [types.KeyboardButton(text) for text in ['start bot']]
    markup.add(*buttons)

    # Send a welcome message with the keyboard
    start_text = 'BOT Started! 😁'
    BOT.send_message(message.chat.id, start_text, reply_markup=markup)

if __name__ == "__main__":
    try:
        BOT.polling(non_stop=True)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
