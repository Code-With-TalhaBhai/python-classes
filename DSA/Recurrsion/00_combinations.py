


def combinations(n,k):
    final = []
    output = []

    def find_combination(idx):
        if len(output) == k:
            final.append(output.copy())
            return
        
        if idx == n+1:
            return
        
        output.append(idx)
        find_combination(idx+1)
        output.pop()
        find_combination(idx+1)


    find_combination(1)
    return final


print(combinations(4,2))