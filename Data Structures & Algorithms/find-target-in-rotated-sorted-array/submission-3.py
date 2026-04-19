class Solution:
    def binarySearch(self, nums: List[int], s: int, e:int, target: int) -> int:
        while s<=e:
            m = s+((e-s)//2)

            if target==nums[m]:
                return m
            
            if target < nums[m]:
                e = m-1
            else:
                s = m+1
        
        return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0, n-1

        while l<r:
            m = l + ((r-l)//2)
            
            if nums[m]<=nums[r]:
                r = m
            else:
                l = m+1
        
        pivot = l

        if target >= nums[pivot] and target<=nums[n-1]:
            return self.binarySearch(nums,pivot,n-1,target)

        else:
            return self.binarySearch(nums,0,pivot-1,target)

        
        
