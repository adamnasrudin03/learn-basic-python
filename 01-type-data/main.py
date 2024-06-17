# Type data numeric
# %% int
number_1 = 10000023
print(number_1)

# %% float
number_2 = 3.14
print(number_2)

# %% complex
number_3 = 120+3j
print(number_3)


# Type data string
# %%
string_1 = "hello python"
print(string_1)

# %%
string_2 = """Selamat
Belajar
Python"""
print(string_2)



# %% Type data bool
bool_1 = True
print(bool_1)

bool_2 = False
print(bool_2)


# Type data list
# %% list with int as element's data type
list_1 = [2, 4, 8, 16]
print(list_1)

# %% list with str as element's data type
list_2 = ["adam", "jason", "tim", "damian"]
print(list_2)

# %% list with various data type in the element
list_3 = [24, False, "Hello Python"]
print(list_3)

# %% access item by index
list_1 = [2, 4, 8, 16]
print(list_1[2])


# Type data tuple
# %% tuple with int as element's data type
tuple_1 = (2, 3, 4)
print(tuple_1)

# %% tuple with str as element's data type
tuple_2 = ("lorem", "ipsum", "dolor")
print(tuple_2)

# %% tuple with various data type in the element
tuple_3 = (24, False, "Hello Python")
print(tuple_3)

# %% access item by index
tuple_1 = (2, 3, 4)
print(tuple_1[2])


# Type data dictionary
# %%
profile_1 = {
  "name": "Adam",
  "is_male": False,
  "age": 16,
  "hobbies": ["gaming","coding", "movies","learning"]
}

print("name: %s" % (profile_1["name"]))
print("hobbies: %s" % (profile_1["hobbies"]))

# %%
profile_1 = { "name": "Adam", "hobbies": ["gaming","coding", "movies","learning"] }
print(profile_1)


# %% Type data sets
set_1 = {"pineapple", "spaghetti"}
print(set_1)