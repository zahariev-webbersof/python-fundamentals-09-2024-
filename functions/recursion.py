def count_numbers(n):
    if n <= 10:
        print(n)
        count_numbers(n + 1)


count_numbers(1)