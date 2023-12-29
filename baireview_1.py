# 1.	Write function to verify credit card from ABCD Bank has the following characteristics: 
# •	It must start with a 4,  5 or 6.
# •	It must contain exactly 16 digits.
# •	It must only consist of digits (0-9).
# •	It may have digits in groups of 4 , separated by one hyphen "-".
# •	It must NOT use any other separator like ' ' , '_', etc.
# •	It must NOT have 4 or more consecutive repeated digits.
# Example:
# Valid Number:
# 4253625879615786
# 4424424424442444
# 5122-2368-7954-3214

# Invalid Number:
# 42536258796157867       #17 digits in card number → Invalid 
# 4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
# 5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
# 44244x4424442444        #Contains non digit characters → Invalid
# 0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
# 123---37464619487382


def verify_card(card_number:str)->bool:
    if len(card_number) == 19:
        for num in card_number.split('-'):
            if len(num) != 4:
                return False  
        # if False in [len(num) != 4 for num in card_number.split("-")]:
        #     return False
        card_number = card_number.replace('-', '')
    if len(card_number) == 16:
        if not card_number.isdigit():
            return False
        if card_number[0] not in "456":
            return False
        # for index, digit in enumerate(card_number[:-3]):
        #     if digit * 3 == card_number[index + 1:index + 4]:
        #         return False
        if True in [digit * 4 in card_number for digit in set(card_number)]:
            return False
        # for digit in set(card_number):
        #     if digit * 4 in card_number:
        #         return False
        return True
    return False    
while True:
    print(verify_card(input("Enter card number: ")))