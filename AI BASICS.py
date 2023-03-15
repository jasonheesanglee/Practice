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