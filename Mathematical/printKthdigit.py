# https://practice.geeksforgeeks.org/problems/print-the-kth-digit/0

# Input:
# 2
# 3 3 1
# 5 2 2
# Output:
# 7
# 21


cases = int(input())
for i in range(cases):
    a,b,c=map(int,(input().split()))
    print(str(a**b)[-c])
