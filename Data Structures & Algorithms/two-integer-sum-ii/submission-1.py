class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        res = []*2
        while l<r:
            s = numbers[l]+numbers[r]
            if s > target:
                r-=1
            elif s < target:
                l+=1
            else:
                res.append(l+1)
                res.append(r+1)
                break
        return res
        
            
