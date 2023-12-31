# Let d be a dictionary that has English words as keys and a list of
# Finnish words as values. So, the dictionary can be used to find out
# the Finnish equivalents of an English word. Make a function 
# reverse_dictionary that creates a Finnish to English
# dictionary based on a English to Finnish dictionary given as a parameter.
# The values of the created dictionary should be lists of words.

def reverse_dictionary(d:dict)->dict:
    fin_to_eng = {}
    for eng_word, fin_words in d.items():
        for fin_word in fin_words:
            if fin_word in fin_to_eng:
                fin_to_eng[fin_word].append(eng_word)
            else:
                fin_to_eng[fin_word] = [eng_word]
    return fin_to_eng

d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
print(reverse_dictionary(d))