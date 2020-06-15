import json
from difflib import get_close_matches
data = json.load(open('dictionary.json'))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input('did you mean % s instead ? enter y if yes,or n if no : ')
        yn = yn.lower()
        if yn == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'n':
            return 'the word does not exists.plz double check it.'
        else:
            return 'we dont understand your entry'
    else:
        return 'the word does not exists.plz double check it'
    word = input('enter word: ')
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    input('please enter to exists')