with open("data.txt","r") as f:
    data = f.readline()
print(data)

# readlines() method is used as prints all the lines in file
# readline() method is used as print the first line in file
# readline(5) it prints first five lines of the file

'''
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
print(data.readline())'''
