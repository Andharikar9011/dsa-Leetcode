class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        pt1 = 0
        pt2 = 0
        arrctr = 0
        while pt1 + pt2 <= m+(2*n):
            if pt2 >=n:
                break
            elif pt1 >= m+pt2 :
                nums1.append(nums2[pt2])
                pt1+=1
                pt2+=1
                arrctr+=1
            elif nums1[pt1] > nums2[pt2]:
                nums1.insert(pt1,nums2[pt2])
                pt1+=1
                pt2+=1
                arrctr +=1
            elif nums1[pt1] == nums2[pt2]:
                nums1.insert(pt1,nums2[pt2])
                pt1+=2
                pt2+=1
                arrctr+=2
            elif nums1[pt1] < nums2[pt2]:
                pt1+=1
                arrctr+=1 
        if len(nums1)%2 ==0 :
            a = int(len(nums1)/2)
            # print(nums1[a-1] + nums1[a])
            return (nums1[a-1] + nums1[a])/2
        else: 
            a = int(len(nums1)/2)
            # print(nums1[a])
            return nums1[a]