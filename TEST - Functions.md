###### 1. What is the purpose of a Python function?

- A: To store variables
- B: To repeat code multiple times
- C: To organize code into reusable blocks
- D: To perform mathematical calculations

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer ->  C: To organize code into reusable blocks

</p>
</details>

---

###### 2. What does this Python code snippet calculate?

```python
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

print(calculate_average([1, 2, 3, 4, 5]))

```

- A: None
- B: 15
- C: 7.5
- D: 3.0

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: 3.0

</p>
</details>

---

###### 3. What is the purpose of parameters in a function definition?

- A: To specify the return value of the function
- B: To provide input data to the function
- C: To define local variables within the function
- D: To control the execution flow of the function

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: To provide input data to the function

</p>
</details>

---

###### 4. What happens if a function is called with fewer arguments than specified in its definition?

- A: Python automatically generates additional arguments
- B: Python raises a runtime error
- C: The missing arguments are set to None
- D: The function executes with default values for the missing arguments

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Python raises a TypeError 

</p>
</details>

---

###### 5. What will be result of this code?

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

```

- A: 25
- B: 5
- C: 130
- D: 120

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: 120

</p>
</details>

---

###### 6. What is a recursive function?

- A: A function that calls itself
- B: A function that returns a boolean value
- C: A function that executes in reverse order
- D: A function that iterates over a sequence

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: A function that calls itself

</p>
</details>

---

###### 7. How do you call a function in Python?

- A: By using the call keyword followed by the function name
- B: By using the execute keyword followed by the function name
- C: By using the function name followed by parentheses and any required arguments
- D: By using the run keyword followed by the function name

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: By using the function name followed by parentheses and any required arguments

</p>
</details>

---

###### 8. What is the purpose of the return statement in a function?

- A: To terminate the function execution
- B: To print output to the console
- C: To specify the function's input parameters
- D: To return a value from the function

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: To return a value from the function

</p>
</details>

---

###### 9. What is the difference between a function definition and a function call?

- A: A function definition defines the behavior of a function, while a function call executes that behavior.
- B: A function definition executes the behavior of a function, while a function call defines that behavior.
- C: There is no difference; both terms refer to the same action.
- D: A function definition defines input parameters, while a function call provides actual arguments.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: A function definition defines the behavior of a function, while a function call executes that behavior.

</p>
</details>

---

###### 10. Which of the following is **not** a valid way to define a Python function?

- A: `def my_function(): pass`
- B: `def my_function(arg1, arg2=10): pass`
- C: `def my_function(*args, **kwargs): pass`
- D: `def my_function(arg1=10, arg2): pass`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: `def my_function(arg1=10, arg2): pass`  
Functions cannot have a default parameter before a non-default parameter.

</p>
</details>

---

###### 11. What is the main difference between a positional argument and a keyword argument in a function call?

- A: Positional arguments are passed based on the position, while keyword arguments are passed with explicit parameter names.
- B: Positional arguments must always be strings, while keyword arguments can be any type.
- C: Positional arguments are passed last, while keyword arguments are passed first.
- D: There is no difference between the two.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: Positional arguments are passed based on the position, while keyword arguments are passed with explicit parameter names.

</p>
</details>

---

###### 12. What does the following Python code do?

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"
    
print(greet("Alice"))
```

- A: Throws a TypeError because 'message' is missing
- B: Prints `Hello, Alice!`
- C: Prints `, Alice!`
- D: Returns `None`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Prints `Hello, Alice!`

</p>
</details>

---

###### 13. BONUS QUESTION -> What is the output of the following Python code that calculates the base 10 logarithm of 100?

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(5)
print(result)

```

- A: 3
- B: 6
- C: 5
- D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 
</p>
</details>

---

###### 14. BONUS QUESTION -> What is the output of the following Python code?

```python
def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(even_or_odd(2) == even_or_odd(3))

```

- A: True
- B: False
- C: Error
- D: None

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

---

###### 15. 😈 DEVIL QUESTION 😈

```python
def func():
    return [lambda x: x * i for i in range(5)]

results = [m(2) for m in func()]
print(results)


```

- A: [8, 8, 8, 8, 8]
- B: [0, 1, 4, 9, 16]
- C: [8, 10, 12, 14, 16]
- D: [0, 2, 4, 6, 8]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

---

###### 16. 😈 DEVIL QUESTION 😈

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling function")
        result = func(*args, **kwargs)
        print("After calling function")
        return result
    return wrapper

@my_decorator
def my_function(x):
    return x * 2

result = my_function(5)
print(result)
```

- A: Before calling function After calling function 10
- B: Before calling function 10 After calling function
- C: 10 Before calling function After calling function
- D: Before calling function 10

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

---

###### 17. 😈 DEVIL QUESTION - What does the `*args` syntax in a function definition allow you to do 😈 

- A: Pass a list of arguments
- B: Pass a dictionary of arguments
- C: Pass a variable number of arguments
- D: Return multiple values

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: Pass a variable number of arguments. Please explain why? 

</p>
</details>

---

###### 18. 😈 DEVIL QUESTION - What will be the output of the following code? 😈

```python
def outer_function():
    x = 5
    def inner_function():
        nonlocal x
        x = 10
    inner_function()
    return x

print(outer_function())
```

- A: 5
- B: 10
- C: None
- D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: 10 but you will explain why!

</p>
</details>
