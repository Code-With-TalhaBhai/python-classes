



def strStr(haystack: str, needle: str) -> int:

    i = 0

    while i < len(haystack)+1-len(needle):
        k = i
        j = 0
        z = len(needle)
        while j < len(needle):
            if haystack[k] != needle[j]:
                break
            k += 1
            j += 1
            z -= 1
            if z == 0:
                return i
        i += 1
    return -1



print(strStr('sadbutsad','sad'))
print(strStr('leetcode','leeto'))
print(strStr('"mississippi"','"issipi"'))