class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        val = False
        d = dict()
        for i in range(len(nums)):
            if d.get(nums[i]) != None:
                if abs(d[nums[i]] - i) <= k:
                    val = True
                else:
                    d[nums[i]] = i
            else:
                d[nums[i]] = i  
        return val