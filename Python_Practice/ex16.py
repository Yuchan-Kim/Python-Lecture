#List 
names = ["박지민","김지민","홍지민"]
print(names[0],names)

#List append
names.append("하하하")
print(names)

#List remove
names.remove("하하하")
print(names)

#List insert
names.insert(1,"하하하")
print(names)

#List pop
names.pop(1)
print(names)

#List extend
names.extend(["하하하","하하하"])
print(names)

#List sort
names.sort()
print(names)

#List reverse
names.reverse()
print(names)

#List index
print(names.index("박지민"))

#List count
print(names.count("하하하"))

#List copy
copied_names = names.copy()
print(copied_names)

#List clear
names.clear()
print(names)



