
    # def burst(i):
    #     if i >= n:
    #         return 1

    #     if i == n - 1:
    #         mul = 1
    #         n1 = i - 1
    #         n2 = i + 1

    #         if n1 > -1:
    #             mul *= nums[i]
    #         if n2 < n:
    #             mul *= nums[i]

    #         return mul


    #     return nums[i] * max(burst(i+1),burst(i+2))


    # return burst(0)


# In Working Not Solved
def burst_ballons(nums):
    n = len(nums)
    nums = [1] + nums + [1]

    def burst(i,arr):
        if i == n-1:
            return 0
        maxi = float("-inf")

        for j in range(len(arr)):
            sub_arr = arr.copy()
            sub_arr.pop(j)

            cal = nums[i]

            # if i - 1 > -1:
            #     cal *= nums[i-1]
            # if i + 1 < n:
            #     cal *= nums[i+1]

            maxi = max(maxi,cal+burst(i+1,sub_arr))
            return maxi

    return burst(0,nums)



nums1 = [3,1,5,8]
nums2 = [1,5]

print(burst_ballons(nums1))
print(burst_ballons(nums2))