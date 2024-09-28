import asyncio
from botscript.src.services import DataBase
from botscript.src.config import Config
from pyrogram import Client, filters, enums
from botscript.src.messages import MESSAGES, MESSAGES2, MESSAGES3
import re
from datetime import date
import pyromod


db = DataBase('auto.db')
app = Client(name='my_account', api_id=Config.api_id, api_hash=Config.api_hash)
today = date.today()
pattern1 = '^[0-9]{1}[0-9]{1}.[0-1]{1}[0-9]{1}.[1,2]{1}[0-9]{3}$'
pattern2 = '^[2]{1}[0]{1}[2]{1}[3-9]{1}-[0-1]{1}[0-9]{1}-[0-9]{1}[0-9]{1}$'

async def check_string(s, pattern):
    if re.fullmatch(pattern, s):
        return True
    else:
        return False


async def message_handler(client, message, time_sleep, time_typing):
    print(1)
    await asyncio.sleep(time_sleep)
    await app.read_chat_history(chat_id=message.chat.id)
    await asyncio.sleep(3)
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    await asyncio.sleep(time_typing)


async def commands(client, message):
    if message.text == '/stopp':
        await client.answer()
    elif message.text == '/статистика':
        date_st = (await client.ask(message.chat.id, 'напишите дату, по которой вас интересует статистика, '
                                                     'в формате год-месяц-день\nнапример:2023-12-25')).text
        if await check_string(date_st, pattern2):
            st = await db.get_statistics(date_st)
            amount = 0
            for i in st:
                amount += 1
            await app.send_message(message.chat.id, f'уникальных пользователей за {date_st}: {amount}')
        else:
            await app.send_message(message.chat.id, 'неверный формат даты')
    elif message.text == '/рассылка':
        spam_text = (await client.ask(message.chat.id, 'напишите сообщение для рассылки')).text
        users = await db.get_users()
        for row in users:
            try:
                if int(row[0]) >= 18:
                    await app.send_message(row[1], spam_text)
            except:
                pass
        await app.send_message(message.chat.id, 'отправлено всем пользователям')
    elif message.text == '/stop':
        await db.update_switch(1, message.chat.id)

async def check_underage(client, message):
    date_of_birth = message.text
    date_of_birth = (date_of_birth.split('.'))
    day = int(date_of_birth[0])
    month = int(date_of_birth[1])
    year = int(date_of_birth[2])
    age = today.year - year - ((today.month, today.day) < (month, day))
    await db.update_age(age, message.chat.id)
    if age >= 18:
        if await db.get_greetings_status(message.chat.id) == (1,):
            await message_handler(client, message, 3, 5)
            await app.send_message(chat_id=message.chat.id, text=MESSAGES['greetings'])
        else:
            pass
        await message_handler(client, message, 1, 5)
        name = (await client.ask(message.chat.id, MESSAGES['get_name'])).text
        await db.update_name(name, message.chat.id)
        await app.read_chat_history(message.chat.id)
        await message_handler(client, message, 1, 30)
        print(2)
        await app.send_message(chat_id=message.chat.id, text=MESSAGES['message1'])
        print(3)
        for i in MESSAGES2:
            await message_handler(client, message, 1, 30)
            await app.send_message(chat_id=message.chat.id, text=i)
        await message_handler(client, message, 9, 30)
        await app.send_message(chat_id=message.chat.id, text=MESSAGES['message10'])
        for i in MESSAGES3:
            await message_handler(client, message, 1, 30)
            await app.send_message(chat_id=message.chat.id, text=i)
        await message_handler(client, message, 9, 30)
        await app.send_message(chat_id=message.chat.id, text=MESSAGES['message16'])
        await message_handler(client, message, 9, 30)
        await app.send_message(chat_id=message.chat.id, text=MESSAGES['message17'])

    else:
        await message_handler(client, message, 3, 5)
        await app.send_message(chat_id=message.chat.id, text=MESSAGES['underage'])


@app.on_message(filters.me & filters.command('continue', prefixes=['/']))
async def continue_sending(client, message):
    await app.send_message(chat_id=message.chat.id, text='gh')
    client.stop()


@app.on_message(filters=filters.private)
async def text_handler(client, message):
    print(message.text)
    if message.from_user.id == (await app.get_me()).id:
        await commands(client, message)
    else:
        try:
            await db.add_user(message.chat.id, message.chat.first_name, today)
        except:
            pass
        finally:
            if await db.get_switch_status(message.chat.id) == (0,):
                if await db.get_age(message.chat.id) != (0,):
                    pass
                else:
                    if await check_string(message.text, pattern1):
                        await check_underage(client, message)
                    else:
                        await message_handler(client, message, 3, 5)
                        await app.send_message(chat_id=message.chat.id, text=MESSAGES['get_date_of_birth'])
                        await db.update_greetings_status(user_id=message.chat.id)
            else:
                # await client.answer((await app.get_me()).id, 'stop')
                # print(12)
                while True:
                    if message.text == 'start':
                        print(1)
                        break




app.run()
