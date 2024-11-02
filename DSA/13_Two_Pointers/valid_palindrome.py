

def validPalindrome1(s):
    i,j = 0,len(s)-1

    while i <= j:
        first = ord(s[i])
        second = ord(s[j])

        if (first > 0 and first < 47) or (first > 57 and first < 65) or (first > 90 and first < 97) or first > 122:
            i += 1
        elif (second > 0 and second < 47) or (second > 57 and second < 65) or (second > 90 and second < 97) or second > 122:
            j -= 1
        else:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
    return True


def validPalindrome2(s):
    i,j = 0,len(s)-1

    while i <= j:
        print(i," ",j)
        if s[i].isalnum() == False:
            i += 1
            continue
        if s[j].isalnum() == False:
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


s1 = "A man, a plan, a canal: Panama"
# amanaplanacanalpanama -> check after removing spaces and special characters
print(validPalindrome1(s1))
print(validPalindrome2(s1))

s2 = "race a car"
print(validPalindrome1(s2))
print(validPalindrome2(s2))
