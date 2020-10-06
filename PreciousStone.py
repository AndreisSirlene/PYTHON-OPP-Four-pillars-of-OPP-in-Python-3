class PreciousStone:
    numberOfPreciousStone = 0
    preciousStoneCollection = []

    def __init__ (self, name):
        self.name = name
        PreciousStone.numberOfPreciousStone +=1
        if PreciousStone.numberOfPreciousStone <= 5:
            PreciousStone.preciousStoneCollection.append(self)
        else:
            del PreciousStone.preciousStoneCollection[0]
            PreciousStone.preciousStoneCollection.append(self)
            
    @staticmethod
    def displayPreciousStones():
        for preciousStone in PreciousStone.preciousStoneCollection:
            print(preciousStone.name ,end=', ')
        print()

preciousStoneOne = PreciousStone('Ruby')
preciousStoneTwo = PreciousStone('Diamond')
preciousStoneThree = PreciousStone('Emerald')
preciousStoneFour = PreciousStone('Sapphire')
preciousStoneFive = PreciousStone('Amber')
preciousStoneFive.displayPreciousStones()
preciousStoneSix = PreciousStone('Onix')
preciousStoneSix.displayPreciousStones()



    


