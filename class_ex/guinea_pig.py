"""
Expand on the class GuineaPig:
    1. Add following attributes: color, age, weight
    2. Add method jump and return true if the pig jumps. Pigs weighted above 2 lbs
        can't jump.
    3. Add appropriate dunder methods so that you can use comparision operators
    (<, >, =) with them.
    4. Can you retrofit the class so we can add 2 guinea pigs to make a super pig?
"""


class GuineaPig:
    def __init__(self, name, color, age, weight, fav_level):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.fav_level = fav_level
    
    def jump(self):
        if self.weight > 2:
            print("Too heavy, can't jump, sorry!")
            return False
        else:
            return True
    
    def __eq__(self, another_pig):
        return self.age == another_pig.age \
           and self.weight == another_pig.weight
    
    def __gt__(self, another_pig):
        if self.age > another_pig.age:
            return True
        elif self.age == another_pig.age:
            return self.weight > another_pig.weight

    def __ge__(self, another_pig):
        return self.__gt__(another_pig) or self.__eq__(another_pig)
    
    def __lt__(self, another_pig):
        if self.age < another_pig.age:
            return True
        elif self.age == another_pig.age:
            return self.weight < another_pig.weight

    def __le__(self, another_pig):
        return self.__lt__(another_pig) or self.__eq__(another_pig)


    def __add__(self, another_pig):
        new_name = "{} {}".format(self.name, another_pig.name)
        new_age = self.age + another_pig.age
        new_weight = self.weight + another_pig.weight
        new_color = "{}/{}" .format(self.color, another_pig.color)
        new_fav_level = (self.fav_level + another_pig.fav_level) // 2
        new_pig = GuineaPig(new_name, new_color, new_age, new_weight, new_fav_level)
        return new_pig