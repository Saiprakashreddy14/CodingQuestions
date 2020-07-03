# https://practice.geeksforgeeks.org/problems/armstrong-numbers/0

# Input:
# 1
# 371
# Output:
# Yes

cases = int(input())
for i in range(cases):
    num=int(input())
    sum = 0  
    temp = num  
    
    while temp > 0:  
        digit = temp % 10  
        sum += digit ** 3  
        temp //= 10  
    
    if num == sum:  
        print("Yes")  
    else:  
        print("No")  
