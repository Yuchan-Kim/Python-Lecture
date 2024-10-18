#튜블로 파라미터 값의 갯수 다양하게 받기
def sum_many(*args):
    print (args)
    sum = 0
    for no in args:
        sum += no
        print(sum)
    
    print("-" * 20)

sum_many(1,2)
sum_many(1,2,3)
sum_many(1,2,3,4)

#다른 타입의 파라미터 값을 같이 사용할떄
def sum_mul(mode, *args):
    if mode == "sum":
        result = 0
        for i in args:
            result += i
    elif mode == "mul":
        result = 1
        for i in args:
            result *= i
    return result

print(sum_mul("sum", 1,2,3,4,5))
print(sum_mul("mul", 1,2,3,4,5))


# *이 한개 인 변수는 갯수만 따지고, ** 두개는 튜플 값으로 온다 (키, 값)
def addperson(hp, **kwargs):
    print("hp" + hp)
    print(kwargs)


addperson(0, (22,3))