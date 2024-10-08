# number_list = input().split()
# absolute_values = []
#
# for str_num in number_list:
#     absolute_values.append(abs(float(str_num)))
#
# print(absolute_values)

numbers = input().split()
absolute_values = [abs(float(num)) for num in numbers]
print(absolute_values)

