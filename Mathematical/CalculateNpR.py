# https://practice.geeksforgeeks.org/problems/npr/0

# Input:
# 2
# 2 1
# 10 4
# Output:
# 2
# 5040

#code

def npr(n,r):
    ans=1
    for _ in range(r):
        ans*=n
        n-=1
    return ans   



cases = int(input())
for i in range(cases):
    n,r = map(int,(input().split()))
    print(npr(n,r))















