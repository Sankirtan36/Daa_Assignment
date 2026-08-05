class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2 
        nums3.sort()
        left=0
        right=len(nums3)-1
        median=0
        if(len(nums3)%2!=0):
            median=nums3[(left+right)//2]
            
        else:
            mid=(left+right)//2
            median=(nums3[mid]+(nums3[mid+1]))/2
        return median