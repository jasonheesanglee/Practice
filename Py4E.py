print("is it working now?")

a = 3
b = 5

print(a*b)

for i in range(1, 11):
    print(a, "X", b*i, "=", a*b*i)

print()
print("OK, Py4E now starts")

print()
print("Vocab")

print()
print("reserved words")
print()

print("False, None, True, and, as, assert")
print("break, class, if, def, del, elif, else, except")
print("return, for, from, global, try, import, in, is")
print("is, lambda, while, not, or, pass, raise")
print("finally, continue, nonlocal, with, yield")


print()
x = 2
x = x + 2
print(x)

print()
x = 5
if x < 10:
    print("Smaller")
if x > 20:
    print("Bigger")
print("Finish")

print()
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff")
print(

)
x = 10
while x > 5:
    print(x)
    x = x-1
if x < 5:
    print("x is smaller than 5")

print()

print("Variables, Expressions, Statements")
print("Constants = Fixed values")
print(123)
print(98.6)
print("hello, world")
print("and reserved words")

print("variables = sth that can change, assigned by variable name, eg. 'x' or 'y'")

x = 12.2
y = 14
print(x, y)
x = 100
print(x, y, "x changed")
print("use variable names sth that other programmers can understand as well at the first sight")

print("assignment statement")
x = 0.6
x = 3.9 * x * (1-x)
print(x)

print()

print("Expressions")
print("+ = Addition")
print("- = Subtraction")
print("* = Multiplication")
print("/ = Division")
print("** = Power")
print("% = Remainder")

print("Order of Evaluation")
x = 1 + 2 * 3 - 5 / 5**6
print(x)
print("Parenthesis ->  Power -> Multiplication -> Addition -> Left to Right")

print("Integer -> numbers with no decimals")
print("string -> words/numbers in word format")
ddd = 1 + 2
eee = "Hello " + "There "
print(ddd)
print(eee)
print(eee + str(1))

print(float(99) + 100)

print()

sval = "123"
print(type(sval))
ival = int(sval)
print(ival + 1)
nsv = "hello bob"
niv = int(len(nsv))
print(niv + 5)

print()
nam = input("Who are you? ")
print("Welcome", nam)

print()
inp = input("Europe Floor? ")
usf = int(inp) + 1
print("US Floor ", usf)


print()
print("Exercise")

nzt = input("Enter your name: ")
print("Hello", nzt)

print()

hrs = input("Enter Hours: ")
rte = input("Enter Rate: ")
print("Pay:", float(hrs) * float(rte))

result = 2+(4/2)*4
print(result)

print()

print("if statement")
print()

x = 5
if x < 10:
    print("Smaller")
if x > 20:
    print("Bigger")

print()
print("Finis")
print("< Less than")
print("<= Less than or Equal to")
print("== Equal to")
print(">= Greater than or Equal to")
print("> Greater than")
print("!= Not equal")
print("\"=\" is used for assignment")

print()
x = 5
if x == 5:
    print("Equals 5")
if x > 4:
    print("Greater than 4")
if x >= 5:
    print("Greater than or Equals 5")
if x < 6: print("Less than 6")
if x <= 5:
    print("Less than or Equals 5")
if x != 6:
    print("Not equal 6")

print()
x = 5
print("Before 5")
if x == 5:
    print("Is 5")
    print("Is still 5")
    print("Third 5")
print("Afterwards 5")
print("Before 6")
if x == 6:
    print("Is 6")
    print("Is still 6")
    print("Third 6")
print("Afterwards 6")

print()
print("Indentation is a KEY for Python")
print("4 spaces = 1 tab, TURN OFF TAB, Python can get confused")

print()
x = 5
if x > 2:
    print("Bigger than 2")
    print("Still Bigger, Indentation lasts til here")
print("Done with 2")
print()
for i in range(5):
    print(i)
    if i > 2:
        print("Bigger than 2")
    print("Done with i", i)
print("All done ")

print()
x = 42
if x > 1:
    print("More than 1")
    if x < 100:
        print("Less than 100")
print("All Done")

print()
x = 4
if x > 2:
    print("Bigger")
else:
    print("Smaller")
print("All Done")

print()
x = 0
if x < 2:
    print("Small")
elif x < 10:
    print("Medium")
else:
    print("Large")
print("All Done")

x = 20
if x < 2:
    print("Small")
elif x < 10:
    print("Medium")
else:
    print("Large")
print("All Done")

print()
print("No Else")
x = 5
if x < 2:
    print("Small")
elif x < 10:
    print("Medium")
print("All Done")

print()
print("Which will never print regardless of the value for X?")
if x < 2:
    print("Below 2")
