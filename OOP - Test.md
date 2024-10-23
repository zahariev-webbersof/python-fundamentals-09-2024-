###### 1. What is the correct way to define a simple class `Person` in Python?

- A: `class Person: pass`
- B: `def Person: pass`
- C: `Person(): pass`
- D: `class Person(): def __init__(self): pass`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `class Person: pass`

</p>
</details>

---

###### 2. What is the output of the following Python code?

```python
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(10)
print(obj.value)
```

- A: 0
- B: 10
- C: None
- D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: 10

</p>
</details>

---

###### 3. What is the correct way to inherit from a base class in Python?

- A: `class Child extends Parent:`
- B: `class Child inherits Parent:`
- C: `class Child(Parent):`
- D: `class Child.Parent:`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `class Child(Parent):`

</p>
</details>

---

###### 4. What is the result of calling the method below?

```python
class A:
    def method(self):
        return "method in class A"

class B(A):
    def method(self):
        return "method in class B"

obj = B()
print(obj.method())
```

- A: method in class A
- B: method in class B
- C: Error
- D: None

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: method in class B

</p>
</details>

---

###### 5. Which of the following defines a class attribute in Python?

- A: `self.attribute = 5`
- B: `attribute = 5`
- C: `def __init__(self): self.attribute = 5`
- D: `cls.attribute = 5`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `attribute = 5`

</p>
</details>

---

###### 6. How do you call a parent class's method from a child class in Python?

- A: `Parent.method(self)`
- B: `super().method()`
- C: `Child.method(self)`
- D: `self.method()`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `super().method()`

</p>
</details>

---

###### 7. Which of the following correctly represents encapsulation in Python?

- A: Private methods and attributes are defined with a single leading underscore `_`
- B: Private methods and attributes are defined with double leading underscores `__`
- C: Methods and attributes defined with `self`
- D: All methods and attributes are public by default

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Private methods and attributes are defined with double leading underscores `__`

</p>
</details>

---

###### 8. Which of the following best represents polymorphism in Python?

- A: The ability to define a function with the same name in multiple classes
- B: Using inheritance to reuse code
- C: Encapsulating data in classes
- D: A class with only one method

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: The ability to define a function with the same name in multiple classes

</p>
</details>

---

###### 9. How do you create a static method in Python?

- A: By using the `@classmethod` decorator
- B: By using the `@staticmethod` decorator
- C: By using `def staticmethod(self)`
- D: Static methods are not supported in Python

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: By using the `@staticmethod` decorator

</p>
</details>

---

###### 10. What is the result of calling `obj.greet()` in the following code?

```python
class Base:
    def greet(self):
        return "Hello from Base"
    
class Derived(Base):
    pass

obj = Derived()
print(obj.greet())
```

- A: Hello from Base
- B: Hello from Derived
- C: Error
- D: None

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: Hello from Base

</p>
</details>

---

###### 11. BONUS QUESTION -> What is method overriding in Python?

- A: When a subclass provides a new implementation of a method defined in its parent class
- B: When a method is defined multiple times in the same class
- C: When multiple methods are combined into one method
- D: When a method calls another method within the same class

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: When a subclass provides a new implementation of a method defined in its parent class

</p>
</details>

---

###### 12. BONUS QUESTION -> What is the output of the following code?

```python
class Parent:
    def __init__(self):
        self.value = 10
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value += 5
        
obj = Child()
print(obj.value)
```

- A: 10
- B: 5
- C: 15
- D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: 15

</p>
</details>

---

###### 13. Additional QUESTION 

```python
class Animal:
    def sound(self):
        return "Some sound"
        
class Dog(Animal):
    def sound(self):
        return "Bark"
        
a = Animal()
d = Dog()
print(a.sound(), d.sound())
```

- A: Some sound Some sound
- B: Bark Bark
- C: Some sound Bark
- D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: Some sound Bark

</p>
</details>

---

###### 14. Additional QUESTION 

```python
class A:
    def f(self):
        return "A's f"
    
class B(A):
    def f(self):
        return "B's f"
    
class C(B):
    pass

c = C()
print(c.f())
```

- A: A's f
- B: B's f
- C: Error
- D: None

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: B's f

</p>
</details>

---

###### 15. 😈 INSANE DIFFICULTY QUESTION 😈

```python
class A:
    def __init__(self, x):
        self.x = x
        
    def method(self):
        return self.x ** 2
        
class B(A):
    def method(self):
        return super().method() + self.x
    
class C(B):
    def method(self):
        return self.x + 10

obj = C(5)
print(obj.method())
```

- A: 25
- B: 20
- C: 15
- D: 30

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: 15

</p>
</details>

---
