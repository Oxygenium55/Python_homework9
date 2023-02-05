from aiogram import types
from loader import dp

total = 150
new_game = False

@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
    print(message)
    
    
    
@dp.message_handler(text=['help'])
async def mes_help(message: types.Message):
    await dp.bot.send_message(message.from_user.id, 'Бог поможет')
    
@dp.message_handler(commands=['new_game'])
async def mes_game(message: types.Message):
    global new_game
    new_game = True
    await message.answer('Игра началась.')
    
@dp.message_handler(commands=['set'])
async def mes_help(message: types.Message):
    global total
    global new_game
    count = message.text.split()[1]
    if not new_game:
        if message.text.split()[1].isdigit():
            total = int(count)
            await message.answer(f'Конфет теперь будет {count}')
        else:
            await message.answer(f'{message.from_user.first_name}, напишите цифрами.')
    else:
        await message.answer(f'{message.from_user.first_name}, нельзя менять правила во время игры.')
    
    
@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    global new_game
    if new_game:
        if message.text.isdigit():
            total -= int(message.text)
            if total <= 0:
                await message.answer(f'Ура! {message.from_user.first_name}, ты победил!')
                new_game = False
                total = 150
            else:
                await message.answer(f'{message.from_user.first_name} взял {message.text} конфет. '
                                f'На столе осталось {total}')

# @dp.message_handler()
# async def mes_all(message: types.Message):
#     await message.answer(f'{message.from_user.first_name} сама такая')