wagons = [0] * int(input())

while True:
    command = input().split()
    currant_command = command[0]

    if currant_command == 'End':
        print(wagons)
        break

    elif currant_command == 'add':
        number_of_people = int(command[1])
        wagons[-1] += number_of_people

    elif currant_command == 'insert':
        index = int(command[1])
        number_of_people = int(command[2])
        wagons[index] += number_of_people

    elif currant_command == 'leave':
        index = int(command[1])
        number_of_people = int(command[2])
        wagons[index] -= number_of_people
