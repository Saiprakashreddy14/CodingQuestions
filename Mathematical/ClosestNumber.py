# https://practice.geeksforgeeks.org/problems/closest-number/0

# Input:
# 2
# 13 4
# -15 6
# Output:
# 12
# -18


cases = int(input())

for i in range(cases):
    a,b=map(int,input().split())
    ans=0
    for i in range(a,a+abs(b)+1):
        if(i%b == 0):
            ans=i
            break
    for i in range(a,a-abs(b)-1,-1):
        if(i%b == 0):
            if(abs(a-i)<abs(a-ans)):
                ans=min(ans,i)
            if(abs(a-i)==abs(a-ans)):
                ans=i if (abs(ans)<abs(i)) else ans            
            break
    print(ans)
    