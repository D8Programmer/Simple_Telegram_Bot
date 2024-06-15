# <p align="center" style="padding: 0; margin: 0;"> Telegram Bot Project </p>

This project provides a basic Telegram bot implementation designed to help others create and understand Telegram bots. The bot responds to the `/start` command and the message "start bot", offering a simple interactive experience.

## Features 🎉
- Responds to the `/start` command
- Responds to the message "start bot"
- Sends a welcome message with a custom keyboard

## Installation Requirements 📦

To install the required packages, run the following command:

```sh
pip install -r requirements.txt
```

## Setup 🛠️

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/telegram-bot.git
   cd telegram-bot
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**

   Create a `.env` file in the root of your project and add your Telegram API key:
   ```dotenv
   TELEGRAM_API_KEY='your_telegram_api_key'
   ```

5. **Run the bot**
   ```sh
   python bot.py
   ```

## Code Explanation 🧩

- **Environment Variables:** The `dotenv` package loads environment variables from a `.env` file, keeping sensitive information like the API key secure.

- **Bot Initialization:** The bot is initialized using the `TeleBot` class from the `telebot` package, with the API key retrieved from environment variables.

- **Logging:** Basic logging is configured to monitor the bot's activity and log any errors.

- **Command Handling:** The bot listens for the `/start` command and messages containing "start bot", responding with a custom keyboard and a welcome message.

- **Polling:** The bot starts polling for new messages, with any exceptions logged for debugging purposes.

## Additional Resources 📚

- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [pyTelegramBotAPI Documentation](https://github.com/eternnoir/pyTelegramBotAPI)

---

<p align="center">For any questions or further assistance, feel free to reach out.</p>