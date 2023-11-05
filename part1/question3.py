class Oven:
    def __init__(self):
        self.ingredients = []
        self.temperature = None
        self.output = None

    def add(self, item):
        self.ingredients.append(item)

    def freeze(self):
        self.temperature = 0

    def boil(self):
        self.temperature = 100

    def wait(self):
        pass

    def get_output(self):
        if self.temperature == 0:
            if "water" in self.ingredients and "air" in self.ingredients:
                return "snow"
        elif self.temperature == 100:
            if "cheese" in self.ingredients and "dough" in self.ingredients and "tomato" in self.ingredients:
                return "pizza"
            elif "lead" in self.ingredients and "mercury" in self.ingredients:
                return "gold"
        return None

def make_oven():
    return Oven()

def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif temperature >= 100:
        oven.boil()
    else:
        oven.wait()

    return oven.get_output()
