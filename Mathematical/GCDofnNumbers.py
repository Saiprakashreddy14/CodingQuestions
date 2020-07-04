# https://practice.geeksforgeeks.org/problems/gcd-of-array/0

# Input:
# 1
# 2
# 5 10

# Output:
# 5

#code
def gcd(a,b): 
	if(b==0): 
		return a 
	else: 
		return gcd(b,a%b) 

cases = int(input())
for i in range(cases):
    length = int(input())
    lis = list(map(int,input().split()))
    if(length==1):
        igcd=lis[0]
    else:
        igcd = gcd(lis[0],lis[1])
        for i in lis[2:]:
            igcd=gcd(igcd,i)
    print(igcd)














