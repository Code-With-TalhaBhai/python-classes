


def longestPrefix(s: str) -> str:

    prefix = ''
    suffix = ''
    final_str = ''
    n = len(s)

    for i in range(n-1):
        prefix = s[:i+1]
        suffix = s[n-i-1:]
        if prefix == suffix:
            final_str = prefix
    return final_str




s1 = "level"
s2 = "ababab"


print(longestPrefix(s1))
print(longestPrefix(s2))