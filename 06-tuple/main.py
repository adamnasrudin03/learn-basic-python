tuple_1 = (2, 3, 4, "hello python", False)

print("data:", tuple_1)
# output ➜ data: (2, 3, 4, "hello python", False)

print("total elem:", len(tuple_1))
# output ➜ total elem: 5

tuple_1 = (2, 3, 4, 5)
print("elem 0:", tuple_1[0])
# output ➜ elem 0: 2

print("elem 1:", tuple_1[1])
# output ➜ elem 1: 3

# %% Loop tuple
tuple_2 = ('ultra instinc shaggy', 'nightwing', 'noob saibot')

for t in tuple_2:
    print(t)
    
for i in range(0, len(tuple_2)):
    print("index:", i, "elem:", tuple_2[i])

for i, v in enumerate(tuple_2):
    print("index:", i, "elem:", v)
    

# $$ check value
tuple_1 = (10, 70, 20)
n = 70

if n in tuple_1:
    print(n, "is exists")
else:
    print(n, "is NOT exists")

# output ➜ 70 is exists

# %% tuple nested
tuple_nested = ((0, 2), (0, 3), (2, 2), (2, 4))

for row in tuple_nested:
    for cell in row:
        print(cell, end=" ")
    print()


# horizontal
tuple_nested = ((0, 2), (0, 3), (2, 2), (2, 4))
# vertikal
tuple_nested = (
    (0, 2),
    (0, 3),
    (2, 2),
    (2, 4)
)

# %% List and tuple
# deklarasi data list berisi elemen tuple
data = [
    ("ultra instinc shaggy", 1, True, ['detective', 'saiyan']),
    ("nightwing", 3, True, ['teen titans', 'bat family']),
]

# append tuple ke list
data.append(("noob saibot", 6, False, ['brotherhood of shadow']))

# append tuple ke list
data.append(("tifa lockhart", 2, True, ['avalanche']))

# print data
print("name | rank | win | affliation")
print("------------------------------")
for row in data:
    for cell in row:
        print(cell, end=" | ")
    print()

# %% func tuple()
alphabets = tuple('abcdefgh')
print(alphabets)
# output ➜ ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

# list to tuple
l = [2, 3, 4, 5]
numbers = tuple(l)
print(numbers)
# output ➜ (2, 3, 4, 5)

# range to tuple
r = range(0, 3)
rTuple = tuple(r)
print(rTuple)
# output ➜ (0, 1, 2)

# %% Tuple packing dan unpacking
print("tuple packing")
# tuple packing
first_name = "aerith gainsborough"
rank = 11
win = False

row_data = (first_name, rank, win)

print(row_data)
# output ➜ ('aerith gainsborough', 11, False)

# dengan ()
row_data = (first_name, rank, win)

# tanpa ()
row_data = first_name, rank, win

# fungsi print() dengan satu argument berisi tuple (first_name, rank, win)
print((first_name, rank, win))

# fungsi print() dengan isi 3 arguments: first_name, rank, win
print(first_name, rank, win)

print()
# tuple unpacking
print("tuple unpacking")
row_data = ('aerith gainsborough', 11, False)
first_name, rank, win = row_data

print(first_name, rank, win)
# output ➜ aerith gainsborough 11 False


# %% empty tuple
empty_tuple = ()
print(empty_tuple)
# output ➜ ()


