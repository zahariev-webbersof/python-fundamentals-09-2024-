# 🚗 RentACar Platform Project (Functions-Based)

## Project Overview

The **RentACar Platform** is a collaborative Python-based project where students will build a car rental management system using only **functions**, **lists**, and **dictionaries**—no object-oriented programming or classes are required. This project simulates the process of renting, returning, and managing a fleet of cars.

### Purpose

The purpose of this project is to:
- Strengthen your understanding of Python **functions**, **dictionaries**, **lists**, and **control flow**.
- Develop collaboration and project management skills.
- Learn how to structure and integrate Python code for a small-scale system.

---

## 🚀 Project Requirements

1. **Python Version**: Python 3.8 or above
2. **Libraries**: None required, built-in functions only
3. **Version Control**: Use GitHub for collaboration and version control.

### Key Functionalities

- **Admin Panel**: Add, remove, or modify cars in the system.
- **User Panel**: Rent and return cars.
- **Payment System**: Calculate total rental cost based on time rented.

---

## 👥 Team Roles

### 1. **Back-End Developer (Student 1)**

**Role Overview**: The Back-End Developer will manage the logic for renting, returning, and displaying cars. They will store data using Python's **dictionaries** and **lists** to represent cars and users.

**Key Responsibilities**:
- Define a **car list** and a **rental status dictionary** to track available cars.
- Create functions for **renting a car**, **returning a car**, and **viewing available cars**.
- Manage the **rental duration** and **cost calculations**.

**Tasks**:
- Create a **list of dictionaries** for storing cars, with each car having `id`, `brand`, `model`, `rental_price`, and `availability`.
- Write the function `rent_car()` which takes the user's input (car id) and updates its availability status.
- Create a function `return_car()` that returns the car and calculates the total rental cost.
- Use dictionaries to store car details and rental status.

**Advice**: Keep each function simple and modular. Communicate with the front-end developer to ensure smooth data flow between logic and interface.

Example functions for this role:

```python
def initialize_cars():
    cars = [
        {"id": 1, "brand": "Toyota", "model": "Camry", "rental_price": 40, "available": True},
        {"id": 2, "brand": "Honda", "model": "Civic", "rental_price": 35, "available": True},
        {"id": 3, "brand": "Ford", "model": "Mustang", "rental_price": 55, "available": True},
    ]
    return cars

def rent_car(cars, car_id):
    for car in cars:
        if car["id"] == car_id and car["available"]:
            car["available"] = False
            return f"You have rented the {car['brand']} {car['model']}."
    return "Car is unavailable or invalid car ID."
```

---

### 2. **Front-End Developer (Student 2)**

**Role Overview**: The Front-End Developer is responsible for creating a **text-based user interface**. They will handle user input, display car information, and ensure the program interacts with the back-end functions.

**Key Responsibilities**:
- Build a **menu system** where users can view cars, rent cars, or return cars.
- Capture user input and pass it to the appropriate functions.
- Display appropriate messages based on the back-end responses.

**Tasks**:
- Create a **main menu** function that displays options like "View Cars", "Rent a Car", "Return a Car", and "Exit".
- Implement input validation to ensure the user enters valid options and car IDs.
- Display car availability and rental details by calling functions from the back-end.

**Advice**: Ensure the interface is intuitive and easy to follow. Work closely with the Back-End Developer to ensure functions are properly connected.

Example code for the front-end:

```python
def display_cars(cars):
    print("\nAvailable Cars:")
    for car in cars:
        status = "Available" if car["available"] else "Rented"
        print(f"ID: {car['id']} - {car['brand']} {car['model']} - ${car['rental_price']}/day - {status}")

def main_menu():
    print("Welcome to RentACar!")
    print("1. View Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")
    return input("Please choose an option (1-4): ")
```

---

### 3. **Project Manager & Tester (Student 3)**

**Role Overview**: The Project Manager ensures that tasks are completed on time and the project is tested thoroughly. They will also write the project's documentation, outlining the setup, usage, and functionality of the system.

**Key Responsibilities**:
- Test the functions by running **manual tests** and ensure everything works as expected.
- **Coordinate** the integration between front-end and back-end components.
- Write the **README.md** file with a description of the project, how to install and run it, and how each function works.

**Tasks**:
- Write simple **test cases** to ensure that renting and returning cars work as expected.
- Verify that the user interface correctly interacts with the backend logic.
- Document the project setup, usage, and functionality in the **README.md** file.

**Advice**: Ensure you test all edge cases, such as attempting to rent a car that is already rented. Write clear documentation for anyone who wants to understand how the system works.

---

## 💡 Recommendations

1. **Communication**: Constant communication is key. Ensure the Front-End Developer and Back-End Developer work closely to integrate the functions smoothly.
2. **Version Control**: Use **GitHub** for version control. Each developer should work on their own branch and submit **pull requests** for review.
3. **Documentation**: Document all functions clearly. This will make testing and debugging easier.

---

## 📋 Project Structure

```
├── rentacar/
│   ├── backend.py         # Backend functions (rent_car, return_car, etc.)
│   ├── frontend.py        # Frontend functions (display_cars, main_menu, etc.)
│   ├── data/              # JSON or text files for storing cars and user data
├── tests/
│   ├── test_backend.py    # Tests for backend functions
│   ├── test_frontend.py   # Tests for frontend functions
├── README.md              # Project documentation
```

---

## 🛠️ Tools and Technologies

1. **Python**: Core programming language.
2. **Git/GitHub**: Version control for collaboration.
3. **Manual Testing**: Ensure functionality through manual tests and basic unit tests.

---

## 🎯 Success Criteria

The project is considered successful if:
1. Users can **view cars**, **rent a car**, and **return a car** successfully.
2. Data is stored and manipulated using **functions**, **dictionaries**, and **lists**.
3. The system is tested and documented, and the team works collaboratively on GitHub.

---

## 🔧 Installation Guide

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/rentacar-platform.git
   cd rentacar-platform
   ```

2. **Run the platform**:
   ```bash
   python frontend.py
   ```

3. **Run manual tests**:
   ```bash
   python tests/test_backend.py
   ```

---

## 📅 Timeline

| Task                  | Deadline         | Responsible Student |
|-----------------------|------------------|---------------------|
| Backend Development    | Week 1           | Back-End Developer   |
| Frontend Development   | Week 2           | Front-End Developer  |
| Testing & Documentation| Week 3           | Project Manager      |
| Final Review & Submit  | End of Week 3    | All                 |

---

### 🎉 Conclusion

This project will help you master how to create a Python-based application using only functions, lists, and dictionaries. Each team member has a crucial role in developing different components, ensuring you all learn how to contribute to a larger project.

Good luck! 🚀

---
