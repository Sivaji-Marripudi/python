list = ['hyd','bnglr','chennai','mumbai','delhi','pune','ong','nlr','gnt']
with open('files_list.txt','w') as f:
    for i in list:
        data = f.write('%s\n'% i)
dataa = open('files_list.txt','r')
for i in dataa:
    print(i)
dataa.close()