"""
CBArray class implementation.
"""

# ------------------------------------- Please do NOT use extra import statements --------------------------------------
class CBArray:
    """
    Array that contains elements with only one data type.
    """

    def __init__(self, content, dtype=None):
        """
        Initialize an array with a list of values.
        :param content: List of all values to initialize this array with. All values in the list should be of the same
        data type, otherwise it should throw an exception. Values cannot be None.
        :param dtype: Data type of array. If this argument is None, datatype will be inferred from values in `content`
        list (default `dtype` should be `int` if `content` is empty); if not, all values will be casted to specified
        type. CBArray should support the following data types: int, float, and str.
        """
        if not all(type(x) in {float, int, str} for x in content):
            raise Exception('Unsupported data type')

        if content:
            if None in content:
                raise Exception('\'None\' exists in the given list')
            if dtype:
                if not all(isinstance(x, dtype) for x in content):
                    if dtype == float and all(isinstance(x, int) for x in content):
                        self.arr_type = float
                    else:
                        raise Exception('Values in the list are not equal to dtype')
                else:
                    self.arr_type = dtype
            else:
                if all(isinstance(x, type(content[0])) for x in content):
                    self.arr_type = type(content[0])
                elif all(isinstance(x, int) or isinstance(x, float) for x in content):
                    self.arr_type = float
                else:
                    raise Exception('Values in the list are not of same type')
            if type(content[0]) == str:
                self.min = 'zzzzz'
            else:
                self.min = float('inf')
        else:
            if dtype:
                self.arr_type = dtype
            else:
                self.arr_type = int
            self.min = float('inf')
        self.arr = content
        self.arr_dict = {}
        for num in self.arr:
            if num < self.min:
                self.min = num
            self.arr_dict[num] = self.arr_dict.setdefault(num, 0) + 1
        
#        pass  # TODO: implementation

    @property
    def dtype(self):
        """
        :return: Data type of elements in the array.
        """
        return self.arr_type
#        pass  # TODO: implementation

    @property
    def size(self):
        """
        :return: Size of this array.
        """
        return len(self.arr)
#        pass  # TODO: implementation

    def append(self, value):
        """
        Append a value to the end of the list.
        :param value: Value of new element.
        """
        if type(value) != self.arr_type:
            if not (isinstance(value, int) and self.arr_type == float): 
                raise Exception('input value is not of the same type.')
        if value == None:
            raise Exception('Can not insert a None value')
        self.arr.append(value)
        if value < self.min:
            self.min = value
        self.arr_dict[value] = self.arr_dict.setdefault(value, 0) + 1
#        pass  # TODO: implementation

    def insert(self, idx, value):
        """
        Insert value at idx.
        :param idx: Index to insert value at.
        :param value: Element to insert.
        """
        if idx < 0 or idx > len(self.arr):
            raise Exception('Can not insert value at this inded')
        if type(value) != self.arr_type:
            if not (isinstance(value, int) and self.arr_type == float): 
                raise Exception('input value is not of the same type.')
        self.arr.insert(idx, value)
        if value < self.min:
            self.min = value
        self.arr_dict[value] = self.arr_dict.setdefault(value, 0) + 1
            
#        pass  # TODO: implementation

    def remove(self, value):
        """
        Remove the first value in the array that is equal to `value`.
        :param value: Value to remove.
        """
        if type(value) != self.arr_type:
            if not (isinstance(value, int) and self.arr_type == float): 
                raise Exception('input value is not of the same type.')
        if value in self.arr:
            self.arr.remove(value)
        if value == self.min:
            if self.arr_dict[value] > 1:
                self.arr_dict[value] -= 1
            else:
                del self.arr_dict[value]
                if self.arr == []:
                    self.min = float('inf')
                else:
                    self.min = min(self.arr)
#        pass  # TODO: implementation
    def remove_all(self, value):
        """
        Remove all values in the array that is equal to `value`.
        :param value: Value to remove.
        """
        if type(value) != self.arr_type:
            if not (isinstance(value, int) and self.arr_type == float): 
                raise Exception('input value is not of the same type.')       
        self.arr = list(filter(lambda a: a != value, self.arr))
        if value == self.min:
            if self.arr:
                self.min = min(self.arr)
            else:
                self.min = float('inf')
        if value in self.arr_dict:   
            del self.arr_dict[value]
#        pass  # TODO: implementation

    # TODO: Implement appropriate methods so that CBArray also supports concatenation like Python list does:
    # arr1 = CBArray([1, 2, 3])
    # arr2 = CBArray([4, 5, 6])
    # arr3 = arr1 + arr2  # arr3 is CBArray([1, 2, 3, 4, 5, 6])
    # Note: Concatenating two CBArrays with dtype int and float should result in a CBArray with dtype float.
        
    def __add__(self, other):
        array_add = self.arr + other.arr
        if self.arr_type == other.arr_type:
            return CBArray(array_add, self.arr_type)
        else:
            if not self.arr:
                return CBArray(array_add, other.arr_type)
            if not other.arr:
                return CBArray(array_add, self.arr_type)
            if (self.arr_type== int and  other.arr_type == float) or (self.arr_type== float and  other.arr_type == int):
                array_add = list(map(float, array_add))
                return CBArray(array_add, float)
            return CBArray(self.arr + other.arr)
    # TODO: Implement appropriate methods so that CBArray also supports subscripting syntax like Python list does:
    # arr = CBArray([1, 2, 3])
    # arr[0]  # 1
    # arr[-1]  # 3
    # arr[-1:]  # CBArray([2, 3])
    # You do NOT need to support subscripting setters (i.e. arr[0] = 3)
    
    def __getitem__(self, key):
        sub_arr = self.arr[key]
        try:
            _ = len(sub_arr)
            return CBArray(sub_arr, self.arr_type)
        except:
            return self.arr[key]
    
    
#a = CBArray(['hi'])
#b = CBArray([1.5,2.5,3.5])
#c = CBArray([3.3])
#d = a + b + c