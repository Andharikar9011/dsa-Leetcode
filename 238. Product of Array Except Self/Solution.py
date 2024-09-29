class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pxl =[nums[0]]
        pxr =[nums[-1]]
        nums2 = []
        c = 1
        for i in range(1,len(nums)):
            pxl.append(pxl[i-1]*nums[i])
            pxr.append(pxr[i-1]*nums[len(nums)-i-1])
        for i in range(len(nums)):
            if i == 0:
                # nums2.append(pxr[len(nums)-i-1])
                nums[i]=pxr[len(nums)-i-2]
            elif i == len(nums)-1:
                # nums2.append(pxl[i-1])
                nums[i]=pxl[i-1]
            else:
                # nums2.append(pxl[i-1]*pxr[len(nums)-i-2])
                nums[i]=pxl[i-1]*pxr[len(nums)-i-2]
        return nums
