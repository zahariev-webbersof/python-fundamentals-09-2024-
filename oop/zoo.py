class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f'Mammals in {self.name}: {", ".join(self.mammals)}\n'
        elif species == 'fish':
            result += f'Fishes in {self.name}: {", ".join(self.fishes)}\n'
        elif species == 'bird':
            result += f'Birds in {self.name}: {", ".join(self.birds)}\n'

        result += f'Total animals: {Zoo.__animals}'

        return result


name_of_zoo = input()
zoo = Zoo(name_of_zoo)

number_of_lines = int(input())

for _ in range(number_of_lines):
    species, type_of_animal = input().split()
    zoo.add_animal(species, type_of_animal)

group_name = input()

print(zoo.get_info(group_name))
