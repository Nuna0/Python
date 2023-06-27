#filter, map

WORD_LIST = ['кошка','собака','тигр','лев','попугай']

def word_filter(word):
    return  len(word) <= 5

def word_adder(word):
    return 'Слово ' + word

# filter(<функция фильтрации>,<коллеккция>)
#res = filter(word_filter, WORD_LIST)
res = list(filter(word_filter, WORD_LIST))
print(res)

# map(<функция>,<коллекция>>)

res2 = list(map(word_adder, WORD_LIST))
print(res2)

print(list(map(int, input().split())))

# lambda <аргументы>: <возвращаемое значение>
print(list(filter(lambda x: len(x) <= 5, WORD_LIST)))