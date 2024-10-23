# 🏋️‍♂️ Fitness Training App 

![Training app Logo](https://preview.redd.it/oi7fw0q55xx11.png?auto=webp&s=ecdd68fc7e0c4587473293530c4ec4414ea86b2f)


## Project Overview

The **Fitness Training App** is a Python-based project designed for individual students to apply **object-oriented programming (OOP)** concepts. The student will develop a fitness app that allows users to create and manage workout routines, track progress, and monitor their personal fitness journey.

### Learning Objectives

- Understand and implement core OOP concepts: **classes**, **objects**, **encapsulation**, **inheritance**, and **polymorphism**.
- Learn how to design a system that manages multiple components (users, exercises, workouts, progress).
- Practice organizing Python code into multiple modules and maintaining clear, reusable class structures.

---

## 🚀 Project Requirements

1. **Python Version**: Python 3.8 or above.
2. **Libraries**: No external libraries required (optional: you can use `datetime` for tracking dates).
3. **Version Control**: Encourage the use of Git/GitHub to manage the project.

### Key Functionalities

- **User Profile Management**: Create, update, and view personal fitness profiles.
- **Workout Plans**: Build, edit, and view personalized workout routines (sets, reps, rest times).
- **Exercise Library**: Maintain a list of exercises with descriptions and difficulty levels.
- **Progress Tracking**: Track workout completion and monitor progress over time.
- **Workout Reports**: Generate reports showing workout history and statistics.

---

## Project Breakdown and Classes

### 1. **User Class** (Handles User Profiles)

**Description**: The `User` class will store and manage information about the user, such as their personal details, fitness goals, and workout history.

**Attributes**:
- `name`: User’s name.
- `age`: User’s age.
- `weight`: User’s current weight (kg).
- `height`: User’s height (cm).
- `goal`: The user’s fitness goal (e.g., "Lose weight", "Build muscle").
- `workout_history`: A list of completed workouts.

**Methods**:
- `update_weight(new_weight)`: Update the user’s weight.
- `update_goal(new_goal)`: Change the user's fitness goal.
- `log_workout(workout)`: Add a completed workout to the workout history.
- `display_info()`: Display the user's profile information.

Example:

```python
class User:
    def __init__(self, name, age, weight, height, goal):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.goal = goal
        self.workout_history = []

    def update_weight(self, new_weight):
        self.weight = new_weight

    def update_goal(self, new_goal):
        self.goal = new_goal

    def log_workout(self, workout):
        self.workout_history.append(workout)

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}kg, Height: {self.height}cm, Goal: {self.goal}"
```

### 2. **Exercise Class** (Handles Individual Exercises)

**Description**: The `Exercise` class represents individual exercises in the app, storing details like the exercise name, description, and difficulty.

**Attributes**:
- `name`: Name of the exercise (e.g., "Squat", "Push-Up").
- `description`: A short description of how to perform the exercise.
- `difficulty`: Difficulty level of the exercise (e.g., "Easy", "Moderate", "Hard").

**Methods**:
- `display_exercise()`: Return a formatted string with exercise details.

Example:

```python
class Exercise:
    def __init__(self, name, description, difficulty):
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def display_exercise(self):
        return f"{self.name} ({self.difficulty}): {self.description}"
```

### 3. **Workout Class** (Handles Workout Plans)

**Description**: The `Workout` class represents a workout routine that includes a list of exercises. Each exercise is associated with the number of sets, repetitions, and rest time.

**Attributes**:
- `name`: The name of the workout (e.g., "Full Body Workout").
- `exercises`: A list of exercises included in the workout. Each exercise will store the sets, reps, and rest time.

**Methods**:
- `add_exercise(exercise, sets, reps, rest_time)`: Add an exercise to the workout.
- `remove_exercise(exercise_name)`: Remove an exercise from the workout by name.
- `view_workout()`: Display all exercises in the workout, with sets, reps, and rest times.

Example:

```python
class Workout:
    def __init__(self, name):
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise, sets, reps, rest_time):
        self.exercises.append({'exercise': exercise, 'sets': sets, 'reps': reps, 'rest_time': rest_time})

    def remove_exercise(self, exercise_name):
        self.exercises = [ex for ex in self.exercises if ex['exercise'].name != exercise_name]

    def view_workout(self):
        print(f"Workout: {self.name}")
        for ex in self.exercises:
            print(f"{ex['exercise'].name}: {ex['sets']} sets, {ex['reps']} reps, {ex['rest_time']} seconds rest")
```

### 4. **ProgressTracker Class** (Tracks User Progress)

**Description**: The `ProgressTracker` class tracks the user’s workout completion over time and can generate reports on workout progress.

**Attributes**:
- `user`: The user whose progress is being tracked.

**Methods**:
- `log_workout(workout)`: Add a completed workout to the user’s workout history.
- `generate_report()`: Generate a report summarizing the user’s workout history and statistics (e.g., number of workouts completed).

Example:

```python
class ProgressTracker:
    def __init__(self, user):
        self.user = user

    def log_workout(self, workout):
        self.user.log_workout(workout)

    def generate_report(self):
        total_workouts = len(self.user.workout_history)
        return f"{self.user.name} has completed {total_workouts} workouts."
```

---

## Suggested Project Workflow

### Step 1: Set Up the User Profile
- Create an instance of the `User` class.
- Allow the user to input their personal information (name, age, weight, height, fitness goal).
- Implement the ability to update their weight and fitness goal as time goes on.

### Step 2: Build the Exercise Library
- Create a list of `Exercise` objects to represent different exercises (e.g., squats, push-ups, lunges).
- Ensure each exercise has a name, description, and difficulty level.

### Step 3: Create Workout Plans
- Create the `Workout` class to build routines from the exercises in the library.
- Allow users to add exercises to their workout plans with sets, reps, and rest times.
- Implement the ability to view and modify workouts.

### Step 4: Track Progress
- Implement the `ProgressTracker` class to log completed workouts for the user.
- Allow users to track their progress over time and generate reports showing workout history and statistics.

### Step 5: Add a Menu System
- Create a basic text-based interface that lets the user navigate through the options:
  - **View Profile**: Display user information.
  - **Edit Profile**: Update weight or fitness goal.
  - **View Exercises**: Display all available exercises.
  - **Create/Modify Workouts**: Build and view workout routines.
  - **Track Progress**: Log workouts and view progress reports.

---

## Project Structure

```
fitness_app/
│
├── user.py           # Contains the User class
├── exercise.py       # Contains the Exercise class
├── workout.py        # Contains the Workout class
├── progress.py       # Contains the ProgressTracker class
├── main.py           # Main script to run the application (menu system)
├── README.md         # Project documentation
```

---

## 🛠️ Tools and Technologies

1. **Python**: Core programming language.
2. **Git/GitHub**: Version control for saving progress and code backups.

---

## 🎯 Success Criteria

The project is considered successful if:
1. Users can create and manage their profiles (update weight, fitness goals).
2. Exercises can be added to and displayed from a library.
3. Workout routines can be built, modified, and displayed.
4. The system tracks completed workouts, and reports can be generated on progress.

---

## 🔧 Installation Guide

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/fitness-training-app.git
   cd fitness-training-app
   ```

2. **Run the app**:
   ```bash
   python main.py
   ```

---

## 📅 Timeline (Suggested for Individual)

| Task                    | Deadline        |
|-------------------------|-----------------|
| User & Exercise Classes  | 1 week          |
| Workout & Progress Classes| 1 week         |
| Menu System & Testing    | 1 week          |
| Final Review & Submit    | End of Week 3   |

---

###

🎉 Conclusion

This **Fitness Training App** will help students develop a comprehensive understanding of OOP concepts and their applications in real-world scenarios. By managing user profiles, exercises, workouts, and progress tracking, the student will get hands-on experience in designing, structuring, and implementing classes.Good luck! 🏋️‍♀️
