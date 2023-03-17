print("Hello World")

print("Dynamic Typing")
a = 1
b = 1
print(a, b)
print(type(a))
print(type(b))
print()

a = 1.5
b = 3.0
print(type(a))
print(type(b))
print()

a = "asldjk;asd"
b = "kjashdfkajsdf"
print(type(a))
print(type(b))
print()

a = "10"
b = "12314.512"
print(type(a))
print(type(b))
print()

a = True
b = False
print(type(a))
print(type(b))
print()


print("Data Type Shift")
a = 10
print(type(a))

float(a)
print(a)
print(type(a))
a = float(a)
print(type(a))
print()

a = 10.3
b = 10.7
a = int(a)
b = int(b)
print(a+b)
print()

a = "76.3"
print(type(a))
b = float(a)
print(type(b))

c = 10
print(b)
print(b+c)
print(a+a)
c = 38.8
print(c)
print()



color = ["red", "blue", "green"]
color2 = ["orange", "black", "white"]
print(color + color2)
print(len(color))
color[0] = "yellow"
print(color * 2)
print("blue" in color2)
total_color = color + color2
print(total_color)
print()

total_color.append("white")
print(total_color)
total_color.extend(["black", "purple"])
print(total_color)
total_color.remove("white")
print(total_color)
del total_color[0]
print(total_color)

print()

a = ["color", 1, 0.2]
print(a)
a[0] = total_color
print(a)

print()

a = [5, 4, 3, 2, 1]
b = [1, 2, 3, 4, 5]
b = a
print(b)

a.sort()
print(b)

b = [6, 7, 8, 9, 10]
print(a, b)

print()
a = [5, 4, 3, 2, 1]
b = a[:]
print(a)
print(b)
a.sort()
print(a)
print(b)
print()

t = [1, 2, 3]
a, b, c = t
print(t, a, b, c)
print()

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79 , 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score)
print(midterm_score[0][2])

midterm_copy = midterm_score[:]
print(midterm_copy)
midterm_score[0][3] = 50
print(midterm_score)
print(midterm_copy)
print()

import copy
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79 , 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
midterm_copy = copy.deepcopy(midterm_score)
midterm_copy[0][0] = 100
print(midterm_copy)
print(midterm_score)

print()

def calculate_rectangle_area(x, y):
    result = x * y
    return result

rectangle_x = 10
rectangle_y = 20
print("rectangle's height x : ", rectangle_x)
print("rectangle's length x : ", rectangle_y)

print("rectangle's width : ", calculate_rectangle_area(rectangle_x, rectangle_y))

print()

def f(x):
		return 2 * x + 7

def g(x):
		return x ** 2

x = 2
print (f(x) + g(x) + f(g(x)) + g(f(x)))

def f(x):
    return 2 * x + 7

def g(x):
    return x ** 2

    print(x + 10)

print(f(10))

c = f(10)
print(c)

print()

list_ex = [5, 4, 3, 2, 1]
print(sorted(list_ex))
print(list_ex)
list_ex.sort()
print(list_ex)
print()

print("Enter your name: ")
somebody = input()
print("Hi", somebody + ". How are you today?")
print()

temperature = float(input("Please enter the outdoor temperature: "))
print(temperature)
print()

print("Please enter the outdoor temperature: ")
temperature = input()
print("It is", float(temperature), "celcius outside")
print()

temp = float(input("Please enter the outdoor temperature: "))
print("It is", temp, "celcius outside")
print()

print("Hello World!!", "Hello Again!!!")
print("Hello World!!" + "Hello Again!!!")
print("Hello World!!" + str(100))
print()

print(1, 2, 3)
print("a" + " " + "b" + " " + "c")
print("%s %s" % ("one", "two"))
print("%d %d %d" % (1, 2, 3))
print("{} {} {}".format("a", "b", "c"))
print("{} {} {}".format(1, 2, 3))
print()

print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 3
day = "three"
print("I ate %d apples. I was sick for %s days" % (number, day))
print("Product: %s, Price per unit: %f" % ("Apple", 5.243))
print("Product: %s, Price per unit: %8.2f" % ("Apple", 5.243))

print()
age = 26
name = "Jason Lee"
print("I'm {0} years old.".format(age))
print("My name is {0} and {1} years old.".format(name, age))
print("My name is {1} and {0} years old.".format(name, age))
print("Product: {0}, Price per unit: {1:.3f}".format("Apple", 5.243))

