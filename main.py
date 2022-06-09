from telegram import *
from telegram.ext import *
from bs4 import BeautifulSoup
from PIL import Image
import requests
import os

API_KEY = "5492549254:AAH0MMsSKCI2-y_QvxdTaqEDVVAVlddZFpo"
print("Bot started")

def start_command(update, context):
    buttons = [
        [
            KeyboardButton("Button 1")
        ],
        [
            KeyboardButton("Button 2")
        ],
        [
            KeyboardButton("person")
        ]
    ]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Choose an option",
        reply_markup = ReplyKeyboardMarkup(buttons)
        )

def help_command(update, context):
    update.message.reply_text("I can help you with your daily tasks")

def message_handler(update, context):
    text = str(update.message.text).casefold()

    if "button 1" in text:
        update.message.reply_text("Button 1 pressed")
    elif "button 2" in text:
        update.message.reply_text("Button 2 pressed")
    elif "person" in text:
        url = "https://thispersondoesnotexist.com/"
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        image = Image.open(requests.get("https://thispersondoesnotexist.com" + soup.find("img")["src"], stream=True).raw)
        
        path = os.getcwd() + "\Telegram Bot\images\image.jpg"
        image.save(path)
        update.message.reply_photo(photo=open(path, "rb"))
        os.remove(path)
        
        update.message.reply_text("Image Sent and Removed.")

    #response = responses.basic_responses(text)
    #update.message.reply_text(response)

def error_handler(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()

main()
