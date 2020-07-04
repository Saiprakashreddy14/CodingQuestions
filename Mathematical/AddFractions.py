# https://practice.geeksforgeeks.org/problems/add-two-fractions/1

# For Input:
# 2
# 384 887 778 916
# 794 336 387 493
# Your Output is:
# 1041830/1803
# 521474/829

def gcd(a,b): 
	if(b==0): 
		return a 
	else: 
		return gcd(b,a%b) 


cases = int(input())
n1,d1,n2,d2 = map(int,input().split())
if(d1==d2):
    n,d=n1+n2,d1
else:
    n,d=n1*d2+n2*d1,d1*d2

a=gcd(n,d)

while(a!=1):
    # print(n,d,a) debug output
    n,d=n//a,d//a
    a=gcd(n,d)    
print("{}/{}".format(n,d))












