sequence_data = input().split()

moves = 0

while True:
    command = input()

    if command == 'end':
        break

    index1, index2 = map(int, command.split())
    moves += 1

    if index1 == index2 or not (0 <= index1 < len(sequence_data)) or not (0 <= index2 < len(sequence_data)):
        middle_index = len(sequence_data) // 2
        sequence_data.insert(middle_index, f'-{moves}a')
        sequence_data.insert(middle_index, f'-{moves}a')
        print('Invalid input! Adding additional elements to the board')
    else:
        if sequence_data[index1] == sequence_data[index2]:
            element = sequence_data[index1]
            print(f"Congrats! You have found matching elements - {element}!")
            sequence_data.pop(max(index1, index2))
            sequence_data.pop(min(index1, index2))
        else:
            print("Try again!")

    if len(sequence_data) == 0:
        print(f"You have won in {moves} turns!")
        break

if len(sequence_data) > 0:
    print('Sorry you lose :(')
    print(' '.join(sequence_data))