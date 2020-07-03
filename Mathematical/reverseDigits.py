# https://practice.geeksforgeeks.org/problems/reverse-digit/0

# Input:
# 2
# 200
# 122
# Output:
# 2
# 221

cases = int(input())
for i in range(cases):
    a=int(input())
    print(int(str(a)[::-1]))