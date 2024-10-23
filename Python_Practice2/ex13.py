

filePath= "/Users/yuchan/Desktop/PhoneDB.txt"
file =open(filePath,"r")
print(file)

data = file.read()
print(data)

file.close()

