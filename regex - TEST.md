###### 1. Which of the following regex patterns will match the whole word "apple" in a string? 🍏

- A: `r'apple'`
- B: `r'\bapple\b'`
- C: `r'\bapple'`
- D: `r'apple\b'`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `r'\bapple\b'`

</p>
</details>

---

###### 2. What is the output of the following code? 📤

```python
import re
text = "I have an apple and an apple pie."
result = re.findall(r'\bapple\b', text)
print(result)
```

- A: `['apple', 'apple']`
- B: `['apple pie']`
- C: `['an apple']`
- D: `['apple', 'pie']`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `['apple', 'apple']`

</p>
</details>

---

###### 3. Which pattern will match words that start with "c" in the sentence "cats and dogs are cool"? 🐱🐶

- A: `r'\bc.*'`
- B: `r'c.*'`
- C: `r'\bc\w*'`
- D: `r'\b\w*c'`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `r'\bc\w*'`

</p>
</details>

---

###### 4. What is the output of the following code? 🤔

```python
import re
text = "The cat sat on the mat."
result = re.findall(r'\bat\b', text)
print(result)
```

- A: `['cat', 'mat']`
- B: `['at', 'cat']`
- C: `['at']`
- D: `[]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `['at']`

</p>
</details>

---

###### 5. Which regex pattern would match any whole word that ends with "ing" in a text? 🔍

- A: `r'ing\b'`
- B: `r'\bing\b'`
- C: `r'\bing\w*'`
- D: `r'\b\w*ing\b'`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: `r'\b\w*ing\b'`

</p>
</details>

---

###### 6. How would you use regex to check if the word "sun" appears as a whole word in a sentence? 🌞

```python
sentence = "The sun rises in the east."
```

- A: `re.search(r'sun', sentence)`
- B: `re.search(r'\bsun\b', sentence)`
- C: `re.search(r'\bsun', sentence)`
- D: `re.search(r'sun\b', sentence)`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `re.search(r'\bsun\b', sentence)`

</p>
</details>

---

###### 7. What would `re.findall(r'\b\w{3}\b', "The cat and dog ran")` return? 🐾

- A: `['cat', 'and', 'dog', 'ran']`
- B: `['cat', 'dog', 'ran']`
- C: `['The', 'cat', 'and', 'dog']`
- D: `[]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `['cat', 'and', 'dog', 'ran']`

</p>
</details>

---

###### 8. Which regex pattern will find words that contain exactly 4 letters in a sentence? 📝

- A: `r'\b\w{4}\b'`
- B: `r'\b\w{4}'`
- C: `r'\b\w{3,4}\b'`
- D: `r'\b\w{3}\b'`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `r'\b\w{4}\b'`

</p>
</details>

---

###### 9. Which pattern would match whole words in a sentence that start with "t"? ✨

- A: `r'\b\w*t'`
- B: `r't\w*'`
- C: `r'\bt\w*'`
- D: `r'\b.*t\b'`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `r'\bt\w*'`

</p>
</details>

---

###### 10. What would be the result of `re.findall(r'\b[a-zA-Z]{3}\b', "cat bat mat")`? 🔍

- A: `['cat']`
- B: `['cat', 'bat']`
- C: `['cat', 'bat', 'mat']`
- D: `[]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `['cat', 'bat', 'mat']`

</p>
</details>

---

###### 11. BONUS QUESTION 🎉 -> What will be the output of the following code?

```python
import re
text = "Running, jumping, and playing."
result = re.findall(r'\b\w*ing\b', text)
print(result)
```

- A: `['Running', 'jumping']`
- B: `['Running', 'jumping', 'playing']`
- C: `['running', 'jumping', 'playing']`
- D: `[]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `['Running', 'jumping', 'playing']`

</p>
</details>

---

###### 12. BONUS QUESTION 🎁 -> What would the following regex match in "The sun rises in the morning."?

```python
pattern = r'\b\w{3,}\b'
```

- A: Words with exactly 3 characters
- B: Words with 3 or more characters
- C: Words with 3 or fewer characters
- D: Words with 4 or more characters

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Words with 3 or more characters

</p>
</details>