print()
print("Product: %5s, Price per unit: %.5f" % ("Apple", 5.243))
print("Product: %10s, Price per unit: %10.5f" % ("Apple", 5.243))
print("Product: {0:5s}, Price per unit: {1:.5f}".format("Apple", 5.243))
print("Product: {0:>10s}, Price per unit: {1:10.3f}".format("Apple", 5.243))

print()
print("Product: %(name)10s, Price per unit: %(price)10.5f" % {"name": "Apple", "price": 5.243})
print("Product: {name:>10s}, Price per unit: {price:10.5f}".format(name="Apple", price=5.243))

print()
value = 12
print(f"value is {value}")

print()
name = "Jason"
age = 26
print(f"Hello, {name}. You are {age}.")
print(f"{name:20}")
print(f"{name:>20}")
print(f"{name:*<20}")
print(f"{name:*>20}")
print(f"{name:*^20}")

number = 3.141592653589793
print(f"{number:.2f}")

print()
print("This is a Celsius-Fahrenheit converter.")
Celsius = float(input("Please enter celsius that you would like to convert: "))
print("Celsius:", Celsius)
Fahrenheit = Celsius * (9/5) + 32
print("Farenheit", Fahrenheit)

print()

print("This is a Celsius-Fahrenheit converter.")
Celsius = float(input("Please enter celsius that you would like to convert: "))
print(f"Celsius: {Celsius:.2f}")
Fahrenheit = Celsius * (9/5) + 32
print(f"Farenheit: {Fahrenheit:.2f}")

print()
print("This is a Celsius-Fahrenheit converter.")
print("Please enter celsius that you would like to convert: ")
cel_value = float(input())
fah_value = ((9/5) * cel_value) + 32

print(f"Celsius Temperature: {cel_value:.2f}")
print(f"Fahrenheit Temperature: {fah_value:.2f}")


print()
print("Tell me yor age?")
myage = int(input())
if myage < 30:
	print("Welcome to the club")
else:
	print("Oh no! You are not accepted.")

if 1:
    print("Hello")
else:
    print("GoodBye")

print()

a = True
b = True
print(a and b)

a = True
b = False
print(a and b)

a = True
b = False
print(a or b)

boolean_list = [True, False, True, False, True]
print(all(boolean_list))
print(any(boolean_list))

value = 12
is_even = True if value % 2 == 0 else False
print(is_even)

print()

age = int(input("Please enter your age: "))
if age < 14 and age > 7:
    print("Elementary School Student")
elif age < 17 and age >13:
    print("Junior High School Student")
elif age < 20 and age > 16:
    print("High School Student")
elif age < 27 and age >19:
    print("Univ student")
else:
    print("You are not a student")

print()
print("3.15 done")
print("Never mind, I'm back")
print("Oh.. never mind the never mind, I just went to fix my airpods and they took it...")
print("I will be back tomorrow")
print()

a, b, *c = (14, 21, 25, 39, 46, 57)
print(c)

print()
class Car():
    def __init__(self):
        self.model = "BEN"

    def change_model(self):
        self.model = "CAR"

    def change_model_another(self):
        self.model = "TRUCK"

car = Car()
car.change_model_another()
car.change_model()
print(car.model)

print()
class House():
    def __init__(self):
        self.__door = []

print()

import random as rd

a = rd.random()
b = rd.random()

print(a, b)

print()

for looper in [1, 2, 3, 4, 5]:
    print("Hello")

for looper in [1, 2, 3, 4, 5]:
    print(f"{looper} : Hello")

print()

for looper in range(0,5):
    print("Hello")

for looper in range(0,5):
    print(f"{looper} : Hello")

print()
for i in "abcdefg":
    print(i)

print()
for i in ["americano", "latte", "frafuchino"]:
    print(i)


print()
for i in range(1,10,2):
    print(i)

print()
for i in range(10, 1, -1):
    print(i)

print()
print("Can you see below?")
for i in range(10, 1):
    print(i)
print("Can you see above?")

print()

i = 1
while i < 10:
    print(i)
    i += 1

i = 1
while i < 10:
    print(f"{i} : Hello")
    i += 1


print()

for i in range(10):
    if i == 5:
        break
    print(i)
print("EOP")

for i in range(10):
    if i == 5:
        continue
    print(i)
