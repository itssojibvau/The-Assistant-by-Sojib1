from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = '7759471885:AAFYcPoiPYm4Hoh4lUKgm7XQRUYdl_0olHA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(lambda message: message.text and message.text.lower().startswith('@'))
async def menu(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton("1. 9proxy", callback_data='9proxy'),
        types.InlineKeyboardButton("2. Tellabot", callback_data='tellabot'),
        types.InlineKeyboardButton("3. Mail Panel", callback_data='mail_panel'),
        types.InlineKeyboardButton("4. Coinbase Link", callback_data='coinbase'),
    )
    await message.reply("🔘 Choose an option:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    info = {
        '9proxy': "🔐 *9Proxy Info:*\n`Mail/Username: example@gmail.com`\n`Password: your-password`",
        'tellabot': "🤖 *Tellabot Info:*\n`Link: https://www.tellabot.com/`\n`Mail: example@mail.com`\n`Pass: your-password`",
        'mail_panel': "📧 *Mail Panel Info:*\n`Link: https://www.emailnator.com/`\n`Mail: example@gmail.com`\n`Pass: your-password`",
        'coinbase': "💰 *Coinbase Link:*\n`https://trl.cldtraflink.com/click?pid=3601&offer_id=2446`"
    }

    text = info.get(data, "❌ Unknown Option!")
    await bot.send_message(callback_query.from_user.id, text, parse_mode="Markdown")
    await callback_query.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
