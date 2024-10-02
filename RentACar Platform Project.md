# 🚗 RentACar Platform Project

## Project Overview

The **RentACar Platform** is a collaborative Python-based project that simulates a car rental management system. The system will allow users to rent, return, and manage cars. Students will work in groups, where each student will take on a specific role, contributing to different parts of the project.

### Purpose

The purpose of this project is to:
- Gain hands-on experience with Python functions, classes, and file handling.
- Develop teamwork and project management skills.
- Understand how different roles work together to build a complete application.

---

## 🚀 Project Requirements

1. **Python Version**: Python 3.8 or above
2. **Libraries**: 
   - `datetime` for managing dates.
   - `json` for storing and managing car and user data.
   - `os` for file handling and directory management.
3. **Version Control**: Use GitHub for collaboration and version control.

### Key Functionalities

- **Admin Panel**: Add, remove, or modify cars in the system.
- **User Panel**: Rent and return cars.
- **Payment System**: Simple payment calculation based on rental time.

---

## 👥 Team Roles

### 1. **Back-End Developer (Student 1)**

**Role Overview**: The Back-End Developer is responsible for building the core functionality of the platform. They will manage the car rental system's logic, data storage, and system functions like renting and returning cars.

**Key Responsibilities**:
- Define the **Car** and **User** classes using object-oriented programming.
- Create methods to **rent a car**, **return a car**, and **display available cars**.
- Implement **file handling** to save and retrieve user and car data (using JSON or CSV).
- Develop a **simple payment calculation** system based on rental duration.

**Tasks**:
- Create the `car.py` module to define the Car class, including attributes like `car_id`, `brand`, `model`, `rental_price`, and `availability`.
- Implement rental logic: when a user rents a car, the system should update the availability status.
- Use file handling (JSON) to save and load the list of available cars.

**Advice**: Focus on clear logic and keep functions modular. Work closely with the front-end developer to ensure seamless integration.

---

### 2. **Front-End Developer (Student 2)**

**Role Overview**: The Front-End Developer is responsible for creating the user interface. This includes taking inputs from the user, displaying available cars, and showing rental receipts and confirmations.

**Key Responsibilities**:
- Create an intuitive **console-based interface**.
- Display available cars and rental options to the user.
- Integrate with the Back-End Developer’s methods to allow users to rent and return cars.
- Ensure that the interface provides **clear error handling** for invalid inputs.

**Tasks**:
- Build a **menu system** that lets users select options like "View Cars", "Rent a Car", "Return a Car", and "Exit".
- Implement user prompts and display feedback from the back-end methods (e.g., successful rental or return).
- Handle **exceptions** for invalid inputs (e.g., user tries to rent an unavailable car).

**Advice**: Keep the interface simple and clean. Communicate regularly with the back-end developer to ensure data flows smoothly between the UI and the business logic.

---

### 3. **Project Manager & Tester (Student 3)**

**Role Overview**: The Project Manager coordinates the project timeline and ensures the code is properly tested before final submission. This role ensures all parts work together correctly and meet the project requirements.

**Key Responsibilities**:
- Create a **timeline** and ensure tasks are delivered on time.
- Test the functionality of the system by creating **unit tests** and manual tests.
- Ensure that the system meets the functional requirements for renting and returning cars.
- Write documentation on how to set up, run, and use the application.

**Tasks**:
- Write **unit tests** for the car rental logic, ensuring that each feature (rent, return, etc.) works as expected.
- Ensure proper **integration** between front-end and back-end components.
- Document how to run the project and include installation steps in the **README.md**.

**Advice**: Pay attention to edge cases (e.g., what happens if all cars are rented?). Make sure to thoroughly test the system before marking it as complete.

---

## 💡 Recommendations

1. **Communication**: Constant communication between all team members is critical. Ensure that each role interacts properly with the others. For example, the Front-End Developer should work closely with the Back-End Developer to make sure the user interface interacts properly with the car rental logic.

2. **Version Control**: Make frequent commits to GitHub with meaningful commit messages. Use **branches** for different features and open **pull requests** when a feature is complete. The Project Manager will review the pull requests before merging them into the main branch.

3. **Code Documentation**: Each member must document their code clearly. For example, include docstrings for all methods and explain the purpose of each function.

---

## 📋 Project Structure

```
├── rentacar/
│   ├── car.py              # Car class and logic
│   ├── user.py             # User class and management
│   ├── rental_system.py    # Backend logic for renting/returning cars
│   ├── interface.py        # Front-end interface
│   ├── data/
│       ├── cars.json       # Data store for cars
│       ├── users.json      # Data store for users
├── tests/
│   ├── test_rental_system.py # Unit tests for backend logic
├── README.md               # Project documentation
```

---

## 🛠️ Tools and Technologies

1. **Python**: Core programming language for building the system.
2. **Git/GitHub**: For version control and collaboration.
3. **JSON**: For storing car and user data.
4. **Unit Testing**: Using Python’s `unittest` library for testing.

---

## 🎯 Success Criteria

The project will be deemed successful if it meets the following criteria:
1. The system can successfully **add**, **rent**, and **return cars**.
2. Users can view available cars and rent cars using a **user-friendly interface**.
3. Data is stored and retrieved using **file handling**.
4. The system is **properly tested** and has unit tests that cover the main functionalities.

---

## 🔧 Installation Guide

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/rentacar-platform.git
   cd rentacar-platform
   ```

2. **Install dependencies** (if any):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the platform**:
   ```bash
   python interface.py
   ```

4. **Run unit tests**:
   ```bash
   python -m unittest discover -s tests
   ```

---

## 📅 Timeline

| Task                  | Deadline         | Responsible Student |
|-----------------------|------------------|---------------------|
| Backend Development    | Week 1           | Back-End Developer   |
| Frontend Development   | Week 2           | Front-End Developer  |
| Testing & Integration  | Week 3           | Project Manager      |
| Final Review & Submit  | End of Week 3    | All                 |

---

### 👏 Conclusion

This project will help you understand how to build a Python-based system from the ground up, working collaboratively with your peers. Each of you will be responsible for crucial components of the system, mimicking real-world project environments where team members specialize in different areas.

Good luck! 🚀

---

