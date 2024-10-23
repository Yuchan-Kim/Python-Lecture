def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        a/b
        return a/b
    except ZeroDivisionError as e:
        print("0으로 나눌 수 없습니다.")
    except Exception as e:
        print(f"에러: {e}")
    finally:
        print("계산이 완료되었습니다.")
    