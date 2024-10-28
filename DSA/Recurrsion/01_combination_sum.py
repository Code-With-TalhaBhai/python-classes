

def combination_sum(candidates,target):
    combinations = []
    final = []

    def get_combinations(i,sum):
        if sum == target:
            final.append(combinations.copy())
            # return

        if sum >= target or i >= len(candidates):
            # print(combinations)
            return

        num = candidates[i]
        combinations.append(num)
        get_combinations(i,sum+num)

        combinations.pop()
        get_combinations(i+1,sum)


    get_combinations(0,0)
    return final





candidates = [2,3,6,7]
target = 7
print(combination_sum(candidates,target))