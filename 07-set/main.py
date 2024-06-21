data_1 = {1, 'abc', False, ('banana', 'spaghetti')}

print("data:", data_1)
# output ➜ data: {1, 'abc', False, ('banana', 'spaghetti')}

print("len:", len(data_1))
# output ➜ len: 4

# %% akses element set
fellowship = {'aragorn', 'gimli', 'legolas'}

for p in fellowship:
    print(p)

# %% element set is not duplicate
# Tipe data set memang didesain untuk menyimpan data unik, duplikasi elemen tidak mungkin terjadi, bahkan meskipun dipaksa.
data = {1, 2, 3, 2, 1, 4, 5, 2, 3, 5}
print(data)
# output ➜ {1, 2, 3, 4, 5}

# example menghilangkan duplikasi pada list
dataList = [1, 2, 3, 2, 1, 4, 5, 2, 3, 5]
print(dataList)
# output ➜ [1, 2, 3, 2, 1, 4, 5, 2, 3, 5]

data_unique_set = set(data)
print(data_unique_set)
# output ➜ {1, 2, 3, 4, 5}

data_unique = list(data_unique_set)
print(data_unique)
# output ➜ [1, 2, 3, 4, 5]

# %% check value element is exist
fellowship = {'aragorn', 'gimli', 'legolas'}
to_find = 'gimli'

if to_find in fellowship:
    print(to_find, 'is exists within fellowship')