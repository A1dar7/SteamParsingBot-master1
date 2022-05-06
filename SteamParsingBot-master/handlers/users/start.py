from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline import start_button
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Я бот, который может помочь тебе с покупками в Торговой площадке стима\n"
                         f"На данный момент я могу искать, разбирать просмотреть ссылки и искать только в игре Dota 2\n"
                         f"БОТ находится в разработке и скоро буду уметь гораздо больше\n"
                         f"Если заметили ошибку или у вас есть идеи для пишите их @username_", reply_markup=start_button.BotOnStart)
