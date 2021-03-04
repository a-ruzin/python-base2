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


def get_jokes(n, uniq=False):
    """
    Функция возвращает шутки в виде списка строк.

    :param n: int - количество шутко, которое надо вернуть
    :param uniq: bool - нужно ли генерировать шутки из слов без повторений
    :return: список строк
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if uniq:
        n = min(n, len(nouns), len(adverbs), len(adjectives))

    jokes = []
    for i in range(n):
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)
        joke = f'{noun} {adverb} {adjective}'
        jokes.append(joke)

        if uniq:
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
    return jokes


print(get_jokes(7))
print(get_jokes(7, False))
print(get_jokes(7, True))
