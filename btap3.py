''' In English, the present participle is formed by adding the suffix -ing to the infinite form: go
-> going. A simple set of heuristic rules can be given as follows:
• If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
• If the verb ends in ie, change ie to y and add ing
• For words consisting of consonant-vowel-consonant, double the final letter before adding
ing
• By default just add ing
Your task in this exercise is to define a function make_ing_form() which given a verb in
infinitive form returns its present participle form. Test your function with words such as lie, see,
move and hug. However, you must not expect such simple rules to work for all cases.
'''

def make_ing_form(inputstr:str)->str:
    vowel = list("ueoai")
    word_exception = ["be", "see", "flee", "knee"]
    # if inputstr[-2:] == 'ie':
    if inputstr.endswith("ie"):
        return inputstr[:-2] + "ying"
    
    elif inputstr[-1] == 'e':
        if inputstr in word_exception:
            return inputstr + "ing"
        else:
            return inputstr[:-1] + "ing"
    
    elif len(inputstr) >= 3 and inputstr[-3] not in vowel and inputstr[-2] in vowel and inputstr[-1] not in vowel:
        return inputstr + inputstr[-1] + "ing"
    
    else:
        return inputstr + "ing"

if __name__ == "__main__":
    while True:
        print(make_ing_form(input("Enter a verb: ")))