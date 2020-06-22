import os
if os.path.exists('new_data.csv'):
    os.remove('new_data.csv')
    print('deleted')
else:
    print('file does not exists')