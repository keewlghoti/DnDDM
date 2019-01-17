"""
add edit methods for these elements. I want to call a method to edit the attributes.


"""



class Player(object):

    def __init__(self):
        self._playername = 'Unnamed Adventurer'
        self._playerdesc = 'This is a hero'
        self._playerhealth = 20
        self._playerattack = 3
        self._playermods = []
        self.dice = []

    def __repr__(self):
        return self.__dict__

    def setplayername(self, newname):
        self._playername = newname

    def setplayerdesc(self, newdesc):
        self._playerdesc = newdesc

    def setplayerhealth(self, newhealth):
        self._playerhealth = newhealth

    def setplayerattack(self, newattack):
        self._playerattack = newattack

    def setplayermods(self):
        self._playermods = []

class Enemy(object):

    def __init__(self):
        self._enemyname = 'Unnamed Enemy'
        self._enemydesc = 'This is a Enemy'
        self._enemyhealth = 20
        self._enemyattack = 3
        self._enemymods = []
        self.dice = []

    def __repr__(self):
        return self.__dict__

    def setenemyname(self, newname):
        self._enemyname = newname

    def setenemydesc(self, newdesc):
        self._enemydesc = newdesc

    def setenemyhealth(self, newhealth):
        self._enemyhealth = newhealth

    def setenemyattack(self, newattack):
        self._enemyattack = newattack

    def setenemymods(self, newmods):
        self._enemymods = []
