class Array:
    def __init__(self, size): 
        self.size = size
        self.data = [None] * size
    def ___len__(self):
        return self.size
    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError('Index out of bounds') 
        return self.data[index]
    def __setitem__(self, index, value):
        if not 0 <= index < self.size:
            raise IndexError('Index out of bounds') 
        self.data[index] = value
    def __iter__(self):
        self.iter_index = 0 # Initialize the iteration index return self
        return self
    def __next__(self):
        if self.iter_index>= self.size:
            raise StopIteration
        value = self.data[self.iter_index] 
        self.iter_index += 1
        return value