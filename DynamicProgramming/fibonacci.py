# https://practice.geeksforgeeks.org/problems/print-first-n-fibonacci-numbers/0

# Input:
# 2
# 7
# 5

# Output:
# 1 1 2 3 5 8 13
# 1 1 2 3 5

#code
def fibonacci(n):       
    f1 = 0
    f2 = 1
    if (n < 1): 
        return
    for _ in range(0, n): 
        print(f2, end = " ") 
        next = f1 + f2 
        f1 = f2 
        f2 = next
  
    

cases=int(input())
for i in range(cases):
    a=int(input())
    fibonacci(a)