print("EOP")

for i in range(10):
    print(i,)
else:
    print("EOP")

print()

print("Muliplication of 5")

mltplctn = int(input("Which set of multiplication should we calculate? "))
print(f"Here is multiplication of {mltplctn}.")

for i in range(1,10):
    print(mltplctn, "X", i, "=", mltplctn*i)
print()

print("Which set of multiplication should we calculate? ")
dan = int(input())
print(f"Here is multiplication of {dan}.")

for i in range(1,10):
    print(f"{dan} X {i} = {dan*i}")

print("Practice")

sentence = "I love you"
reverse_sentence = ""
for char in sentence:
    reverse_sentence = char + reverse_sentence
    print(reverse_sentence)

print()
decimal = 10
result = ""
while (decimal > 0):
    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result
print(result)

print()

decimal_num = int(input("Please enter decimal number: "))
print(f"Your number is {decimal_num}")
result_2 = ""
while (decimal_num > 0):
    remainder_2 = decimal_num % 2
    decimal_num = decimal_num // 2
    result_2 = str(remainder_2) + result_2
print(result_2)

print("Input decimal number: ",)
decimal = int(input())
result = ""
loop_counter = 0
while (decimal > 0):
    temp_decimal_input = decimal
    temp_result_input = result

    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result

    print("------------------", loop_counter, "loop value check ------------------")
    print("Initial decimal:", temp_decimal_input, ", Remainder:", remainder, ", Initial result", temp_result_input)
    print("Output decimal:", decimal, ", Output result:", result)
    print("-----------------------------------------------------------")
    print()

    loop_counter += 1
print("Binary number is :", result)

print()

import random as rd

guess_number = int(input("Try to guess the number. number is between 1 to 100."))
number = (rd.randint(1, 100))
for guess_number in range(1, 101):
    if guess_number == number:
        print(f"Yes, it's correct! {number} is a correct number")
    elif guess_number > number and guess_number < 102:
        print("Oops, the number you entered is bigger than the correct number")
    elif guess_number < number and guess_number > 0:
        print("Oops, the number you entered is smaller than the correct number")
    else:
        print("You are way too off, the number is between 1 to 100")
print("Nice Try")

print()

true_value = rd.randint(1, 100)
input_value = 99999999

print("Try to guess the number. number is between 1 to 100: ")
while true_value != input_value:
    input_value = int(input())

    if input_value > true_value and input_value < 101:
        print("Oops, the number you entered is bigger than the correct number")
    elif input_value < true_value and input_value > 0:
        print("Oops, the number you entered is smaller than the correct number")
    elif input_value == true_value:
        print(f"Yes, it's correct! {input_value} is a correct number")
    else:
        print("You are way too off, the number is between 1 to 100")

print("Nice Try")

print()

print("Try to guess the number. number is between 1 to 100: ")
while true_value != input_value:
    input_value = int(input())

    if input_value > true_value:
        print("Oops, the number you entered is bigger than the correct number")
    elif input_value < true_value:
        print("Oops, the number you entered is smaller than the correct number")
    else:
        break
print(f"Yes, it's correct! {true_value} is a correct number")


print()

print("Average score per person")
print("I don't have data, please refer to my notion")
print("https://www.notion.so/Basic-Python-Grammar-c8a8c90209954a95812eef04cf2a9877?pvs=4")
print("nvm, lecturer gave the data.")

print()

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 97, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0


print()
print("Where are you error")

for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0

else:
    student_average_two_decimal = list()
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    for j in student_average:
        j = float(f"{j:.2f}")  # 여기까진 오케이
        student_average_two_decimal.append(j)
    print(student_average_two_decimal)

print()
print("Are you here?")

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 97, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0

for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0

else:
    student_average_two_decimal = list()
    student_average_integer = list()
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]

    for j in student_average:
        j = float(f"{j:.2f}")  # 여기까진 오케이
        student_average_two_decimal.append(j)

        for k in student_average_two_decimal:
            if k.is_integer() == True:
                k = int(k)
            else:
                continue
        student_average_integer.append(k)
    print(student_average_integer)

print("Yay!!!!!!!!!!!!!!!!!!!!!! Please check this file to check my effort\nhttps://github.com/jasonheesanglee/Practice/blob/main/Took%20me%202%20hours%20to%20solve%20this")

print()

print("To be continued in AI BASICS 2.py")