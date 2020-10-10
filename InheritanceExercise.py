class Furniture:
    def __init__(self):
        self._typeOfWood = 'Teakwood'


class Chair(Furniture):
    def __init__(self):
        super().__init__()
        self._numberOfLegs = 4

    def SetWoodType(self, typeOfWood):
        self._typeOfWood = typeOfWood

    def displayChairSpecification(self):
        print(f'This chair is made of {self._typeOfWood} and has {self._numberOfLegs} legs.')


chair = Chair()
print('Do you like to change the type of wood from Teakwood? [Y/N]: ')
userChoice = input().upper()

if userChoice == 'Y':
    print('Enter the type of wood you would like your chair to be made of:')
    typeOfWood = input()
    chair.SetWoodType(typeOfWood)
    chair.displayChairSpecification()
elif userChoice == 'N':
    chair.displayChairSpecification()
else:
    print('Please answer Y or N!')
    if userChoice != 'Y/N':
        print('Do you like to change the type of wood from Teakwood? [Y/N]: ')
        userChoice = input().upper()
    else:
        print('Sorry you are not follow the rules!')




    


