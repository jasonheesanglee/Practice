#import k as k

print("hello world")
print(3 + 4)
a = 3
b = 789
print(a * b)
a = "유진이"
b = "사랑해"
print(a + b)

a = [1, 2, 3]
b = ['life', 'is', 'short']
print(a[2] * b[2])
print(b[-1])

print(a[-2])
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1])
print(a[-1][2])
print(a[0:2])
print(a[2:4])
print(a[3][2])
print(len(a))
print(str(a[2]) + "hi")
del a[2]
print(a)
a.append(3)
print(a)
a.reverse()
print(a)
a.reverse()
print(a.index(3))
a = [1, 2, 3]
a.index(2)
print(a.index(2))
a = [1, 2, ['a', 'b', 'c']]
a.index(2)
print(a.index(2))
print(a.index(['a', 'b', 'c']))
a.insert(2, 5)
print(a)
a.remove(['a', 'b', 'c'])
print(a)
a.insert(2, 3)
a.insert(4, 3)
print(a)
a.remove(3)
print(a)
a.pop()
print(a)
a.pop(1)
print(a)
a.insert(2, 3)
a.insert(3, 5)
a.insert(4, 3)
print(a)
print(a.count(3))
print(a)
a.extend([4, 5])
print(a)
b = [8, 10]
a.extend(b)
print(a)
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
print(t2)
print(t4[0])

t1 = (1, 2, 'a', 'b')
print(t1[0] + t1[1])

a = 1
b = 2
print(a + b)
print(t1[1:])
print(len(t1))

dic = {'name': 'pey', 'phone': '010-4167-3900', 'birth date': '961128'}
print(dic)
a = {'jason', 'hi'}
print(a)

a = {1: 'a'}
a[2] = 'b'
print(a)
a[4] = 'c'
print(a)
a[3] = 'd'
print(a)
a['tyrieikls'] = 'name'
print(a)
del a['tyrieikls']
print(a)

grade = {'jason': 10, 'yujin': 100}
print(grade['jason'])
print(grade['yujin'])
print(grade['jason'] + grade['yujin'])
print(grade['jason'])

print(dic['name'])
print(dic['phone'])
print(grade.keys())
print(list(grade.keys()))
print(list(dic.keys()))
print(dic.keys())
# for k in dic.keys():
print(dic.values())
for k in dic.values():
    print(k)
print(dic.items())
for k in dic.items():
    print(k)
print(dic.items())
print(grade.items())
print(dic.get('name'))
print(dic.get('phone'))

a = {t1[1:2]: 'hi'}
print(a[t1[1:2]])

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
area = (base * height) / 2
print(area)

print(7 + 8.5)

print("a" + "b" + "c")
print("this " + "is " + "pretty " + "neat")

base = 6
height = 3
area = (base * height) / 2
print("The area of the triangle is: " + str(area))


def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)


greeting("Blake", "IT Support")


def print_seconds(hours, minutes, seconds):
    print(3600 * hours)
    print(60 * minutes)
    print(1 * seconds)


print_seconds(1, 2, 3)
print_seconds(56, 59, 48)

base = 6
height = 3
area = (base * height) / 2
print(area)


def area_triangle(base, height):
    return base * height / 2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))


def get_seconds(hours, minutes, seconds):
    return 3600 * hours + 60 * minutes + seconds


amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
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
print("Hello " + name + ". Your lucky number is " + str(number))

name = "Cameron"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))


def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))


lucky_number("Kay")
lucky_number("Cameron")

june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")


def month_days(month, days):
    print(month + " has " + str(days) + " days.")


month_days("June", 30)
month_days("July", 31)


def calculate(d):  # this is an equation for calcuating radius of a circle
    q = 3.14
    z = q * (d ** 2)
    print(z)


calculate(5)


def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)


circle_area(5)


def f1(x, y):
    z = x * y  # the area is base*height
    print("The area is " + str(z))


f1(5, 6)


def rectangle_area(base, height):
    square = base * height
    print("The area is " + str(square))


rectangle_area(5, 6)


def convert_distance(miles):
    return miles * 1.6


convert_distance(55)

km = convert_distance(55)

print("The distance in kilometers is " + str(km))
print("The round-trip in kilometers is " + str(km * 2))


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
print(square)  # 결국 출력되는 값은 똑같은데 왜 이게 정답이 아닌지? 궁금해~

