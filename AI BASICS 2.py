a = [1,2,3,4,5]
print(a)
a.append(10)
print(a)
a.append(20)
print(a)

c = a.pop()
print(a)
print(c)
print()

word = input("Input a word Stack: ")
word_list = list(word)
# print(word_list)
for _ in range(len(word_list)):
    print(word_list.pop())
    print(word_list)

print()
a = [1,2,3,4,5]
print(a)
a.append(10)
print(a)
a.append(20)
print(a)

c = a.pop(0)
print(a)
print(c)

word = input("Input a word Queue: ")
word_list = list(word)
# print(word_list)
for _ in range(len(word_list)):
    print(word_list.pop(0))
    print(word_list)

print()

t = (1,2,3)
print(type(t))
print(t + t)
print(t * 2)
print(t)
print(len(t))
#  t[1] = 5
#  print(t)

t = (1)
print(type(t))

t = (1,)
print(type(t))


print()
s = set([1,2,3,1,2,3])
print(s)

s.add(1)
print(s)

s.remove(1)
print(s)

s.update([1,4,5,6,7])
print(s)

s.discard(3)
print(s)
s.clear()
print(s)

print()

s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])

print(s1.union(s2))

print(s1 | s2)

print(s1.intersection(s2))
print(s1 & s2)
print(s1.difference(s2))
print(s1 - s2)

print()
country_code = {}
country_code = {"America": 1, "Korea": 82, "China": 86, "Japan": 81}
print(country_code)
print(country_code.items())
print(country_code.keys())
country_code["German"] = 49
print(country_code)
print(country_code.values())


for k, v in country_code.items():
    print("Key :", k)
    print("Value :", v)

print("Korea" in country_code.keys())
print(82 in country_code.values())

print()

import csv
def getKey(item):
    return item[1]
command_data = []
with open('command_data.csv', 'r', encoding='utf8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        command_data.append(row)

command_counter = {}
for data in command_data:
    if data[1] in command_counter.keys():
        command_counter[data[1]] += 1
    else:
        command_counter[data[1]] = 1

print(command_counter)

dictlist = []
for key, value in command_counter.items():
    temp = [key,value]
    dictlist.append(temp)

sorted_dict = sorted(dictlist, key=getKey, reverse=True)
print(sorted_dict)

print()

from collections import deque

deque_list = deque()
for i in range (5):
	deque_list.append(i)
print(deque_list)
deque_list.appendleft(10)
print(deque_list)

print()

deque_list = deque()
for i in range(5):
    deque_list.append(i)
deque_list.appendleft(10)
print(deque_list)
print()

deque_list.rotate(2)
print(deque_list)
deque_list.rotate(1)
print(deque_list)
deque_list.append(100)
print(deque_list)
deque_list.appendleft(200)
print(deque_list)
deque_list.extend([5, 6, 7])
deque_list.extendleft([5, 6, 7])

print()
#  def general_list():
#      just_list = []
#      for i in range(100):
#          just_list.append(i)
#          just_list.pop()
#  %timeit general_list()

print()
#  def deque_list():
#      deque_list = deque()

#      for i in range(100):
#          for i in range(100):
#              deque_list.append(i)
#              deque_list.pop()

#  %timeit deque_list()


f = open("yesterday.txt", "r")
yesterday = ""
while True:
    line = f.readline()
    if not line:
        break
    yesterday = yesterday + line.strip() + "\n"
f.close()
print(yesterday)

from collections import defaultdict
from collections import OrderedDict


d = defaultdict(lambda : 0)
print(d)
for word in yesterday.split():
    d[word] += 1
print(d)

def get_key(x):
    return x[1]

sorted_dict = OrderedDict()
for i, v in sorted(d.items(), key=getKey, reverse=True):
    sorted_dict[i] = v
print(sorted_dict)
sorted_dict["to"]

print()

from collections import Counter

ball_or_strike_list = Counter(["B", "S", "S", "S", "S", "B", "B"])
c = Counter(ball_or_strike_list)
print(c)
print(list(c.elements()))

print()

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)
print(c + d)
print(c & d)
print(c | d)
print()

