# In Python, an iterator is an object that implements the iterator protocol,
# which consists of two methods: __iter__() and __next__().


class MyIterator:
    def __init__(self, max_val):
        self.max_val = max_val
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_val:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration

# Using the iterator
iterator = MyIterator(5)
for i in iterator:
    print(i)
