def split_dictionary(input_dict:dict)->[dict]:
    keys = input_dict.keys()
    values = input_dict.values()
    list_dict = []
    for v in zip(*values):
        d = {k:v for k, v in zip(keys, v)}
        # for k, v in zip(keys, v):
        #     d[k] = v
        list_dict.append(d)
    return list_dict

if __name__ == "__main__":
    input_dict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80], 
                  'English': [83, 79, 68, 92]}
    print(split_dictionary(input_dict))  