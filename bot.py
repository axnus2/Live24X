from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from stream import start_stream, stop_stream, get_hls_url

TOKEN = "YOUR_BOT_TOKEN"

def go(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text("Usage: /go <HLS_URL>")
        return
    input_hls = context.args[0]
    start_stream(input_hls)
    update.message.reply_text(f"Streaming started from {input_hls}")

def stop(update: Update, context: CallbackContext):
    stop_stream()
    update.message.reply_text("Stream stopped")

def url(update: Update, context: CallbackContext):
    hls = get_hls_url()
    if hls:
        update.message.reply_text(f"HLS URL: {hls}")
    else:
        update.message.reply_text("No stream running currently.")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("go", go))
updater.dispatcher.add_handler(CommandHandler("stop", stop))
updater.dispatcher.add_handler(CommandHandler("url", url))

updater.start_polling()
updater.idle()
