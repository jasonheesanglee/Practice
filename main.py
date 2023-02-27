
print("Coursera - Google Python")
print("Christine Rafla")
print("Hello, world!")

print()
print(type("a"))
print(type(2))
print(type(2.5))

print(type(25534452))

print()

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


print()
color = "Orange"
print(color[1:4])

fruit = "pineapple"
print(fruit[:4])
print(fruit[4:])

print()
print("creating new string")
print()

message = "A kong string with a silly typo"
print(message)
#message[2] = "l"

new_message = message[0:2] + "l" + message[3:]
print(new_message)
message = "this is a new message"
print(message)

print()
pets = "Cats & Dogs"
print(pets.index("&"))
print(pets.index("C"))
print(pets.index("Dog"))
print(pets.index("s"))
#print(pets.index("x"))
print("Dragons" in pets)
if "Cats" in pets:
    print("Wohahaha")

print()
def replace_domain(email, old_domain, new_domain):
    if"@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
print(replace_domain("heesang.lee@atheneum-partners.com","atheneum-partners.com","atheneum.ai"))

print()
print("Mountains".upper())
print("Mountains".lower())

print()
answer = 'YES'
if answer.lower() == "yes":
    print("User says yes")

print()
print(" yes ".strip())
print(" yes ".lstrip())
print(" yes ".rstrip())

print()
print("The number of times e occurs in this string is 4".count("e"))

print()
print("Forest".endswith("rest"))

print()
print("Forest".isnumeric())
print("12345".isnumeric())

print()
print(int("12345")+int("54321"))

print()
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))
print(("This is another example").split())
print(("Thismismanothermexample").split("m"))


print()
print("sample question to take out first letter of each word then capitalize it")
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

print()
print("format method")
name = "Manny"
number = len(name)*3
print("Hello {}, your lucky number is {}".format(name, number))

print()
print("Your lucky number is {number}, {name}".format(name=name, number=len(name)*3))

print()
print("format sample question")
print()
def student_grade(name, grade):
	return "{} received {}% on the exam".format(name,grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

print()
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

print()
print("recap on celius example with format to reduce decimals")
def to_celcius(x):
    return(x-32)*5/9
for x in range(0,101,10):
    print(x, to_celcius(x))

print()
print("now look at below")
def to_celcius(x):
    return(x-32)*5/9
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celcius(x)))
print()
print(":>숫자 이거는 오른쪽으로 숫자만큼 정렬")


#Expr   의미 예시

#{:d}   정수 값        '{:d}'.format(10.5) → '10'
#{:.2f} 소수점이 많은 부동 소수점       '{:.2f}'.format(0.5) → '0.50'
#{:.2s} 많은 문자가 포함된 문자열         '{:.2s}'.format('Python') → 'Py'
#{:<6s} 많은 공백의 왼쪽으로 정렬된 문자열  '{:<6s}'.format('Py') → 'Py    '
#{:>6s} 많은 공백의 오른쪽으로 정렬된 문자열    '{:>6s}'.format('Py') → '    Py'
#{:^6s} 많은 공백의 가운데에 있는 문자열       '{:^6s}'.format('Py') → '  Py  '

print("연습문제 1")
print("is_palindrome 함수는 문자열이 회문인지 확인합니다.")
print("회문은 왼쪽에서 오른쪽으로 읽거나 오른쪽에서 왼쪽으로 읽어도 똑같이 읽히며, 공백을 생락하고 대문자를 사용하지 않는 문자열입니다.")
print("회문의 예로는 kayak(카약) 및 radar(레이더)와 같은 단어와 ‘Never Odd or Even’(홀수 또는 짝수 아님)과 같은 구문이 있습니다.")
print("전달된 문자열이 회문이면 True(참)를 리턴하고 그렇지 않으면 False(거짓)를 리턴하도록 이 함수의 빈칸을 채우십시오. ")

def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string.strip():
		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
		new_string = new_string+letter.replace(" ", "")
		reverse_string = letter.replace(" ","") + reverse_string
	# Compare the strings
	if new_string.lower() == reverse_string.lower():
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
print()
print("OR")
print()
def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    for letter in input_string.lower():
        if letter != " ":
            new_string = new_string + letter
            reverse_string = letter + reverse_string
    if new_string == reverse_string:
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

