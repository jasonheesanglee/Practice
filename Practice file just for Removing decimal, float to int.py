print("Trial 1")

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 97, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0

for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0

else:
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)


print()

print("Trial 2")

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 97, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0

for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0

else:
    student_average_two_decimal = list()
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    for j in student_average:
        j = float(f"{j:.2f}")
        student_average_two_decimal.append(j)
    print(student_average_two_decimal)


print()

print("Trial 3")

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 97, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0

for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0

else:
    student_average_two_decimal = list()
    student_average_integer = list()
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]

    for j in student_average:
        j = float(f"{j:.2f}")  # 여기까진 오케이
        student_average_two_decimal.append(j)

        for k in student_average_two_decimal:
            if k.is_integer() == True:
                k = int(k)
            else:
                continue
        student_average_integer.append(k)
    print(student_average_integer)


print()
print("Trial 4")

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 97, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0

for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0

else:
    student_average_two_decimal = list()
    student_average_integer = list()
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    for j in student_average:
        j = float(f"{j:.2f}")  # 여기까진 오케이
        student_average_two_decimal.append(j)
        for k in student_average_two_decimal:
            if k.is_integer() == True:
                k = int(k)
            else:
                k = k
            student_average_integer.append(k)
    print(student_average_integer)

print()
print("Trial 5")


kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 97, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0

for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0

else:
    student_average_two_decimal = list()
    student_average_integer = list()
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    for j in student_average:
        j = float(f"{j:.2f}")  # 여기까진 오케이
        student_average_two_decimal.append(j)
        for k in student_average_two_decimal:
            if k.is_integer() == True:
                k = int(k)
            else:
                k = k
            student_average_integer.append(k)
    print(student_average_integer)

print()

print("Trial 6")
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 97, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0

for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0

else:
    student_average_two_decimal = list()
    student_average_integer = list()
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    for j in student_average:
        j = float(f"{j:.2f}")  # 여기까진 오케이
        student_average_two_decimal.append(j)
        for k in student_average_two_decimal:
            if k.is_integer() == True:
                k = int(k)
            else:
                k = k
            student_average_integer.append(k)
            print(student_average_integer)


print()
print("Trial 7")

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 97, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0

for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0

else:
    student_average_two_decimal = list()
    student_average_integer = list()
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]

    for j in student_average:
        j = float(f"{j:.2f}")  # 여기까진 오케이
        student_average_two_decimal.append(j)

        for k in student_average_two_decimal:
            if k.is_integer() == True:
                k = int(k)
            else:
                continue
        student_average_integer.append(k)
    print(student_average_integer)

print("Yay!!!!!!!!!!!!!!!!!!!!!!")