import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN=os.getenv("TOKEN")
#print(API_TOKEN)

#configure logging
logging.basicConfig(level=logging.INFO)

#initializer bot and dispather
bot=Bot(token=API_TOKEN)
dispatcher=Dispatcher(bot)


@dispatcher.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    await message.reply("hii my name is arjun's servent")


@dispatcher.message_handler()
async def echo(message: types.Message):
    """
    This handler re
    """
    await message.answer(message.text)

if __name__=="__main__":
    executor.start_polling(dispatcher,skip_updates=True)