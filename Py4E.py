print("is it working now?")

a = 3
b = 5

print(a*b)

for i in range(1,11):
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
x = 1 + 2* 3 - 5 / 5**6
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
if x < 6: print ("Less than 6")
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
    print("Something else") #This will never be printed

print()

if x < 2:
    print("Below 2")
elif x < 20:
    print("Below 20")
elif x < 10: #This will never be printed
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
