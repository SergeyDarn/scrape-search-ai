from typing import List

class ArrayUtils:
    @staticmethod
    def combine_arrays[T](array1: List[T], array2: List[T]):
        res = array1
        
        for item in array2:
            try:
                res.index(item)
            except:
                res.append(item)
                
        return res

    @staticmethod
    def filter_array[T](array_to_filter: List[T], values_to_exclude: List[T]):
        filtered_array = []
        
        for item in array_to_filter:
            try:
                values_to_exclude.index(item)
            except:
                filtered_array.append(item)
                
        return filtered_array
    