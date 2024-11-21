


def house_robber_ii_1(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0],nums[1])
    
    #1st way
    # def rob1(i):
    #     if i < 1:
    #         return 0
    #     return max(nums[i]+rob1(i-2),rob1(i-1))

    # def rob2(i):
    #     if i < 0:
    #         return 0
    #     return max(nums[i]+rob2(i-2),rob2(i-1))

    # return max(rob1(n-1),rob2(n-2))

    #2nd way
    def rob(i,num):
        if i < 0:
            return 0

        return max(num[i]+rob(i-2,num),rob(i-1,num))
    # return max(rob(n-2,nums[:n-1]),rob(n-2,nums[1:n]))
    return max(rob(n-2,nums[:-1]),rob(n-2,nums[1:]))

    

def house_robber_ii_2(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0],nums[1])

    memo1 = {
        -1: 0,
        -2: 0
    }

    memo2 = {
        -1: 0,
        -2: 0
    }


    def rob(num,memo,i):
        if i in memo:
            return memo[i]


        memo[i] = max(num[i]+rob(num,memo,i-2),rob(num,memo,i-1))
        return memo[i]

    rob(nums[:-1],memo1,n-2)
    rob(nums[1:],memo2,n-2)
    return max(memo1[n-2],memo2[n-2])



def house_robber_ii_3(nums):
    n = len(nums)
    if n == 1:
            return nums[0]
    if n == 2:
        return max(nums[0],nums[1])


    tab1 = [0] * (n-1)
    tab1[0] = nums[0]
    tab1[1] = max(nums[0],nums[1])

    tab2 = [0] * (n-1)
    tab2[0] = nums[1]
    tab2[1] = max(nums[1],nums[2])


    for i in range(2,n-1):
        tab1[i] = max(nums[i]+tab1[i-2],tab1[i-1])

    for j in range(3,n):
        tab2[j-1] = max(nums[j]+tab2[j-3],tab2[j-2])


    return max(tab1[n-2],tab2[n-2])
    

def house_robber_ii_4(nums):
    n = len(nums)
    if n == 1:
            return nums[0]
    if n == 2:
        return max(nums[0],nums[1])


    prev1 = nums[0]
    curr1 = max(nums[0],nums[1])

    prev2 = nums[1]
    curr2 = max(nums[1],nums[2])

    # for i in range(2,n-1):
    #     curr1,prev1 = max(nums[i]+prev1,curr1),curr1

    # for j in range(3,n):
    #     curr2,prev2 = max(nums[j]+prev2,curr2),curr2

    for i in range(2,n):
        if i < n-1:
            curr1,prev1 = max(nums[i]+prev1,curr1),curr1
        if i > 2:
            curr2,prev2 = max(nums[i]+prev2,curr2),curr2

    return max(curr1,curr2)


nums1 = [2,3,2]
nums2 = [1,2,3,1]
nums3 = [1,2,3]
nums4 = [2,1,1,1]
nums5 = [4,9,7,1]
nums6 = [6,6,4,8,4,3,3,10]

print('with recurrsion')
print(house_robber_ii_1(nums1))
print(house_robber_ii_1(nums2))
print(house_robber_ii_1(nums3))
print(house_robber_ii_1(nums4))
print(house_robber_ii_1(nums5))
print(house_robber_ii_1(nums6))
print('with memoization')
print(house_robber_ii_2(nums1))
print(house_robber_ii_2(nums2))
print(house_robber_ii_2(nums3))
print(house_robber_ii_2(nums4))
print(house_robber_ii_2(nums5))
print(house_robber_ii_2(nums6))
print('with tabulation')
print(house_robber_ii_3(nums1))
print(house_robber_ii_3(nums2))
print(house_robber_ii_3(nums3))
print(house_robber_ii_3(nums4))
print(house_robber_ii_3(nums5))
print(house_robber_ii_3(nums6))
print('with bottom-up Constant Space')
print(house_robber_ii_4(nums1))
print(house_robber_ii_4(nums2))
print(house_robber_ii_4(nums3))
print(house_robber_ii_4(nums4))
print(house_robber_ii_4(nums5))
print(house_robber_ii_4(nums6))