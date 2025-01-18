import os
import httpx
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_fixed
import logging
from typing import List

load_dotenv()
TELEGRAM_BOT_TOKEN = "8122445200:AAF6Kh0kqdQyS-y-Y1wfrQ_6EsxiaiVCNVU"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Caught u lacking, what do you want')

def notes(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Do it yourself la')

def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("notes", notes))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()