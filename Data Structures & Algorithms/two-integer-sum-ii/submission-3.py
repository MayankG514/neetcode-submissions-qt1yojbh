class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        n = len(numbers)
        l,r = 0, n-1

        while l<=r:
            t = numbers[l]+numbers[r]

            if t<target:
                l+=1
            elif t>target:
                r-=1
            else:
                res.append(l+1)
                res.append(r+1)
                return res
        return []