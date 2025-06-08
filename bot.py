import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# Главное меню
async def send_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🍽️ Блюда", callback_data="food")],
        [InlineKeyboardButton("💆 Услуги", callback_data="service")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await update.callback_query.edit_message_text("Меню любви 💖", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Меню любви 💖", reply_markup=reply_markup)

# Обработчик кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "menu":
        await send_menu(update, context)
    elif data == "food":
        await query.edit_message_text(
            text="🍽️ **Блюда**\n\n1. Завтрак — 3 поцелуя\n2. Ужин — 5 поцелуев",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="menu")]])
        )
    elif data == "service":
        await query.edit_message_text(
            text="💆 **Услуги**\n\n1. Массаж — 7 объятий\n2. Песенка на ушко — 4 поцелуя",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="menu")]])
        )

# Стартовая команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_menu(update, context)

# Запуск бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Бот запущен 🦾")
    app.run_polling()

