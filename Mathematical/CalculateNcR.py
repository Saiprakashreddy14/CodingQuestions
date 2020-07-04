# https://practice.geeksforgeeks.org/problems/ncr/0


# Input:
# 2
# 3 2
# 4 2
# Output:
# 3
# 6

#code

def npr(n,r):
    ans=1
    for _ in range(r):
        ans*=n
        n-=1
    return ans 

def fac(n):
    if(n==0):
        return 1
    else:
        return n*fac(n-1)  



cases = int(input())
for i in range(cases):
    n,r = map(int,(input().split()))
    print(int(npr(n,r)/fac(r)%(1000000009)))















