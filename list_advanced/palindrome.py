words = input().split()
special_palindrome = input()

palindrome_list = [word for word in words if word == word[::-1]]

count_of_special_palindrome = palindrome_list.count(special_palindrome)

print(palindrome_list)
print(f'Found palindrome {count_of_special_palindrome} times')