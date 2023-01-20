import json

class Event:
    def __init__(self, title, date, time_string, location, city, pictureUrl, tenant):
        self.eventId = title
        self.eventTitle = title
        self.eventDate = date
        self.eventTimeString = time_string
        self.eventLocation = location
        self.eventCity = city
        self.eventPictureUrl = pictureUrl
        self.city = tenant

    def pretty_print(self):
        print("Title: %s, Date: %s, Timestring: %s, Location: %s, City: %s" %(self.eventTitle, self.eventDate, self.eventTimeString, self.eventLocation, self.city))

    def toJSON(self):
            return json.dumps(self, default=lambda o: o.__dict__, 
                sort_keys=False, indent=4)