# right-angle triangle in numbers from 0 to
for i in range(6):
    for j in range(i):
        print(j , end = " ")
    print()

# right-angle in stars
for i in range(6):
    print("*"*i)
# reverse right-angle triangle in stars
n = int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end ="")
    print()
##  ANOTHER METHOD
for i in range(6):
    for j in range(6-i):
        print("*",end ="")
    print()