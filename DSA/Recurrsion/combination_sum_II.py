


def combination_sum_II(candidates,target):
    final = []
    combinations = []

    def find_combinations(i,sum):
        if sum == target:
            final.append(combinations.copy())

        if sum >= target or i >= len(candidates):
            return
        
        num = candidates[i]
        combinations.append(num)
        find_combinations(i+1,sum+num)

        while (i+1) < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1

        combinations.pop()
        find_combinations(i+1,sum)


    find_combinations(0,0)
    return final 



candidates = [10,1,2,7,6,1,5]
target = 8

print(combination_sum_II(sorted(candidates),target))