# 🚀 Learn JavaScript as a Python Developer?
![1705906038412](https://github.com/user-attachments/assets/893e0641-5a41-4035-958e-4170ae770da6)

Welcome, SoftUni Students! 🐍 You’ve been learning Python, building awesome projects like Interactive Data Type Operations System, Bank Account Management System, and more. Now, it's time to expand your skill set by learning JavaScript (JS), one of the most popular programming languages for web development. Here’s why you should learn JavaScript at a base level:

### 🎯 Purpose of Learning JavaScript

JavaScript allows you to create dynamic and interactive content in web browsers. It is **the language of the web**, meaning if you want to work on front-end projects (things users interact with on websites), JavaScript is essential.

By learning JavaScript, you’ll be able to:
- Build **full-stack applications** (combining Python in the backend with JS in the frontend).
- Understand how **web development** works.
- Expand your **job opportunities** as both Python and JavaScript are highly in-demand.
- Learn **new concepts** that will help you grow as a developer.

### 🧠 Differences and Similarities Between Python and JavaScript

| **Feature**               | **Python**                            | **JavaScript**                          |
|---------------------------|---------------------------------------|-----------------------------------------|
| **Typing**                | Dynamically typed                     | Dynamically typed                       |
| **Variable declaration**  | No declaration keyword (just assign)  | `let`, `const`, `var`                  |
| **String formatting**     | `f"Hello, {name}"`                   | `` `Hello, ${name}` ``                  |
| **Loops**                 | `for item in list`                   | `for (let i = 0; i < array.length; i++)`|
| **Functions**             | `def greet(name):`                   | `function greet(name) {}`              |
| **Indentation**           | Required for block definitions        | Curly braces `{}` used for blocks      |
| **Web Usage**             | Mostly for backend and scripting      | Frontend for web pages (and backend using Node.js) |

#### 👩‍💻 Similarities:
- Both languages are **dynamically typed**: You don’t need to declare the type of a variable.
- **Loops** and **functions** in Python and JavaScript have similar concepts.
- Both languages can be used for **scripting** and have a wide range of **libraries**.

#### 🔄 Differences:
- **Variable Declaration**: In Python, you declare a variable like this:
  ```python
  name = "John"
  ```
  In JavaScript, you must use `let`, `const`, or `var`:
  ```javascript
  let name = "John";
  const age = 25;
  ```

- **String Formatting**: Python uses `f-strings`:
  ```python
  name = "Alice"
  print(f"Hello, {name}")
  ```
  JavaScript uses template literals:
  ```javascript
  let name = "Alice";
  console.log(`Hello, ${name}`);
  ```

- **Indentation vs Curly Braces**: In Python, you use indentation to define code blocks. JavaScript uses curly braces `{}`:
  - Python:
    ```python
    if x > 10:
        print("Greater than 10")
    ```
  - JavaScript:
    ```javascript
    if (x > 10) {
        console.log("Greater than 10");
    }
    ```

### 🎯 Example: Basic Loops in Python and JavaScript

#### Python:
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```

#### JavaScript:
```javascript
let numbers = [1, 2, 3, 4, 5];
for (let num of numbers) {
    console.log(num);
}
```

### 📝 JavaScript Task: Number Guessing Game

**Description**: Create a simple number guessing game where the computer randomly selects a number between 1 and 100, and the user has to guess it. The game will provide feedback on whether the guess is too high or too low, and it will count the number of attempts until the user guesses correctly.

#### 🎯 Requirements:
1. Generate a random number between 1 and 100.
2. Prompt the user to enter their guess.
3. Provide feedback:
   - If the guess is too high, display "Too high! Try again."
   - If the guess is too low, display "Too low! Try again."
   - If the guess is correct, display "Congratulations! You guessed the number in X attempts!"
4. Allow the user to continue guessing until they find the correct number.

### 🎉 Additional Features to Implement:
- **Guess Range**: Allow the user to specify a custom range (e.g., between 1 and N) for the random number.
- **Hint System**: Provide hints after a few incorrect guesses, such as whether the number is odd or even.
- **Replay Option**: After a correct guess, ask the user if they want to play again without needing to refresh the page.
- **Score Tracking**: Keep track of the user's score based on the number of attempts. Fewer attempts should yield a higher score.

### 🗂️ Skeleton Code
Here’s a skeleton code structure to get your students started (the actual implementation is hidden for you to reveal later):

```javascript
function numberGuessingGame() {
    // Step 1: Generate a random number
    // const randomNumber = ...;

    let guess = null; // User's guess
    let attempts = 0; // Count of attempts

    // Step 2: Loop until the guess is correct
    while (guess !== randomNumber) {
        // Prompt the user for their guess
        // guess = ...;

        attempts++;

        // Step 3: Provide feedback based on the guess
        if (guess > randomNumber) {
            console.log("Too high! Try again.");
        } else if (guess < randomNumber) {
            console.log("Too low! Try again.");
        } else {
            console.log(`Congratulations! You guessed the number in ${attempts} attempts!`);
        }
    }

    // Step 4: Ask if the user wants to play again
    // If yes, restart the game
}

// To start the game, call the function:
numberGuessingGame();
```

#### 🎯 Points Breakdown:
| **Task**                                      | **Points** |
|-----------------------------------------------|------------|
| Random number generation                      | 20         |
| User input and guessing logic                 | 30         |
| Feedback for high/low guesses                 | 20         |
| Count and display attempts                    | 20         |
| Additional features implementation             | 10         |

### 📚 Additional Resources

- [JavaScript Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript) 🌐
- [JavaScript Basics for Beginners](https://www.w3schools.com/js/js_intro.asp) 🚀
- [Math Object in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math) 📖

---

Learning JavaScript will make you a more versatile developer. 💪 It’s time to dive in, experiment, and create something awesome. Let's get started with this number guessing game project and explore more advanced features in the future!

Happy Coding! 💻🌟

---
