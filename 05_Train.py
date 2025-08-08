# write a class Train with methods to book a ticket, get status(no of seats) and get fare information of trains

import random

class Train():
    
    def __init__(self, name, trainNo, fare, seats):
        self.name = name
        self.trainNo = trainNo
        self.fare = fare
        self.seats = seats
        # self.start = start
        # self.to = to
    
    def book_ticket(self):
        if self.seats>0:
            print(f"Your ticket is booked in train {self.name} with train no. {self.trainNo}")
            self.seats -=1
        else: print("Sorry, no seats available!")
        
    def get_status(self):
        print(f"Train: {self.trainNo}")
        print(f"No. of seats: {self.seats}")
    
    def get_fare_info(self):
        print(f"Ticket fare in {self.name}, train no.: {self.trainNo} is {self.fare}")
        
train1= Train("Rajdhani Express", "xyz012", 5000, 3)

while True:
    print("\nChoose an option:")
    print("1. Get Train Status")
    print("2. Get Fare Information")
    print("3. Book Ticket")
    print("4. Exit")
    
    choice = input("Enter choise: ")
    
    if choice == "1":
        train1.get_status()
    elif choice == "2":
        train1.get_fare_info()
    elif choice == "3":
        train1.book_ticket()
    elif choice == "4":
        break
    else: 
        print("\nEnter valid input")
        continue