sorted(Counter(yesterday).items(), key=lambda t: t[1], reverse=True)
print(Counter(yesterday)["a"])

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(11, y=22)
print(p[0] + p[1])

x, y = p
print(x, y)
print(p.x + p.y)
print(Point(x=11, y=22))

# f = open("users.csv", "r")
# next(f)
# reader = csv.reader(f)
# student_list = []
# for row in reader :
#     student_list.append(row)
#     print(row)
#
# columns = ["user_id", "integration_id", "login_id", "password", "first_name", "last_name", "full_name", "sortable_name", "short_name", "email", "status"]
#
# Student = namedtuple("Student", " ".join(columns))
# student_nametuple_list = []
# for row in student_list:
#     student = Student(*row)
#     student_nametuple_list.append(student)
# print(student_nametuple_list)
# print(student_nametuple_list[0].full_name)

print()

colors = ["red", "blue", "green", "yellow"]
result = ""
for s in colors:
    result += s
print(result)

colors = ["red", "blue", "green", "yellow"]
result = "".join(colors)
print(result)

print()

items = "zero one two three".split()
print(items)

example = "python, java, javascript"
for content in example.split(","):
    print(content.strip())

a, b, c = example.split(",")
print(a, b, c)

example = "teamlab.technology.io"
subdomain, domain, tld = example.split(".")
print(subdomain, domain, tld)

print()

colors = ["red", "blue", "green", "yellow"]
result = "-".join(colors)
print(result)

print("        ".join(colors))

print()

result = []
for i in range(10):
    result.append(i)

print(result)

result = [i for i in range(10)]
print(result)
result = [i for i in range(10) if i % 2 ==0]
print(result)

word_1 = "Hello"
word_2 = "World"
result = [i+j for i in word_1 for j in word_2]
print(result)

print()

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i+j for i in case_1 for j in case_2]
print(result)
result = [i+j for i in case_1 for j in case_2 if not(i==j)]
print(result)
result.sort()
print(result)

result = [i+j if not(i==j) else "BEE" for i in case_1 for j in case_2]
print(result)

print()

words = "The quick brown fox jumps over the lazy dog".split()
print(words)

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)

import pprint as pp
pp.pprint(stuff)

print()

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i+j for i in case_1 for j in case_2]
print(result)
result = [[i+j for i in case_1]for j in case_2]
print(result)
result = [[j + i for i in case_1 if j !="D"] for j in case_2]
print(result)

print()

for i, v in enumerate(["tic", "tac", "toe"]):
    print(i,v)

print()

for i, v in enumerate("ABC"):
    print("{0} \t {1}".format(i, v))


print()

my_str = "ABCD"
print({v : i for i, v in enumerate(my_str)})


text = "Samsung Group is a South Korean multinational conglomerate headquartered in Samsung town, Seoul"
set_text = list(set(text.split()))
print({i : v.lower() for i, v in enumerate(text.split())})

print({i:v.lower() for i, v in enumerate(set_text)})

print({v.lower():i for i, v in enumerate(set_text)})

print()

alist = ["a1", "a2", "a3"]
blist = ["b1", "b2", "b3"]
print([[a,b] for a, b in zip(alist, blist)])

print([c for c in zip(alist, blist)])

print()

math = (100, 90, 80)
kor = (90, 90, 70)
eng = (90, 80, 70)

average_score = [sum(value) / 3 for value in zip(math, kor, eng)]
print(average_score)
for i in average_score:
    i = float(f"{i:.2f}")
    print(i)

print()

alist = ["a1", "a2", "a3"]
blist = ["b1", "b2", "b3"]
for i, values in enumerate(zip(alist, blist)):
    print(i, values)
print()
print(zip(alist, blist))
print(list(zip(alist, blist)))
print(enumerate(list(zip(alist, blist))))
print(list(enumerate(list(zip(alist, blist)))))

print()

def f(x, y):
    return x + y
print(f(1, 4))

f = lambda x, y: x + y
print(f(1, 4))

print()
f = (lambda x, y: x + y)
print(f(10, 50))

print((lambda x, y: x + y)(10, 50))
print()

