# week10_class_object04

class PrettyMixin:
    def dump(self):
        print(f"{self.hidden_name} pokemon")
        import pprint
        pprint.pprint(vars(self))


class Pokemon(PrettyMixin):
    def __init__(self, name, hp, level):
        self.hidden_name = name
        self.hp = hp
        self.level = level
    def get_name(self):
        print("getter executed")
        return self.hidden_name
    def set_name(self,input_name):
        self.hidden_name=input_name

    def info(self):
        print("============")
        print(f"Name : {self.hidden_name}")
        print(f"Hp : {self.hp}")
        print(f"level : {self.level}")
        print("============")



if __name__ == "__main__":
    p1 = Pokemon("pikachu", 35, 1)
    p2 = Pokemon("squirtle", 40, 1)
    p2.info()
    p1.dump()
    p2.dump()
    p2.level=2
    p2.set_name("wartortle")
    print(p2.get_name())