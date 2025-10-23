class SummingList:
    """A list that automatically calculates the total of the elements"""

    def __init__(self):        # magic methods like __init__ are private
        self.items_list = [] # public field
        self.__total = 0     # private field

    def __inc_total(self,val): # private method
        self.__total += val


    def get_total(self):       # public method
        return self.total

    def append(self,val):    # public method
        self.item_list.append(val)
        __inc_total(self,val)  # calling private method

 