import sys
print(sys.getsizeof("a"), sys.getsizeof("ab"), sys.getsizeof("abc"))
print()

a = "abcde"
print(a[0], a[4])
print(a[-1], a[-5])
print()

a = "Artificial Intelligence and Machine Learning"
print(a[0:6], " AND ", a[-9:])
print(a[:])
print(a[-50:50])
print(a[::2], " AND ", a[::-1])

a = "TEAM"
b = "LAB"

print(a + b)
print("T" in a)
print("L" in a)

print()

title = "TEAMLAB X Upstage"
print(title.lower())
print(title.split())
print(title.isdigit())
print(title.title())
print(title.count("a"))
print("12345".isdigit())

print("It\'s OK")

a = """
Happy New Year,
 This is a class"""
print(a)
b = "\n Happy New Year,\n This is a class"
print(b)

print()

raw_string = "This is my fourth time going through Python basics. \n for real"
print(raw_string)
raw_string = r"This is my fourth time going through Python basics. \n for real"
print(raw_string)

trial = "This is a \
trial"
print(trial)

print()
f = open("yesterday.txt", "r")
yesterday = ""
while True:
    line = f.readline()
    if not line:
        break
    yesterday = yesterday + line.strip() + "\n"
f.close()
print(type(yesterday))

lower_yesterday = yesterday.lower()

print(yesterday.count("yesterday"))
print(yesterday.count("Yesterday"))
print(lower_yesterday.count("yesterday"))
print()

def swap_value(x, y):
    temp = x
    x = y
    y = temp

def swap_offset(offset_x, offset_y):
    temp = ex[offset_x]
    ex[offset_x] = ex[offset_y]
    ex[offset_y] = temp

def swap_reference(list, offset_x, offset_y):
    temp = list[offset_x]
    list[offset_x] = list[offset_y]
    list[offset_y] = temp

ex = [1, 2, 3, 4, 5]
swap_value(ex[0], ex[1])
print(ex)

ex = [1, 2, 3, 4, 5]
swap_offset(0,1)
print(ex)

ex = [1, 2, 3, 4, 5]
swap_reference(ex, 3, 4)
print(ex)

print()

def test(t):
    print(x)
    t = 20
    print("In function :", t)

x = 10
test(x)
# print(t)

print()

def test(t):
    t = 20
    print("In Function :", t)
x = 10
print("Before :", x)
test(x)
print("After :", x)

print()

def f():
    s = "I love London"
    print(s)
s = "I love Paris"
f()
print(s)

def f():
    global s
    s = "I love London"
    print(s)
s = "I love Paris"
f()
print(s)
print()
def calculate(x, y):
    total = x +y
    print("In Function :")
    print("a:", str(a) + ", b:", str(b) + ", a+b", str(a+b) + ", total :", str(a+b))
    return total

a = 5
b = 7
total = 0
print("In program - 1")
print("a:", str(a) + ", b:", str(b) + ", a+b" + str("a+b"))
print()
sum = calculate(a, b)
print("After Calculation")
print("Total :", str(total) + ", Sum :", str(sum))

