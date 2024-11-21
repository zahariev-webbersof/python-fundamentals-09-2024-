import re

n = int(input())

barcode_pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

for _ in range(n):
    barcode = input()
    matches = re.findall(barcode_pattern, barcode)

    if matches:
        core = matches[0]
        product_group = ''.join(filter(str.isdigit, core)) or '00'
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')