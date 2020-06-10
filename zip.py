lst1 = []
dict = {}
lst2 = ["hyd","bangalore","chennai","mumbai","pune","noida","kolkata","delhi"]
for i in range(1,len(lst2)+1):
    lst1.append(i)
c = list(zip(lst1,lst2))
for i in c:
    dict[i[1]] = i[0]
print(dict)