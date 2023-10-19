from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import openai
import os
import sys

class Reference:
    def __init__(self) -> None:
        self.response=""

load_dotenv()
openai.api_key=os.getenv("OpenAI_API_KEY")

reference=Reference()
TOKEN=os.getenv('Token')

MODEL_NAME='gpt-3.5-turbo'

bot=Bot(token=TOKEN)
dispatcher=Dispatcher(bot)

def clear_past():
    reference.response=''

@dispatcher.message_handler(commands=['start'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    await message.reply("hii my name is arjun's servent and\n what is your name and \n plz add '/' before your name:-")


@dispatcher.message_handler(commands=['anuj'])
async def command(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    await message.reply("you are chutiya")


# c=1
# for i in range(c):
#     @dispatcher.message_handler()
#     async def command_start_handler(message: types.Message):
#         """
#         This handler receives messages with `/start` command
#         """
#         await message.reply("nice to meet u ")




@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    clear_past()
    await message.reply("hii claearsd succeffuly")



@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    helpercc='''
    /start
    /stop
    /clear'''
    await message.reply(helpercc)


# @dispatcher.message_handler()
# async def chat(message: types.Message):
#     """
#     This handler receives messages with `/start` command
#     """
#     clear_past()
#     await message.answer()

@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    print(f">>> USER: \n\t{message.text}")
    response=openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {'role':'assistant','content':reference.response},
            {'role':'user','content':message.text}
        ]
    )
    reference.response=response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id=message.chat_id,text=reference.response)



if __name__=="__main__":
    executor.start_polling(dispatcher,skip_updates=True)