elif x >= 2:
    print("2 or more")
else:
    print("Something else")  #  This will never be printed

print()

if x < 2:
    print("Below 2")
elif x < 20:
    print("Below 20")
elif x < 10:   #  This will never be printed
    print("Below 10")
else:
    print("Something else")

print("")
rawstr = input("Enter a Number:")
try:
    ival = int(rawstr)
except: - 1
if ival > 0:
    print("Nicework")
else:
    print("Not a number")

print()
print("Practice Exercise 1")
print()
hours = input("Enter Hours:")
rate = input("Enter Rate:")
floating_point_hours = float(hours)
floating_point_rate = float(rate)
# print(floating_point_hours, floating_point_rate)
if floating_point_hours > 40:
    #print("Overtime")
    reg = floating_point_hours * floating_point_rate
    otp = (floating_point_hours - 40) * (floating_point_rate * 0.5)
    #print(reg, otp)
    xp = reg + otp
else:
    #print("Regular")
    xp = floating_point_hours * floating_point_rate
print("Pay:", xp)

print()
print("Practice Exercise 2")

hour = input("Enter Hours:")
rates = input("Enter Rate:")
try:
    fh = float(hour)
    fr = float(rates)
except:
    print("Error, please enter numeric input")
    quit()

print(fh, fr)
if fh > 40:
    reg = fh * fr
    otp = (fh - 40) * (fr* 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:", xp)

print()

print("Functions")
print("Store & Reuse")
print()
print("def stores the codes indented")
def thing():
    print("Hello")
    print("Fun")

print()
thing()
print("Zip")
thing()

print()

big = max("Hello world")
print(big)

tiny = min("Helloworld")
print(tiny)

tiny = min("helloworld")
print(tiny)

print()

print(float(99)/100)
i = 42
print(type(i))
f = float(i)
print(f)
print(type(f))
print(1+2*float(3)/4-5)

print()
print()
print("Building our own functions")
print()

print("Invoking")
x=5
print("Hello")
def print_lyrics():
    print("I'm a lumberjack, and I'm okay")
    print("I sleep all night and I work all day.")
print("Yo")
print_lyrics()
x = x + 2
print(x)

print()

def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"
greet("en")
greet("es")
greet("fr")

print()

print(greet("en"), "Glenn")
print(greet("es"), "Sally")
print(greet("fr"), "Michael")

print()

def addtwo(a,b):
    added = a + b
    return added
x = addtwo(3,5)
print(x)

print("Practice Exercise 1")

def computepay(hours, rate):
    #print("In computepay", hours, rate)
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    #print("Returning", pay)
    return pay

sh = input("Enter Hours:")
sr = input("Enter Rate:")
fh = float(sh)
fr = float(sr)
xp = computepay(fh, fr)

computepay(fh, fr)
print("Pay:", xp)

print()
print("Loops and Iteration")

print()
print("While Loop")

print()
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")
print(n)

print()
n = 0
while n > 0:
    print("Lather")
    print("Rinse")
print("Dry off!")

print()
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("Done!")

print()
while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")

print()

print("Definite Loops")
print("For Loops")
print()

for i in [5,4,3,2,1]:
    print(i)
print("Blastoff")

print()

friends = ["Joseph","Glenn","Sally"]
for friend in friends:
    print("Happy New Year", friend)
print("Done!")

print()

어쩔 =['냉장고','세탁기','믹서기','헤어드라이기','티비']
for 가전이름 in 어쩔:
    print("어쩔", 가전이름)
print("끗!")

print()
print("Loop Idioms")

print()
print("Before")
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print("After")

print()
largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num) # this is to show the progress of how computer works in order
print("After", largest_so_far)

print()
print("Counting in a Loop")

zork = 0
print("Before, zork")
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print("After", zork)

print()
print("Total sum of all values")
zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print("After", zork)

print()
print("Finding Average in Loop")

count = 0
summ = 0
print("Before", count, summ)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    summ = summ + value
    print(count, summ, value)
print("After", count, summ, summ / count)

print()
print("Filtering in a Loop")

print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print("Large number", value)
print("After")

print()
print("Search using a Boolean Variable")

found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print("After", found)

print()
print("How to find the smallest value")
print()

smallest = None
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)  # this is to show the progress of how computer works in order
print("After", smallest)

print()
print("The \"is\" and \"is not\" Operators")
print("\"is\" is stronger than \"==\", but try to use less of it. It might get confusing")

print()
print(0 is 0.0)
print(0 == 0.0)

print()

print("Practice Exercise")
print()

num = 0
tot = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except Exception as e:
        print(f"Invalid Input:\n{e}")
        continue
    num = num + 1
    tot = tot + fval
