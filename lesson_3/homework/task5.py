"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех слов,
взятых из трёх списков (по одному слову из каждого списка):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
#>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий
повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?
"""


import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_joke():
    """
    Функция возвращает одну шутки в виде строки

    :return: строка
    """
    noun = random.choice(nouns)
    adverb = random.choice(adverbs)
    adjective = random.choice(adjectives)
    return f'{noun} {adverb} {adjective}'


def get_jokes(n):
    """
    Функция возвращает шутки в виде списка строк

    :param n: int - количество шутко, которое надо вернуть
    :return: список строк
    """
    jokes = []
    for i in range(n):
        jokes.append(get_joke())
    return jokes


print(get_jokes(n=2))


def get_jokes_uniq(n):
    """
    Функция возвращает шутки в виде списка строк

    :param n: int - количество шутко, которое надо вернуть
    :return: список строк
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    n = min(n, len(nouns), len(adverbs), len(adjectives))

    jokes = []
    for i in range(n):
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)
        joke = f'{noun} {adverb} {adjective}'
        jokes.append(joke)

        nouns.remove(noun)
        adverbs.remove(adverb)
        adjectives.remove(adjective)
    return jokes


print(get_jokes_uniq(7))
