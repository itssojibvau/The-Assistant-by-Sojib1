from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = '7759471885:AAFYcPoiPYm4Hoh4lUKgm7XQRUYdl_0olHA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# === Editable Info Variables ===
proxy_email = "sojibali816@gmail.com"
proxy_password = "Sojib.12#@"

tellabot_email = "Ziaull000.6"
tellabot_password = "12Ww12wq#@"

mail_panel_email = "sojibali816@gmail.com"
mail_panel_password = "FfFLZ7.j#7nYigf"

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
        await message.reply("🔘 *Choose an option:*", reply_markup=keyboard, parse_mode="Markdown")

# === Respond to button clicks ===
@dp.callback_query_handler(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data

    if data == '9proxy':
        text = (
            f"🔐 *9Proxy Info:*\n"
            f"`Mail/Username: {sojibali816@gmail.com}`\n"
            f"`Password: {Sojib.12#@}`"
        )

    elif data == 'tellabot':
        text = (
            f"🤖 *Tellabot Info:*\n"
            f"`Link: https://www.tellabot.com/`\n"
            f"`Mail/Username: {Ziaull000.6}`\n"
            f"`Password: {12Ww12wq#@}`"
        )

    elif data == 'mail_panel':
        text = (
            f"📧 *Mail Panel Info:*\n"
            f"`Gmailnator Link: https://www.emailnator.com/`\n"
            f"`Mail/Username: {sojibali816@gmail.com}`\n"
            f"`Password: {FfFLZ7.j#7nYigf}`"
        )

    elif data == 'coinbase':
        text = (
            "💰 *Coinbase Link:*\n"
            "`Link 1: https://trl.cldtraflink.com/click?pid=3601&offer_id=2446`"
        )

    else:
        text = "❌ Unknown Option!"

    # Send reply to the same group
    await bot.send_message(callback_query.message.chat.id, text, parse_mode="Markdown")
    await callback_query.answer()

# === Start polling ===
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
