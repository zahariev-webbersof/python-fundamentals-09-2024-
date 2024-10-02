my_list = []

for _ in range(3):
    text = input()
    my_list.append(text)

my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)