print()
print("연습문제 2")
print("format 메서드를 사용하여 convert_distance 함수의 공백을 채워서 Y가 소수점 이하 1자리만 가지면서 ‘X miles equals Y km’(X마일은 Ykm와 같다)라는 구문을 리턴하도록 합니다.")
print("예를 들어, convert_distance(12)는 ‘12 miles equals 19.2 km’(12마일은 19.2km와 같다)를 리턴해야 합니다.")
print()
def convert_distance(miles):
	km = miles * 1.6
	result = "{} miles equals ${:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

print()
print("연습문제 3")
print("Weather = \"Rainfall\"이라는 문자열 변수가 있는 경우 다음 중 \"f\" 앞의 하위 문자열 또는 모든 문자를 인쇄하는 것은 무엇입니까?")
Weather = "Rainfall"
print(Weather[:4])

print()
print("연습문제 4")
print("first_name과 last_name의 첫 번째 이니셜 다음에 마침표를 리턴하도록 format 메서드를 사용하여 nametag 함수의 공백을 채우십시오.")
print("예를 들어, nametag(\"Jane\", \"Smith\")는 ‘Jane S.’를 리턴해야 합니다.")
def nametag(first_name, last_name):
    return ("{}".format(first_name[0].upper()) + first_name[1:] + " {}.".format(last_name[0]).upper())

print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."

print()
print("연습문제 5")
print("replace_ending 함수는 문장의 이전 문자열을 새 문자열로 바꿉니다. ")
print("단, 문장이 이전 문자열로 끝나는 경우에만 가능합니다.")
print("문장에 이전 문자열이 두 번 이상 있는 경우 전체가 아닌 끝에 있는 문자열만 대체됩니다.")
print("예를 들어, replace_ending(“abcabc”, “abc”, “xyz”)은 xyzxyz 또는 xyzabc가 아니라 abcxyz로 리턴합니다.")
print("문자열 비교는 대소문자를 구분하므로 replace_ending(“abcabc\", \"ABC\", \"xyz\")는 abcabc(변경 사항 없음)를 리턴해야 합니다.")
print()

def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    sentences = sentence.split()
    if sentences[-1] == old:
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        sentences[-1] = new
        new_sentence = " ".join(sentences)
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"


print()
print("list")

x = ["Now", "we", "are", "cooking!"]
print(type(x))
print(x)
print("length of the list: ", len(x))

print ("are" in x)
print (x[0])
print(x[3])
print(x[-1])

print(x[1:3])
print(x[:2])
print(x[2:])

print()
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
print(fruits)
fruits.append("kiwi")
print(fruits)
print()
fruits.insert(0,"Orange")
print(fruits)

fruits.insert(25,"peach")
print(fruits)
fruits.remove("Melon")
print(fruits)
print(fruits.pop(3))
fruits[2]= "Strawberry"
print(fruits)

print()
print("skip element question")
print("skip_elements 함수는 첫 번째 요소부터 시작하여 입력 목록의 다른 모든 요소를 포함하는 목록을 반환합니다. 입력 목록을 반복하기 위해 for 루프를 사용하여 해당 작업을 수행하려면 이 함수를 완료하십시오.")
print("")
def skip_elements(elements):
	new_list = []
	for element in elements[::2]:
		new_list.append(element)
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

print()

Fullname = ("Grace", "M", "Harper")
print()
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes *60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
print(result)
print(type(result))

print()
hours, minutes, seconds = result
print(hours,minutes,seconds)
hours, minutes, seconds = convert_seconds(1000)
print (hours, minutes, seconds)

print()
print("Tuple Practice Questions")
print("튜플을 사용하여 파일에 대한 정보(이름, 형식 및 크기(바이트))를 저장해 보겠습니다. 이 코드의 공백을 채워 소수점 이하 2자리까지 크기를 킬로바이트(킬로바이트는 1024바이트)로 반환합니다.")
def file_size(file_info):
	Name, Type, Size = file_info
	return("{:.2f}".format(Size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

print()
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total Characters: {}, Average Length: {}".format(chars, chars/len(animals)))

print()
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index+1, person))

print()
print("enumerate practice question")
print("이 빠른 연습에서 직접 열거 함수를 사용해 보십시오. skip_elements 함수를 완료하여 목록에서 다른 모든 요소를 반환합니다. 이번에는 요소가 짝수 위치에 있는지 또는 홀수 위치에 있는지 확인하기 위해 열거 함수를 사용합니다.")

def skip_elements(elements):
	# code goes here
	element = []
	for i, e in enumerate(elements):
		if i % 2 == 0:
			element.append(e)
	return element

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name,email))
    return result

print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

print()

multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)
multiples = [x*7 for x in range(1,11)]
print(multiples)

print()
languages = ["Python", "Pearl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)
z = [x for x in range(0,101) if x%3 == 0]
print(z)

print()
print("practice question")
print("odd_numbers 함수는 1과 n 사이의 홀수 목록을 반환합니다. 목록 이해를 사용하여 함수의 공백을 채우십시오. 힌트: 목록 및 범위 카운터는 0에서 시작하여 한계에서 1을 뺀 값에서 끝납니다.")
def odd_numbers(n):
	return [x for x in range(1,n+1,2) if x%1 == 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

print()
print("Practice Quiz")
print()
print("Practice Quiz 1")
print("파일 이름 목록이 있는 상태에서 확장자 hpp로 된 모든 파일 이름을 확장자 h로 이름을 바꾸고자 합니다.")
print("이를 수행하기 위해 새 파일 이름으로 구성된 newfilenames라는 새 목록을 생성하려고 합니다.")
print("for 루프나 리스트 컴프리헨션과 같이 지금까지 배운 메서드를 사용하여 코드의 빈칸을 채우십시오.")

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
print("program"+"."+"c", "studio"+"."+"h", "sample"+"."+"h", "a"+"."+"out", "math"+"."+"h", "hpp"+"."+"out")
print("이건 당연히 되겠지")
print()
print()

def replace_extension(filename,old_extension,new_extension):
    if"." + old_extension in filename:
        filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
        index = filenames.index("."+ old_extension)
        newfilenames = filenames[:index] + "." + new_extension
        return newfilenames
    return filename
print(replace_extension(filenames,"hpp","h"))
print()
print("왜 위에께 안돼...?")

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
firstname = [firsthalf.split(".",1)[0] for firsthalf in filenames]
secondname = [secondhalf.split(".",1)[1] for secondhalf in filenames]

print(str(firstname),".",secondname)

print("이게 안돼...?")

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
for filename in filenames:
    for firsthalf in filename:
        firstname = filename.split(".",1)[0]
    for secondhalf in filename:
        secondname = filename.split(".",1)[1]
        secondname.replace("hpp","h")
print(filename)

print("이건 또 왜 이렇게 나와...")

print()
filenames = 0
filename = 0
print("차근차근해보자고")
print("일단 전체 리스트부터 작은 리스트로 쪼개주기")
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
for filename in filenames:
    oldfilenames = filename.split(".")
    newfilenames = oldfilenames[1].replace("hpp","h")
    print(oldfilenames[0]+"."+newfilenames)
print("adsljdfl;kasl;ask;asdkl;askf;lk 와 진짜... 드디어.... 이 문제로 2시간 잡아먹었네... 연습문제 27번이랑 30번, 그리고 구글에 경의를 표합니다")
print()
print("아니 근데 잠깐만... 이거를 리스트로 다시 만들어야되잖아...")

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
for filename in filenames:
    oldfilenames = filename.split(".")
    newfilenames = oldfilenames[1].replace("hpp","h")
    print([oldfilenames[0]+"."+newfilenames])

print("이건 아니고...")
print()
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
new_name = []
for filename in filenames:
    oldfilenames = filename.split(".")
    newfilenames = oldfilenames[1].replace("hpp","h")
    new_name.extend([oldfilenames[0]+"."+newfilenames])
print(new_name)
print()
print("응...??")
print("된건가...?")
print("됐다... 마지막 코드들 보니까... 내가 처음에 괜히 복잡하게 생각했었네...")

word = "python"
print(word[0])


print("Practice Quiz 2")
print("텍스트를 피그 라틴으로 변경하는 함수를 생성해보겠습니다.")
print("각 단어의 첫 번째 글자를 끝으로 옮기고 끝에 ‘ay’를 덧붙여 수정하는 방식으로 간단하게 텍스트를 변환합니다. 예를 들어, python은 ythonpay가 됩니다.")

def pig_latin(text):
    say = ""
    # Separate the text into words
    newpiglatinword = []
    words = text.split(" ")

    for word in words:
        # Create the pig latin word and add it to the list
        newpiglatinword.extend(word[1:] + word[0] + "ay")
        # Turn the list back into a phrase
    return newpiglatinword


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"

print("자... 아웃풋이 맞긴 맞는데... 왜 다 분리됐냐... 다시 해보자")


def pig_latin(text):
    say = " "
    # Separate the text into words
    newpiglatinword = []
    words = text.split(" ")
    for word in words:
        # Create the pig latin word and add it to the list
        word = word[1:] + word[0] + "ay"
        newpiglatinword.append(word)
        # Turn the list back into a phrase
    return say.join(newpiglatinword)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"

print("음.. 일단 구글링으로 해봤네... 오케... 어펜드랑... 조인")
print("그럼 원래 내 코드에 append만 붙여볼까?")
print()

def pig_latin(text):
    say = ""
    # Separate the text into words
    newpiglatinword = []
    words = text.split(" ")

    for word in words:
        # Create the pig latin word and add it to the list
        newpiglatinword.append(word[1:] + word[0] + "ay")
        # Turn the list back into a phrase
    return newpiglatinword


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"
print("아 이렇게되면 아예 separate 리스트가 되는구나")


print()
print("Practice Quiz 3")
print("Linux 시스템에서 파일의 권한은 소유자, 그룹 및 기타의 세 권한에 대한 읽기, 쓰기 및 실행의 세 가지 세트로 나뉩니다.")
print("각각의 세 가지 값은 각 권한을 합한 8진수로 표현할 수 있으며, 4는 읽기, 2는 쓰기, 1은 실행으로 표현됩니다.")
print("또는 권한이 부여되지 않은 경우 r, w, x 또는 - 문자를 사용하여 문자열로 작성될 수 있습니다.")
print("예: 640은 소유자에 대한 읽기/쓰기, 그룹에 대한 읽기, 다른 사람에 대한 권한 없음을 뜻합니다.")
print("문자열로 변환하면 ‘rw-r-----’과 같습니다.")
print()
print("755는 소유자에 대한 읽기/쓰기/실행이고 그룹 및 기타에 대한 읽기/실행입니다. 문자열로 변환하면 ‘rwxr-xr-x’입니다. 코드가 권한을 8진수에서 문자열 형식으로 변환하도록 빈칸을 채우십시오.")

print("??? 8진수요?")


def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for digits in [int(n) for n in str(octal)]: #value_letters = 755
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digits >= value:
                result += letter
                digits -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------

print("이야 이거 문자열이 무슨 의미인진 진짜 모르겠다... ")


print()
print("Practice Quiz 4는 코드 짜는 문제 아니라서 패스")

print()
print("Practice Quiz 5")
print("group_list 함수는 그룹 이름과 구성원 목록을 수락하고 다음 형식의 문자열을 리턴합니다.")
print("group_name: member1, member2, … 예를 들어 group_list(\"g\", [\"a\",\"b\",\"c\"] )는 ‘g: a, b, c’를 리턴합니다.")
print("해당 함수에서 이를 실행하도록 공백을 채우십시오.")

def group_list(group, users):
    new_list = []
    members = users
    return group, members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
print("자 이건 아닌거 같고... 다시 해봅시다")

def group_list(group, users):
    return group + ": " + str(users)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
print("자 일단 이정도까진 만들어놨다... 이제 이 users를 리스트에서 어떻게 빼냐")

print()
def group_list(group, users):
    return group + ": " + " ".join(users)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
print("join을 잊지말자")
print("잠깐만... 콤마 어디갔는데...")

print()

def group_list(group, users):
    return group + ": " + ", ".join(users)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
print("됐다")

print()
print()


print("guest_list 함수는 파티에 온 각 손님의 이름, 나이, 직업이 포함된 튜플 목록을 읽고 각각에 ‘Guest is X years and works as __.’(손님은 X세이며 직업은 __입니다.)라는 문장을 출력합니다.")
print("예를 들어 guest_list(('Ken', 30, \"Chef\"), (\"Pat\", 35, 'Lawyer'), ('Amanda', 25, \"Engineer\"))는 다음과 같이 출력됩니다. ")
print("Ken is 30 years old and works as Chef.(Ken은 30세이며 직업은 셰프입니다.)")
print("Pat is 35 years old and works as Lawyer.(Pat은 35세이며 직업은 변호사입니다.)")
print("Amanda is 25 years old and works as Engineer.(Amanda는 25세이며 직업은 엔지니어입니다.)")
print("해당 함수에서 이를 실행하도록 공백을 채우십시오.")

print()

def guest_list(guests):
    for guest in guests:
        print("{} is {} years old and works as {}".format(guest[0], guest[1], guest[2]))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
print("""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
""")
print("wohahaha")
def guest_list(guests):
    for guest in guests:
        name,age,job = guest
        print("{} is {} years old and works as {}".format(name,age,job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
print("""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
""")

print()
print("Dictionary")
print("Key - Value : One Set")
x = {}
print(type(x))

print()
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)
print(file_counts["txt"])
print("jpg" in file_counts)
print("html" in file_counts)

print()
file_counts["cfg"] = 8
print(file_counts)
file_counts["csv"] = 17
print(file_counts)
del file_counts["cfg"]
print(file_counts)

print()
file_counts = {"jpg":10, "txt": 14, "csv": 2, "py": 23}
for extension in file_counts:
    print(extension)
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount,ext))
print(file_counts.keys())
print(file_counts.values())
print()
for value in file_counts.values():
    print(value)


print()
print("Practice Questions - Dictionary & Format")
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animals, characteristics in cool_beasts.items():
    print("{} have {}".format(animals, characteristics))

print()
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return print(result)
count_letters("aaaaa")
count_letters("tenant")
count_letters("a long string with a lot of letters")

ip_addresses = ["192.168.1.1","127.0.0.1","8.8.8.8"]
host_addresses = {"router": "192.168.1.1", "localhost":"127.0.0.1","google":"8.8.8.8"}
print("use dictionary when you are searching for a specific data; large data set")
print()

print("practice question:")
print("파이썬에서 사전은 주어진 키에 대해 단일 값만 보유할 수 있습니다.")
print("이 문제를 해결하기 위해 단일 값은 여러 값을 포함하는 목록이 될 수 있습니다. ")
print("여기에 의류 항목과 색상이 포함된 \"wardrobe\"라는 사전이 있습니다. 예를 들어 \"red shirt\", \"blue shirt\" 등의 색상으로 각 의류 품목에 대한 줄을 인쇄하도록 공백을 채우십시오.")

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothes in wardrobe:
	for colors in wardrobe[clothes]:
		print("{} {}".format(colors, clothes))

print()
print("practice quiz")

print("Question 1")
print("email_list 함수는 도메인 이름을 키로 포함하고 사용자 목록을 값으로 포함하는 딕셔너리를 받습니다.")
print("완전한 이메일 주소(예: diana.prince@gmail.com)가 포함된 목록을 생성하려면 빈칸을 채우십시오.")

def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user+"@"+domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

print()
print("Question 2")
print("groups_per_user 함수는 사용자 목록과 함께 그룹 이름이 포함된 딕셔너리를 받습니다.")
print("사용자는 여러 그룹에 속할 수 있습니다.")
print("사용자를 키로, 이들의 그룹 목록을 값으로 포함하는 딕셔너리를 리턴하도록 빈칸을 채우십시오.")
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			user_groups[user] = user_groups.get(user,[])+[group]
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

print()
print("Question 3")
print("dict.update 메서드는 하나의 사전을 다른 사전에서 가져온 항목으로 업데이트하므로 기존 항목이 대체되고 새 항목이 추가됩니다.")
print("다음 코드 끝에 있는 사전 \"wardrobe\"의 내용은 무엇입니까?")

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

print()
print("Question 4")
print("목록보다 사전을 사용하는 주요 이점은 무엇입니까?")
print("Answer: 사전에서 특정 요소를 더 빠르고 쉽게 찾을 수 있습니다.")

print()
print("Question 5")
print("add_prices 함수는 딕셔너리에 있는 모든 식료품의 총 가격을 리턴합니다.")
print("이 함수 작성을 완료하려면 빈칸을 채우십시오. ")

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for items in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += items
	# Limit the return value to 2 decimal places
	return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

print()
print()
print("Module 4 Quiz")
print()
print("Question 1")
print("format_address 함수는 주소 문자열의 일부를 새로운 문자열인 house_number 및 street_name으로 분리하고 ‘house number X on street named Y’(도로명 Y의 X번지)로 리턴합니다.")
print("입력 문자열의 형식은 다음과 같습니다. 숫자로 된 번지, 그 뒤에 도로명이 오며 도로명은 숫자를 포함할 수 있지만 단독으로 사용할 수 없으며 여러 단어로 이어질 수 있습니다.")
print("예를 들어, ‘123 Main Street’, ‘1001 1st Ave’ 또는 ‘55 North Center Drive’ 등이 될 수 있습니다. 이 함수 작성을 완료하려면 공백을 채우십시오.")
def format_address(address_string):
  # Declare variables
    house_number = 0
    street_name = []
  # Separate the address string into parts
    address = address_string.split()
  # Traverse through the address parts
    for item in address:
      if item.isnumeric():
          house_number = item
      else:
          street_name.append(item)
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done
  # before returning the result?

  # Return the formatted string
    return "house number {} on street named {}".format(house_number, " ".join(street_name))

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


print()
print("Question 2")
print("highlight_word 함수는 문장에서 주어진 단어를 대문자 버전으로 변경합니다.")
print("예를 들어, highlight_word(\"Have a nice day\", \"nice\")는 ‘Have a NICE day’(좋은 하루 보내세요)를 리턴합니다. ")
print("이 함수를 단 한 줄로 작성할 수 있습니까?")

def highlight_word(sentence, word):
	return(sentence.replace(word,word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

print()
print("Question 3")
print("amie와 Drew라는 두 명의 조수가 있는 교수는 학생들이 교실에 도착한 순서대로 작성한 출석 목록을 원합니다.")
print("Drew는 도착한 학생들을 작성한 첫 번째 사람이고, 그 다음은 Jamie가 이어 적었습니다.")
print("수업이 끝난 후, 그들은 각자 자신의 목록을 컴퓨터에 입력하고 교수에게 이메일로 보냈고 교수는 이 목록을 각 학생이 도착한 순서대로 하나로 만들고자 합니다.")
print("한편 Jamie는 곧이어 그녀의 목록이 역순이라고 메일을 보냈습니다.")
print("다음과 같이 하나의 목록으로 결합하는 단계를 수행하십시오.")
print("Drew 목록의 내용과 그 후 이어지는 Jamie 의 역순 목록을 가지고 도착한 순서대로 정확한 학생의 목록을 작성하십시오.")


def combine_lists(list1, list2):
    return list2 + list1[::-1]

# Generate a new list containing the elements of list2
# Followed by the elements of list1 in reverse order


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

print()
print()


print("Question 4")
print("리스트 컴프리헨션을 사용하여 제곱수(n*n) 목록을 만듭니다.")
print("이 함수는 변수 start와 end를 받고 start와 end 사이의 전부를 통틀어 연속 숫자 제곱 목록을 리턴합니다.")
print("예를 들어, squares(2, 3)은 [4, 9]를 리턴합니다. ")
def squares(start, end):
	return [n*n for n in range(start, end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print()
print("Question 5")
print("car_prices 딕셔너리의 키와 값을 반복하는 코드를 완성하고 각각에 대한 정보를 출력합니다.")
def car_listing(car_prices):
  result = ""
  for carname,price in car_prices.items():
    result += "{} costs {} dollars".format(carname,price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

print()
print("Question 6")
print("Taylor와 Rory가 파티를 열려고 합니다.")
print("그들은 초대장을 보냈고, 각 친구의 이름과 각 친구가 데려올 손님의 수가 포함된 답변을 딕셔너리에 각각 모았습니다.")
print("각 딕셔너리는 부분적인 목록이지만 Rory의 목록에는 손님 수에 대한 최신 정보가 있습니다.")
print("두 딕셔너리를 하나로 합하려면 빈칸을 채우십시오.")
print("이름이 두 딕셔너리에 모두 포함되어 있는 경우 각 친구는 한 번만 나열되고 Rory의 딕셔너리에 있는 손님 수가 우선 적용됩니다.")
print("그런 다음 딕셔너리 결과를 출력합니다.")

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed
  # only once, and the value from guests1 taking precedence
  guests2.update(guests1)
  return guests2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

print()
print("Question 7")
print("딕셔너리를 사용하여 입력 문자열의 문자 빈도를 계산합니다.")
print("공백, 숫자 또는 구두점이 아닌 문자만 계산해야 합니다. 대문자는 소문자와 동일하게 간주해야 합니다.")
print("예를 들어 count_letters(\"This is a sentence.\"(이것은 문장입니다.))는 다음과 같이 리턴합니다.")
print("{'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.")
print()
def count_letters(text):
  result = {}
  text = text.lower()
  # Go through each letter in the text
  #for letter in text:
    # Check if the letter needs to be counted or not
  for letter in text:
    if letter.isalpha():
        count = text.count(letter)
        result[letter] = count
    # Add or increment the value in the dictionary

  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

print()
print("Question 8")
print("animal = \"Hippopotamus\"일 때 다음 명령은 무엇을 반환합니까?")
animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])

print()
print("Question 9")
print("이 명령이 실행된 후 \"colors\" 목록에는 무엇이 포함됩니까?")
colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)

print()
print("Question 10")
print("다음 명령은 무엇을 반환합니까?")
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())