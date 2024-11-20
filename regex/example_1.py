import re


text = "There are 3 dogs and 4 cats 5 example 6 example"

result = re.subn('\d', 'number', text)

print(result)
