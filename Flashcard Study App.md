# 📚 Flashcard Study App

![firmbee-com-gcsNOsPEXfs-unsplash](https://github.com/user-attachments/assets/1e408093-6b18-462c-a8ab-86d2174239f7)


## Project Overview

The **Flashcard Study App** is a Python-based project where students create, organize, and review flashcards to study various topics. The app will utilize dictionaries to store flashcards, each containing a question and answer pair. This project helps students build practical skills in dictionary management, as they perform tasks like adding, updating, retrieving, and deleting flashcards from a dictionary database.

### Learning Objectives

- Gain experience using Python dictionaries to store, update, and retrieve data.
- Practice CRUD (Create, Read, Update, Delete) operations on dictionary entries.
- Build a text-based application that simulates a digital flashcard review experience.
- Implement user interaction for real-time flashcard creation, review, and management.

---

## 🔧 Project Requirements

1. **Python Version**: Python 3.8 or above.
2. **Libraries**: No external libraries are required.
3. **Version Control**: Use Git/GitHub to manage project progress.

---

## 🎯 Key Functionalities

- **Create Flashcards**: Users can add new flashcards by entering a question and answer pair.
- **Edit Flashcards**: Users can update existing questions or answers.
- **Review Flashcards**: Randomly display a question for users to answer, with the option to show the answer if they need it.
- **Delete Flashcards**: Users can remove a flashcard if it is no longer needed.
- **List Flashcards**: Display all flashcards available in the system.

---

## Project Breakdown and Structure

### 1. **Flashcard Class**

**Description**: This class manages individual flashcards, which include a question and answer. Each flashcard is stored as a key-value pair within a dictionary.

**Attributes**:
- `question`: The flashcard question.
- `answer`: The answer to the flashcard question.

**Methods**:
- `display_question()`: Display the question.
- `display_answer()`: Display the answer.

Example:

```python
class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def display_question(self):
        return f"Question: {self.question}"

    def display_answer(self):
        return f"Answer: {self.answer}"
```

### 2. **FlashcardManager Class**

**Description**: This class manages all flashcards using a dictionary, where each entry stores a `Flashcard` instance with the question as the key.

**Attributes**:
- `flashcards`: A dictionary to store flashcards, where the question is the key and the `Flashcard` object is the value.

**Methods**:
- `add_flashcard(question, answer)`: Add a new flashcard.
- `edit_flashcard(question, new_question, new_answer)`: Edit an existing flashcard.
- `delete_flashcard(question)`: Delete a flashcard.
- `list_flashcards()`: Display all flashcards.
- `review_flashcard()`: Pick a random flashcard to display for review.

Example:

```python
import random

class FlashcardManager:
    def __init__(self):
        self.flashcards = {}

    def add_flashcard(self, question, answer):
        self.flashcards[question] = Flashcard(question, answer)

    def edit_flashcard(self, question, new_question, new_answer):
        if question in self.flashcards:
            self.flashcards[new_question] = Flashcard(new_question, new_answer)
            if new_question != question:
                del self.flashcards[question]

    def delete_flashcard(self, question):
        if question in self.flashcards:
            del self.flashcards[question]

    def list_flashcards(self):
        for question, flashcard in self.flashcards.items():
            print(flashcard.display_question())

    def review_flashcard(self):
        if self.flashcards:
            question = random.choice(list(self.flashcards.keys()))
            flashcard = self.flashcards[question]
            print(flashcard.display_question())
            input("Press Enter to show the answer...")
            print(flashcard.display_answer())
        else:
            print("No flashcards to review!")
```

---

## Suggested Project Workflow

1. **Create Basic Flashcards**:
   - Start by defining the `Flashcard` and `FlashcardManager` classes.
   - Implement adding and listing flashcards.

2. **Implement CRUD Operations**:
   - Add editing and deleting capabilities in the `FlashcardManager` class.

3. **Add Review Functionality**:
   - Implement the `review_flashcard()` method for random review of flashcards.

4. **Build a Menu System**:
   - Create a basic interface in the main script to navigate flashcard options:
     - **Add Flashcard**
     - **Edit Flashcard**
     - **Delete Flashcard**
     - **List Flashcards**
     - **Review Flashcards**

---

## Project Structure

```
flashcard_app/
│
├── flashcard.py            # Contains the Flashcard class
├── flashcard_manager.py    # Contains the FlashcardManager class
├── main.py                 # Main script to run the application (menu system)
├── README.md               # Project documentation
```

---

## Sample User Flow

1. **Menu Display**:
   - The user is prompted with options to add, edit, delete, list, or review flashcards.

2. **Create Flashcard**:
   - User inputs a question and answer, which are saved as a dictionary entry in `flashcards`.

3. **Review Mode**:
   - A random question is displayed for the user to answer mentally, with an option to display the correct answer.

---

## 📅 Suggested Timeline

| Task                   | Duration       |
|------------------------|----------------|
| Create Classes         | 1 day          |
| Implement CRUD         | 1 day          |
| Add Review Mode        | 1 day          |
| Build Menu & Testing   | 1 day          |

---

## 🎉 Conclusion

This **Flashcard Study App** is a hands-on way for students to strengthen their skills in Python dictionaries, data management, and user interaction. By managing and reviewing flashcards, they will practice key coding concepts while creating a practical study tool.
