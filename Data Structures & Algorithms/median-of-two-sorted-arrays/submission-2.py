class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2 
        totalLen = len(A)+len(B)
        half = totalLen // 2

        if len(A) > len(B):
            A,B = B,A
        
        l, r = 0, len(A)-1

        while True:
            i = (l+r) //2 
            j = half - i - 2

            ALeft = A[i] if i>=0 else float("-infinity")
            ARight = A[i+1] if (i+1) < len(A) else float("infinity")
            BLeft = B[j] if j>=0 else float("-infinity")
            BRight = B[j+1] if (j+1) < len(B) else float("infinity")

            if ALeft<= BRight and BLeft<=ARight:
                if totalLen % 2:
                    return min(ARight,BRight)
                else:
                    return (min(ARight,BRight)+max(ALeft,BLeft)) / 2

            elif ALeft > BRight:
                r = i-1
            elif BLeft > ARight:
                l = i+1
        
