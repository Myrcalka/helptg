import json
from aiogram import types

# Початкове значення для змінної мови
language = "ukr"  # Початково - українська мова

# Словник для збереження інфо користувачів
user_info = {}

# Функція для зміни тексту інфо
async def change_info(message: types.Message, new_info: str):
    user_info[message.from_user.id] = new_info
    await message.edit(text=f"{get_text('info_changed')}: {new_info}")

# Функція для отримання коду або тексту інфо в залежності від мови
async def get_code(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_info:
        # Якщо інформація для користувача ще не задана
        info_text = get_text('no_info')
    else:
        info_text = user_info[user_id]

    info_text += f"\n\n{get_text('update_info_instruction')}"
    await message.edit(text=info_text)

# Функція для зміни мови
async def set_language(message: types.Message, lang: str):
    global language
    if lang == "ukr":
        language = "ukr"
        await message.edit(text=get_text('language_changed_ukr'))
    elif lang == "rus":
        language = "rus"
        await message.edit(text=get_text('language_changed_rus'))
    elif lang == "eng":
        language = "eng"
        await message.edit(text=get_text('language_changed_eng'))
    else:
        await message.edit(text=get_text('unknown_language'))

# Функція для отримання тексту в залежності від мови
def get_text(key: str):
    texts = {
        'info_changed': {
            'ukr': "Інформація для вас змінена на",
            'rus': "Информация для вас изменена на",
            'eng': "Your information has been changed to"
        },
        'no_info': {
            'ukr': "Ваші дані ще не встановлені. Використовуйте команду для оновлення.",
            'rus': "Ваши данные еще не установлены. Используйте команду для обновления.",
            'eng': "Your data has not been set yet. Use the command to update."
        },
        'update_info_instruction': {
            'ukr': "Щоб оновити інформацію, використовуйте команду: `/change_info Нове_інфо`",
            'rus': "Чтобы обновить информацию, используйте команду: `/change_info Новое_инфо`",
            'eng': "To update the information, use the command: `/change_info New_info`"
        },
        'language_changed_ukr': {
            'ukr': "Мова змінена на українську.",
            'rus': "Язык изменен на русский.",
            'eng': "Language changed to English."
        },
        'language_changed_rus': {
            'ukr': "Мова змінена на російську.",
            'rus': "Язык изменен на русский.",
            'eng': "Language changed to Russian."
        },
        'language_changed_eng': {
            'ukr': "Мова змінена на англійську.",
            'rus': "Язык изменен на английский.",
            'eng': "Language changed to English."
        },
        'unknown_language': {
            'ukr': "Невідома мова. Використовуйте 'ukr', 'rus' або 'eng'.",
            'rus': "Неизвестный язык. Используйте 'ukr', 'rus' или 'eng'.",
            'eng': "Unknown language. Use 'ukr', 'rus', or 'eng'."
        }
    }
    return texts[key][language]

# Точка входу для обробки команд
async def handle_command(message: types.Message):
    text = message.text.lower()
    
    # Обробка команди для зміни мови
    if text.startswith("/set_language"):
        # Наприклад: /set_language ukr
        lang = text.split()[1]
        await set_language(message, lang)
    
    # Обробка команди для отримання інформації
    elif text == "/get_info":
        await get_code(message)
    
    # Обробка команди для зміни інфо
    elif text.startswith("/change_info"):
        new_info = " ".join(text.split()[1:])  # залишок тексту після команди
        await change_info(message, new_info)￼Enter
