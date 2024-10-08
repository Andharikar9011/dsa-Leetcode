class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pt1 = 0
        pt2 = 0
        arrctr = 0
        while pt1 + pt2 <= m+(2*n):
            if pt2 >=n:
                break
            elif pt1 >= m+pt2 :
                nums1[pt1] = nums2[pt2]
                pt1+=1
                pt2+=1
                arrctr+=1
            elif nums1[pt1] > nums2[pt2]:
                nums1.pop()
                nums1.insert(pt1,nums2[pt2])
                pt1+=1
                pt2+=1
                arrctr +=1
            elif nums1[pt1] == nums2[pt2]:
                nums1.pop()
                nums1.insert(pt1,nums2[pt2])
                pt1+=2
                pt2+=1
                arrctr+=2
            elif nums1[pt1] < nums2[pt2]:
                pt1+=1
                arrctr+=1