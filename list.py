# list is a collection of heterogeneous data items
# list is a mutable i.e changble
# example of a list :-
list = ["siva",22,5.11,"india"]
print(list)
# access the list using index numbers
print(list[1]) # 22
print(list[0:len(list)+1]) # ["siva",22,5.11,"india"]
print(list[::-1]) # it prints reverse of a list
# loop through list
for i in list:
  print(i)
