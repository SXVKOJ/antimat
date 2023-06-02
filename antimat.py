import re

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from rapidfuzz import fuzz

TOKEN = ""

bad_words = []

with open("bad_words.txt", "r", encoding='utf-8') as f:
    bad_words = f.readlines()
    bad_words = [word.replace("\n", "") for word in bad_words]


def replace_english_letters(text):
    replacements = {
        'a': 'а',
        'b': 'в',
        'e': 'е',
        'k': 'к',
        'm': 'м',
        'h': 'н',
        'o': 'о',
        'p': 'р',
        'c': 'с',
        't': 'т',
        'y': 'у',
        'x': 'х'
    }

    print("SRC", [ord(text[i]) for i in range(len(text))])

    for eng, rus in replacements.items():
        text = text.replace(eng, rus)

    print("NEW", [ord(text[i]) for i in range(len(text))])

    return text


def is_bad_word(source: list, dist: str):
    current_percent = 85

    for word in source:
        ratio = fuzz.ratio(dist, word)

        if ratio >= current_percent:
            return True, ratio

    return False, ratio


def extract_regular_chars(text):
    regular_chars = re.sub('[^a-zA-Zа-яА-Я0-9\s]', '', text)
    return regular_chars


async def check_message(message: types.Message):
    message_text = extract_regular_chars(message.text.lower())

    for word in message_text.split(' '):
        translit_word = replace_english_letters(word)

        is_bad, similarity_ratio = is_bad_word(bad_words, translit_word)

        print("DEBUG:", word, translit_word, is_bad, similarity_ratio)
        
        if is_bad:
            return await message.delete()


def main():
    bot = Bot(token=TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    dp.register_message_handler(check_message, content_types=types.ContentType.TEXT)

    executor.start_polling(dp, skip_updates=True)
    

if __name__ == '__main__':
    main()