print()

print(10 > 1)
print("cat" == "dog")
print(1 != 2)
print(2 != 2)

print()

print(1 == "1")

print()

print("cat" > "Cat")

print()

print("Yellow" > "Cyan" and "Brown" > "Magenta")
print(25 > 50 or 1 != 2)
print(not 42 == "Answer")

print()


def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")


hint_username("ja")

print()


def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    else:
        print("Valid username.")


hint_username("ja")
hint_username("volvstang")
hint_username("rlfls_rhfo")

print()


# is_positive 함수는 수신된 숫자가 양수이면 참을 반환해야 하고, 그렇지 않으면 없음을 반환합니다. 그렇게 하기 위해 부족한 부분을 채울 수 있습니까?
def is_positive(number):
    if number > 0:
        return print("True")
    else:
        return print("None")


is_positive(-5)
is_positive(0)
is_positive(13)

print()


# is_positive 함수는 수신된 숫자가 양수이면 참을 반환하고 그렇지 않으면 거짓을 반환해야 합니다. 그렇게 하기 위해 부족한 부분을 채울 수 있습니까?
def is_positive(number):
    if number > 0:
        return print("True")
    else:
        return print("False")


is_positive(-5)
is_positive(0)
is_positive(13)

print()


def is_even(number):
    if number % 2 == 0:
        return print("True")
    return print("False")
    # else:
    #   return print("False") 와 동일함


is_even(5)
is_even(4)

print()

print("without elif")


def hint_username(username):
    if len(username) < 3:
        print("Invalid Username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid Username. Must be at most 15 characters long")
        else:
            print("Valid Username.")


hint_username("volvstang")
hint_username("vo")
hint_username("jasonthegreatest")

print()
print("with elif")


def hint_username(username):
    if len(username) < 3:
        print("Invalid Username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid Username. Must be at most 15 characters long")
    else:
        print("Valid Username.")


hint_username("volvstang")
hint_username("vo")
hint_username("jasonthegreatest")

print()

print("number_group 함수는 수신된 숫자가 양수이면 \"양수\", 음수이면 \"음수\", 0이면 \"0\"을 반환해야 합니다. 그렇게 하기 위해 부족한 부분을 채울 수 있습니까?")


def number_group(number):
    if number > 0:
        return print("Positive")
    elif number < 0:
        return print("Negative")
    else:
        return print("Zero")


number_group(10)  # Should be Positive
number_group(0)  # Should be Zero
number_group(-5)  # Should be Negative

# 조건부 치트 시트
# 이전 비디오에서 값을 비교할 수 있는 내장 파이썬 연산자와 값을 결합하는 데 사용할 수 있는 논리 연산자를 살펴보았습니다. 또한 if-else-elif 블록에서 연산자를 사용하는 방법도 배웠습니다.
# 배울 것이 많지만 연습을 하면 모든 것을 더 쉽게 기억할 수 있습니다. 그 동안 이 편리한 치트 시트는 필요한 모든 정보를 한 눈에 제공합니다.

# 비교 연산자
# a == b: a는 b와 같습니다.
# a != b: a는 b와 다릅니다.
# a < b: a는 b보다 작습니다.
# a <= b: a는 b보다 작거나 같습니다.
# a > b: a는 b보다 큽니다.
# a >= b: a는 b보다 크거나 같습니다.
# 논리 연산자
# a and b: a와 b가 모두 참이면 참입니다. 그렇지 않으면 거짓입니다.
# a or b: a 또는 b 또는 둘 다 참이면 참입니다. 둘 다 거짓이면 거짓입니다.
# not a: a가 거짓이면 참, 참이면 거짓입니다.

print()

print("A dog" > "A mouse")
print(9999 + 8888 > 100 * 100)

# Question 5
# 파일 시스템의 블록 크기가 4096바이트인 경우, 이는 1바이트로만 구성된 파일이 여전히 4096바이트의 스토리지를 사용한다는 것을 의미합니다.
# 4097바이트로 구성된 파일은 4096*2=8192바이트의 스토리지를 사용합니다.
# 이를 유념하여 주어진 크기의 파일을 저장하는데 필요한 총 바이트 수를 계산하는 아래의 calculate_storage 함수의 공백을 채울 수 있습니까?


print()
print("진짜 질문에 대한 답만 구한 케이스")


