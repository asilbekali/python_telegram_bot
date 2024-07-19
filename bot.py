from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = "7332270069:AAHEq2CwApGgDbYz4ff-BdVrtvirVAlPOjI"

BOT_USERNAME: Final = "@dvlsjvjhdklfjnvlkjdnfv_bot"


#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom ramhat bizni botni tanlaganiz uchun")



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bu bot sinov uchun yaratildi")



async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pythonda yaratilgan bot")

#responses

def handle_responses(text: str):
    processed: str = text.lower()

    if 'hello' in processed:
        return 'salom'
    if 'qalaysan' in processed:
        return 'yaxshi'
    else:
        return 'nima istavosan mandan'



async def handle_massage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text 

    print(f"\nUser name: {update.message.chat.first_name}\nUser id: {update.message.chat.id}\nMessage type: {message_type}: {text}")

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            responses: str = handle_responses(new_text)
        else:
            return
    else:
        responses: str = handle_responses(text)

    print('Bot:', responses)
    await update.message.reply_text(responses)



async def erorr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update: {update} error {context.error}')


if __name__ == '__main__':
    print('Start...')
    app = Application.builder().token(TOKEN).build()
    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_massage))

    #ERRORS
    app.add_error_handler(erorr)

    #Polling
    print("Polling...")
    app.run_polling(poll_interval=3)










