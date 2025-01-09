


def longest_palindromic_string(s):
    n = len(s)
    palindrome = ""
    palindrome_len = 0

    for i in range(n):

        l,r = i,i
        while l >= 0 and r < n and s[l] == s[r]:
            curr_len = (r-l)+1
            if curr_len > palindrome_len:
                palindrome_len = curr_len
                palindrome = s[l:r+1]
            l -= 1
            r += 1

        l,r = i,i+1
        while l >= 0 and r < n and s[l] == s[r]:
            curr_len = (r-l)+1
            if curr_len > palindrome_len:
                palindrome_len = curr_len
                palindrome = s[l:r+1]
            l -= 1
            r += 1

    return palindrome
        
            




pal_str1 = "babad"
pal_str2 = "naak"
pal_str3 = "bb"


print(longest_palindromic_string(pal_str1))
print(longest_palindromic_string(pal_str2))
print(longest_palindromic_string(pal_str3))


