print("*" * 36)
print("*      전화번호 관리 프로그램      *") 
print("*" * 36)
print("\n")

print("1.리스트 2.등록 3.삭제 4.검색 5.종료")
print("-" * 36)
menu_choice = int(input(">메뉴번호: "))

while menu_choice != 5:
    match menu_choice:
        case 1:
            print("<1.리스트>")
            filePath = "/Users/yuchan/Desktop/PhoneDB.txt"
            with open(filePath, "r") as file:
                print("\n")
                data = file.read()
                for index, entry in enumerate(data.split("\n")):
                    entry = entry.strip()
                    personVo = entry.split(",")
                    for index2, entry2 in enumerate(personVo):
                        person_vo = {name  }
        case 2:
            print("<2.등록>")
            name = input(">이름: ")
            hp = input(">전화번호: ")  
            company = input(">회사전화: ") 
            filePath = "/Users/yuchan/Desktop/PhoneDB.txt"
            with open(filePath, "a") as file:
                file.write(f"{name},{hp},{company}\n")
            print("[등록되었습니다]")
        case 3:
            print("<3.삭제>")
            index = int(input(">번호: "))
            filePath = "/Users/yuchan/Desktop/PhoneDB.txt"
            with open(filePath, "r") as file:
                data = file.read()
            with open(filePath, "w") as file:
                for line_index, line in enumerate(data):
                    if line_index + 1 == index:
                        file.write("")
                        print("[삭제되었습니다]")
                    elif index > len(data):
                        print("존재하지 않는 번호입니다.")
                


    print("\n1.리스트 2.등록 3.삭제 4.검색 5.종료")
    print("-" * 36)
    menu_choice = int(input(">메뉴번호: "))
