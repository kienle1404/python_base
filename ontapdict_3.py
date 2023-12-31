# Write function find_matching that gets a list of strings and a search
# string as parameters. The function should return the indices to those
# elements in the input list that contain the search string. Use the
# function enumerate. An example: find_matching(["sensitive",
# "engine", "rubbish", "comment"], "en") should return the list [0, 1, 3].

def find_matching(input_list:list, search_string:str)->[int]:
    indicies = [index for index, string in enumerate(input_list) if search_string in string]
    return indicies

print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))   