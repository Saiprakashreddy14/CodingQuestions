# https://practice.geeksforgeeks.org/problems/sum-of-digit-is-pallindrome-or-not/0

# Example:
# Input:
# 2
# 56
# 98
# Output:
# YES
# NO

cases = int(input())
for i in range(cases):
    a=int(input())
    su = 0 
    for i in str(a):
        su+=int(i)
    if(str(su)[::-1]==str(su)):
        print('YES')
    else:
        print("NO")