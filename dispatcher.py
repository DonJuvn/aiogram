from main import bot, dp
from config import id

from aiogram.types import Message
from config import id
async def send_to_admin(dp):
    await bot.send_message(chat_id = id, text = 'Hey, lets answer some questions!')