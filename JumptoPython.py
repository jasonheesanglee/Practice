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
print()
