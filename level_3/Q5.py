class Time():
    
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def add_time(self, t1, t2):
        self.hours = t1.hours + t2.hours
        self.minutes = t1.minutes + t2.minutes
        if self.minutes >= 60:
            self.hours += 1
            self.minutes -= 60

    def display_time(self):
        print(f"{self.hours} hr and {self.minutes} min")
    
    def display_minutes(self):
        print(f"{self.hours*60 + self.minutes} minutes")