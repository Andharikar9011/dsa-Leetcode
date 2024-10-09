class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        m = nums[0]
        c = 0
        for i in nums:
            if d.get(i) == None :
                d[i] = 1
            else:
                d[i] +=1
                if d[i] > c:
                    c = d[i]
                    m = i
        return m
        