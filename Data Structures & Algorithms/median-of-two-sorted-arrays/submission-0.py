class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j = 0,0
        l1 = len(nums1)
        l2 = len(nums2)
        mergedArr = []

        while i<l1 and j<l2:
            if nums1[i]<=nums2[j]:
                mergedArr.append(nums1[i])
                i+=1
            elif nums1[i] > nums2[j]:
                mergedArr.append(nums2[j])
                j+=1
        if i<l1:
            while i<l1:
                mergedArr.append(nums1[i])
                i+=1
        elif j<l2:
            while j<l2:
                mergedArr.append(nums2[j])
                j+=1
        
        print(mergedArr)
        l = len(mergedArr)

        if l%2==0:
            m = (mergedArr[l//2] + mergedArr[(l//2)-1]) / 2
            return m
        else:
            return mergedArr[l//2]


