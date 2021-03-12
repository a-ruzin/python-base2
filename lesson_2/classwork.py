# Работа со строками:
# 	unicode
# 	chr()
# 	ord()
#
# 	.split()
# 	.join()
# 	.upper() и .lower()
# 	.title() и .capitalize()

# xxx = ' asdflkasjdlfkj   русские буквы' + '44444 '
# yyy = xxx.split()
# print(yyy)
#
# print(' '.join(yyy).capitalize())

# Форматирование:
# 	"%s" % (1,)
# 	"{}".format(1)
# 	f"{1}"

# print('Вася любит %s за %d рублей' % ('мороженное', 50))

# print('Вася любит {what} за {price:.2f} рублей'.format(what='мороженное', price=50))

# what = (1,2,3,4)
# price = 50
# print(f'Вася любит {what} за {price:.2f} рублей')
#
# print(len(what), what)
#
# '2'

#
# for ch in xxx[6:]:
#     print(ch, ord(ch))
# print(chr(1091))

# for ch in '1234':
#     print(ch)



#     name = None
#     color = None
#
#     def describe(self):
#         print(f'{self.name} is {self.color}')
#
#
# cat = Cat()
#
# cat.name = 'Marusya'
# cat.color = 'white'
# cat.describe()
#
# cat2 = Cat()
# cat2.name = 'Barsik'
# cat2.color = 'black'
# cat2.describe()
#
# cat.describe()
#
# other_cat = cat
# other_cat.describe()
#
# other_cat.color = 'red'
# other_cat.describe()
# cat.describe()
#
# price = 8.1
# price2 = 4 + 4.1
#
# if abs(price-price2) < 0.00001:
#     # price == price2
#     pass
#
# # Переменные в Python принято называть маленькими буквами через подчеркивание PriceList
#
# element = ';'
# if element.isdigit():
#     pass

# нормально, но нагляднее было бы "+" вместо chr(43)

# Не используйте с параметром: `split(' ')` без необходимости, лучше пишите `split()`.
# Если в строке встретятся двойные пробелы, то у вас в результирующем списке будут пустые строчки.

# string = "слово   другое слово"
# print(string.split(' '))
# print(string.split())

word = "+5.5"
