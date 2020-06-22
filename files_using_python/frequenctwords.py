with open('data.txt','r') as f:
    data = f.readlines()
    from collections import Counter
    a = Counter(data)
    print(a)