import sys
print(sys.getsizeof("a"), sys.getsizeof("ab"), sys.getsizeof("abc"))
print()

a = "abcde"
print(a[0], a[4])
print(a[-1], a[-5])
print()

a = "Artificial Intelligence and Machine Learning"
print(a[0:6], " AND ", a[-9:])
print(a[:])
print(a[-50:50])
print(a[::2], " AND ", a[::-1])

a = "TEAM"
b = "LAB"

print(a + b)
print("T" in a)
print("L" in a)

print()

title = "TEAMLAB X Upstage"
print(title.lower())
print(title.split())
print(title.isdigit())
print(title.title())
print(title.count("a"))
print("12345".isdigit())

print("It\'s OK")

a = """
Happy New Year,
 This is a class"""
print(a)
b = "\n Happy New Year,\n This is a class"
print(b)

print()

raw_string = "This is my fourth time going through Python basics. \n for real"
print(raw_string)
raw_string = r"This is my fourth time going through Python basics. \n for real"
print(raw_string)

trial = "This is a \
trial"
print(trial)

print()
f = open("yesterday.txt", "r")
yesterday = ""
while True:
    line = f.readline()
    if not line:
        break
    yesterday = yesterday + line.strip() + "\n"
f.close()
print(type(yesterday))

lower_yesterday = yesterday.lower()

print(lower_yesterday.count("yesterday"))

