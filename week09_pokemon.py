class Pokemon:
    def __init__(self,name,level,hp):
        self.name = name
        self.level = level
        self.hp = hp
    pass
    def attack(self):
        print(f"{self,name} launches an area attack")
    def attack_target(self,target):
        print(f"{self,name} attacks {target}!")

class Pikachu(Pokemon): #is a relationship
    pass
class Squirtle(Pokemon):
    pass

if __name__ == "__main__":
    pikachu = Pikachu("pikachu",1,35)
    squirtle = Squirtle("squirtle",1,44)
    charizard = Pokemon("charizard",36,78)

    print(pikachu.hp)
    print(pikachu.level)
    print(pikachu.name)
    print(pikachu)

