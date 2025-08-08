def list_sum(list):
    sum = 0
    for l in list:
        sum += l
    return sum

my_list = list(map(int, input("Enter the list of numbers to add(space seperated): ").split()))
sum = list_sum(my_list)

print(f"The sum of the numbers provided is {sum}")
