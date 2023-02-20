import k as k

print ("hello world")
print (3+4)
a = 3
b = 789
print (a*b)
a = "유진이"
b = "사랑해"
print (a+b)

a = [1, 2, 3]
b = ['life', 'is', 'short']
print (a[2] * b[2])
print(b[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print (a[-2])
print (a[-1])
print (a[-1][2])
print (a[0:2])
print (a[2:4])
print (a[3][2])
print (len(a))
print (str(a[2]) + "hi")
del a[2]
print (a)
a.append(3)
print (a)
a.reverse()
print (a)
a.reverse()
print(a.index(3))
a = [1, 2, 3]
a.index(2)
print(a.index(2))
a = [1, 2, ['a', 'b', 'c']]
a.index(2)
print (a.index(2))
print (a.index(['a', 'b', 'c']))
a.insert(2, 5)
print(a)
a.remove(['a', 'b', 'c'])
print(a)
a.insert(2,3)
a.insert(4,3)
print(a)
a.remove(3)
print(a)
a.pop()
print (a)
a.pop(1)
print (a)
a.insert(2, 3)
a.insert(3, 5)
a.insert(4, 3)
print (a)
print(a.count(3))
print (a)
a.extend([4, 5])
print (a)
b = [8, 10]
a.extend(b)
print (a)
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
print (t2)
print(t4 [0])

t1 = (1, 2, 'a', 'b')
print(t1[0] + t1[1])

a = 1
b = 2
print (a + b)
print (t1[1:])
print (len(t1))

dic = {'name':'pey', 'phone':'010-4167-3900', 'birth date':'961128'}
print (dic)
a = {'jason','hi'}
print (a)

a = {1:'a'}
a[2] = 'b'
print (a)
a[4] = 'c'
print (a)
a[3] = 'd'
print (a)
a['tyrieikls'] = 'name'
print (a)
del a['tyrieikls']
print (a)

grade = {'jason':10, 'yujin':100}
print (grade['jason'])
print (grade['yujin'])
print (grade['jason'] + grade['yujin'])
print (grade['jason'])

print (dic['name'])
print (dic['phone'])
print (grade.keys())
print(list(grade.keys()))
print(list(dic.keys()))
print (dic.keys())
# for k in dic.keys():
print (dic.values())
for k in dic.values():
    print(k)
print (dic.items())
for k in dic.items():
    print(k)
print (dic.items())
print (grade.items())
print (dic.get('name'))
print (dic.get('phone'))


a = {t1[1:2]:'hi'}
print (a [t1[1:2]])

print(dic.get('nokey'))
print(dic.get('nalsdj', '값이 존재하지 않습니다'))
print(dic.get('name', '값이 존재하지 않습니다'))


print(type("a"))
print(type(2))
print(type(2.5))

print(type(25534452))

length = 10
width = 2
area = length * width
print(area)

base = 5
height = 3
area = (base*height)/2
print(area)

print(7+8.5)

print("a"+"b"+"c")
print("this " + "is " + "pretty " + "neat")

base = 6
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area))

def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)

greeting("Blake", "IT Support")


def print_seconds(hours, minutes, seconds):
    print(3600*hours)
    print(60*minutes)
    print(1*seconds)

print_seconds(1,2,3)
print_seconds(56,59,48)


base = 6
height = 3
area = (base*height)/2
print (area)

def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

def greeting(name):
    print("Welcome, " + name)

result = greeting("Christine")
print(result)


name = "Kay"
number = len(name) * 9
print ("Hello " + name + ". Your lucky number is " + str(number))

name = "Cameron"
number = len(name) * 9
print ("Hello " + name + ". Your lucky number is " + str(number))

def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron")

june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print ("July has " + str(july_days) + " days.")

def month_days(month, days):
    print(month + " has " + str(days) + " days.")

month_days("June", 30)
month_days("July", 31)

def calculate(d): #this is an equation for calcuating radius of a circle
    q = 3.14
    z = q * (d ** 2)
    print(z)

calculate(5)

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)


def f1(x,y):
    z = x*y #the area is base*height
    print ("The area is " + str(z))
f1(5,6)

def rectangle_area(base, height):
    square = base*height
    print("The area is " + str (square))
rectangle_area(5,6)


def convert_distance(miles):
    return miles*1.6
convert_distance(55)

km = convert_distance(55)

print("The distance in kilometers is " + str(km))
print("The round-trip in kilometers is " + str(km*2))


def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1

smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1

