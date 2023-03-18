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


