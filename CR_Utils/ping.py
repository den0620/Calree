@dp.message(prefix_command(CMD_PREFIX, "ping"))
async def cr_command_ping(message: Message) -> None:
    await message.reply("Pong!")
    return

