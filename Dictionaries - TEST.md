###### 1. Which method is used to retrieve the value associated with a specific key in a Python dictionary? 🔍

- A: `dict.get(key)`
- B: `dict.add(key)`
- C: `dict.value(key)`
- D: `dict.fetch(key)`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `dict.get(key)`

</p>
</details>

---

###### 2. What will be the output of the following code? 📤

```python
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
print(my_dict['banana'])
```

- A: `{'banana': 2}`
- B: `banana`
- C: `2`
- D: `3`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `2`

</p>
</details>

---

###### 3. Which method would you use to add a new key-value pair to an existing dictionary? ➕🔑

- A: `dict.append(key, value)`
- B: `dict.add(key, value)`
- C: `dict[key] = value`
- D: `dict.insert(key, value)`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `dict[key] = value`

</p>
</details>

---

###### 4. What is the output of the following code? 🤔

```python
my_dict = {'x': 10, 'y': 20, 'z': 30}
my_dict['y'] = 50
print(my_dict)
```

- A: `{'x': 10, 'y': 20, 'z': 30}`
- B: `{'x': 10, 'y': 50, 'z': 30}`
- C: `{'x': 10, 'y': 50}`
- D: `{'x': 10, 'z': 30}`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `{'x': 10, 'y': 50, 'z': 30}`

</p>
</details>

---

###### 5. Which of the following will delete a key-value pair from a dictionary in Python? ❌

```python
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
```

- A: `my_dict.remove('banana')`
- B: `del my_dict['banana']`
- C: `my_dict.pop('banana')`
- D: Both B and C

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: Both B and C

</p>
</details>

---

###### 6. How can you check if a specific key exists in a Python dictionary? 🔍✅

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
```

- A: `if my_dict.has('a')`
- B: `if 'a' exists in my_dict`
- C: `if 'a' in my_dict`
- D: `if my_dict.key('a')`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `if 'a' in my_dict`

</p>
</details>

---

###### 7. What is the result of `len(my_dict)` when `my_dict = {'one': 1, 'two': 2, 'three': 3}`? 📏

- A: `3`
- B: `6`
- C: `0`
- D: `2`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `3`

</p>
</details>

---

###### 8. What is the result of the following code? 💡

```python
my_dict = {'a': 1, 'b': 2}
value = my_dict.get('c', 3)
print(value)
```

- A: `1`
- B: `2`
- C: `None`
- D: `3`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: `3`

</p>
</details>

---

###### 9. Which of the following methods will remove all items from a dictionary? 🗑️

- A: `dict.delete()`
- B: `dict.clear()`
- C: `dict.remove()`
- D: `dict.empty()`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `dict.clear()`

</p>
</details>

---

###### 10. Which statement is true about dictionary keys? 🔑🔒

- A: Dictionary keys can be any data type.
- B: Dictionary keys must be strings.
- C: Dictionary keys must be immutable data types.
- D: Dictionary keys must be unique values.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: Dictionary keys must be immutable data types, and D: Dictionary keys must be unique values.

</p>
</details>

---

###### 11. BONUS QUESTION 🎉 -> What will be the output of this code?

```python
fruits = {'apple': 2, 'banana': 3, 'cherry': 5}
fruits.update({'banana': 4, 'grape': 6})
print(fruits)
```

- A: `{'apple': 2, 'banana': 4, 'cherry': 5, 'grape': 6}`
- B: `{'apple': 2, 'banana': 3, 'cherry': 5}`
- C: `{'apple': 2, 'banana': 3, 'grape': 6}`
- D: `{'apple': 2, 'banana': 4, 'cherry': 5}`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `{'apple': 2, 'banana': 4, 'cherry': 5, 'grape': 6}`

</p>
</details>

---

###### 12. BONUS QUESTION 🎁 -> What will be the output of this code?

```python
inventory = {'apples': 10, 'oranges': 5}
new_stock = {'bananas': 15}
inventory.update(new_stock)
inventory['apples'] += 5
print(inventory)
```

- A: `{'apples': 15, 'oranges': 5, 'bananas': 15}`
- B: `{'apples': 10, 'oranges': 5, 'bananas': 15}`
- C: `{'apples': 5, 'oranges': 5, 'bananas': 15}`
- D: `{'apples': 10, 'bananas': 15}`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `{'apples': 15, 'oranges': 5, 'bananas': 15}`

</p>
</details>
