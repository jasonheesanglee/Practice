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
print("11. 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 화면에 출력하라. 단 부가세는 10원으로 가정한다.")
for practice_11 in [100, 200, 300]:
    print(practice_11+10)
print("나는 이렇게 했는데 답은 아래처럼 하라고 하네...?")
print()
리스트 = [100, 200, 300]
for 변수 in 리스트:
  print(변수 + 10)

print()
print("12. 리스트에 저장된 값을 다음과 같이 출력하라.")
for practice_12 in ["김밥", "라면", "튀김"]:
    print("오늘의 메뉴: " + practice_12)
print("좋아좋아")

print()
print("13. 리스트에 주식 종목이름이 저장돼 있다." + "저장된 문자열의 길이를 다음과 같이 출력하라.")
for practice_13 in ["SK하이닉스", "삼성전자", "LG전자"]:
    print(len(practice_13))
print("잘하고 있군")

print()
print("14. 리스트에는 동물이름이 문자열로 저장돼 있다." + "동물 이름과 글자수를 다음과 같이 출력하라.")
print()
#for practice_14 in ['dog', 'cat', 'parrot']:
#    print(practice_14 + len(practice_14))
print("이거 왜 안돼냐...")
print()
for practice_14 in ['dog', 'cat', 'parrot']:
    print(practice_14, len(practice_14))
print("아... 오케...")
print()

print("15. 리스트에 동물 이름 저장돼 있다. for문을 사용해서 동물 이름의 첫 글자만 출력하라.")
for practice_15 in ['dog', 'cat', 'parrot']:
    print(practice_15[0])
print("조금 헷갈렸지만, 리스트라는 특성 사용!")

print()
print("16. 리스트에는 세 개의 숫자가 바인딩 돼 있다. for문을 사용해서 다음과 같이 출력하라.")
for practice_16 in [1, 2, 3]:
    print("3 X", practice_16)
print("나는 이렇게 했지만")
print()
for practice_16 in [1, 2, 3]:
    print("3 X " + str(practice_16))
print("이렇게도 할 수 있다고 하네!")

print()
print("17. 리스트에는 세 개의 숫자가 바인딩돼 있다. for문을 사용해서 다음과 같이 출력하라.")
for practice_17 in [1, 2, 3]:
    print("3 X", practice_17, "=", practice_17*3)
print("어렵지 않군...!")
print()
for practice_17 in [1, 2, 3]:
    print("3 X {} = {}".format(practice_17, practice_17*3))
print("이렇게도 할 수 있다고 하네..!")

print()
print("18. 리스트에는 네 개의 문자열이 바인딩돼 있다. for문을 사용해서 다음과 같이 출력하라.")
#for practice_18 in ["가", "나", "다", "라"]:
#    print(str(practice_18 (1,3)))
print("음... 잠시만...")
practice_18 = ["가", "나", "다", "라"]
practice_18_1 = practice_18[1:]
for practice_18_2 in practice_18_1:
    print(practice_18_2)
print("아! 슬라이싱!")
print()
print("조금 더 간략화 해서 아래처럼 쓸 수도 있다!")
practice_18 = ["가", "나", "다", "라"]
for practice_18_3 in practice_18[1:]:
    print(practice_18_3)

print()
print("19. 리스트에는 네 개의 문자열이 바인딩돼 있다. for문을 사용해서 다음과 같이 출력하라.")
practice_19 = ["가", "나", "다", "라"]
for practice_19_1 in practice_19[0]:
    print(practice_19_1)
for practice_19_2 in practice_19[2]:
    print(practice_19_2)
print("이렇게 말고 다른 방법이 있을거 같은데...")
print()
print("리스트 슬라이싱에서 `[시작:끝:증감폭] ` 세번째 값은 값을 가져오는 단위를 의미했습니다. 증감폭을 2로 설정해서 \"가\"와 \"다\" 값만 슬라이싱합니다.")
practice_19 = ["가", "나", "다", "라"]
for practice_19_3 in practice_19[::2]:
    print(practice_19_3)
print("역시...!")

