class AnimalBehaviour():
    def __init__(self,name,reproduction,incubationPeriod,diet ):
      
        self.name = name
        self._reproduction= reproduction
        self._diet = diet
        self.incubationPeriod = incubationPeriod

    def setAnimalData(self,name,reproduction,incubationPeriod,diet ):

        self.name = name
        name =input('Enter sound')
        self.reproduction= reproduction
        reproduction= input('Enter reproducttion')
        self.diet = diet
        diet=input('Enter diet')
        self.incubationPeriod = incubationPeriod
        incubationPeriod=input('Enter incubation period')
        

    def getAnimalData (self):
       print(self.name,self.reproduction,self.diet,self.incubationPeriod)
    
class carnivores(AnimalBehaviour):
    pass  
class omnivores(AnimalBehaviour):
    pass
class herbivores(AnimalBehaviour):
    pass
  

newHerbivor = herbivores('Lion', 'sexually','9 months', 'leaves')
herbivores.getAnimalData