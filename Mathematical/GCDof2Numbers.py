# https://practice.geeksforgeeks.org/problems/gcd-of-two-numbers/0


# Example:
# Input:
# 98 56
# 48 18

# Output:
# 14
# 6

def gcd(a,b): 
	if(b==0): 
		return a 
	else: 
		return gcd(b,a%b) 

cases = int(input())
for i in range(cases):
    a,b = map(int,input().split())
    print(gcd(a,b))








