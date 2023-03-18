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