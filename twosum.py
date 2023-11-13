# implementing two sum problem here 
''' The enumerate function in Python is a built-in function 
that allows you to iterate over a sequence (such as a list, tuple, or string)
 while keeping track of the index and the corresponding element.
It returns pairs of index and element,
 making it convenient for situations 
 where you need both the value and its position in the sequence.
'''
#time complexity of this solution is O(n)
#The space complexity is also O(n), as in the worst case, 
# the stack can contain all elements of the array.


def two_sum(nums,target):
    dict1 = {}  # using dictionary here
    for i,num in enumerate(nums):
        other_num = target - num

        if other_num in dict1:
            return (dict[other_num],i)
        #retrieves the index of the complement (the other element in the pair),
        #  and i is the index of the current element.
        dict1[num] = i

    # No solution found
    return None



nums = [2, 7, 9, 15]
target = 9
result = two_sum(nums, target)
print(result)
