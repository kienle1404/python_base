# 2.	Write a function to calculate the depth of nested parentheses in a string containing matched groups of parentheses. Each group of parentheses is separated by space. 
# Example:
# Input: (()) (()) () ((()()()))
# Output: [2, 2, 1, 3]
# Input: () (()) () () () ()
# Output: [1, 2, 1, 1, 1, 1] 
# Input: (((((((()))))))) () (()) ((()()())) 
# Output: [8, 1, 2, 3]

def parentheses_depth(parentheses:str)->list:
    depth = []
    current = 0
    for c in parentheses:
        if c == "(":
            current += 1
        elif c == ")":
            