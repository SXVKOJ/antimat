# **Telegram бот, который удаляет сообщения с матом**

![ff](https://img.shields.io/badge/price-FREE-green)
![src](https://img.shields.io/badge/source%20code-open-red)
![src2](https://img.shields.io/badge/language-python-blue)

author: @halupasss

------------
# Принцип работы

* Сначала мы заменяем английские транслит символы на русские
* Удаляем лишние приколы (всякие спецсимволы и тому подобное)
* Потом сравниваем каждое сообщение со словами из базы данных (bad_words.txt) с помощью 
расстояния левенштейна

------------
# Требования
* Python 3.10