up_low = lambda x : x.upper() + x.lower()
print(up_low("My Happy"))
print((lambda x : x.upper() + x.lower())("My Happy"))

print()
up_low = lambda x : "-".join(x.split())
print(up_low("My Happy"))
print((lambda x : "-".join(x.split()))("My Happy"))

print()
up_low = lambda x : "-".join(x.split())
print(up_low("My Happy"))
print((lambda x : "-".join(x.split()))("My Happy"))

print()

ex = [1, 2, 3, 4, 5]
f = lambda x, y: x + y
print(list(map(f, ex, ex)))


f = lambda x: x ** 2
print(list(map(f, ex)))
print([f(value) for value in ex])

def f(x):
    return x + 5
print(list(map(f, ex)))

print([f(value) for value in ex])

print()

print(list(map(lambda x : x ** 2 if x % 2 == 0 else x, ex)))

print([value**2 if value % 2 == 0 else value for value in ex])

print()

from functools import reduce
print(reduce(lambda x, y : x+y, [1, 2, 3, 4, 5]))

print()

for city in ["Seoul", "Busan", "Pohoang"]:
    print(city, end="\t")

for language in ("Python", "C", "Java"):
    print(language, end="\t")
for char in "Python is easy":
    print(char, end=" ")

print()

cities = ["Seoul", "Busan", "Pohoang"]
iter_obj = iter(cities)

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
# print(next(iter_obj))


print()

def general_list(value):
    result = []
    for i in range(value):
        result.append(i)
    return result
print(general_list(50))

import sys
result = general_list(50)
print(sys.getsizeof(result))

def generator_list(value):
    result = []
    for i in range(value):
        yield i

for a in generator_list(50):
    print(a)

result = generator_list(50)
print(sys.getsizeof(result))

gen_ex = (n*n for n in range(500))
print(type(gen_ex))
print(list(gen_ex))

print()
from sys import getsizeof

gen_ex = (n*n for n in range(500))
print(getsizeof(gen_ex))
print(getsizeof(list(gen_ex)))


gen_ex = (n*n for n in range(5000))
print(getsizeof(gen_ex))
print(getsizeof(list(gen_ex)))

list_ex = [n*n for n in range(500)]
print(getsizeof(list_ex))


list_ex = [n*n for n in range(5000)]
print(getsizeof(list_ex))


print()

def print_something(my_name, your_name, third_name):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something(third_name="abc", my_name="Jason", your_name="TeamLab")
print_something("abc", "Jason", "TeamLab")


print()

def print_something_2(my_name, your_name = "TeamLab"):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something_2("Jason")
print_something_2("Jason", "Naver")

print()

def asterisk_test(a, b, *args):
    print(list(args))
    print(type(args))
    return a+b+sum(args)

print(asterisk_test(1,2,3,4,5))

print()

def kwargs_test_1(**kwargs):
    print(kwargs)
    print(type(kwargs))

kwargs_test_1(first=3, second=4, third=5)

print()
def kwargs_test_3(one, two=3, *args,**kwargs):
    print(one + two + sum(args))
    print(args)
    print(kwargs)

kwargs_test_3(10, 30, 3, 5, 6, 7, 8, first=3, second=4, third=5)

print()

def asterisk_test(a, *args):
    print(a, args)
    print(*args)
    print(args)
    print(type(args))
asterisk_test(1, *(2,3,4,5,6))

print()

def asterisk_test(a, args):
    print(a, *args)
    print(*args)
    print(args)
    print(type(args))
asterisk_test(1, (2,3,4,5,6))

print()

a, b, c = ([1, 2], [3, 4], [5,6])
print(a, b, c)

data = ([1, 2], [3, 4], [5,6])
print(*data)

def asterisk_test(a, b, c, d):
    print(a, b, c, d)
data = {"b":1, "c":2, "d":3}
asterisk_test(10, **data)

print()

ex = ([1, 2], [3, 4], [5, 6], [5, 6], [5, 6])
print(ex)
print(*ex)
print()
for value in zip(ex):
    print(value)

for value in zip(*ex):
    print(value)
    print(sum(value))
