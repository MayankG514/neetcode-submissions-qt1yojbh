class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0, n-1

        while l<r:
            m = l + ((r-l)//2)

            if nums[m] > nums[r]:
                l = m+1
            elif nums[m] < nums[r]:
                r = m-1
        pivot = l

        def bin_search(low:int,high:int):
            while low<=high:
                m = low + ((high-low)//2)
                if nums[m] > target:
                    high = m-1
                elif nums[m] < target:
                    low = m+1
                else:
                    return m
            return -1
        
        a = bin_search(0,pivot)
        if a != -1:
            return a
        
        return bin_search(pivot,n-1)

                