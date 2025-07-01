class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self._location = "unset"
    
    def getLocation(self):
        return self._location

    def setLocation(self, location):
        self._location = location