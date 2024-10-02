n = int(input())

POSITIVE = []
NEGATIVE = []

for _ in range(n):
    current_number = int(input())

    if current_number >= 0:
        POSITIVE.append(current_number)
    else:
        NEGATIVE.append(current_number)

count_of_positive_numbers = len(POSITIVE)
sum_of_negative_numbers = sum(NEGATIVE)

print(POSITIVE)
print(NEGATIVE)
print(f'Count of positives: {count_of_positive_numbers}')
print(f'Sum of negatives: {sum_of_negative_numbers}')

