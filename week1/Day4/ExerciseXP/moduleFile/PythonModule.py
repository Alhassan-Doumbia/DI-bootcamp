class Dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def bark(self):
        print(f"{self.name} is barking")
    def run_speed(self):
        return self.weight/self.age*10
    

    def fight(self,other):
        if isinstance:
            other_dog_power=other.run_speed()*other.weight
            current_dog_power=self.run_speed()*other.weight
            
            if(other_dog_power>current_dog_power):
                print(f"{other_dog.name} is the winner")
            else:
                print(f"{self.name} is the winner")

dog1=Dog("Médor",2,14)
dog2=Dog("Brutus",4,10)
dog3=Dog("Goat",1,12)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
