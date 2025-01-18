import os
import httpx
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_fixed
import logging
from typing import List

load_dotenv()
TELEGRAM_BOT_TOKEN = "8192019759:AAHFGG-fMpIh-pj-gqALqJRd3CWeN7rOxTI"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Erm what the sigma??')

def split(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Do it yourself la')

def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("split", split))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()