print(tot, num, tot/num)

print()
print("hi")

print()
i = 0
while i < 5:
    print(i)
    i = i + 1

print()
x = 0
while x < 10:
    if x < 10:
        x = x + 1
    elif x > 8:
        print(x)
print(x)

print()

print("String")
fruit = "Banana"
letter = fruit[0]
print(letter)
x = 3
w = fruit[x - 1]
print(w)

print()
print(len(fruit))
x = len(fruit)
print(x)

print()
fruit = "Banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

print()
for letter in fruit:
    print(letter)

print()
word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count = count + 1
    print(count)

print()
s = "Monty Python"
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])

print()

fruit = "Banana"
print("n" in fruit)
print("m" in fruit)
print("nan" in fruit)
print("a" in fruit)

print()

word = "Canana"
if word == "Banana":
    print("Alright, Bananas")
if word < "Banana":
    print("Your word, " + word + ", comes before Banana")
elif word > "Banana":
    print("Your word, " + word + ", comes after Banana")
else:
    print("Alright, Bananas")

print()

greet = "Hello Bob"
zap = greet.lower()
print(zap)
print(greet)
print("Hi There".lower())

print()
stuff = "Hello World"
print(type(stuff))
print(dir(stuff))

print()
fruit = "I Like Banana"
print(fruit.replace("Banana", "Apple"))
print(fruit. replace("a", "x"))

print()
greet = "    Hello     Bob     "
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

print()
line = "Please have a nice day"
print(line.startswith("Please"))
print(line.startswith("P"))
print(line.startswith("p"))

print()
data = "From stephen.macquard@uct.ac.za Sat Jan   5  09:14:16 2008"
atpos = data.find("@")
print(atpos)
sppos = data.find(" ",atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

print()

x = "이광춘"
print(type(x))
x = u"이광춘"
print(type(x))


print()
print("Practice Exercise")
str = "X-DSPAM-Confidence: 0.8475"
#  print(str)
ipos = str.find(":")
#  print(ipos)

piece = str[ipos+1:]
#  print(piece)
value = float(piece)
#  print(value)
print(value+42)

print()
print()
print("Reading Files")

#  handle = open(filename, mode)
#  fhand = open(mbox.rtf, "r")
#  fhand = open(mbox.rtf)
#  print(fhand)
print()
stuff = "Hello\nworld!"
print(stuff)
stuff = "X\nY"
print(stuff)
print(len(stuff))

print()

print("Practice Exercise")
print()
fh = open("mbox-short.txt")
print(fh)

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())

print()
print()
print("LISTS")

friends = ["Joseph", "Glenn", "Sally"]
caarryon = ["socks", "shirts", "perfume"]

print()
print([1, 24, 76])
print(["red", "yellow", "blue"])
print(["red", 24, 98.6])
print([1, [5, 6], 7])
print([])

print()

for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!")

print()

friends = ["Joseph", "Glenn", "Sally"]
print(friends[1])

print()
print("string is immutable")
fruit = "Banana"
print(fruit[0] == "b")
x = fruit.lower()
print(x)

print()
print("List is mutable")
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)

print()
print("Length of a list")
x = [1, 2, "joe", 99]
print(len(x))


print("range function")
print(range(4))

friends = ["Joseph", "Glenn", "Sally"]
print(range(len(friends)))

print("for loops with list")

friends = ["Joseph", "Glenn", "Sally"]
for friend in friends:
    print("Happy New Year", friend)

print()
for i in range(len(friends)):
    friend = friends[i]
    print("Happy New Year", friend)

print()
print(len(friends))
print(range(len(friends)))

print()

print("concatenating with list")
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)

print()
print("list slicing")

t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

print()
print("List Methods")
x = list()
print(type(x))
print(dir(x))

print()
print("Building a list from scratch")
stuff = list()
stuff.append("book")
stuff.append(99)
print(stuff)
stuff.append("cookie")
print(stuff)

print()
print("Is sth in the list?")

some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)

print()
print("list in order")
friends = ["Joseph", "Glenn", "Sally"]
friends.sort()
print(friends)
print(friends[1])

print()
print("Built-in functions and lists")
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

print()

total = 0
count = 0
while True:
    inp = input("Enter a number: ")
    if inp == "done": break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print("Average:", average)

print()

numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done": break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print("Average:", average)

print()

print("List & Spring")

abc = "With three words"
stuff = abc.split()
print(len(stuff))
print(stuff[0])

print()
print(stuff)
for w in stuff:
    print(w)

print()

line = "A lot                    of spaces"
etc = line.split()
print(etc)


line = "first;second;third"
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(";")
print(thing)
print(len(thing))