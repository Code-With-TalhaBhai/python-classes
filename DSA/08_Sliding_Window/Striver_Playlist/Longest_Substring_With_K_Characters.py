


def longest_substring_with_at_most_k_distinct_characters1(s,k) -> int:
    n = len(s)
    basket = {}
    max_len = 0
    l = 0


    for r in range(n):
        if s[r] not in basket:
            basket[s[r]] = 1
        else:
            basket[s[r]] += 1

        while len(basket) > k:
            basket[s[l]] -= 1
            if basket[s[l]] == 0:
                basket.pop(s[l])
            l += 1
        max_len = max(max_len,r-l+1)
    return max_len



def longest_substring_with_at_most_k_distinct_characters2(s,k) -> int:
    n = len(s)
    basket = {}
    max_len = 0
    l = 0

    for r in range(n):
        if s[r] not in basket:
            basket[s[r]] = 0
        basket[s[r]] += 1

        if len(basket) > 2:
            basket[s[l]] -= 1
            if basket[s[l]] == 0:
                basket.pop(s[l])
            l += 1
        max_len = max(max_len,r-l+1)
    return max_len


s1 = "eceba"
s2 = "aa"


print(longest_substring_with_at_most_k_distinct_characters1(s1,2))
print(longest_substring_with_at_most_k_distinct_characters1(s2,2))
print('Optimal')
print(longest_substring_with_at_most_k_distinct_characters2(s1,2))
print(longest_substring_with_at_most_k_distinct_characters2(s2,2))
