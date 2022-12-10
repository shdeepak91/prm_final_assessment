#Find nth fibonacci number. If it starts with 0,1,1,2.....

#Also, Print Incorrect Input if n is less than or equal to 0

def fib(n):
    if n <= 0:
        print("incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = 4
print(fib(n))
