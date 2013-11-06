

class Squad():
    def __init__(self, squadID, ships):
        self.squadID = squadID
        self.ships = []
        for blah in range(ships):
            self.ships.append(blah)

    def getID(self):
        return self.squadID

    def addShip(self, shipID):
        self.ships.append(shipID)

    def getShips(self):
        return self.ships

    def killShip(self, shipID):
        newShips = []
        for ship in self.ships:
            if ship == ship.ID:
                pass
            else:
                newShips.append(ship)
        self.ships = newShips


class Fleet():
    def __init__(self, user):
        self.user = user
        self.squads = []
        self.squads.append(Squad("default", 0))

    def printSquadNames(self):
        for squad in self.squads:
            print squad.getID()

    def addSquad(self, squadName, ships):
        self.squads.append(Squad(squadName, ships))

    def getSquadNames(self):
        names = []
        for squad in self.squads:
            names.append(squad.getID())
        return names

    def getAllShips(self):
        returnShips = []
        for squad in self.squads:
            for ship in squad.getShips():
                returnShips.append(ship)
        return returnShips


if __name__ == '__main__':
    fleetList = {}
    fleetList["Dan"] = Fleet("Dan")
    fleetList["Brian"] = Fleet("Brian")

    print "Fleets are:"
    for name in fleetList.keys():
        print name
    print "\n"

    fleetList["Dan"].addSquad("test", 4)

    print "Dan's Squads are:"
    for name in fleetList["Dan"].getSquadNames():
        print name
