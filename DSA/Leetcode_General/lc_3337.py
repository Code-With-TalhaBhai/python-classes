


def lengthAfterTransformations1(s,t,nums):

    res = s
    for _ in range(t):
        final = ''
        for char in res:
            no_of_characters = nums[ord(char) - ord('a')]
            for j in range(1,no_of_characters+1):
                check = ord(char)+j
                if check > ord('z'):
                    final += chr((check % ord('z'))+ord('a')-1)
                else:
                    final += chr(check)
            res = final
    return len(final)



def lengthAfterTransformations2(s,t,nums):
    n = len(nums)
    T = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            ...




s1 = "abcyy"
t1 = 2
nums1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

s2 = "azbk"
t2 = 1
nums2 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]



print('brute-force')
print(lengthAfterTransformations1(s1,t1,nums1))
print(lengthAfterTransformations1(s2,t2,nums2))
print('optimal')
print(lengthAfterTransformations2(s1,t1,nums1))
print(lengthAfterTransformations2(s2,t2,nums2))