print()
print("20. 리스트에는 네 개의 문자열이 바인딩돼 있다. for문을 사용해서 다음과 같이 출력하라.")
practice_20 = ["가", "나", "다", "라"]
print()
#for practice_20_1 in practice_20[3:0]:
#    print(practice_20_1)
print("아 이게 안되네..")
print("아!")
print()
print("증감폭을 음수로 설정하면 끝에서 앞방향으로 값을 슬라이싱합니다.")
practice_20 = ["가", "나", "다", "라"]
for practice_20_2 in practice_20[::-1]:
    print(practice_20_2)

print()
print("21. 리스트에는 네 개의 정수가 저장돼 있다. for문을 사용해서 리스트의 음수를 출력하라.")
print()
#practice_21 = [3, -20, -3, 44]
#for practice_21_1 in practice_21[0>:]:
#    print(practice_21_1)
print("아... 이거 아니구")
print()
practice_21 = [3, -20, -3, 44]
for practice_21_1 in practice_21:
    if practice_21_1 < 0:
        print(practice_21_1)
print("음 이거군!")

print()
print("22. for문을 사용해서 3의 배수만을 출력하라.")
practice_22 = [3, 100, 23, 44]
for practice_22_1 in practice_22:
    if practice_22_1 % 3 == 0:
        print (practice_22_1)
print("1트만에 성공!")

print()
print("23. 리스트에서 20 보다 작은 3의 배수를 출력하라")
practice_23 = [13, 21, 12, 14, 30, 18]
for practice_23_1 in practice_23:
    if practice_23_1 < 20:
        if practice_23_1 % 3 == 0:
            print(practice_23_1)
print("출력값은 맞는데, and 로도 쓸수 있다!")
print()
practice_23 = [13, 21, 12, 14, 30, 18]
for practice_23_1 in practice_23:
    if practice_23_1 < 20 and practice_23_1 % 3 == 0:
        print(practice_23_1)
print("이렇게!")

print()
print("24. 리스트에서 세 글자 이상의 문자를 화면에 출력하라")
practice_24 = ["I", "study", "python", "language", "!"]
for practice_24_1 in practice_24:
    if len(practice_24_1) >= 3:
        print (practice_24_1)
print("str을 붙여줘야 하나 했는데 이게 맞네?")
print()
practice_24 = ["I", "study", "python", "language", "!"]
for practice_24_1 in practice_24:
    if len(str(practice_24_1)) >= 3:
        print (practice_24_1)
print("str 붙여줘도 값은 동일하게 나오는구나!")

print()
print("25. 리스트에서 대문자만 화면에 출력하라.")
print("난관이다.. 안배운건데...")
print()
print("(참고) isupper() 메서드는 대문자 여부를 판별합니다.")
print("문제에서 알려줘서 다행ㅎㅎ")
print()
practice_25 = ["A", "b", "c", "D"]
for practice_25_1 in practice_25:
    if practice_25_1.isupper() == True:
        print(practice_25)
print("알려줘도 틀리네...")
print()
practice_25 = ["A", "b", "c", "D"]
for practice_25_2 in practice_25:
    if practice_25_2.isupper():
        print(practice_25_2)
print("아 뭐야... 틀렸던 답에서 변수 프린트 안하고 리스트를 프린트했잖아...? 여러분 코드 한줄 한줄 잘 봅시다...")
print("이건 일단 정답지 답안")
print()
practice_25 = ["A", "b", "c", "D"]
for practice_25_1 in practice_25:
    if practice_25_1.isupper() == True:
        print(practice_25_1)
print("그래서 내가 쓴 코드로 다시 해봄...! 이거도 되네! 실수만 하지 맙시다...")

print()
print("26. 리스트에서 소문자만 화면에 출력하라.")
practice_26 = ["A", "b", "c", "D"]
for practice_26_1 in practice_26:
    if practice_26_1.isupper() == False:
        print(practice_26_1)
print("25번문제 다시 해보길 잘했네")
print("아래 방법들로도 할 수 있구나!")
print()
practice_26 = ["A", "b", "c", "D"]
for practice_26_2 in practice_26:
    if practice_26_2.isupper() != True:
        print(practice_26_2)
print()
print("혹은")
print()
practice_26 = ["A", "b", "c", "D"]
for practice_26_3 in practice_26:
    if not practice_26_3.isupper():
        print(practice_26_3)
