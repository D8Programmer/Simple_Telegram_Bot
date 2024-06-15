# Telegram Bot

This repository contains the source code for a simple Telegram bot built using the `Telebot` librarie. The bot can handle basic commands and provide information about itself.

## Features

- **/start**: Start the bot and display a welcome message with a custom keyboard.
- **/about**: Display information about the bot.
- **/help**: Provide a list of available commands.
- Handles text commands through buttons in the custom keyboard.

## Prerequisites

To run this bot, you need to have Python installed on your system. You will also need to create a bot on Telegram and obtain an API key.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/D8Programmer/Simple_Telegram_Bot.git
    cd telegram-bot
    ```

2. **Create a virtual environment and activate it (optional but recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the project directory and add your Telegram API key:**

    ```plaintext
    # Replace with your actual Telegram API key obtained from BotFather
    TELEGRAM_API_KEY='your_actual_api_key_here'
    ```

## Usage

1. **Run the bot:**

    ```sh
    python bot.py
    ```

2. **Interact with the bot on Telegram:**

    - **/start**: Initializes the bot and displays a custom keyboard with options.
    - **/about**: Provides information about the bot.
    - **/help**: Lists available commands.

## Project Structure

```plaintext
telegram-bot/
│
├── bot.py            # Main script for the bot
├── .env              # Environment variables
├── requirements.txt  # Dependencies
└── README.md         # Project documentation
