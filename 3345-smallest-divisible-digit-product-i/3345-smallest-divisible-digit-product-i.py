class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+11):
            product=1
            temp=i
            while(temp!=0):
                rem=temp%10
                product=product*rem
                temp=temp//10
            if(product%t==0):
                return i