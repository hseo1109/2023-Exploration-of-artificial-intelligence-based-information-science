# week10_class_object04

class PrettyMixin:
    def dump(self):
        print(f"{self.hidden_name} pokemon")
        import pprint
        pprint.pprint(vars(self))


class Pokemon(PrettyMixin):
    pokemon_count=0

    def __init__(self, name, hp, level):
        self.hidden_name = name
        self.hp = hp
        self.level = level
        Pokemon.pokemon_count = Pokemon.pokemon_count+1
    @property
    def name(self):
        print("getter executed")
        return self.hidden_name
    @name.setter
    def name(self,input_name):
        print("setter executed")
        self.hidden_name=input_name

    def info(self):
        print("============")
        print(f"Name : {self.hidden_name}")
        print(f"Hp : {self.hp}")
        print(f"level : {self.level}")
        print("============")


if __name__ == "__main__":
    p1=Pokemon("pikachu",)
