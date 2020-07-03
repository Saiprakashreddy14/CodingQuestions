# https://practice.geeksforgeeks.org/problems/series-gp/0

# Example:
# Input:
# 2
# 2 3
# 1
# 1 2
# 2

# Output:
# 2
# 2

import math
cases = int(input())
for i in range(cases):
    a1,a2 = map(int,input().split())
    b= float(a2)/a1
    n=int(input())
    print(math.floor(a1*(b**(n-1))))

