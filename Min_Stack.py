class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        

    def push(self, x: int) -> None:
        self.nums.append(x)

    def pop(self) -> None:
        self.nums.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return min(self.nums)