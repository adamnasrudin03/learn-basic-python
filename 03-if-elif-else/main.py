# %% if
grade = 100
if grade == 100:
    print("perfect")

if grade == 90:
    print("ok")
    print("keep working hard!")


# %% elif
# elif (kependekan dari else if) 
str_input = input('Enter your grade: ')
grade = int(str_input)
print("inputan user:", grade, type(grade))

if grade == 100:
    print("perfect")
elif grade >= 85:
    print("awesome")
elif grade >= 65:
    print("passed the exam")


# %% else
str_input = input('Enter your grade: ')
grade = int(str_input)

if grade == 100:
    print("perfect")

elif grade >= 85:
    print("awesome")

elif grade >= 65:
    print("passed the exam")

    if grade <= 70:
        print("but you need to improve it!")
    else:
        print("with ok grade")

else:
    print("below the passing grade")


# %% nested 
str_input = input('Enter your grade: ')
grade = int(str_input)

if grade == 100:
    print("perfect")

elif grade >= 85:
    print("awesome")

elif grade >= 65:
    print("passed the exam")

    if grade <= 70:
        print("but you need to improve it!")
    else:
        print("with ok grade")

else:
    print("below the passing grade")


# %% op logical
grade = int(input('Enter your current grade: '))
prev_grade = int(input('Enter your previous grade: '))

if grade >= 90 and prev_grade >= 65:
    print("awesome")
if grade >= 90 and prev_grade < 65:
    print("awesome. you definitely working hard, right?")
elif grade >= 65:
    print("passed the exam")
else:
    print("below the passing grade")

if (grade >= 65 and not prev_grade >= 65) or (not grade >= 65 and prev_grade >= 65):
    print("at least you passed one exam. good job!")

# %% sebaris & ternary
str_input = input('Enter your grade: ')
grade = int(str_input)

# sebaris
if grade >= 65: print("passed the exam")
if grade < 65: print("below the passing grade")

# ternary
print("passed the exam") if grade >= 65 else print("below the passing grade")

# ternary call back value
message = "passed the exam" if grade >= 65 else "below the passing grade"
print(message)

