from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = '7759471885:AAFYcPoiPYm4Hoh4lUKgm7XQRUYdl_0olHA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# === Trigger when bot is mentioned in a group ===
@dp.message_handler(lambda message: message.text and '@the_assistant_by_sojib_bot' in message.text.lower())
async def menu(message: types.Message):
    if message.chat.type in ['group', 'supergroup']:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton("1️⃣ 9Proxy", callback_data='9proxy'),
            types.InlineKeyboardButton("2️⃣ Tellabot", callback_data='tellabot'),
            types.InlineKeyboardButton("3️⃣ Mail Panel", callback_data='mail_panel'),
            types.InlineKeyboardButton("4️⃣ Coinbase Link", callback_data='coinbase'),
        )
        await message.reply("🔘 *একটি অপশন বাছাই করুন:*", reply_markup=keyboard, parse_mode="Markdown")

# === Button click handler — reply in group ===
@dp.callback_query_handler(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data

    if data == '9proxy':
        text = (
            "*🔐 9Proxy Info:*\n"
            "Mail/Username: `sojibali816@gmail.com`\n"
            "Password: `Sojib.12#@`"
        )

    elif data == 'tellabot':
        text = (
            "*🤖 Tellabot Info:*\n"
            "Link: `https://www.tellabot.com/`\n"
            "Mail/Username: `Ziaull000.6`\n"
            "Password: `12Ww12wq#@`"
        )

    elif data == 'mail_panel':
        text = (
            "*📧 Mail Panel Info:*\n"
            "Gmailnator Link: `https://www.emailnator.com/`\n"
            "Mail/Username: `sojibali816@gmail.com`\n"
            "Password: `FfFLZ7.j#7nYigf`"
        )

    elif data == 'coinbase':
        text = (
            "*💰 Coinbase Link:*\n"
            "Link 1: `https://trl.cldtraflink.com/click?pid=3601&offer_id=2446`"
        )

    else:
        text = "❌ Unknown Option!"

    # ✅ Send reply in the same group (NOT inbox!)
    await bot.send_message(callback_query.message.chat.id, text, parse_mode="Markdown")
    await callback_query.answer()
    
# === Start polling ===
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
