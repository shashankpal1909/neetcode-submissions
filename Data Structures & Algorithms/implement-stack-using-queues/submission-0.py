class MyStack:

    def __init__(self):
        self._queue = deque()
        self._top = None

    def push(self, x: int) -> None:
        self._queue.append(x)
        self._top = x

    def pop(self) -> int:
        size = len(self._queue)
        self._top = None

        for _ in range(size - 1):
            top = self._queue.popleft()
            self._top = top
            self._queue.append(top)
        
        res = self._queue.popleft()

        return res

    def top(self) -> int:
        return self._top or -1
        

    def empty(self) -> bool:
        return self._top is None


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()