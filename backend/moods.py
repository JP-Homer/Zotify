#moods.py

class Mood:
    
    choices:int = 0

    def __init__(self, choice) -> None:
        self.choices = choice

    def choose(self):
        if self.choices == 0:
            Mood.happy()
        elif self.choices == 1:
            Mood.happy()
        elif self.choices == 2:
            Mood.sad()
        elif self.choices == 3:
            Mood.angry()
        elif self.choices == 4:
            Mood.chill()
        elif self.choices == 5:
            Mood.pumped()
        elif self.choices == 6:
            Mood.tired()
    
    def happy(self):
        pass

    def sad(self):
        pass

    def angry(self):
        pass

    def chill(self):
        pass

    def pumped(self):
        pass

    def tired(self):
        pass