def calculate_storage(filesize):
    block_size = 4096
    partial_block_remainder = filesize % block_size
    if filesize < 4097:
        return 4096
    elif partial_block_remainder > 0:
        return 8192
    return 8192


print(calculate_storage(1))
print(calculate_storage(4096))
print(calculate_storage(4097))
print(calculate_storage(8192))
print(calculate_storage(16397))

print()
print("\"자 나는 어떠한 값을 넣어도 자동화돼서 수치가 들어가게 하고싶다\"라는 포부를 갖고 코드를 짜본 케이스")


# 자 나는 어떠한 값을 넣어도 자동화돼서 수치가 들어가게 하고싶다.

def calculate_storage(filesize):
    block_size = 4096  # 고정 블록 값
    partial_block_remainder = filesize % block_size  # 나머지
    number_of_block = filesize // block_size  # 몫
    if partial_block_remainder == 0:  # 나머지가 0일 때
        return filesize
    elif partial_block_remainder > 0:  # 나머지가 0보다 클 때
        return (number_of_block + 1) * block_size


print(calculate_storage(1))
print(calculate_storage(4096))
print(calculate_storage(4097))
print(calculate_storage(8192))
print(calculate_storage(16397))
print(calculate_storage(594156313))

print("#이걸 내가 해내다니ㅋㅋㅋㅋㅋㅋㅋ")

print()


# Question 1
# 빠진 부분을 채워서 함수 작성을 완료하십시오. color_translator 함수는 색상 이름을 받아 16진수 값을 출력합니다. 현재 3가지 추가 기본 색상(red(빨간색), green(녹색), blue(파란색))만 지원하므로 다른 모든 색상에 대해서는 ‘unknown’(알 수 없음)으로 리턴합니다.

def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color


print(color_translator("blue"))  # Should be #0000ff
print(color_translator("yellow"))  # Should be unknown
print(color_translator("red"))  # Should be #ff0000
print(color_translator("black"))  # Should be unknown
print(color_translator("green"))  # Should be #00ff00
print(color_translator(""))  # Should be unknown

print()

# 이 파이썬 표현식의 값은 무엇입니까? "big" > "small"
print("big" > "small")

print()


# 한 수업의 학생들은 Pass/Fail(합격/불합격)로 성적을 받습니다. 100점 만점에 60점 이상은 ‘Pass’(합격)를 의미합니다. 이보다 낮은 점수는 ‘Fail’(불합격)입니다. 또한 95점이 넘는 점수(포함되지 않음)는 ‘Top Score’(상위 등급)입니다. 적절한 등급이 리턴되도록 함수를 채우십시오.

def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade


print(exam_grade(65))  # Should be Pass
print(exam_grade(55))  # Should be Fail
print(exam_grade(60))  # Should be Pass
print(exam_grade(95))  # Should be Pass
print(exam_grade(100))  # Should be Top Score
print(exam_grade(0))  # Should be Fail

print()

print(11 % 5)

print()


# format_name 함수의 본문 작성을 완성합니다. 이 함수는 first_name 및 last_name 매개변수를 받은 다음 올바른 형식의 문자열을 리턴합니다.
def format_name(first_name, last_name):
    if first_name and last_name:
        return ("Name: " + last_name + ", " + first_name)
    elif last_name:
        return ("Name: " + last_name)
    elif first_name:
        return ("Name: " + first_name)
    else:
        return ""


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

print()


# 3개의 단어를 비교하기 위해 longest_word 함수를 사용합니다. 가장 많은 문자가 있는 단어를 리턴해야 하며 길이가 같은 경우 목록의 첫 번째를 사용합니다. 이렇게 하려면 빈칸을 채우십시오.

def longest_word(word1, word2, word3):
    if len(word1) == len(word2) and len(word2) == len(word3):
        word = word1
    elif len(word1) > len(word2) and len(word2) > len(word3):
        word = word1
    elif len(word2) > len(word3) and len(word3) > len(word1):
        word = word2
    else:
        word = word3
    return (word)


print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

print()


def sum(x, y):
    return (x + y)


print(sum(sum(1, 2), sum(3, 4)))

print((10 >= 5 * 2) and (10 <= 5 * 2))

print ()

x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x+1
print("x=" + str(x))

print()

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1 #same as x = x+1
    print("Done")
attempts(5)

