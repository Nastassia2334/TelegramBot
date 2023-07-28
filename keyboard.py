from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#создаем разметку клавиатуры
start = ReplyKeyboardMarkup(resize_keyboard=True)

info = KeyboardButton("Информация") #кнопка информации
stats = KeyboardButton("Статистика") #кнопка статистика
rasrab = KeyboardButton("Разработчик")
user_name = KeyboardButton("Покажи пользователя")
photo_add = KeyboardButton("Добавить фото")
photo_open = KeyboardButton("Открыть фото из галереи")
#добавляет кнопки в основу бота
start.add(stats, info)
start.add(rasrab, user_name)
start.add(photo_add, photo_open)

stats = InlineKeyboardMarkup()
stats.add(InlineKeyboardButton(f'Да', callback_data='join'))
stats.add(InlineKeyboardButton(f'Нет', callback_data='cancle'))
stats_user = InlineKeyboardMarkup()
stats_user.add(InlineKeyboardButton(f'Хочу увидеть id', callback_data='user_id'))
stats_user.add(InlineKeyboardButton(f'Вернуться обратно', callback_data='deselected'))