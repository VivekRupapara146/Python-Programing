def temp_f(celcius):
    fahrenheit = (celcius * (9/5))+ 32
    return fahrenheit

def inch_to_cm(inch):
    return inch * 2.54

def multi_table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

c = float(input("Enter temperature in °C: "))

f = temp_f(c)

print(f"Temperature in fahreheit is {f:.2f}°F")

inch = float(input("Enter distance in inches: "))

cms = inch_to_cm(inch)

print(f"{inch:.2f} inch = {cms:.2f} cm")

n = int(input("Enter a number to obtain its multiplication table: "))

multi_table(n)