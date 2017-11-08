class Team(object):
    def __init__(self, players):
        self.players = players

    def __add__(self, self2):       # with help of this function we are performing overloading operation
        return self.players + self2.players
    def __len__(self):
        return len(self.players)

     def __gt__(self, self2):
         if len(self.players) > len(self2.players)
             return True
         else:
             return False


    def __str__(self):
        return str(self.players)

india = Team(['Dhoni','Kohli','Raina','Jadeja'])
australlia = Team(['Lee','Smith','ponting','finch'])

#print india + australlia
print len(india)
print india
