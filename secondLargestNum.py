#Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

#Note: The second largest element should not be equal to the largest element.

#Examples:

#Input: arr[] = [12, 35, 1, 10, 34, 1]
#Output: 34
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        if n < 2:
            return -1 
        firstLNum = secondLNum = float('-inf')
        for num in arr:
            if num > firstLNum:
                secondLNum = firstLNum
                firstLNum = num
            elif num > secondLNum and num != firstLNum:
                secondLNum = num
        if secondLNum == float('-inf'):
            return -1
        else:
            return secondLNum
arr = [12, 35, 1, 10, 34, 1]
obj = Solution()
print(obj.getSecondLargest(arr))