# https://www.youtube.com/watch?v=gCin6Qz-eJQ

def two_sum(A, target):
    i=0
    j=len(A)-1
    
    while i <=j:
        if A[i]+A[j]==target:
            return i, j
        elif A[i]+A[j] < target:
            i+=1
        else: # A[i]+A[j] > target
            j-=1
    return -1
    
print(two_sum([2,1,5,-6,4,21], 9))