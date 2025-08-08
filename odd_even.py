def is_even(n):
    if n % 2 == 0:
        print(f"{n} is even.")
    else:
        print(f"{n} is odd")

num = int(input("Enter a number to check for odd/even: "))
is_even(num)