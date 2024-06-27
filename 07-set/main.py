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


# Operation element set
# %% Add element
fellowship = set()
fellowship.add('aragorn')
print("len:", len(fellowship), "data:", fellowship)

fellowship.add('gollum')
print("len:", len(fellowship), "data:", fellowship)

# %% Remove element
fellowship = {'gollum', 'aragorn', 'gimli', 'legolas'}
print("len:", len(fellowship), "data:", fellowship)

fellowship.remove('gollum')
print("len:", len(fellowship), "data:", fellowship)

fellowship.discard('legolas')
print("len:", len(fellowship), "data:", fellowship)

# %% Remove element acak
fellowship = {'gollum', 'aragorn', 'gimli', 'legolas'}
print("len:", len(fellowship), "data:", fellowship)

fellowship.pop()
print("len:", len(fellowship), "data:", fellowship)

# %% Clear set / mengkosongkan isi set
fellowship = {'gollum', 'aragorn', 'gimli', 'legolas'}
print("len:", len(fellowship), "data:", fellowship)

fellowship.clear()
print("len:", len(fellowship), "data:", fellowship)

# %% Copy set
fellowship = {'gollum', 'aragorn', 'gimli', 'legolas'}
print("len:", len(fellowship), "data:", fellowship)

copy_fellowship = fellowship.copy()
print("len:", len(copy_fellowship), "data:", copy_fellowship)

# %% pengechekkan difference antar set
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Method difference() digunakan untuk mencari perbedaan elemen antara data (dimana method dipanggil) 
# vs. data pada argument pemanggilan method tersebut.
diff = a.difference(b)
print("diff:", diff)
print("a:", a)

# Method difference_update() yang kegunaannya adalah mengubah nilai data (dimana method dipanggil) 
# dengan nilai baru yang didapat dari perbedaan elemen antara data tersebut vs. data pada argument pemanggilan method.
a.difference_update(b)
print("a:", a)

# %% Pengechekan intersection antar set
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Method intersection() digunakan untuk mencari perbedaan elemen antara data (dimana method dipanggil)
# vs. data pada argument pemanggilan method tersebut.
inter = a.intersection(b)
print("inter:", inter)
print("a:", a)

# Method intersection_update() yang kegunaannya adalah mengubah nilai data (dimana method dipanggil) 
# dengan nilai baru yang didapat dari perbedaan elemen antara data tersebut vs. data pada argument pemanggilan method.
a.intersection_update(b)
print("a:", a)

# %%
