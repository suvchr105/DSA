# Max Sum Subarray of size K
# Easy
"""
Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.
Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.
Input: arr[] = [100, 200, 300, 400], k = 1
Output: 400
Explanation: arr3 = 400, which is maximum.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
1 ≤ k ≤ arr.size()
"""

# Code:

class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        n = len(arr)
        
        window_sum = sum(arr[:k])
        max_sum = window_sum
        
        for i in range(k,n):
            window_sum +=arr[i]
            window_sum -= arr[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum