# 0 1 1 2 3 5 8 ...

n = int(input("Enter the number of elements you want of the Fibonacci series: "))

fib_list = [0,1,1]
x = 1

for i in range(4, n+1):
    x = x + fib_list[len(fib_list)-2]
    fib_list.append(x)

print(fib_list)