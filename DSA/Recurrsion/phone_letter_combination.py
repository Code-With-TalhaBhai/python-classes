

def letterCombinations(digits: str):
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
    output = []

    def find_combination(idx,comb):
        if len(comb) >= len(digits):
            output.append(comb)
            return
        
        # print('enterings')
        for i in range(len(phone_number_letters[digits[idx]])):
            comb += phone_number_letters[digits[idx]][i]
            find_combination(idx+1,comb)
            comb = comb[:-1]


    find_combination(0,"")
    return output




print(letterCombinations("237"))
