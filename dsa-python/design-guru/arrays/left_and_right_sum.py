'''
Given an input array of integers nums, find an integer array,
let's call it differenceArray, of the same length as an input integer array.

Each element of differenceArray, i.e., differenceArray[i],
should be calculated as follows: take the sum of all elements to the
left of index i in array nums (denoted as leftSum[i]),
and subtract it from the sum of all elements to the right of
index i in array nums (denoted as rightSum[i]), taking the
absolute value of the result. Formally:

differenceArray[i] = | leftSum[i] - rightSum[i] |

If there are no elements to the left/right of i,
the corresponding sum should be taken as 0.
'''

def findDifferenceArray_brute_force(nums):
    n = len(nums)
    differenceArray = [0] * n

    #brute force
    for i in range(len(nums)):
        rSum = 0
        lSum = 0
        for rIdx in range((i+1),len(nums)):
            rSum = rSum + nums[rIdx]
        for lIdx in range(0, i):
            lSum = lSum + nums[lIdx]

        differenceArray[i] = abs(lSum - rSum)

    return differenceArray

def findDifferenceArray_betterApproach(nums):
        n = len(nums)
        differenceArray = [0] * n
        leftArr = [0] * n
        rightArr = [0] * n
        leftSum = 0
        rightSum = 0

        #leftSum
        for i in range(len(nums)):
            leftSum = leftSum + nums[i]
            leftArr[i] = leftSum

        #rightSum
        for j in range(len(nums)-1,-1,-1):
            rightSum = rightSum + nums[j]
            rightArr[j] = rightSum

        #differenceArray
        for d in range(len(nums)):
            differenceArray[d] = abs(leftArr[d] - rightArr[d])

        return differenceArray

print(findDifferenceArray_brute_force([1,2,3,4]))  #[9, 6, 1, 6]
print(findDifferenceArray_brute_force([5,4,3,2,1])) #[10, 1, 6, 11, 14]
print(findDifferenceArray_brute_force([5, 5, 5, 5, 5])) #[20, 10, 0, 10, 20]


print('~'*20)
print(findDifferenceArray_betterApproach([1,2,3,4]))
print(findDifferenceArray_betterApproach([5,4,3,2,1]))
print(findDifferenceArray_betterApproach([5, 5, 5, 5, 5]))