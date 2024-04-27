from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputFile
import TOKEN

bot = Bot(TOKEN.APITOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите команду")
keyboard.add(KeyboardButton("Начало работы надо проектом(1-5 главы)"), KeyboardButton("Основная часть проекта(6-14 "
                                                                                      "главы)"))
keyboard.add(KeyboardButton("Критерии оценки проекта(15-16)"))

firstPartOfTopicsInlineKeyboard = InlineKeyboardMarkup(row_width=2)
firstPartOfTopicsInlineKeyboard.add(InlineKeyboardButton(text="Тема 1. Общее пониятие о проекте и проектной "
                                                              "деятельности",
                                                         callback_data="topic1GeneralUnderstanding"),
                                    InlineKeyboardButton(
                                        text="Тема 2. Поиск актуальной проблематики, выбор темы прокекта",
                                        callback_data="topic2SearchForCurrentProblems"),
                                    InlineKeyboardButton(text="Тема 3. Планирование роботы над проектом",
                                                         callback_data="topic3ProjectPlanning"),
                                    InlineKeyboardButton(text="Тема 5. Разработка паспорта проекта",
                                                         callback_data="topic5DevelopingAProjectPassport"))

secondPartOfTopicsInlineKeyboard = InlineKeyboardMarkup(row_width=2)
secondPartOfTopicsInlineKeyboard.add(
    InlineKeyboardButton(text="Тема 6. Введение как вступительная часть учебной работы",
                         callback_data="topic6IntroductionAsAnIntroductory"),
    InlineKeyboardButton(text="Тема 7. Технология работы с информационными источниками",
                         callback_data="topic7TechnologyOfWork"),
    InlineKeyboardButton(text="Тема 9.-11. Разработка практической части исследования",
                         callback_data="topic9-11Development"),
    InlineKeyboardButton(text="Тема 12-14 Готовимся к защите проекта",
                         callback_data="topic12-14PreparingForProjectDefence"))


async def onStartup(_):
    print("Бот работает")


@dp.message_handler(commands=["start"])
async def help(message: types.Message):
    await message.answer(text="Начало", reply_markup=keyboard)


@dp.message_handler(text="Начало работы надо проектом(1-5 главы)")
async def gettingStartedOnTheProject(message: types.Message):
    await message.answer(text="Начало работы надо проектом(1-5 главы)", reply_markup=firstPartOfTopicsInlineKeyboard)
    await message.delete()


@dp.message_handler(text="Основная часть проекта(6-14 главы)")
async def gettingStartedOnTheProject(message: types.Message):
    await message.answer(text="Основная часть проекта(6-14 главы)", reply_markup=secondPartOfTopicsInlineKeyboard)
    await message.delete()


@dp.callback_query_handler(text="topic1GeneralUnderstanding")
async def topic1(message: types.Message): 
    presentation = open("Тема 1 Понятие о проектной деятельности.pdf", "rb")
    doc = open("1. Что понимают под проектом.docx", "rb")
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Тема 1. Общее пониятие о проекте и проектной деятельности")
    await bot.send_document(message.from_user.id, document=doc)
    await bot.send_document(message.from_user.id, document=presentation)


@dp.callback_query_handler(text="topic2SearchForCurrentProblems")
async def topic2(message: types.Message):
    presentation = open("Тема 2 Выбор темы проекта.pptx", "rb")
    photo = InputFile("5 заданий в практической работе по теме2.jpg")
    doc = open("титул.docx", "rb")
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Тема 2. Поиск актуальной проблематики, выбор темы прокекта")
    await bot.send_photo(message.from_user.id, photo=photo)
    await bot.send_document(message.from_user.id, document=presentation)
    await bot.send_document(message.from_user.id, document=doc)
    await bot.send_message(message.from_user.id, text="https://cloud.mail.ru/public/YprT/k8qP3WmGE")


@dp.callback_query_handler(text="topic3ProjectPlanning")
async def topic3(message: types.Message):
    presentation = open("Тема 3 Планирование проекта.pdf", "rb")
    doc = open("3.1. Понятие о плане и значение планирования.docx", "rb")
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Тема 3. Планирование роботы над проектом")
    await bot.send_document(message.from_user.id, document=doc)
    await bot.send_message(message.from_user.id,
                           text="Нажмите на ссылку https://cloud.mail.ru/public/s7RM/T9qR5YUHR, чтобы открыть ресурс.")
    await bot.send_message(message.from_user.id,
                           text="Выберите тему из предложенной примерной тематике  (1 столбец) или напечатайте свою тему ниже в таблице. укажите ФИО. Будь внимательным, сначала найди лист именно той группы, в которой учишься. Нажмите на ссылку https://disk.yandex.ru/i/8b8mn2pdghBXmA, чтобы открыть ресурс.")
    await bot.send_document(message.from_user.id, document=presentation)


@dp.callback_query_handler(text="topic7TechnologyOfWorkWithInformationSources")
async def topic5(message: types.Message):
    presentation = open("Тема 5 Формулирование цели, задач. паспорт проекта.pptx", "rb")
    doc = open("Паспорт шаблон.docx", "rb")
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Тема 5. Разработка паспорта проекта")
    await bot.send_document(message.from_user.id, document=presentation)
    await bot.send_document(message.from_user.id, document=doc)
    await bot.send_message(message.from_user.id, text="Нажмите на ссылку https://cloud.mail.ru/public/LZPV/sx6jiCr4d, "
                                                      "чтобы открыть ресурс.")


@dp.callback_query_handler(text="topic6IntroductionAsAnIntroductory")
async def topic6(message: types.Message):
    presentation = open("Тема 6 Введение ,методы разработки проекта.pdf", "rb")
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Тема 6. Введение как вступительная часть учебной работы")
    await bot.send_document(message.from_user.id, document=presentation)
    await bot.send_message(message.from_user.id,
                           text="Нажмите на ссылку https://cloud.mail.ru/public/tq6T/NF8nZzuHd, чтобы открыть ресурс.")

@dp.callback_query_handler(text="topic7TechnologyOfWork")
async def topic7(message: types.Message):
    presentation = open("Тема 7 Работа с текстом. библиография.pptx", "rb")
    doc = open("техника чтения.docx", "rb")
    doc2 = open("2020 БИБЛИОГРАФИЧЕСКОЕ ОПИСАНИЕ.pdf", "rb")
    doc3 = open("памятка студенту1.docx", "rb")
    doc4 = open("итоговое занятие №8 в 1 семестре.docx", "rb")
    doc5 = open("Инструкция как создать Оглавление.docx", "rb")
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Тема 7. Технология работы с информационными источниками")
    await bot.send_document(message.from_user.id, document=presentation)
    await bot.send_document(message.from_user.id, document=doc)
    await bot.send_document(message.from_user.id, document=doc2)
    await bot.send_document(message.from_user.id, document=doc3)
    await bot.send_document(message.from_user.id, document=doc4)
    await bot.send_document(message.from_user.id, document=doc5)
    await bot.send_message(message.from_user.id,
                           text="Нажмите на ссылку https://pc-consultant.ru/microsoft-word/kak-rabotat-v-vorde-dlya-chajnikov/, чтобы открыть ресурс.")
    await bot.send_message(message.from_user.id,
                           text="Нажмите на ссылку https://cloud.mail.ru/public/sLmy/CFrv9EJo2, чтобы открыть ресурс.")

@dp.callback_query_handler(text="topic9-11Development")
async def topicsFrom9to11(message: types.Message):
    presentation = open("Тема 11 Разработка продукта (Сценирование ).pptx", "rb")
    doc = open("Тема 9 Разработка анкеты.pptx", "rb")
    doc2 = open("примеры проектов-20240422.zip", "rb")
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Тема 9.-11. Разработка практической части исследования")
    await bot.send_document(message.from_user.id, document=doc)
    await bot.send_document(message.from_user.id, document=presentation)
    await bot.send_document(message.from_user.id, document=doc2)
    await bot.send_message(message.from_user.id, text="Пройдите квест Сетивичок. Получите информацию о своей цифровой грамотности. О результатах сообщите преподавателю Нажмите на ссылку http://сетевичок.рф/, чтобы открыть ресурс.")


@dp.callback_query_handler(text="topic12-14PreparingForProjectDefence")
async def topicsFrom12to14(message: types.Message):
    presentation = open("тема 12-13 публичное выступление критерии оценки..pptx", "rb")
    doc = open("памятка студенту.docx", "rb")
    doc2 = open("Готовим доклад к защите..pdf", "rb")
    doc3 = open("шаблон презентации на защиту.pptx", "rb")
    doc4 = open("Пример doklad_ИП про ИИ.docx", "rb")
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Тема 12-14 Готовимся к защите проекта")
    await bot.send_document(message.from_user.id, document=presentation)
    await bot.send_document(message.from_user.id, document=doc)
    await bot.send_document(message.from_user.id, document=doc2)
    await bot.send_document(message.from_user.id, document=doc3)
    await bot.send_message(message.from_user.id,
                           text="Нажмите на ссылку https://cloud.mail.ru/public/Kgjw/HDg6kvoYz, чтобы открыть ресурс.")
    await bot.send_document(message.from_user.id, document=doc4)


@dp.message_handler(text="Критерии оценки проекта(15-16)")
async def evaluationCriteria(message: types.Message):
    doc = open("критерии оценки.docx", "rb")
    doc2 = open("тема 15-16 защита.pptx", "rb")
    await message.delete()
    await bot.send_message(message.from_user.id, text="КРИТЕРИИ ОЦЕНКИ ПРОЕКТА")
    await bot.send_document(message.from_user.id, document=doc)
    await bot.send_document(message.from_user.id, document=doc2)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=onStartup)
