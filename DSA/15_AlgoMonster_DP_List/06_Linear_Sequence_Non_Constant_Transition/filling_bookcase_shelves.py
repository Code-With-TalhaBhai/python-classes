

def minHeightShelves(books, shelfWidth: int):
    n = len(books)
    memo : dict[int,float] = {
        n : 0
    }
    def m_h_shelves(i):
        # if i == n:
        #     return 0
        if i in memo:
            return memo[i]
        
        # curr_width = books[i][0]
        # max_book_height = 0
        # min_shelf_height = float('inf')
        # j = i
        # while j < n and curr_width <= shelfWidth:
        #     max_book_height = max(max_book_height,books[j][1])
        #     j += 1
        #     min_shelf_height = min(min_shelf_height,max_book_height + m_h_shelves(j))
        #     if j < n:
        #         curr_width += books[j][0]
        # return min_shelf_height
    


        curr_width = 0
        max_book_height = 0
        min_shelf_height = float('inf')
        j = i
        while j < n and curr_width + books[j][0] <= shelfWidth:
            curr_width += books[j][0]
            max_book_height = max(max_book_height,books[j][1])
            j += 1
            min_shelf_height = min(min_shelf_height,max_book_height + m_h_shelves(j))
        memo[i] = min_shelf_height
        return memo[i]
        # return min_shelf_height
    return m_h_shelves(0)






books1 = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth1 = 4
books2 = [[1,3],[2,4],[3,2]]
shelfWidth2 = 6
print(minHeightShelves(books1,shelfWidth1))
print(minHeightShelves(books2,shelfWidth2))
