repeat_string = lambda string, n: string * n

input_string = input()
counter = int(input())
result = repeat_string(input_string, counter)

print(result)