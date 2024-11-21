# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"([#|])([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"

test_str = input()

matches = re.findall(regex, test_str)

total_calories = 0
food_items = []

for match in matches:
    delimiter, item_name, expiration_date, calories = match
    calories = int(calories)
    total_calories += calories

    food_items.append(f'Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}')

days = total_calories // 2000

print(f'You have food to last you for: {days} days!')

for item in food_items:
    print(item)