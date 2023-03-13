print("Hello World")

print("Dynamic Typing")
a = 1
b = 1
print(a, b)
print(type(a))
print(type(b))
print()

a = 1.5
b = 3.0
print(type(a))
print(type(b))
print()

a = "asldjk;asd"
b = "kjashdfkajsdf"
print(type(a))
print(type(b))
print()

a = "10"
b = "12314.512"
print(type(a))
print(type(b))
print()

a = True
b = False
print(type(a))
print(type(b))
print()


print("Data Type Shift")
a = 10
print(type(a))

float(a)
print(a)
print(type(a))
a = float(a)
print(type(a))