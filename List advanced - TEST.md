
###### 1. What is the correct way to create a list from a set of numbers in Python?

- A: my_list = set(1, 2, 3)
- B: my_list = list({1, 2, 3})
- C: my_list = {1, 2, 3}
- D: my_list = (1, 2, 3)

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: my_list = list({1, 2, 3})

</p>
</details>

###### 2. What is the output of the following Python code that squares all even numbers in a list?

```python
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers if x % 2 == 0]
result = sum(squared)

```

- A: 20
- B: 30
- C: 10
- D: 15

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: 20

</p>
</details>

###### 3. Which list method is used to remove and return the last element from a list?

- A: my_list.remove()
- B: my_list.pop()
- C: my_list.extract()
- D: my_list.delete()

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: my_list.pop()

</p>
</details>

###### 4. What is the result of len([1, 2, 3] * 2)?

- A: 3
- B: 6
- C: Error
- D: 4

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: 6

</p>
</details>

###### 5. What is the output of the following code snippet?

```python
my_list = [1, 2, 3, 4]
my_list.extend([5, 6])
print(my_list)
```

- A: [1, 2, 3, 4, 5, 6]
- B: [1, 2, 3, 4, [5, 6]]
- C: [1, 2, 3, 4, (5, 6)]
- D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: [1, 2, 3, 4, 5, 6]

</p>
</details>

###### 6. How do you check if all elements in a list are unique using a built-in function?

- A: if len(my_list) == len(set(my_list)):
- B: if my_list.is_unique():
- C: if len(set(my_list)) == 1:
- D: if all(my_list):

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: if len(my_list) == len(set(my_list)):

</p>
</details>

###### 7. Which list comprehension would create a list of squares of numbers from 1 to 5?

- A: squares = [x^2 for x in range(1, 6)]
- B: squares = [x**2 for x in range(1, 6)]
- C: squares = [pow(x, 2) for x in 1..5]
- D: squares = [x*2 for x in range(1, 6)]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: squares = [x**2 for x in range(1, 6)]

</p>
</details>

###### 8. How do you reverse the elements of a list in Python?

- A: my_list.reverse()
- B: my_list = my_list[::-1]
- C: reversed(my_list)
- D: All of the above

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: All of the above

</p>
</details>

###### 9. How do you apply a function to all elements of a list and return a single result using the `reduce` function?

- A: result = reduce(lambda x, y: x * y, my_list)
- B: result = map(lambda x, y: x * y, my_list)
- C: result = sum(lambda x, y: x * y, my_list)
- D: result = filter(lambda x: x * x, my_list)

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: result = reduce(lambda x, y: x * y, my_list)

</p>
</details>

###### 10. What will be the output of the following list comprehension?

```python
result = [x + y for x in [10, 20] for y in [30, 40]]
```

- A: [10, 30, 20, 40]
- B: [40, 50, 50, 60]
- C: [40, 50, 50, 60, 70]
- D: [40, 50, 60]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: [40, 50, 50, 60]

</p>
</details>

###### 11. BONUS QUESTION -> What is the output of the following Python code using `set()` on a list?

```python
my_list = [1, 2, 2, 3, 3, 3, 4]
unique_items = set(my_list)
print(len(unique_items))
```

- A: 7
- B: 4
- C: 3
- D: 6

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: 4

</p>
</details>

###### 12. BONUS QUESTION -> What is the output of the following Python code?

```python
numbers = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))
```

- A: [1, 2, 3, 4, 5]
- B: [2, 4]
- C: [2, 3, 5]
- D: [1, 3, 5]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: [2, 4]

</p>
</details>

###### 13.  Additional QUESTION 

```python
numbers = [1, 2, 3, 4]
result = [x**2 for x in numbers if x % 2 == 0]
```

- A: [1, 4, 9, 16]
- B: [4, 16]
- C: [1, 9]
- D: []

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: [4, 16]

</p>
</details>

###### 14. Additional QUESTION 

```python
numbers = [2, 4, 6, 8, 10]
result = reduce(lambda x, y: x + y, numbers)
```

- A: 30
- B: 20
- C: 50
- D: 40

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: 30

</p>
</details>

###### 15. 😈 INSANE DIFFICULTY QUESTION 😈

```python
my_list = [1, 2, [3, 4, [5, 6, [7, 8]]]]
result = my_list[2][2][2][0]
my_list[2][2].append(9)
flattened = sum([i if isinstance(i, list) else [i] for i in my_list[2][2]], [])
final_result = flattened[-2]
print(result, final_result)
```

- A: 7 9
- B: 7 8
- C: 8 9
- D: 8 7

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: 7 8

</p>
</details>
