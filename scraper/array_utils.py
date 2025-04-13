class ArrayUtils:
    # todo: add typing
    def combine_arrays(array1, array2):
        res = array1
        
        for item in array2:
            try:
                res.index(item)
            except:
                res.append(item)
                
        return res
    
    # todo: add typing
    def filter_array(array_to_filter, values_to_exclude):
        filtered_array = []
        
        for item in array_to_filter:
            try:
                values_to_exclude.index(item)
            except:
                filtered_array.append(item)
                
        return filtered_array
    