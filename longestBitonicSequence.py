
from typing import List


class Solution:
    def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
        
        LIS_left = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS_left[i] = max(LIS_left[i], 1 + LIS_left[j])

        LIS_right = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[j] < nums[i]:
                    LIS_right[i] = max(LIS_right[i], 1 + LIS_right[j])


        max_bitonic = 0
        for i in range(n):
            if LIS_left[i] > 1 and LIS_right[i] > 1:
                bitonic_len = LIS_left[i] + LIS_right[i] - 1
                max_bitonic = max(max_bitonic, bitonic_len)

        return max_bitonic
        
