class appointment():
    def __init__(self, name, date, time):
        self.name = name
        self.date = date
        self.time = time

    def getName(self):
        return self.name
    
    def change_name(self, name):
        self.name = name
    
    def getDate(self):
        return self.date

    def change_date(self, new_date):
        self.date = new_date

    def getTime(self):
        return self.time
    
    def change_time(self, new_time):
        self.time = new_time
