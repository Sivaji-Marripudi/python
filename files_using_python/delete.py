import os
if os.path.exists('data1.txt'):
    os.remove('data1.txt')
    print('deleted')
else:
    print('file does not exists')
'''
# remove folder using python
import os
os.rmdir('myfolder')
'''