

class Dequeue:
    _container = []

    def push_front(self,data):
        self._container.insert(0,data)

    def push_back(self,data):
        self._container.append(data)

    def pop_front(self):
        self._container.pop(0)

    def pop_back(self):
        self._container.pop()

    def print_queue(self):
        print(self._container)



dequeue = Dequeue()
dequeue.push_back(4)
dequeue.push_back(5)
dequeue.push_back(6)
dequeue.push_back(7)
dequeue.pop_back()
dequeue.pop_back()
dequeue.push_front(3)

dequeue.print_queue()

