


def compute_lps(pattern):
    n = len(pattern)
    lps = [0] * n

    p,i = 0,1

    while i < n:
        if pattern[i] == pattern[p]:
            p += 1
            lps[i] = p
            i += 1
        else:
            if p != 0:
                p = lps[p-1]
            else:
                lps[i] = 0
                i += 1
    return lps





def string_matching_kmp_first_occurrence(haystack,needle):
    lps = compute_lps(needle)

    i,j = 0,0
    while i < len(haystack):
        
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == len(needle):
            return i - len(needle)
    return -1



def string_matching_kmp_all_occurrences(haystack,needle):
    lps = compute_lps(needle)

    i,j = 0,0
    occurrences = []
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == len(needle):
            occurrences.append(i-len(needle))
            j = lps[j-1]
        
        
    return occurrences



print(string_matching_kmp_first_occurrence('sadbutsad','sad'))
print(string_matching_kmp_first_occurrence('butsad','sad'))
print(string_matching_kmp_first_occurrence('leetcode','leeto'))
print()
print(string_matching_kmp_all_occurrences('sadbutsad','sad'))
print(string_matching_kmp_all_occurrences('butsad','sad'))
print(string_matching_kmp_all_occurrences('leetcode','leeto'))
