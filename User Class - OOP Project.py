class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self._location = "unset"
        self.skills = {}
    
    def getLocation(self):
        return self._location

    def setLocation(self, location: str):
        self._location = location
    
    def info(self):
        print(f"Username: {self.username}\nEmail: {self.email}\nLocation: {self._location}")
    
    def learn(self, skill):
        if skill not in self.skills:
            self.skills[skill] = 1
        else:
            self.skills[skill] += 1

    
    def showSkills(self):
        for key, val in sorted(self.skills.items()):
            print(f"{key}: {val}")