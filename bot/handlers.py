import telebot
import threading
from django.conf import settings
from bot.services.ai_logic import get_ai_response

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Salom! Men AI yordamchi botman.\nMenga savol yozing — men sizga sun’iy intellekt yordamida javob beraman!"
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    threading.Thread(target=process_message, args=(message,)).start()

def process_message(message):
    user_text = message.text
    user_id = message.chat.id
    ai_reply = get_ai_response(user_id, user_text)
    bot.reply_to(message, ai_reply)
