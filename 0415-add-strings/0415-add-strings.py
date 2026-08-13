class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        digits="0123456789"
        i=len(num1)-1
        j=len(num2)-1
        carry=0
        ans=""
        while(i>=0 or j>=0 or carry):
            x=0
            y=0
            if(i>=0):
                x=digits.index(num1[i])
            if(j>=0):
                y=digits.index(num2[j])
            total=x+y+carry
            ans=digits[total%10]+ans
            carry=total//10
            i-=1
            j-=1
        return ans