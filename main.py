import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
import random
from config import TOKEN
import keyboard as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
   await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.inline_keyboard_test)

@dp.message(F.text == "Привет")
async def test_button(message: Message):
   await message.answer(f'Привет, {message.from_user.first_name}')

@dp.message(F.text == "Пока")
async def test_button(message: Message):
   await message.answer(f'Пока, {message.from_user.first_name}')


@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1],destination=f'img/{message.photo[-1].file_id}.jpg')

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile("sample.ogg")
    await message.answer_voice(voice)

@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого как фотка', 'Непонятно, что это такое', 'Не отправляй мне такое']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

@dp.message(F.text == 'Что такое ИИ?')
async def aitext(message: Message):
    await message.answer("Иску́сственный интелле́кт в самом широком смысле – это интеллект, демонстрируемый машинами, в частности компьютерными системами. Это область исследований в области компьютерных наук, которая разрабатывает и изучает методы и программное обеспечение, позволяющие машинам воспринимать окружающую среду и использовать обучение и интеллект для выполнения действий, которые максимально увеличивают их шансы на достижение поставленных целей[1]. Такие машины можно назвать искусственным интеллектом.")
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Приветики, я бот!')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

