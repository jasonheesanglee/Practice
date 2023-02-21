print("Additional Practice for \"For Loops\"")
print()
print("1. for문의 실행결과를 예측하라")
print("Answer: 각 과일이 한 줄당 하나씩")
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print(변수)

print()
print("2. for문의 실행결과를 예측하라")
print("Answer: none?" + "이 아니었다.. 과일 갯수별로 #####이 나올줄이야...")
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")

print()
print("3. for문을 풀어서 동일한 동작을 하는 코드를 작성하라.")
for 변수 in ["A", "B", "C"]:
  print(변수)

print()
print("Answer")
변수 = (["A","B","C"])
print(변수)
print("아... 위처럼 어떻게 해보는건가 했는데... 모르겠어서 정답을 보니...")
print()

print("A")
print("B")
print("C")
print("그냥 이렇게하네... 그래... 복잡하게 생각하지 말자")


print()
print("4. for문을 풀어서 동일한 동작을 하는 코드를 작성하라.")

for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)
print()
print("Answer")
print("출력: A")
print("출력: B")
print("출력: C")

print()
print("5. for문을 풀어서 동일한 동작을 하는 코드를 작성하라.")
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)
print()
print("Answer")
print("변환: a")
print("변환: b")
print("변환: c")
print("방심했다... 위에도 이렇게 해서 다 이렇게 하는줄 알았지... 이거 차이점 보려면 코드 뜯어봐야됨ㅇㅇ")

print()
변수 = "A"
b = 변수.lower()
print("변환: " + b)
변수 = "B"
b = 변수.lower()
print("변환: " + b)
변수 = "C"
b = 변수.lower()
print("변환: " + b)
print("답안지에서 굳이 이렇게 돌아가면서 할 줄은 몰랐지... 같은 사람이 답안지 쓴거 맞냐... 그래도 도움되니 익혀두자")

print()
print("6. 다음 코드를 for문으로 작성하라.")
변수 = 10
print(변수)
변수 = 20
print(변수)
변수 = 30
print(변수)

print()
print("Answer")
for practice_6 in ["10","20","30"]:
    print(practice_6)
print("설마 이게 틀리진 않겠지... 두구두구...")
print()

print("아 위처럼 해도 되고 아니면 아래처럼 해도 됨")
practice_6 = [10, 20, 30]
for parameter_6 in practice_6:
    print(parameter_6)

print()
print("7. 다음 코드를 for문으로 작성하라.")
print(10)
print(20)
print(30)
print("뭐야... 내가 써야할 답안은 결국 위 문제랑 같은거 같은데... 함정인가...")

print()
print("Answer")
for practice_7 in ["10","20","30"]:
    print(practice_7)
print("뭐야... 맞네...")
print()

print("8. 다음 코드를 for문으로 작성하라")
print(10)
print("-------")
print(20)
print("-------")
print(30)
print("-------")
print("오... 조금 어려운가...")

print()
for practice_8 in [10,20,30]:
    print(practice_8)
    print("-------")
print()
print("조금... 어려웠다...")

print()
print("9. 다음 코드를 for문으로 작성하라.")
print("++++")
print(10)
print(20)
print(30)

print()
print("Answer")
print("++++")
for practice_9 in [10,20,30]:
    print(practice_9)
print("답안지에 ++++가 함정이었다는데... 다행히... 잘 넘겼군!")

print()
print("10. 다음 코드를 for문으로 작성하라.")
print("-------")
print("-------")
print("-------")
print("-------")
print("흠... 이건 쉽겠...나...?")

print()
print("Answer")
for practice_10 in range(3):
    practice_10 = ("-------")
    print(practice_10)
print("오... 이게 맞다고...?")
print()
print("아 일단은 이렇게 하라는구만, 아직 range는 안나왔으니")
for practice_10 in [1,2,3,4]:
    print("-------")
print("오케이 다음으로 넘어가보자")















print()
print("41. for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.")

for practice_41 in range(100):
    print(practice_41)

print()
print("42. 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.")

for practice_42 in range(2002,2051,4):
    print(practice_42)

print()
print("43. 1부터 30까지의 숫자 중 3의 배수를 출력하라.")

for practice_43 in range(3, 31, 3):
    print(practice_43)

print()
print("44. 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.")

for practice_44 in range(100):
    print(99 - practice_44)

print()
print("45. for문을 사용해서 아래와 같이 출력하라.")

for practice_45 in range(10):
    print(practice_45/10)

print()
print("46. 구구단 3단을 출력하라.")

for practice_46 in range(1,10):
    print(3, " X ", practice_46, "=", 3 * practice_46)

print()
print("47. 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.")

for practice_47 in range(1,10,2):
    print(3, " X ", practice_47, "=", 3 * practice_47)

print()
print("48. 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.")

sum = 0 #sum 위치 매우 중요
for practice_48 in range(1, 11):
    #여기에 sum들어가면 합 안나오고, 리스트로만 나옴
    sum += practice_48
    print(sum)
print("indent의 중요성")
print(sum)


print()
print("49. 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.")

sum = 0
for practice_49 in range(1,11,2):
    sum += practice_49
print(sum)

print()
print("50. 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.")

multiplier = 1
for practice_50 in range (1,11):
    multiplier *= practice_50
print(multiplier)