data = input().split('!')

while True:

    command = input()

    if command == 'Go Shopping!':
        break

    command_parts = command.split()
    action = command_parts[0]

    if action == 'Urgent':
        item = command_parts[1]
        if item not in data:
            data.insert(0, item)

    elif action == 'Unnecessary':
        item = command_parts[1]
        if item in data:
            data.remove(item)

    elif action == 'Correct':
        old_item = command_parts[1]
        new_item = command_parts[2]

        if old_item in data:
            index = data.index(old_item)
            data[index] = new_item

    elif action == 'Rearrange':
        item = command_parts[1]
        if item in data:
            data.remove(item)
            data.append(item)

print(', '.join(data))