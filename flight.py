class Flight:
    def __init__(self,capacity):
        self.capacity=capacity
        self.passanges=[]
        
    def add_passenge(self,name):
        if not self.open_seat():
            return False
        self.passanges.append(name)
        return True
        
    def open_seat(self):
        return self.capacity-len(self.passanges)
        
        
        
flight = Flight(3)
people =["rajinda","pun","poornima","adhisha"]
for person in people:
    success = flight.add_passenge(person)
    if success:
        print(f"Added {person} to the flight successsfully")
    else:
        print(f"No available seats for {person}")