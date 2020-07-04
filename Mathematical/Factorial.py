# https://practice.geeksforgeeks.org/problems/factorial/0

# Input:
# 2
# 1
# 4

# Output:
# 1
# 24

#code

def fac(n):
    if(n==0):
        return 1
    else:
        return n*fac(n-1)


cases = int(input())
for i in range(cases):
    n = int(input())
    print(fac(n))















