import re

numbers = input()

pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

valid_numbers = re.findall(pattern, numbers)

for i in range(len(valid_numbers)):
    if i < len(valid_numbers) - 1:
        print(valid_numbers[i], end=', ')
    else:
        print(valid_numbers[i])