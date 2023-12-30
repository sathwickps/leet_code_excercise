class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        N = m + n

        while left <= right:
            A = (left + right) // 2
            B = ((N + 1) // 2) - A

            x1 = -float("inf") if A - 1 < 0 else nums1[A - 1]
            y1 = float("inf") if A == m else nums1[A]
            x2 = -float("inf") if B - 1 < 0 else nums2[B - 1]
            y2 = float("inf") if B == n else nums2[B]

            if x1 <= y2 and x2 <= y1:
                if N % 2 == 0:
                    return (max(x1, x2) + min(y1, y2)) / 2
                else:
                    return max(x1, x2)
            elif x1 > y2:
                right = A - 1
            else:
                left = A + 1