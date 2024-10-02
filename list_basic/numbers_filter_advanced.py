n = int(input())
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'

all_numbers = [int(input()) for _ in range(n)]

filtered_numbers = []

command = input()

for num in all_numbers:
    filter_command = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_NEGATIVE and num < 0) or
        (command == COMMAND_POSITIVE and num >= 0)
    )

    if filter_command:
        filtered_numbers.append(num)

print(filtered_numbers)