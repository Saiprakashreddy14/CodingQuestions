# https://practice.geeksforgeeks.org/problems/series-ap/0

# Input:
# 2
# 2 3
# 4
# 1 2
# 10

# Output:
# 5
# 10


cases = int(input())
for i in range(cases):
    a1,a2 = map(int,input().split())
    b=a2-a1
    n=int(input())
    print(a1+(n-1)*b)

