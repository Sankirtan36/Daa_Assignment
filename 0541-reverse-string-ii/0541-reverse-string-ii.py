class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n=len(s)
        arr=[]
        for i in s:
            arr.append(i)
        for i in range(0,len(s),2*k):
            left=i
            right=i+k-1
            if(right>=n):
                right=n-1
            while(left<right):
                temp=arr[left]
                arr[left]=arr[right]
                arr[right]=temp
                left=left+1
                right=right-1
        ans=""
        for j in arr:
            ans+=j
        return ans