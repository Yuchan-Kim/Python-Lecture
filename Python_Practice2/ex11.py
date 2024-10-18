x=5
def calPlus(no):
    return no + x

print(calPlus(10))

def calPlus2(no):
    x=1
    return no + x

print(calPlus2(10))

def calPlus3(mode, no):
    if mode == "sum":
        return no + x
    elif mode == "mul":
        return no * x
    else:
        print("error")

    return no

print(calPlus3("mul",10))
print(calPlus3("sum",10))