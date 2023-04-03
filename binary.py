Input = float(input("Please enter your number: "))
print("Your input number is", Input)

decimal = int(Input)
fractions = Input - float(decimal)
fractions = float(fractions)

if Input < 0:
    positive_negative = 1
else:
    positive_negative = 0


# print(decimal) # decimal = integer
# print(fractions) # fractions = float

decimal = int(decimal)
fractions = float(fractions)

print()

result = ""


while (decimal > 0):
    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result

result_1 = ""
result_1 = result[::-1]
result += "."
    
while (fractions < 0):
    fractions *= 2
    fractions_1 = int(fractions)
    
    if fractions_1 == 1:
        fractions -= fractions_1
        result_1 += "1"
        
    else :
        result_1 += "0"
    fractions -= 1

print(result)
print(result_1)

binary = result + result_1
print(binary)

print()

if binary.find(".") == 1 or 0:
    binary = binary

else:
    binary_first_char = binary[:1]
    binary_rest = binary[1:]
    
    print("binary first char =", binary_first_char)
    print("rest of binary =", binary_rest)

    br_1 = str(binary_rest).split(".")[0]
    br_2 = str(binary_rest).split(".")[1]
    binary_rest = br_1 + br_2

print("rest of binary =", binary_rest)

result_2 = ""

print()

exponent = 127 +(binary.find(".") - 1)

while(exponent > 0):
    remainder_1 = exponent % 2
    exponent = exponent // 2
    result_2 = str(remainder_1) + result_2
    
bit = str(positive_negative) + str(result_2) + str(binary_rest)
print(len(bit))

print()

if len(bit) > 32:
    bit = bit[0:32]

else:
    for i in range(32 - len(bit)):
        bit = bit + "0"
    
print(bit)
print(len(bit))

print()

class Binary_hexa:
    def __init__(self, val_1, val_2, val_3, val_4):
        self.val_1 = int(val_1)*8
        self.val_2 = int(val_2)*4
        self.val_3 = int(val_3)*2
        self.val_4 = int(val_4)*1
        self.multi = self.val_1 + self.val_2 + self.val_3 + self.val_4


first = bit[0:4]
second = bit[4:8]
third = bit[8:12]
fourth = bit[12:16]
fifth = bit[16:20]
sixth = bit[20:24]
seventh = bit[24:28]
eighth = bit[28:32]


first = Binary_hexa(first[0], first[1], first[2], first[3])
first = first.multi

second = Binary_hexa(second[0], second[1], second[2], second[3])
second = second.multi


third = Binary_hexa(third[0], third[1], third[2], third[3])
third = third.multi

fourth = Binary_hexa(fourth[0], fourth[1], fourth[2], fourth[3])
fourth = fourth.multi

fifth = Binary_hexa(fifth[0], fifth[1], fifth[2], fifth[3])
fifth = fifth.multi

sixth = Binary_hexa(sixth[0], sixth[1], sixth[2], sixth[3])
sixth = sixth.multi

seventh = Binary_hexa(seventh[0], seventh[1], seventh[2], seventh[3])
seventh = seventh.multi

eighth = Binary_hexa(eighth[0], eighth[1], eighth[2], eighth[3])
eighth = eighth.multi


_32bit = str(positive_negative) + "x" + str(first) + str(second) + str(third) + str(fourth) + str(fifth) + str(sixth) + str(seventh) + str(eighth)
print(_32bit)