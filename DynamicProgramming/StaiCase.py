# https://practice.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair/0

# Input:
# 3
# 4
# 10
# 24
# Output:
# 5
# 89
# 75025


# Exlpanation
#     reach nth stairecase by
#         1 step  from n-1 stair
#         2 steps from n-2 stair

def Staircase(n):
    if(n==1):
        return 1
    if(n==2):
        return 2
    return Staircase(n-1)+Staircase(n-2)

cases=int(input())
for i in range(cases):
    a=int(input())
    print(Staircase(a))
