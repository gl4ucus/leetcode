class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # A typical merge sort, but need in-place
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        
        i = 0
        while i < len(nums1):
            if len(nums2) == 0:
                break
            if nums1[i] < nums2[0]:
                i += 1
                continue
            else:
                nums1.insert(i, nums2.pop(0))
        
        if len(nums2) != 0:
            nums1.extend(nums2)
        
        return nums1