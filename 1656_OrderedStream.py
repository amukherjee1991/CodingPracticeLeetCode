class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
         # Initialize the OrderedStream with an empty buffer of size n
        self.n = n
        self.ptr = 0
        self.buffer = [None] * n

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        # Subtract 1 from idKey to convert from 1-indexing to 0-indexing
        idKey -= 1
        # Insert the value into the buffer at the correct index
        self.buffer[idKey] = value
        # If the inserted idKey is not equal to the current pointer ptr,
        # then return an empty list since we don't have a contiguous chunk
        if idKey != self.ptr:
            return []
        # If the inserted idKey is equal to ptr, find the next contiguous
        # chunk of non-None values in the buffer
        while self.ptr < self.n and self.buffer[self.ptr] is not None:
            self.ptr += 1
        # Return the contiguous chunk from idKey up to ptr
        return self.buffer[idKey:self.ptr]
