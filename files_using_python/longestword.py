with open('data.txt','r') as f:
    data = f.readlines()
    #print(data)
    first = data[0]
    print(first)
    for i in data:
        if len(i) > len(first):
            maxx = i
    print(maxx)