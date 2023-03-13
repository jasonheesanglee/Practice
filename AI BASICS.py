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
