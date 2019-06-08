import json
import difflib

data = json.load(open("data.json"))
word = str(input('Enter a word: ')).strip()

def findMeaning(w):
    w = w.lower()
    guess = difflib.get_close_matches(w, data.keys())
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(guess) > 0:
        response = input("Did you mean {} instead? Type 'Y' for Yes and 'N' for No: " .format(guess[0])).upper()
        
        suggestion = lambda r: \
        {'Y':data[guess[0]],'N':'Then please check the word and try again'} \
        .get(r,"Sorry, I didn't get that.")
        return suggestion(response)
    
               
    else:
        return 'The word does not exist. Please double check it.'


output = findMeaning(word)


if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
    