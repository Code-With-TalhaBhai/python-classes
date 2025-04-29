

def numTeams1a(ratings) -> int:
    n = len(ratings)
    cache = {}

    def count_teams(i,prev_rating,cnt,rating_type):
        if (i,prev_rating,cnt,rating_type) in cache:
            return cache[(i,prev_rating,cnt,rating_type)]

        if cnt == 3:
            return 1
        if i == n:
            return 0
        
        
        taken = 0
        if rating_type == '+' and ratings[i] > prev_rating or rating_type == '-' and ratings[i] < prev_rating:
            taken = count_teams(i+1,ratings[i],cnt+1,rating_type)
        skip = count_teams(i+1,prev_rating,cnt,rating_type)
        
        cache[(i,prev_rating,cnt,rating_type)] = taken + skip
        return cache[(i,prev_rating,cnt,rating_type)]
    return count_teams(0,float('-inf'),0,'+') + count_teams(0,float('inf'),0,'-')


def numTeams1b(ratings) -> int:
    n = len(ratings)

    def count_teams(i,cnt,inc):
        if cnt == 3:
            return 1
        
        if i == n:
            return 0
        
        total = 0
        for j in range(i+1,n):
            if inc and ratings[i] < ratings[j]:
                total += count_teams(j,cnt+1,inc)
            elif not inc and ratings[i] > ratings[j]:
                total += count_teams(j,cnt+1,inc)
        return total
    
    teams = 0
    for i in range(n):
        teams += count_teams(i,1,True)
        teams += count_teams(i,1,False)
    return teams



def numTeams2(ratings) -> int:
    n = len(ratings)

    total_teams = 0
    for i in range(1,n-1):
        left_smaller = 0
        right_larger = 0

        j = i - 1
        while j >= 0:
            if ratings[j] < ratings[i]:
                left_smaller += 1
            j -= 1

        j = i + 1
        while j < n:
            if ratings[j] > ratings[i]:
                right_larger += 1
            j += 1

        left_larger = i - left_smaller
        right_smaller = n - 1 - i - right_larger

        total_teams += left_smaller * right_larger
        total_teams += left_larger * right_smaller
    return total_teams


rating1 = [2,5,3,4,1]
rating2 = [2,1,3]
rating3 = [1,2,3,4]


print('Recurrsion')
print(numTeams1a(rating1))
print(numTeams1a(rating2))
print(numTeams1a(rating3))
print()
print(numTeams1b(rating1))
print(numTeams1b(rating2))
print(numTeams1b(rating3))  


print('Optimized Solution')
print(numTeams2(rating1))
print(numTeams2(rating2))
print(numTeams2(rating3))
