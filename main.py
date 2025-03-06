import asyncio
import logging
import sys
from os import getenv
import os
import importlib.util
import json

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


dp = Dispatcher()


def import_all_utils(directory: str) -> None:
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            with open(directory + "/" + filename, "r") as IF:
                exec(IF.read())
            print(f"Imported {filename}")
    return
def prefix_command(prefix, command):
    async def filter(message: Message):
        if message.text and message.text.startswith(prefix + command):
            return True
        return False
    return filter


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN)
    
    # And the run events dispatching
    await dp.start_polling(bot)
    return


if __name__ == "__main__":
    # should be kinda /path/to/config.json
    configPath = getenv("CONFIG")
    with open(configPath, "r") as IF:
        CONFIG = json.load(IF)

    TOKEN = CONFIG["TOKEN"]
    CMD_PREFIX = CONFIG["CMD_PREFIX"]

    # import all utils
    import_all_utils("CR_Utils")

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

