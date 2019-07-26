class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.flattenVector = []
        self.nextIndex = 0
        for vector in v:
            self.flattenVector += vector

    def next(self) -> int:
        if self.flattenVector:
            n = self.flattenVector[self.nextIndex]
            self.nextIndex += 1
            return n
        return 0

    def hasNext(self) -> bool:
        if self.nextIndex < len(self.flattenVector) and self.flattenVector[self.nextIndex] is not None:
            return True
        return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
nested_vector = [[0]]
obj = Vector2D(nested_vector)
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())