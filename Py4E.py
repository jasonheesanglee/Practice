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
print("Pay:", int(hrs) * int(rte))

