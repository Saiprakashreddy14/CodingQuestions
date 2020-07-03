# https://practice.geeksforgeeks.org/problems/jumping-numbers/0

# Input:
# 2
# 10
# 50
# Output:
# 0 1 2 3 4 5 6 7 8 9 10
# 0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45


# TODO

    # timecomplexity - k*n   (k max 9 -> 9* 10e9)


def isJumping(j):
    if(j<11):
        return True
    st = str(j)
    for i in range(len(st)-1):
        if(abs(int(st[i])-int(st[i+1])))!=1:
            return False
    return True
    
cases = int(input())
for i in range(cases):
    n=int(input())
    for i in range(1,n+1):
        if(isJumping(i)):
            print(i,end=" ")
            




