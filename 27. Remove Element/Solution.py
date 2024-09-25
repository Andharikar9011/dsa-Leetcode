class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        f = len(nums)-1
        c =0
        while i <= f:
            if len(nums) == 1:
                if nums[i] == val:
                    c+=1
                i+=1
            elif (nums[i] == val) :
                if (nums[f] != val ) :
                    temp = nums[f]
                    nums[f] = nums[i]
                    nums[i] = temp
                    c+=1
                    i+=1
                    f-=1
                else:
                    f-=1
                    c+=1
            else:
                i+=1
        return len(nums) - c