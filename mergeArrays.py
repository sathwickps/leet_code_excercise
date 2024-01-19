from ast import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ret = []
        while nums1 and nums2:
            if nums1[0][0] == nums2[0][0]:
                arr1 = nums1.pop(0)
                arr2 = nums2.pop(0)
                arr1[-1] += arr2[-1]
                ret.append(arr1)
            elif nums1[0][0] > nums2[0][0]:
                ret.append(nums2.pop(0))
            else:
                ret.append(nums1.pop(0))
        ret.extend(nums1)
        ret.extend(nums2)
        return ret