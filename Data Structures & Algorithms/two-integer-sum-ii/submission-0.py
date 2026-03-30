class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hlist ={}
        res =[0]*2
        n=len(numbers)
        for i in range(0,n):
            number_to_be_checked = target-numbers[i]
            if number_to_be_checked in hlist.keys():
                res[0]=hlist[number_to_be_checked]+1
                res[1]=i+1
                return res
            else:
                hlist[numbers[i]]=i
        