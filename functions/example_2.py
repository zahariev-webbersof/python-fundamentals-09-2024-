cars = [
    {'model': 'BMW', 'price': 100000},
    {'model': 'Audi', 'price': 50000},
    {'model': 'Ford', 'price': 40000},
]

sorted_cars = sorted(cars, key=lambda car: car['price'])

print(sorted_cars)