square = order_numbers(100, 99)
print(square) #결국 출력되는 값은 똑같은데 왜 이게 정답이 아닌지? 궁금해~

print( )

print(10>1)
print("cat"=="dog")
print(1!=2)
print(2!=2)

print( )

print(1=="1")

print( )

print("cat">"Cat")

print( )

print("Yellow" > "Cyan" and "Brown" > "Magenta")
print(25 > 50 or 1!=2)
print(not 42 == "Answer")

print( )

def hint_username(username):
     if len(username) < 3:
         print("Invalid username. Must be at least 3 characters long")
hint_username("ja")

print( )

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    else:
        print("Valid username.")

hint_username("ja")
hint_username("volvstang")
hint_username("rlfls_rhfo")

print( )

#is_positive 함수는 수신된 숫자가 양수이면 참을 반환해야 하고, 그렇지 않으면 없음을 반환합니다. 그렇게 하기 위해 부족한 부분을 채울 수 있습니까?
def is_positive(number):
  if number > 0:
    return print("True")
  else:
    return print("None")

is_positive(-5)
is_positive(0)
is_positive(13)

print( )

#is_positive 함수는 수신된 숫자가 양수이면 참을 반환하고 그렇지 않으면 거짓을 반환해야 합니다. 그렇게 하기 위해 부족한 부분을 채울 수 있습니까?
def is_positive(number):
    if number>0:
        return print("True")
    else:
        return print("False")
is_positive(-5)
is_positive(0)
is_positive(13)

print( )

def is_even(number):
    if number % 2 == 0:
        return print("True")
    return print("False")
    # else:
    #   return print("False") 와 동일함

is_even(5)
is_even(4)

print( )

print("without elif")

def hint_username(username):
    if len(username) < 3:
        print("Invalid Username. Must be at least 3 characters long")
    else:
        if len (username)>15:
            print("Invalid Username. Must be at most 15 characters long")
        else:
            print("Valid Username.")

hint_username("volvstang")
hint_username("vo")
hint_username("jasonthegreatest")

print( )
print("with elif")

def hint_username(username):
    if len(username) < 3:
        print("Invalid Username. Must be at least 3 characters long")
    elif len (username)>15:
        print("Invalid Username. Must be at most 15 characters long")
    else:
        print("Valid Username.")

hint_username("volvstang")
hint_username("vo")
hint_username("jasonthegreatest")

print( )

print("number_group 함수는 수신된 숫자가 양수이면 \"양수\", 음수이면 \"음수\", 0이면 \"0\"을 반환해야 합니다. 그렇게 하기 위해 부족한 부분을 채울 수 있습니까?")
def number_group(number):
  if number > 0:
    return print("Positive")
  elif number < 0:
    return print("Negative")
  else:
    return print("Zero")

number_group(10) #Should be Positive
number_group(0) #Should be Zero
number_group(-5) #Should be Negative

#조건부 치트 시트
#이전 비디오에서 값을 비교할 수 있는 내장 파이썬 연산자와 값을 결합하는 데 사용할 수 있는 논리 연산자를 살펴보았습니다. 또한 if-else-elif 블록에서 연산자를 사용하는 방법도 배웠습니다.
#배울 것이 많지만 연습을 하면 모든 것을 더 쉽게 기억할 수 있습니다. 그 동안 이 편리한 치트 시트는 필요한 모든 정보를 한 눈에 제공합니다.

#비교 연산자
#a == b: a는 b와 같습니다.
#a != b: a는 b와 다릅니다.
#a < b: a는 b보다 작습니다.
#a <= b: a는 b보다 작거나 같습니다.
#a > b: a는 b보다 큽니다.
#a >= b: a는 b보다 크거나 같습니다.
#논리 연산자
#a and b: a와 b가 모두 참이면 참입니다. 그렇지 않으면 거짓입니다.
#a or b: a 또는 b 또는 둘 다 참이면 참입니다. 둘 다 거짓이면 거짓입니다.
#not a: a가 거짓이면 참, 참이면 거짓입니다.

print( )

print("A dog" > "A mouse")
print(9999+8888 > 100*100)

print( )

def calculate_storage(filesize):
    block_size = 4096
    partial_block_remainder = filesize % block_size
    if filesize < 4097:0
        return 4096
    elif partial_block_remainder > 0:
        return 8192
    return 8192
#자 나는

print(calculate_storage(1))
print(calculate_storage(4096))
print(calculate_storage(4097))
print(calculate_storage(8192))
print(calculate_storage(16384))