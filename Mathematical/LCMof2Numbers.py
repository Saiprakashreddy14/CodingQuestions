# https://practice.geeksforgeeks.org/problems/lcm-of-two-numbers/0

# Example:
# Input:
# 2
# 5 10
# 14 8

# Output:
# 10 5
# 56 2

def gcd(a,b): 
	if(b==0): 
		return a 
	else: 
		return gcd(b,a%b) 

cases = int(input())
for i in range(cases):
    a,b = map(int,input().split())
    if b>a :
        a,b=b,a
    print(int((a*b)//gcd(a,b)),gcd(a,b))








