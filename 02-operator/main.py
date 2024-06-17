# Operator assignment (=)
# digunakan untuk menugaskan sebuah variabel dengan sebuah nilai baru.

# deklarasi variable num_1
num_1 = 12

# deklarasi variable num_2
num_2 = 24

# nilai baru ditugaskan ke variabel num_2
num_2 = 12

# deklarasi variabel num_3 dengan isi nilai hasil operasi aritmatika `num_1 + num_2`
num_3 = num_1 + num_2

print(num_3)
# output ➜ 24


# %% Operator perbandingan
# perbandingan antara dua buah variabel
res = 4 == 5
print("4 == 5 =", res)

res = 4 != 5
print("4 != 5 =", res)

res = 4 > 5
print("4 > 5 =", res)

res = 4 < 5
print("4 < 5 =", res)

res = 5 >= 5
print("5 >= 5 =", res)

res = 4 <= 5
print("4 <= 5 =", res)

# %% Operator aritmatika
num = 2 + 2
print("2 + 2 = %d" % (num))

num = 3 - 2
print("3 - 2 = %d" % (num))

num = 3 * 3
print("3 * 3 = %d" % (num))

num = 8 / 2
print("8 / 2 = %d" % (num))

num = 10 // 3
print("10 // 3 = %d" % (num))

num = 7 % 4
print("7 %% 4 = %d" % (num))

num = 3 ** 2
print("3 ** 2 = %d" % (num))

# %% Operator logika (and, or, not)
res = (4 == 5) and (2 != 3)
print("(4 == 5) and (2 != 3) =", res)

res = (4 == 5) or (2 != 3)
print("(4 == 5) and (2 != 3) =", res)

res = not (2 == 3)
print("not 2 == 3 =", res)

# %% Operator identity (is)
# membandingkan id dari dua buah variabel
num_1 = 100001
num_2 = 100001
res = num_1 is num_2
print("num_1 is num_2 =", res)
print("id(num_1): %s, id(num_2): %s" % (id(num_1), id(num_2)))

# %% Fungsi print() tanpa output formatting
print("message: %s %s %s" % ("hello", "python", "learner"))
print("message:", "hello", "python", "learner")

# %% Fungsi id()
# membandingkan id dari sebuah variabel
data_1 = "hello world"
id_data_1 = id(data_1)

print("data_1:", data_1)        # hello world
print("id_data_1:", id_data_1)  # 19441xxxxxxxx


# %% Operator membership (in)
# perbandingan antara sebuah variabel dengan sebuah objek
# %% op membership dengan list
sample_list = [2, 3, 4]
is_3_exists = 3 in sample_list
print(is_3_exists)

# %% op membership dengan tuple
sample_tuple = ("golang", "python")
is_hello_exists = "hello" in sample_tuple
print(is_hello_exists)

# %% op membership dengan dictionary
sample_dict = { "nama": "adam", "age": 12 }
is_key_nama_exists = "nama" in sample_dict
print(is_key_nama_exists)

# %% op membership dengan set
sample_set = { "lorem", "ipsum" }
is_ipsum = "ipsum" in sample_set
print(is_ipsum)

# %% op membership dengan string
text = 'Hello world'
is_substring_exists = 'orl' in text
print(is_substring_exists)

