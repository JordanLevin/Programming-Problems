class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i1 = 0
        i2 = 0
        ret = []
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                ret.append(nums1[i1])
                i1+=1
                i2+=1
            elif nums1[i1] < nums2[i2]:
                i1+=1
            elif nums1[i1] > nums2[i2]:
                i2+=1
        return ret