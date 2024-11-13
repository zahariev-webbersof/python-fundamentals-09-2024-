data = input().split()
new_text = [text * len(text) for text in data]
print(''.join(new_text))