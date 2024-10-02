n = int(input())
special_word = input()

strings = []

for _ in range(n):
    current_string = input()
    strings.append(current_string)

filtered_strings = []

for current_string in strings:
    if special_word in current_string:
        filtered_strings.append(current_string)

print(strings)
print(filtered_strings)