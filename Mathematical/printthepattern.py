# https://practice.geeksforgeeks.org/problems/print-the-pattern-set-1/1

# Input
# 2
# 2
# 3
# Output
# 2 2 1 1 $2 1 $
# 3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1 $

noofcases=int(input())
for i in range(noofcases):
    n=int(input())
    ans=""
    num=[i for i in range(1,n+1)]

    for i in range(n,0,-1):
        ans+=' '.join(str(i) for i in sorted(num*i)[::-1])
        ans+=' $'
    print(ans)









