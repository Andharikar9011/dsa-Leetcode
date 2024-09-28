class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums)-1
        val = None
        while s <= e:
            m = (s+e)//2
            if s>=e:
                if target > nums[m]:
                    val = m+1
                elif target <= nums[m]:
                    val = m
                break
            if target == nums[m]:
                val = m
                break
            if target > nums[m]:
                s = m+1
            elif target< nums[m]:
                e = m

        return val