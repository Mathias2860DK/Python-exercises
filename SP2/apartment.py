class Apartment:
    def __init__(self, type, price, square_meter, street, room, link):
        self.type = type
        self.price = price
        self.square_meter = square_meter
        self.street = street
        self.room = room
        self.link = link

    def __str__(self):
        return 'type ' + self.type + ", price " + str(self.price) + ", square_meter " + str(self.square_meter) + ", street " + self.street + ", room " + str(self.room) + ", link " + self.link
        
    def is_cheap(self):
        return self.price < 4000
