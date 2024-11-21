def need_for_speed():
    n = int(input())

    cars = {}

    for _ in range(n):
        car_data = input().split('|')
        car, mileage, fuel = car_data[0], int(car_data[1]), int(car_data[2])
        cars[car] = {'mileage': mileage, 'fuel': fuel}

    while True:
        command = input()

        if command == 'Stop':
            break

        command_parts = command.split(' : ')
        action = command_parts[0]
        car = command_parts[1]

        if action == 'Drive':
            distance = int(command_parts[2])
            fuel = int(command_parts[3])

            if cars[car]['fuel'] < fuel:
                print("Not enough fuel to make that ride")
            else:
                cars[car]['mileage'] += distance
                cars[car]['fuel'] -= fuel
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

                if cars[car]['mileage'] >= 100000:
                    print(f"Time to sell the {car}!")
                    del cars[car]

        elif action == 'Refuel':
            fuel = int(command_parts[2])
            current_fuel = cars[car]['fuel']
            added_fuel = min(75 - current_fuel, fuel)
            cars[car]['fuel'] += added_fuel
            print(f"{car} refueled with {added_fuel} liters")

        elif action == 'Revert':
            kilometers = int(command_parts[2])
            if cars[car]['mileage'] - kilometers < 10000:
                cars[car]['mileage'] = 10000
            else:
                cars[car]['mileage'] -= kilometers
                print(f"{car} mileage decreased by {kilometers} kilometers")

    for car, data in cars.items():
        print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")


need_for_speed()
