num = input("숫자 입력:")
num = int(num)

if num > 0:
    if num%2 == 0:
        print("짝수")
    elif num%2 == 1:
        print("홀수")
elif num < 0:
    print("음수")
else:
    print("0")


lectureCode = int(input("Enter lecture code: "))

if lectureCode == 1:
    print("R01")
elif lectureCode == 2:
    print("R02")
elif lectureCode == 3:
    print("R03")
elif lectureCode == 4:
    print("R04")
elif lectureCode == 5:
    print("R05")
else:
    print("해당 강의실은 존재하지 않습니다.")

lectureCode = int(input("Enter lecture code: "))

rooms = {
    1: "R01",
    2: "R02",
    3: "R03",
    4: "R04",
    5: "R05"
}

print(rooms.get(lectureCode, "해당 강의실은 존재하지 않습니다."))

lectureCode = int(input("Enter lecture code: "))
match lectureCode:
    case 1:
        print("R01")
    case 2:
        print("R02")
    case 3:
        print("R03")
    case 4:
        print("R04")
    case 5:
        print("R05")
    case _:
        print("해당 ��의실은 ���재하지 않습니다.")


