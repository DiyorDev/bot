
import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1977994218:AAEjVP5XSBCv5wLvhFAb7_wmQ0IceIACiWo'
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Bu handler foydalanuvchi "/start" yoki "/help" buyrug'ini yuborganida chaqiriladi
    """
    await message.reply("Wikipedia botiga xush kelibsiz.")



@dp.message_handler()
async def echo(message: types.Message):                 
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
