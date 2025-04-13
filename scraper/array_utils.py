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
    