class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        temp=set()
        mod=0
        count=1
        
        # even number and number ending with 5 is not divisible by number ending '1'
        if K%2==0 or K%5==0: return -1
        
        while True:
            mod=(mod*10+1)%K
            if mod==0: return count
            if mod in temp: return -1

            temp.add(mod)
            count+=1
