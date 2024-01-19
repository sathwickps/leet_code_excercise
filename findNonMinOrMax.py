from ast import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mi=min(nums)
        ma=max(nums)
        c=0
        for i in set(nums):
            if i!=ma and i!=mi:
                return i
        return -1