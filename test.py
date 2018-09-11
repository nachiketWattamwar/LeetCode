class Solution: 
   def numSquares(self,n): 
        
        nums= [n+1];
        nums[0]=0;
        for i in range(1,n+1,1):
            nums[i]=100;
            counter=1;
            for j in range(1,i+1,j=j+counter):
                nums[i]=Math.min(nums[i],nums[i-j]+1);
                counter+=2;
            
        
        return nums[n];
    


s= Solution()
print(s.numSquares(13))