print()
print("27. 이름의 첫 글자를 대문자로 변경해서 출력하라.")
print("위 방법들을 잘 섞으면 되는건가...?")
practice_27 = ['dog', 'cat', 'parrot']
for practice_27_1 in practice_27:
    if practice_27_1[0].isupper():
        print(practice_27_1)
print()
print("아니네, isupper은 대문자 판별이구나... 대문자로 만드는게 아니라... 자 예문에서 준 .upper을 써보자")
print("(참고) upper() 메서드는 문자열을 대문자로 변경합니다.")
practice_27 = ['dog', 'cat', 'parrot']
for practice_27_2 in practice_27:
    if practice_27_2.upper():
        print(practice_27_2)
print("뭐지... .upper쓰면 된다매... 왜 안되는데... 리스트라 안되는건가")
print("차근차근 해보자 일단 분리")
practice_27 = ['dog', 'cat', 'parrot']
for practice_27_3 in practice_27:
    print(practice_27_3[0])
print("일단 맨 글자 분리 성공")
print()
for practice_27_4 in practice_27:
    print(practice_27_4[1:])
print("쭉 뒤로 분리 성공, 자 이제 첫번째 꺼만 대문자로 바꿔서 뒷글자들이랑 합쳐보자")
print()
print(practice_27_3.upper()+practice_27_4)
print("아 형 잠깐만... 다시 해볼게요")
print()
print(practice_27_3[0].upper(), practice_27_4[1:])
print("뭔가 이상한데... 다시 해보자")
print()
print(practice_27_3[0].upper() + practice_27_4[1:])
print("Parrot은 됐다... 근데 나머지는 어디갔는데... 하아..")
print("처음부터 다시 해보자")
print()
practice_27 = ['dog', 'cat', 'parrot']
for practice_27_5 in practice_27:
    practice_27_5 = practice_27_5[0]
    print(practice_27_5.upper())
print("좋아... 일단 첫 글자들을 대문자로 만들기 성공... 대문자로 만든걸 또 변수로 만들자")
print()
practice_27_6 = (practice_27_5.upper())
print(practice_27_6)
print("아니 practice_27.5.upper()을 그대로 practice_27_6으로만 만든건데 왜 이게 프린트가 안되는데... 하아... 정답지를 한번 보자...")
print()
practice_27 = ['dog', 'cat', 'parrot']
for practice_27_7 in practice_27:
    practice_27_8 = practice_27_7[0]
    practice_27_9 = practice_27_8.upper()
    print(practice_27_9 + practice_27_7[1:])
print("뭐야 왜 이게 돼, 내가 위에서 비슷하게 했구만")
print()
practice_27 = ['dog', 'cat', 'parrot']
for practice_27_10 in practice_27:
    practice_27_11 = practice_27_10[0]
    print(practice_27_11.upper())
    practice_27_12 = practice_27_11.upper()
    print(practice_27_12 + practice_27_10[1:])
print("위에꺼 그대로 가져오고 비슷하게 했는데 왜 중간에 저게 들어가는데... 설마 중간에 프린트한번 넣어서 그래...?")
print()
for practice_27_13 in practice_27:
    practice_27_14 = practice_27_13[0]
    practice_27_15 = practice_27_14.upper()
    print(practice_27_15 + practice_27_13[1:])
print("어휴... 중간에 프린트 넣으면 안되는군... 다음으로 넘어가 보자")

print()
print("28. 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)")
practice_28 = ['hello.py', 'ex01.py', 'intro.hwp']
for practice_28_1 in practice_28:
    practice_28_2 = practice_28_1.split(".")
    print(practice_28_2)
print("아니 .split을 이렇게 쓰는게 맞다고??ㅋㅋㅋㅋㅋ 갑자기 기분 좋아지네")
print()
practice_28 = ['hello.py', 'ex01.py', 'intro.hwp']
for practice_28_3 in practice_28:
    practice_28_4 = practice_28_3.split(".")
    print(practice_28_4[0])
print("위에서 당하고 왔더니 이건 쉽네")

print()
print("29. 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.")
practice_29 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for practice_29_1 in practice_29:
    practice_29_2 = practice_29_1.split(".")
    if practice_29_2[1] == "h":
        print(practice_29_2)
