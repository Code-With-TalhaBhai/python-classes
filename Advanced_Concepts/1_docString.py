

def quack(n:int):
    '''
    Print n time quack

    n(int) -> Takes integer arguement
    :param n: Number of times want to print quack
    :type n: int
    :raise TypeError: If n is not int
    :rtype: str
    '''

    for _ in range(n):
        print("quack")





quack(234)
# quack("234")