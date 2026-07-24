class Pokemon:
    name:str
    abilities:list
    def __init__(self,name,abilities):
        self.name = name
        self.abilities = abilities

    def __str__(self):
        str_ability = ""
        for ability in self.abilities:
            str_ability += ability + ", "

        return f"name: {self.name}, Abilities: {str_ability}"