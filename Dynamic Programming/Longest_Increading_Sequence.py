"""  
The longest Increasing Sequence problem is to find a sub-sequence 
of a given sequence in which the sub-sequence's elements are in sorted 
order (lowest to highest) and in which the sub-sequence is as long as
possible. 
Ex. [3,5,2,7,3,8]  -> (3,5,7,8)

    [1,1,1,1,1,1]

lis(2) > lis(1) 
    
"""
def lis(seq):
    #
    maximum = 1
    # number of elements in the sequence
    n = len(seq)
    # an unit list which counts the longest sequence
    arr = [1]*n
    
    for i in range(1,n):
        for j in range(0,i):
            if (seq[i] > seq[j]):
                arr[i]=max(arr[i], arr[j]+1)
    
    # displays the actual sequence
    sequence = []
    temp = arr[0]
    for i in range(0,n):
        if arr[i] >= temp:
            sequence.append(seq[i])
            temp = arr[i]
    print(sequence)
    
    # the max() instead of a loop for finding the max value     
    return max(maximum, max(arr)) 
    
    
    

seq = [3,5,2,7,3,8]
seq2 = [3, 10, 2, 1, 20]
print(lis(seq))
print("=====")
print(lis(seq2))