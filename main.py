import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Insert your OpenAI key and Telegram Bot token
openai.api_key = 'YOUR_OPENAI_API_KEY'
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Logging for debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# GPT function
async def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4 if you have access
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    return response.choices[0].message['content'].strip()

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    reply = await chat_with_gpt(user_message)
    await update.message.reply_text(reply)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Yo! I'm alive. Ask me anything.")

# Run bot
if _name_ == '_main_':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