print("아... 뭔가 아쉽게 틀렸는데... 잠시만...")
print()
practice_29 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for practice_29_3 in practice_29:
    practice_29_4= practice_29_3.split(".")
    if practice_29_4[1] == "h":
        print(practice_29_3)
print("위에랑... 다른게... 뭐지...")
print("왜... 29_3을 프린트하지..?")

print()
print("30. 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.")
practice_30 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for practice_30_1 in practice_30:
    practice_30_2 = practice_30_1.split(".")
    if practice_30_2[1] != "py":
        print(practice_30_1)
print("이게 맞긴한데.. 난 이거 말고 다른 방법으로 해보고 싶은데... 이거는 py만 아니면 되는거라 h나 c가 아닌 확장자가 많아지면 무용지물임...")
print()
practice_30 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for practice_30_3 in practice_30:
    practice_30_4 = practice_30_3.split(".")
    if practice_30_4[1] == "h" or "c":
        print(practice_30_3)
print("아니 이건 왜 또 안되는데")
print("아... or을 따로 넣어야 되는구나...")
print()
practice_30 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for practice_30_5 in practice_30:
    practice_30_6 = practice_30_5.split(".")
    if practice_30_6[1] == "h" or practice_30_6[1] == "c":
        print(practice_30_5)
print("됐다")


print()
print()
print("사실 이 연습문제를 풀기 시작한게 31번 - 40번 풀어보려고 시작한거라...")
print("가장 처음에 풀었던 31번부터 40번까지는 이런 주석 안달고 문제만 풀어서 재미 없을수도 있어요...!")
print("감안하고 봐주세요! (근데 누가 본다는거지 이런걸...)")

print()
print()
print()
print("31. for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.")

for practice_31 in range(100):
    print(practice_31)

print()
print("32. 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.")

for practice_32 in range(2002,2051,4):
    print(practice_32)

print()
print("33. 1부터 30까지의 숫자 중 3의 배수를 출력하라.")

for practice_33 in range(3, 31, 3):
    print(practice_33)

print()
print("34. 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.")

for practice_34 in range(100):
    print(99 - practice_34)

print()
print("35. for문을 사용해서 아래와 같이 출력하라.")

for practice_35 in range(10):
    print(practice_35/10)

print()
print("36. 구구단 3단을 출력하라.")

for practice_36 in range(1,10):
    print(3, " X ", practice_36, "=", 3 * practice_36)

print()
print("37. 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.")

for practice_37 in range(1,10,2):
    print(3, " X ", practice_37, "=", 3 * practice_37)

print()
print("38. 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.")

sum = 0
print("sum 위치 매우 중요")
for practice_38 in range(1, 11):
#print("여기에 sum들어가면 합 안나오고, 리스트로만 나옴")
    sum += practice_38
    print(sum)
print("indent의 중요성")
print(sum)


print()
print("39. 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.")

sum = 0
for practice_39 in range(1,11,2):
    sum += practice_39
print(sum)

print()
print("40. 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.")

multiplier = 1
for practice_40 in range (1,11):
    multiplier *= practice_40
print(multiplier)

print()
print("41. 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.")
practice_41 = [32100, 32150, 32000, 32500]
for practice_41_1 in range(4):
    print(practice_41[practice_41_1])
print("음...")
print()
practice_41 = [32100, 32150, 32000, 32500]
for practice_41_2 in range(len(practice_41)):
    print(practice_41[practice_41_2])
print("이렇게 해도 된다네...?")

print()
print("42. 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.")
practice_42 = [32100, 32150, 32000, 32500]
for practice_42_1 in range(4):
    print(len(practice_42) + practice_42[practice_42_1])
print("아 이게 아니잖아.. 다시")
print()

practice_42 = [32100, 32150, 32000, 32500]
for practice_42_2 in range(4):
    print(practice_42_2, practice_42[practice_42_2])
print("와 이건... 답안지도 없길래 겨우 했네..")

print()
print("43. 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.")
practice_43 = [32100, 32150, 32000, 32500]
for practice_43_1 in range(-1):
    print(practice_43_1, practice_43[practice_43_1])
