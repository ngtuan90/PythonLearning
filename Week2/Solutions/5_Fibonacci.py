#find Fibonacci Sequence
#Author:Minh Nguyen
#date:10/15/2016
def print_fib(n):
    a, b = 0, 1
    if n == 0:
        print a
    elif n == 1:
        print a, b
    else:
        print 0, 1, 
        for i in range(2, n):
            c = a + b
            a, b = b, c
            print c,
n=int(raw_input('Enter n: '))
print 'the Fibonacci Sequence is:'
print_fib(n)
