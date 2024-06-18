# contoh list
list_1 = [10, 70, 20]

# list dengan deklarasi element secara vertikal 
list_2 = [
    'ab',
    'cd',
    'hi',
    'ca'
]

# list dengan element berisi bermacam-macam tipe data
list_3 = [3.14, 'hello python', True, False]

# list kosong
list_4 = []


# %% Loop list

list_1 = [10, 70, 20]

for e in list_1:
    print("elem:", e)


print("Range:")
for i in range(0, len(list_1)):
    print("index:", i, "elem:", list_1[i])


print("enumerate:")
for i, v in enumerate(list_1):
    print("index:", i, "elem:", v)


# %% Nested list
matrix = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
]

for row in matrix:
    for cel in row:
        print(cel, end=" ")
    print()
# %% Range to List
range_1 = range(0, 10)
list_1 = list(range_1)
print(list_1)
# output ➜ [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

range_2 = range(0, 22, 3)
list_2 = list(range_2)
print(list_2)
# output ➜ [0, 3, 6, 9, 12, 15, 18, 21]

range_3 = range(100, 0, -10)
list_3 = list(range_3)
print(list_3)
# output ➜ [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

# %% String to list
str_1 = "hello python"
list_1 = list(str_1)
print(list_1)
# output ➜ ['h', 'e', 'l', 'l', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n']

# %% Tuple to list
tuple_1 = (1, 2, 3)
list_1 = list(tuple_1)
print(list_1)
# output ➜ [1, 2, 3]


# %% Operasi pada list
# akses element via index
list_1 = [10, 70, 20]

elem_1st = list_1[0]
elem_2nd = list_1[1]
elem_3rd = list_1[2]

print(elem_1st, elem_2nd, elem_3rd)
# output ➜ [10, 70, 20]

# Check element is exist
list_1 = [10, 70, 20]
n = 70

if n in list_1:
    print(n, "is exists")
else:
    print(n, "is NOT exists")
# output ➜ 70 is exists


# Slicing list
list_2 = ['ab', 'cd', 'hi', 'ca']
print('list_2:', list_2)
# output ➜ list2: ['ab', 'cd', 'hi', 'ca']

slice_1 = list_2[1:3]
print('slice_1:', slice_1)
# output ➜ slice_1: ['cd', 'hi']


# %% mengubah list
list_2 = ['ab', 'cd', 'hi', 'ca']
print('before:', list_2)
# output ➜ before: ['ab', 'cd', 'hi', 'ca']

list_2[1] = 'zk'
list_2[2] = 'sa'
print('after: ', list_2)
# output ➜ after: ['ab', 'zk', 'sa', 'ca']

# %% append
list_1 = [10, 70, 20]
print('before: ', list_1)
# output ➜ before: [10, 70, 20]

list_1.append(88)
list_1.append(87)
print('after: ', list_1)
# output ➜ after : [10, 70, 20, 88, 87]

print('append via slicing ')
list_1 = [10, 70, 20]
print('before: ', list_1)
# output ➜ before: [10, 70, 20]

list_1[len(list_1):] = [88, 87]
print('after: ', list_1)
# output ➜ after : [10, 70, 20, 88, 87]


# %% menggabungkan list
list_1 = [10, 70, 20]
list_2 = [88, 77]
list_1.extend(list_2)
print(list_1)
# output ➜ [10, 70, 20, 88, 87]

print('append via slicing ')
list_1 = [10, 70, 20]
list_2 = [88, 77]
list_1[len(list_1):] = list_2
print(list_1)
# output ➜ [10, 70, 20, 88, 87]

print('via operator +')
list_1 = [10, 70, 20]
list_2 = [88, 77]
list_3 = list_1 + list_2
print(list_3)
# output ➜ [10, 70, 20, 88, 87]

# %% Menyisipkan element pada index i
list_3 = [10, 70, 20, 70]

list_3.insert(0, 15)
print(list_3)
# output ➜ [15, 10, 70, 20, 70]

list_3.insert(2, 25)
print(list_3)
# output ➜ [15, 10, 25, 70, 20, 70]

# %% menghapus element
list_3 = [10, 70, 20, 80]
list_3.remove(70)
print(list_3)
# output ➜ [10, 20, 80]


print('via pop()')
# Method pop() berfungsi untuk menghapus element pada index tertentu. J
# ika tidak ada index yang ditentukan, maka data element terakhir yang dihapus.
list_3 = [10, 70, 20, 80]
list_3.pop()
print(list_3)
# output ➜ [10, 70, 20]

list_3 = [10, 70, 20, 80]
list_3.pop(1)
print(list_3)
# output ➜ [10, 20, 80]

print('via del')
list_3 = [10, 70, 20, 80]
print('len:', len(list_3), "data:", list_3)
# output ➜ len: 4 data: [10, 70, 20, 80]
del list_3[1]
print('len:', len(list_3), "data:", list_3)
# output ➜ len: 3 data: [10, 20, 80]

list_3 = [10, 70, 20, 80]
del list_3[1:3]
print(list_3)
# output ➜ [10, 80]
# %% len list
list_3 = [10, 70, 20, 70]
total = len(list_3)
print(total)
# output ➜ 4

# %% Count list
list_3 = [10, 70, 20, 70]
count = list_3.count(70)
print('jumlah element dengan data `70`:', count)
# output ➜ jumlah element dengan data `70`: 2

# %% get Index  element in list
list_2 = ['ab', 'cd', 'hi', 'ca']

idx_1st = list_2.index('cd')
print('idx_1st: ', idx_1st)
# output ➜ idx_1st: 1


# %% mengkosongkan list
list_1 = [10, 70, 20]
list_1.clear()
print(list_1)
# output ➜ []

list_1 = [10, 70, 20]
list_1 = []
print(list_1)
# output ➜ []

print('via del and slicing' )
list_1 = [10, 70, 20]
del list_1[:]
print(list_1)
# output ➜ []


# %% membalikan urutan element list
list_1 = [10, 70, 20]
list_1.reverse()
print(list_1)
# output ➜ [20, 70, 10]


# %% copy list
list_1 = [10, 70, 20]
list_2 = list_1.copy()
print(list_1)
# output ➜ [10, 70, 20]
print(list_2)
# output ➜ [10, 70, 20]


print('via kombinasi operasi assignment dan slicing' )
list_1 = [10, 70, 20]
list_2 = list_1[:]
print(list_1)
# output ➜ [10, 70, 20]
print(list_2)
# output ➜ [10, 70, 20]


# %% sort list
list_1 = [10, 70, 20]
list_1.sort()
print(list_1)
# output ➜ [10, 20, 70]

list_2 = [ 'h','z', 'c']
list_2.sort()
print(list_2)
# output ➜ ['c', 'h', 'z']
