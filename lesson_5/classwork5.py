

# O(N)    C1*N*N          C1*M*M

def gen_odd_numbers():
    number = 1
    while number < 100:
        yield number
        number += number


values = list(gen_odd_numbers())
print(values)


g1 = gen_odd_numbers()
g2 = gen_odd_numbers()
print(next(g1))
print(next(g2))
print(next(g1))
print(next(g1))
print(next(g2))
print(next(g1))
print(next(g2))
print(next(g2))
print(next(g1))
print(next(g2))


# except StopIteration:
#     pass
# print(values)


# for i in gen_odd_numbers():
#     print(i)
#
#
# for i in range(1, 100, 25):
#     print(i)

values = []
for i in range(5):
    values.append(2**i)

print(values)
