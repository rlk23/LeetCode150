'''
(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: mountainArr = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: mountainArr = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
 

Constraints:

3 <= mountainArr.length() <= 104
0 <= target <= 109
0 <= mountainArr.get(index) <= 109

'''
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def find_peak():
            low, high = 0, mountainArr.length()- 1

            while low < high:
                mid = (low+high) // 2
                if mountainArr.get(mid) < mountainArr.get(mid+1):
                    low  = mid + 1
                else:
                    high = mid 

            return low

        def binary_search(low,high, increasing=True):
            while low <= high:
                mid = (low+high) // 2
                mid_value = mountainArr.get(mid)

                if mid_value == target:
                    return mid
                
                if increasing:
                    if mid_value < target:
                        low = mid + 1
                    else:
                        high = mid - 1
                else:
                    if mid_value > target:
                        low = mid + 1
                    else:
                        high = mid -1
            return -1

        
        peak = find_peak()

        left_search = binary_search(0,peak, increasing=True)

        if left_search != -1:
            return left_search
        
        return binary_search(peak+1, mountainArr.length()-1, increasing=False)
                
