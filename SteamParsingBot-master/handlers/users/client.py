import logging
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from keyboards.inline import ConfirmData
from keyboards.inline import Choice_country

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
    if message.text.lstrip("-").isdigit():
        if float(message.text) <= 0:
            await message.answer('Цена должна быть больше 0!\nПовторите ввод')
        else:
            price = float(message.text)
            await state.update_data(Price=price)
            await New_Item.next()
            await message.answer('Выберите страну', reply_markup=Choice_country.choice_country)
    else:
        await message.answer('Только числа чувак')


@dp.callback_query_handler(Choice_country.Country.filter(), state=New_Item.Country)
async def to_sho_country(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    strana = callback_data['country']
    await state.update_data(Сountry=strana)
    card_data = await state.get_data()
    await call.message.answer(card_data, reply_markup=ConfirmData.confirm_data)
    logging.info(card_data)
    await New_Item.next()


@dp.callback_query_handler(text='confirm_data', state=New_Item.Confirm)
async def confirm(call: types.CallbackQuery, state: FSMContext):
    await call.answer('Понял, принял')
    await call.message.answer('Выполнено, ожидайте оповещения!')
    await state.reset_state()


@dp.callback_query_handler(text='reset_data', state=New_Item.Confirm)
async def confirm(call: types.CallbackQuery, state: FSMContext):
    await New_Item.New_item.set()
    await call.message.answer('Send link')