print()
print("get username, please check #codes")
#username = get_username()
#while not valid_username(username):
#   print("Invalid username")
#    username = get_username()

print()

my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable +=1

print()

x = 1
sum = 0
while x < 10:
    sum += x
    x += 1

product = 1
while x < 10:
    product = product * x
    x += 1

print (sum, product)

print("error above as I didn't initialized x")

x = 1
sum = 0
while x < 10:
    sum += x
    x += 1

x = 1
product = 1
while x < 10:
    product = product * x
    x += 1

print (sum, product)

print ()

def count_down(start_number):
    current = 3
    while current > 0:
        print(current)
        current -= 1
    print("Zero!")

count_down(3)

print()

print("Infinite Loop")
print()

if x != 0:
    while x % 2 == 0:
        x = x/2
while x != 0 and  x % 2 == 0:
    x = x / 2

print(x)

print()

def print_range(start, end):
    n = start
    while n <= end:
        print(n)
        n += 1 #이걸 추가 안하면 계에에에에에속 1만 반복됨
print_range(1, 5)


print()

def print_prime_factors(number):
    factor = 2
    while factor <= number:
        if number % factor == 0:
            print(factor)
            number = number / factor
        else:
            factor += 1
    return "Done"

print_prime_factors(100)

print()


def sum_divisors(n):
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            sum += i


# Return the sum of all divisors of n, not including n
    return sum - n

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

print()

def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier
		# What is the additional condition to exit out of the loop?
		if result > 25:
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24

print()

for x in range(5):
    print (x)

print()


def square(n):
    return n*n
def sum_square(x):
    sum = 0
    for n in range(x):
        sum += n*n
    return sum

print(sum_square(10))

print()

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

print()

values = [23,52,59,37,48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("Total sum: " + str(sum) + " - Average:" + str(sum/length))

print()

product = 1
for n in range(1,10):
    product = product * n

print (product)

print()

def factorial(n):
    result = 1
    for i in range (1,(n+1)):
        result =  result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

print()

def to_celsius(x):
    return (x-32)*5/9
for x in range (0,101,10):
    print(x, to_celsius(x))

print()

print("loops inside of loops - nested for loops")

print()

for left in range(7):
    for right in range(left, 7):
        print("["+ str(left) + "|" + str(right) + "]", end= "")
    print()

print()

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

print()

#for element1 in long_list:
#    for element2 in long_list:
#        do_something(element1, element2)

for x in [25]:
    print(x)

print()

for x in range(25):
    print(x)

print()

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)
greet_friends (['Taylor','Luisa','Jamaal','Eli'])
print()
greet_friends("Barry")


#def validate_users(user):
#    for user in users:
#        if is_valid(user):
#            print(user + " is valid")
#        else:
#            print(user + "is invalid")
#validate_users(["purplecat"])

print()

print("Recursion")
print("base case")
print()

def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

factorial (4)

print()

def sum_positive_numbers(n):
    if n<2:
        return 1
    return n + sum_positive_numbers(n-1)
print(sum_positive_numbers(3))
print(sum_positive_numbers(5))

print()

print("Maximum Depth Reached (1000), remove # from the code below if want to check the Error message")
#def factorial(n):
#    if n<2:
#        return 1
#    return n * factorial(n-1)
#factorial (1000)

print("haha")

for x in range (1,10,3):
    print(x)
print("x")

for x in range(10):
    for y in range(x):
        print(y)

print()
print()

def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > start:
				return_string += ","
			break
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < start:
				return_string += ","
			break
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

print()
print("double_word 함수를 수정하여 동일한 단어를 두 번 반복하고 그 뒤에 새로 추가된 단어의 길이를 반환하도록 합니다. 예를 들어, double_word(\"hello\")는 hellohello10을 반환해야 합니다.")
def double_word(word):
    return word + word + str(len(word)*2)

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

print()
print("string indexing")
name = "Jaylen"
print(name[1])
print(name[0])
print(name[len(name)-1])
print()
text = "Random string with a lot of characters"
print(name[len(name)-5])
print(text[len(text)-13])

print()
print("string index question")
def first_and_last(message):
    if message:
        if message == "" or message[0] == message[-1]:
            return True
        else:
            return False
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
print()
print("simple way to do it")
def first_and_last(message):
    return message == "" or message[0] == message[-1]

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
print("is there one? I don't find this correct")
print("oh nevermind, this was the correct one! :)")