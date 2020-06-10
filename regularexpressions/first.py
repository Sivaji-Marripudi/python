import re
emails = '''
CoreyMSchafer@gmail.com
corey+schafer@university.edu
corey-321-schafer@my-work.net
'''
pattern = re.compile("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
# finditer is used as iterate the matchings
matches = pattern.finditer(emails)
for match in matches:
    print(match)
# findall is used to create the matches on the list
matchess = pattern.findall(emails)
print(matchess)

