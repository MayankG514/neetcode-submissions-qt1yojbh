class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force 
        # loop on every element
        # start another loop to check for target-element
        # return ans if present

        # time -> O(n**2)
        # space -> O(1)

        hmap = {}

        for i,num in enumerate(nums):
            t = target-num
            if t not in hmap:
                hmap[nums[i]] = i
            else:
                return [hmap[t],i]
        
