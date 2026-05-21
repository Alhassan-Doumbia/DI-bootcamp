class Farm:

    def __init__(self,farm_name):
        self.name=farm_name
        self.animals={}

    def add_animal(self,**kwargs):

        for animal_name in kwargs:

            if(animal_name in self.animals):
                self.animals[animal_name]+=kwargs[animal_name]

            else:
                self.animals.update({animal_name:kwargs[animal_name]})

    def get_info(self):

        farm_info=f"{self.name}'s farm\n\n"

        for animal_name in self.animals:
            farm_info+=f"{animal_name} : {self.animals[animal_name]}\n"

        farm_info+="\n    E-I-E-I-0!"

        return farm_info

    def get_animal_types(self):

        animal_list=sorted(self.animals.keys())

        return animal_list

    def get_short_info(self):

        animal_list=[]

        for animal_name in self.get_animal_types():

            if(self.animals[animal_name]>1):
                animal_list.append(f"{animal_name}s")

            else:
                animal_list.append(animal_name)

        if(len(animal_list)>1):

            final_animals=", ".join(animal_list[:-1])
            final_animals+=f" and {animal_list[-1]}"

        else:
            final_animals=animal_list[0]

        return f"{self.name}'s farm has {final_animals}."


macdonald=Farm("McDonald")

macdonald.add_animal(cow=5,sheep=2,goat=12)

print(macdonald.get_info())

print(macdonald.get_animal_types())

print(macdonald.get_short_info())