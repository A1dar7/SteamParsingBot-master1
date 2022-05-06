import logging
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from keyboards.inline import ConfirmData
from keyboards.inline.Select_country import select_country, Country

from states.new_item import New_Item


@dp.callback_query_handler(text='item', state="*")
async def add_item(call: types.CallbackQuery, state: FSMContext):
    await New_Item.New_item.set()
    await call.message.answer('Отправьте ссылку на предмет')


@dp.message_handler(state=New_Item.New_item)
async def get_link(message: types.Message, state: FSMContext):
    link = message.text.split('/')
    item = link[-1].partition('?')[0]
    await state.update_data(Предмет=item)
    await New_Item.next()
    await message.answer('Введите цену')


@dp.message_handler(state=New_Item.New_item_price)
async def get_price(message: types.Message, state: FSMContext):
    price = float(message.text)
    await state.update_data(Price=price)
    await New_Item.next()
    await message.answer('Выберите страну', reply_markup=seleсt_country)


@dp.callback_query_handler(Country.filter(), state=New_Item.Country)
async def to_sho_country(message: types.Message, state: FSMContext, callback_data: dict):
    print(callback_data['country'])
    card_data = await state.get_data()
    await message.answer(card_data, reply_markup=ConfirmData.confirm_data)
    logging.info(card_data)


@dp.callback_query_handler(text='confirm_data', state=New_Item.Confirm)
async def confirm(call: types.CallbackQuery, state: FSMContext):
    # await state.reset_state()
    await call.message.answer('Выполнено, ожидайте оповещения!')


@dp.callback_query_handler(text='reset_data', state=New_Item.Confirm)
async def confirm(call: types.CallbackQuery, state: FSMContext):
    await New_Item.New_item.set()
    await call.message.answer('Send link')
