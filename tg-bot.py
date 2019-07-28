from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import random
import os
import logging

class MyLogsHandler(logging.Handler):
    def emit(self, record):
        telegram_bot_information_token = os.environ['TELEGRAM_BOT_INFORMATION_TOKEN']
        chat_id_telegram_information = os.environ['CHAT_ID_TELEGRAM_INFORMATION']
        log_entry = self.format(record)
        bot_error = telegram.Bot(token=telegram_bot_information_token)
        bot_error.send_message(chat_id=chat_id_telegram_information, text=log_entry)

def echo_text(bot, update):
    chat_id = update.message.chat_id
    bot_answer = os.environ['STANDART_TEXT_PHRASE']
    update.message.reply_text(bot_answer)
        
def echo_photo(bot, update):
    chat_id = update.message.chat_id
    sticker_or_text = random.randint(0, 1)
    if sticker_or_text == 0:
        bot_answer_number = random.randint(0, len(list(list_answers)))
        bot_answer = list_answers[bot_answer_number]
        update.message.reply_text(bot_answer)
    else:
        bot_answer_number = random.randint(0, len(list(list_stickers)))
        bot_answer = list_stickers[bot_answer_number]
        bot.sendSticker(chat_id = chat_id, sticker = bot_answer)
    
def start(bot, update):
    update.message.reply_text(os.environ['START_PHARSE'])

if __name__ == '__main__': 
    telegram_token = os.environ['TELEGRAM_TOKEN']
    list_answers = os.environ['LIST_ANSWERS']
    list_stickers = os.environ['LIST_STICKERS']
    updater = Updater(telegram_token)
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    echo_handler = MessageHandler(Filters.text, echo_text)
    picture_handler = MessageHandler(Filters.video | Filters.photo | Filters.document | Filters.forwarded, echo_photo)
    dp.add_handler(echo_handler)
    dp.add_handler(picture_handler)

    updater.start_polling()
    updater.idle()