print("앗 이건 아니네")
print()
practice_43 = [32100, 32150, 32000, 32500]
for practice_43_2 in range(len(practice_43)):
    print(3-practice_43_2, practice_43[practice_43_2])
print("음... 뭐지... 아 아래처럼 해보면 더 이해가 쉽다!")
print()
practice_43 = [32100, 32150, 32000, 32500]
for practice_43_3 in range(len(practice_43)):
    print((len(practice_43)-1) - practice_43_3, practice_43[practice_43_3])

print()
print("44. 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.")
practice_44 = [32100, 32150, 32000, 32500]
for practice_44_1 in range(1, len(practice_44)):
    print(100+(practice_44_1-1)*10, practice_44[practice_44_1])
print("음... 100을 더하는거 까진 알겠는데 (practice_44_1-1)*10 왜 이거지...")

print()
print("45. my_list를 아래와 같이 출력하라.")
print("조금 헷갈려서 일단 for 안쓰고 해봄...!")
practice_45 = ["가", "나", "다", "라"]
print(practice_45[0], practice_45[1])
print(practice_45[1], practice_45[2])
print(practice_45[2], practice_45[3])
print()
print("이 방법은 for도 안썼고, 질문이 의도한 답은 당연히 아닌거 같으니 한번 답안지를 보자")
for practice_45_1 in [0,1,2]:
    print(practice_45[practice_45_1])
print("이건 한 줄만 쓰는 법")
print()
print("한 행에 두 개의 데이터를 출력하고 싶기 때문에 이전 코드의 print 문에 출력하고 싶은 데이터를 추가합니다.")
print("같은 행의 두 데이터는 인덱스 차이가 +1 이라는 것을 잊지마세요.")
print("i가 0일 때는 0, 1 위치의 값이 출력됩니다.")
print("i가 1일 때는 1, 2 위치의 값이 출력됩니다.")
print("i가 2일 때는 2, 3 위치의 값이 출력됩니다.")

print("라고 한다")
print()
for practice_45_2 in [0,1,2]:
    print(practice_45[practice_45_2], practice_45[practice_45_2+1])
print("이렇게 하는구만...")
print()
print("그런데 이렇게 아래처럼 쓸수도 있다고 함")
for practice_45_3 in range(len(practice_45)-1):
    print(practice_45[practice_45_3], practice_45[practice_45_3+1])
print("혹은 아래처럼")
for practice_45_4 in range(1, len(practice_45)):
    print(practice_45[practice_45_4-1], practice_45[practice_45_4])
print("어렵구만...")

print()
print("46. 리스트를 아래와 같이 출력하라.")
print("자 45번의 저걸 활용해서 다시 한번 해보자")
practice_46 = ["가", "나", "다", "라", "마"]
for practice_46_1 in range(2, len(practice_46)):
    print(practice_46[practice_46_1-2], practice_46[practice_46_1-1], practice_46[practice_46_1])
print("잘 쓴거 같은데 왜 에러가 뜨나 고민했었는데 중간 practice_46[practice_46_1-1] 이거를 practice_46[practice_46-1] 이렇게 써서 안되는 거였다...")

print()
print("47. 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.")
practice_47 = ["가", "나", "다", "라"]
for practice_47_1 in range(2, len(practice_47)+1):
    print(practice_47[practice_47_1-3], practice_47[practice_47_1-4])
print("흠... 왜 두번째가 \"가\"로 시작하지?")
print()
practice_47 = ["가", "나", "다", "라"]
for practice_47_2 in range(len(practice_47)-1):
    print(practice_47[len(practice_47) -1- practice_47_2], practice_47[len(practice_47)-2-practice_47_2])
print("다시 변수 하나를 빼주면서 전체를 반전시킨건가...?")

print()
print("48. 리스트에는 네 개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.")
print("예를들어 100을 기준으로 우측에 위치한 200과의 차분 값를 화면에 출력하고, 200을 기준으로 우측에 위치한 400과의 차분값을 화면에 출력한다. 이어서 400을 기준으로 우측에 위치한 800과의 차분값을 화면에 출력한다.")
print()
print("차분값이 뭔데... = 수열에서 연속하는 두 항의 차")
print()
practice_48 = [100, 200, 400, 800]
for practice_48_1 in range(len(practice_48)-1):
    print(practice_48[len(practice_48) - 1 -practice_48_1] - practice_48[len(practice_48)-1] - 2 - practice_48_1)
