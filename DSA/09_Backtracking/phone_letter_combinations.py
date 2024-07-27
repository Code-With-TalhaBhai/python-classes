

def phone_letter_combination(phone_number_letters,digits):
    res = []
    n = len(digits)

    if digits == "":
        return []


    def backtrack(x,my_str):

        if x == n:
            res.append(my_str)
            return

        # digit = int(digits[x]) # For List
        digit = digits[x] # For Dictionary
        digit_letters = phone_number_letters[digit]

        for char in digit_letters:
            my_str += char
            backtrack(x+1,my_str)
            my_str = my_str[:-1]


    backtrack(0,"")
    return res





# phone_number_letters = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
phone_number_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
print(phone_letter_combination(phone_number_letters,"23"))
print(phone_letter_combination(phone_number_letters,""))
print(phone_letter_combination(phone_number_letters,"2"))
print(phone_letter_combination(phone_number_letters,"234"))