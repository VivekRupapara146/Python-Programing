fruits = []

count = 1
while count <8:

   f =  str(input(f"Enter name of the fruit {count}: " ))
   fruits.append(f)
   print(f"Fruit {f} added to the list")
   count +=1 
   
print(fruits)