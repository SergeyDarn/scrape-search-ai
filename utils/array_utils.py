from typing import List

class ArrayUtils:
    @staticmethod
    def combine_arrays[T](array1: List[T], array2: List[T]):
        return array1 + [
            item for item in array2 if (item not in array1)
        ]

    @staticmethod
    def filter_array[T](array_to_filter: List[T], values_to_exclude: List[T]):
        return [
            item for item in array_to_filter if (item not in values_to_exclude)
        ]
