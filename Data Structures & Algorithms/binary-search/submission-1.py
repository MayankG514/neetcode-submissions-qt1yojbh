class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        h=n-1
        l=0

        while l<=h:
            mid = l+((h-l)//2)

            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                h=mid-1
            else:
                return mid

        return -1