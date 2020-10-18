class Item(object):
    def __init__(self, name="Blank Item"):
        self.name = name

class DiggingTool(Item):
    def __init__(self, name=None, durability=0, effectiveness=0):
        if name:
            self.name = name
        self.durability = durability
        self.effectiveness = effectiveness

    def new_random_tool(self):
        pass
