
# %% for range
for i in range(5):
    print("index:", i)

for i in range(0, 3):
    print("case 2 index:", i)

for i in range(0, 3, 1):
    print("case 3 index:", i)

for i in range(2, 10, 2):
    print("case 4 index:", i)

for i in range(5, -5, -1):
    print("case 5 index:", i)

# %% list
r = range(5)
print("r:", list(r))

# %% iterator list
messages = ["morning", "afternoon", "evening"]
for m in messages:
    print(m)

# %% iterator tuple
numbers = ("twenty four", 24)
for n in numbers:
    print(n)
# %% iterator string
for char in "hello python":
    print(char)

# %% iterator dictionary
sample_dict = { 
    "name": "adam", 
    "age": 26
}
for k, v in sample_dict.items():
    print("key:", k,  " value:", v)

# %% iterator set
numbers = {"twenty four", 24}
for n in numbers:
    print(n)


# %% nested for
max = int(input("jumlah bintang: "))

for i in range(max):
    for j in range(0, max - i):
        print("*", end=" ")
    print()

# %% while
should_continue = True

while should_continue:
    n = int(input("enter an even number greater than 0: "))

    if n <= 0 or n % 2 == 1:
        print(n, "is not an even number greater than 0")
        should_continue = False
    else:
        print("number:", n)


n = int(input("enter max data: "))
i = 0
while i < n:
    print("number", i)
    i += 1
# i += 1 => i = i + 1

# %% break and continue
n = int(input("enter max data: "))
i = 0
while True:
    if i % 2 == 1:
        print("skip number", i)
        i += 1
        continue

    print("number", i)
    i += 1
    if i >= n:
        break

# %% nested while
n = int(input("enter max data: "))
i = 0

while i < n:
    j = 0

    while j < n - i:
        print("*", end=" ")
        j += 1
    
    print()
    i += 1

# %% combination of for and while
n = int(input("enter max data: "))
i = 0

for i in range(n):
    j = 0

    while j < n - i:
        print("*", end=" ")
        j += 1
    
    print()

