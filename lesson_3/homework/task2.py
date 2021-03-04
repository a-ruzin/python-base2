"""
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать
корректную работу с числительными, начинающимися с заглавной буквы. Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
>>> num_translate_adv("tWo")

"""

dictionary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}


def num_translate(word):
    temp_word = word[0].lower() + word[1:]
    russian_word = dictionary.get(temp_word)
    if russian_word is not None:
        if temp_word[0] == word[0]:
            return russian_word
        else:
            return russian_word[0].upper() + russian_word[1:]


print(num_translate('oNe'))
print(num_translate('two'))
print(num_translate('Two'))
