# https://practice.geeksforgeeks.org/problems/print-table/0

# Input:
# 1
# 9 

# Output:
# 9 18 27 36 45 54 63 72 81 90

#code
cases=int(input())
for i in range(cases):
    n=int(input())
    lis=[n*i for i in range(1,11)]
    for i in lis:
        print(i,end=" ")
    print()
