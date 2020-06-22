with open('data.txt','r') as f:
    data = f.read().split()
    from collections import Counter
    a = Counter(data)
    print(a)