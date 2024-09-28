# from aiogram.types import LabeledPrice, Message, PreCheckoutQuery, ContentType, ShippingQuery, ShippingOption
# from aiogram.dispatcher.filters import Command
# from botscript import src
# from botscript.src.bot import bot, dp
import asyncio

from botscript.src.config import Config
from pyrogram import Client, filters
from botscript.src.messages import MESSAGES

app = Client(name='my_account', api_id=Config.api_id, api_hash=Config.api_hash)


async def message_handler(client_obj):
    print(1)
    await asyncio.sleep(5)
    print(2)
    await client_obj.read_history()
    # print(3)
    # await asyncio.sleep(3)
    # print(4)
    # await client_obj.sern_chat_action(message_obj.chat.id, "typing")
    # print(5)
    # await asyncio.sleep(10)
    # await client_obj.send_message(message_obj.chat.id, text)


@app.on_message(filters=filters.private)
async def text_handler(event, message, client_obj):
    if message.from_user.id == (await app.get_me()).id:
        pass
    else:
        await app.send_message(chat_id=message.chat.id, text=MESSAGES['start'])

app.run()


# @dp.message_handler(Command('start'))
# async def start(message: Message):
#     await bot.send_message(message.chat.id, 'hi')