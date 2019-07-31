def merge_sort(array):
    if len(array) <= 1:
        return array
    # else if length > 1
    mid_index = len(array)/2
    leftside = array[:mid_index]
    rightside = array[mid_index:]
    
    # recursively calling merge_sort to split the array to half and finaly to array with only 1 element, then return the 1 ele array as sorted array
    left_sorted = merge_sort(leftside)
    right_sorted = merge_sort(rightside)
    
    result = []
    i = 0
    j = 0
    while(i < len(left_sorted) and j < len(right_sorted)):
        if left_sorted[i] < right_sorted[j]:
            result.append(left_sorted[i])
            i += 1
        else:
            result.append(right_sorted[j])
            j += 1
            
    # If left_sorted still have elements left, we add all the elements to the end of result[], same for right_sorted
    result.extend(left_sorted[i:])
    result.extend(right_sorted[j:])
    
    return result
    
print(merge_sort([2,1,4,14,7,5,4,3,24]))
        