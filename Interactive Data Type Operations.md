### 🎓 Interactive Data Type Operations System

![rsz_python_task_representation](https://github.com/user-attachments/assets/2052bb82-ad94-4f3d-ab32-03135528d0db)

Welcome to your interactive Python project! In this exercise, you will create a dynamic script where the user gets to choose a data type and perform related operations. The goal is to reinforce your understanding of Python data types, including strings, numbers, booleans, lists, tuples, and dictionaries, by implementing different actions based on the user's input.

### 🌟 Project Overview

You will write a Python program that:
1. Prompts the user to select a data type from a list of choices.
2. Based on the user’s selection, performs specific operations related to that data type.
3. Provides meaningful output and handles edge cases (like dividing by zero or modifying an immutable type).

This project is designed to give you hands-on experience with fundamental Python concepts while making it fun and interactive! 💡

---

### 📋 Project Requirements

#### 1️⃣ User Interaction:
- Prompt the user with a **menu** to select from four options:
  1. **Strings**
  2. **Numbers**
  3. **Booleans**
  4. **Additional Data Types (List, Tuple, Dictionary)**
  
  Example:
  ```python
  Choose a data type to perform operations on:
  1. Strings
  2. Numbers
  3. Booleans
  4. Additional Data Types (List, Tuple, Dictionary)
  ```

#### 2️⃣ Operations Based on User Choice:

- **Strings**:
  - Declare a string variable (`sentence = "Learning Python is fun!"`).
  - **Extract a substring** (e.g., "Python") using string slicing and display it.
  - Convert the string to **uppercase** and print it.
  - **Replace** a word in the string (e.g., replace "fun" with "awesome") and print the result.

- **Numbers**:
  - Prompt the user to input **two numbers** (`num1` and `num2`).
  - Perform **basic arithmetic operations**: addition, subtraction, multiplication, and division.
  - Handle the case where the second number is **zero** to avoid division by zero errors.
  - Calculate the **power** of one number raised to another and print the result.

- **Booleans**:
  - Declare two boolean variables (`is_python_fun = True` and `is_sunny = False`).
  - Perform **logical operations** (AND, OR, NOT) on these variables and display the results.
  - Perform **comparison operations** (e.g., `10 > 5`, `5 == 5`) and print the outcomes.

- **Additional Data Types**:
  - **List**: Create a list with mixed data types (`[1, 2, 3, "Python", True]`).
    - Append an item to the list and print the updated list.
    - Access and print the **4th element** in the list.
  - **Tuple**: Create a tuple with a few items (e.g., fruits: `("apple", "banana", "cherry")`).
    - Print the **length of the tuple**.
    - Try to **modify** an element (and handle the resulting TypeError).
  - **Dictionary**: Create a dictionary with key-value pairs (e.g., `{"name": "Alice", "age": 25, "city": "New York"}`).
    - Access and print the value for the key **"age"**.
    - Add a new key-value pair (e.g., `"country": "USA"`) and print the updated dictionary.

---

### 🔧 Requirements Checklist

1. **User Choice Menu**: The script should display a menu with four choices for the user.
2. **Conditional Logic**: Based on the user’s choice, execute the correct block of code for that data type.
3. **String Operations**: Implement slicing, case conversion, and word replacement.
4. **Number Operations**: Perform arithmetic and handle division by zero.
5. **Boolean Operations**: Execute logical and comparison operations.
6. **Additional Data Types**: Demonstrate list manipulation, tuple immutability, and dictionary operations.
7. **Error Handling**: Ensure that potential errors (like modifying tuples or dividing by zero) are managed gracefully.
8. **User Inputs**: For the number operations, gather user input to perform dynamic calculations.
9. **Comments**: Write clear, descriptive comments that guide through the code’s logic.

---

### 🛠 Skills You'll Practice

- **String manipulation** 🧵
- **Basic arithmetic** and **number handling** ➕➖✖️➗
- **Boolean logic** 🤔 (AND, OR, NOT)
- **Working with lists, tuples, and dictionaries** 📋🗂️
- **Error handling** 🚫
- **User input & output** 🖥️

---

### 🎯 Project Goals

By the end of this project, you should be able to:
- Understand and manipulate core Python data types.
- Write clean, interactive Python code that performs multiple operations based on user input.
- Handle potential errors and edge cases in your code.
- Gain confidence working with strings, numbers, booleans, lists, tuples, and dictionaries!

---

### 🎉 Project Tips & Hints

- **Make it interactive**: Test the script multiple times by choosing different data types and inputs. This will give you insight into how each part of the script works.
- **Think about edge cases**: What happens if the user tries to divide by zero? What happens if they input invalid data?
- **Experiment**: Try different string operations, number manipulations, and even modify the list or dictionary with different values.
- **Stay curious!**: The more you try out and experiment with the data types, the better you will understand how they work in Python.

---

### 🔍 Additional Challenge

To make your project even more interesting, try adding:
- A **loop** to allow the user to select different data types in the same session.
- **Input validation** to ensure the user only selects a valid option from the menu.
- **More operations**: For example, adding string concatenation, modulus operation for numbers, or iterating over a dictionary.

---

### 💻 Example Interaction:
```python
# Prompt the user to choose a data type to perform operations on
print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

# Get the user's choice and store it in a variable
choice = input("Enter the number of your choice (1-4): ")

# If the user chooses Strings (choice == '1'):
if choice == '1':
    # Declare a string variable, e.g., sentence = "Learning Python is fun!"
    
    # Extract and print a substring, such as the word "Python" from the sentence.
    
    # Convert the entire sentence to uppercase and print it.
    
    # Replace a word in the sentence (e.g., replace "fun" with "awesome") and print the modified sentence.

# If the user chooses Numbers (choice == '2'):
elif choice == '2':
    # Prompt the user to input two numbers, e.g., num1 and num2.
    
    # Perform and print the results of addition, subtraction, multiplication, and division.
    
    # Handle division by zero (e.g., print an error message if num2 is zero).
    
    # Perform a power operation, raising num1 to the power of num2, and print the result.

# If the user chooses Booleans (choice == '3'):
elif choice == '3':
    # Declare two boolean variables, e.g., is_python_fun = True, is_sunny = False.
    
    # Perform and print the results of logical operations: AND, OR, NOT.
    
    # Perform and print the results of comparison operations (e.g., 10 > 5 and 5 == 5).

# If the user chooses Additional Data Types (choice == '4'):
elif choice == '4':
    # ### List Operations ###
    # Create a list with mixed data types (e.g., numbers, strings, booleans).
    
    # Append a new element to the list and print the updated list.
    
    # Access and print the 4th element in the list.
    
    # ### Tuple Operations ###
    # Create a tuple with some string elements (e.g., fruits).
    
    # Print the length of the tuple.
    
    # Try to modify one element in the tuple and handle the resulting TypeError.
    
    # ### Dictionary Operations ###
    # Create a dictionary with some key-value pairs (e.g., name, age, city).
    
    # Access and print the value for one of the keys (e.g., "age").
    
    # Add a new key-value pair to the dictionary and print the updated dictionary.

# If the user enters an invalid choice:
else:
    # Print an error message indicating an invalid selection.

```

Output:
```python
Choose a data type to perform operations on:
1. Strings
2. Numbers
3. Booleans
4. Additional Data Types (List, Tuple, Dictionary)
Enter the number of your choice (1-4): 2

You chose Numbers!
Enter the first number: 10
Enter the second number: 5
Addition: 15.0
Subtraction: 5.0
Multiplication: 50.0
Division: 2.0
10.0 raised to the power of 5.0 is: 100000.0
```

---

### 📝 What to Submit:
- Your **Python script** with all the comments and logic implemented.
- A **short reflection** (a few sentences) describing what you found challenging or interesting while working on this project.

---

Good luck! 🚀 Dive in, have fun with it, and remember, **practice makes perfect!** 👨‍💻👩‍💻

