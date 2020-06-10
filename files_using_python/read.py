with open("data.txt","r") as f:
    data = f.read()
print(data)
# using loops
for i in data:
    print(i)
##### another method for open the file  ######
data = open("data.txt","r")
print(data.read())
# read only 5 lines
print(data.read(5))
# only one line
print(data.read(1))
#.......or
print(data.readline())
