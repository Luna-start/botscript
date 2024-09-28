# from aiogram import Bot, Dispatcher
#
# from config import Config
from handlers import app
import asyncio

# bot = Bot(token=Config.token)
# dp = Dispatcher(bot=bot)

# async def main():
    # from handlers import dp
    # from handlers import app
    # try:
    # #     await dp.start_polling()
    # app.run()
    # finally:
    #     await bot.session.close()

if __name__ == '__main__':
    app.run()
#     try:
#         asyncio.run(main())
#     except (KeyboardInterrupt, SystemExit):
#         print('Bot stopped')