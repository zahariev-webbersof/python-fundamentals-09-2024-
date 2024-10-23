def urgent_func(data, item):
    if item not in data:
        data.insert(0, item)


def unnecessary_func(data, item):
    if item in data:
        data.remove(item)


def correct_func(data, old_item, new_item):
    for index, element in enumerate(data):
        if element in old_item:
            data[index] = new_item
            break

def rearrange_func(data, item):
    if item in data:
        data.remove(item)
        data.append(item)


def process_command(data, command):
    command_parts = command.split()
    action = command_parts[0]

    if action == 'Urgent':
        urgent_func(data, command_parts[1])
    elif action == 'Unnecessary':
        unnecessary_func(data, command_parts[1])
    elif action == 'Correct':
        correct_func(data, command_parts[1], command_parts[2])
    elif action == 'Rearrange':
        rearrange_func(data, command_parts[1])


def main():
    data = input().split('!')

    while True:
        command = input()

        if command == 'Go Shopping!':
            break

        process_command(data, command)

    print(', '.join(data))


main()