print("자 이건 아무래도 아닌거 같다")
print()
print("한번 차근차근 해보자")
practice_48 = [100, 200, 400, 800]
print(practice_48[1] - practice_48[0])
print(practice_48[2] - practice_48[1])
print(practice_48[3] - practice_48[2])

print("원래는 이렇게 나와야 한다")
print()
print("for을 한번 써보자, 너무 복잡하지 않은 걸로")
practice_48 = [100, 200, 400, 800]
for practice_48_2 in [0, 1, 2, 3]:
    print(practice_48[practice_48_2] - practice_48[practice_48_2-1])
print("잘... 나왔는데... -700은 왜...")
print()
print("다시 해보자")
practice_48 = [100, 200, 400, 800]
for practice_48_3 in [0, 1, 2, 3]:
    print(practice_48[practice_48_3] - practice_48[practice_48_3-1])
print("잘... 나왔는데... -700은 왜...")
print("또.. 다시 해보자")
practice_48 = [100, 200, 400, 800]
for practice_48_4 in [0, 1, 2, 3]:
    print(practice_48[practice_48_4] - practice_48[practice_48_4-1])
    if (practice_48[practice_48_4] - practice_48[practice_48_4-1]) < 0:
        print("")
print("일단 값은.. 다 잘 나왔네..")
print()
print("이번엔 공백을 없애보자")
practice_48 = [100, 200, 400, 800]
for practice_48_5 in [0, 1, 2, 3]:
    if practice_48_5 == 0:
        break
    else:
        print(practice_48[practice_48_5] - practice_48[practice_48_5-1])
print("안되는군..")
print()
print("먼저 다른 방식으로 다시 해보자")
for practice_48_6 in range(3):
    print(practice_48[practice_48_6] - practice_48[practice_48_6-1])
print("오.. 뭔가 될꺼 같다... 잠시만")
print()
print("Range에 시작점을... 추가해주면...?")
for practice_48_7 in range(1,4):
    print(practice_48[practice_48_7] - practice_48[practice_48_7-1])
print("오.. 됐다...!!!!!!!")
print()
print("답안지에선 아래와 같은 방법으로 한다")
for practice_48_8 in range(len(practice_48)-1):
    print(abs(practice_48[practice_48_8+1] - practice_48[practice_48_8]))
print("abs (Absolute) 연산자를 쓰면... 굳이 나처럼 안해도 됐었군...!")

print()
print("49. 리스트에는 6일 간의 종가 데이터가 저장되어 있다. 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.")
print("일단 간단하게 먼저 해본다")
practice_49 = [100, 200, 400, 800, 1000, 1300]
print((practice_49[2] + practice_49[1] + practice_49[0])/3)
print((practice_49[3] + practice_49[2] + practice_49[1])/3)
print((practice_49[4] + practice_49[3] + practice_49[2])/3)
print((practice_49[5] + practice_49[4] + practice_49[3])/3)

print()
print("이제 for을 써본다")
practice_49 = [100, 200, 400, 800, 1000, 1300]
for practice_49_1 in range(4):
    print((practice_49[practice_49_1] + practice_49[practice_49_1+1] + practice_49[practice_49_1+2])/3)
print("... 이게 왜 되는거지...???")

print()
print("50. 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.")
practice_50_low = [100, 200, 400, 800, 1000]
practice_50_high = [150, 300, 430, 880, 1000]
print ("먼저 for 안쓰기!")
print(practice_50_high[0] - practice_50_low[0])
print(practice_50_high[1] - practice_50_low[1])
print(practice_50_high[2] - practice_50_low[2])
print(practice_50_high[3] - practice_50_low[3])
print(practice_50_high[4] - practice_50_low[4])

print("예시 답안... 왜... 답이 안나오냐... 이건 당당히 패스하자 문제 자체가 이해가 안된다...!")
practice_50_low = [100, 200, 400, 800, 1000]
practice_50_high = [150, 300, 430, 880, 1000]

volatility = []
for i in range(len(practice_50_low)):
    volatility.append(practice_50_high[i] - practice_50_low[i])

print("일단 여기까지!")
