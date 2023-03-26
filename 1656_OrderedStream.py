class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.ptr = 0
        self.buffer = [None] * n

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        idKey -= 1
        self.buffer[idKey] = value
        if idKey != self.ptr:
            return []
        while self.ptr < self.n and self.buffer[self.ptr] is not None:
            self.ptr += 1
        return self.buffer[idKey:self.ptr]
