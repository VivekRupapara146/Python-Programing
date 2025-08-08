class Temperature:
    def __init__(self, celsius):
        self._celsius = None
        self.celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value<-273.15:
            raise ValueError("Temperature below Absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return ((self.celsius * (9/5)) + 32)

temp = Temperature(25)
print(f"Celsius : {temp.celsius}")
print(f"Fahrenheit : {temp.fahrenheit}")

temp.celsius = int(input("Enter tempetature in Celsius: "))
print(f"Celsius : {temp.celsius}")
print(f"Fahrenheit : {temp.fahrenheit}")