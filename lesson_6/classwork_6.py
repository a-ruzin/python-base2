

# f = open('file.txt', 'w+', encoding='utf8')
# # f.write('Привет, я Python\n')
# for i in range(10):
#     print(f'Привет, я Python #{i}', file=f)
# f.close()

# a = [1,2,3,4,5,6,7,8]
# print(a)
# a[3:6] = []
# print(a)

# f = open('file.txt', 'r+', encoding='utf-8')
# f.seek(0)
# f.write('Фраза')
# print(f.tell())

# content = f.read()

# while True:
#     line = f.readline()
#     if not line:
#         break
#
#     print(line, line.encode(encoding='utf8'))
#     line2 = line.strip()
#     print(line2, line2.encode(encoding='utf8'))

# for line in f:
#     line2 = line.strip()
#     print(line2, line)

# print(type(content), content, content.decode(encoding='utf8'))
# f.close()

# b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, \xd1\x8f Python'


# with open('file.txt', 'r+', encoding='utf-8') as f:
#     for y in range(20):
#         print(f'Фраза {y}', file=f)

d = {
    'values': (1, 2, 3, 4, 5),
    'keys': ['a\na', 'b', 'c']
}

# json    - текстовый   JSON - JavaScript Object Notation
# pickle  - бинарный

# import json
#
# with open('serialized_dict.json', 'w', encoding='utf8') as f:
#     json.dump(d, f, indent=4)
#
# with open('serialized_dict.json', 'r', encoding='utf8') as f2:
#     d2 = json.load(f2)
#
# print(d2)
# print(d)

# d2 = json.loads(c)
#
# print(type(d2), d2)
# for k, v in d2.items():
#     print(k, v)


import pickle

d = {
    'values': (1, 2, 3, 4, 5),
    'keys': ['a\na', 'b', 'c']
}

with open('pick', 'wb') as f:
    pickle.dump(d, f)

with open('pick', 'rb') as f2:
    num2 = pickle.load(f2)

with open('pick', 'rb') as f2:
    print(f2.read())

print(num2)
print(d)
