class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking" 

    def run_speed(self):
        return (self.weight / self.age) * 10
    
    def fight(self, other):
        if isinstance(other, Dog): 
            other_dog_power = other.run_speed() * other.weight
            current_dog_power = self.run_speed() * self.weight 
            
            if other_dog_power > current_dog_power:
                print(f"{other.name} is the winner") 
            else:
                print(f"{self.name} is the winner")