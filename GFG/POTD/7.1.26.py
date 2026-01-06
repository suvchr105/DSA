# Count distinct elements in every window
# Medium

"""Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.

Examples:

Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output: [3, 4, 4, 3]
Explanation:
First window is [1, 2, 1, 3], count of distinct numbers is 3.
Second window is [2, 1, 3, 4] count of distinct numbers is 4.
Third window is [1, 3, 4, 2] count of distinct numbers is 4.
Fourth window is [3, 4, 2, 3] count of distinct numbers is 3.
Input: arr[] = [4, 1, 1], k = 2
Output: [2, 1]
Explanation:
First window is [4, 1], count of distinct numbers is 2.
Second window is [1, 1], count of distinct numbers is 1.
Input: arr[] = [1, 1, 1, 1, 1], k = 3
Output: [1, 1, 1]
Explanation: Every window of size 3 in the array [1, 1, 1, 1, 1], contains only the element 1, so the number of distinct elements in each window is 1.
Constraints:
1 ≤ k ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105

"""
# Code:

class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        freq = {}
        result = []
        
        # First window
        for i in range(k):
            freq[arr[i]] = freq.get(arr[i], 0) + 1
        
        result.append(len(freq))
        
        # Sliding the window
        for i in range(k, n):
            # Remove outgoing element
            out_elem = arr[i - k]
            freq[out_elem] -= 1
            if freq[out_elem] == 0:
                del freq[out_elem]
            
            # Add incoming element
            in_elem = arr[i]
            freq[in_elem] = freq.get(in_elem, 0) + 1
            
            result.append(len(freq))
        
        return result
