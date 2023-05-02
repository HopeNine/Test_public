#создаем класс Pat

class Pet:

    def __init__(self, animal="", name="", gender="", age<=0):
        self.animal = animal
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, cats_dict):
        self.animal = cats_dict.get("animal")
        self.name = cats_dict.get("name")
        self.gender = cats_dict.get("gender")
        self.age = cats_dict.get("age")

#создаем класс Cat

class Cat:

    def __init__(self, name="", gender="", age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, cats_dict):
        self.name = cats_dict.get("name")
        self.gender = cats_dict.get("gender")
        self.age = cats_dict.get("age")
