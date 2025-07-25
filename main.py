import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'YOUR_BOT_TOKEN_HERE'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Xush kelibsiz XJoineBot ga!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
