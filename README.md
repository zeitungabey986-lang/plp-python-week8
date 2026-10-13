
# Personal Mini-Toolkit

## Project Description

The Personal Mini-Toolkit is a Python program that provides three useful tools in one menu-driven application. It allows users to calculate numbers, manage their tasks, and play a number guessing game. This project demonstrates the Python programming concepts I learned during Week 8.

## Tools Included

### 1. Simple Calculator
The calculator allows users to add, subtract, multiply, and divide two numbers. It handles invalid input and prevents division by zero.

### 2. To-Do List
The to-do list allows users to add new tasks, view their tasks, and remove tasks. It uses a Python list to manage tasks while the program is running.

### 3. Number Guessing Game
The game generates a random number between 1 and 10. The user guesses the number and receives hints until the correct number is found.

## Python Concepts Used

- Variables
- Input and output
- Conditional statements: `if`, `elif`, and `else`
- Loops: `while` and `for`
- Lists and list methods
- Functions
- F-strings
- Error handling with `try` and `except`
- The `random` module

## Project Files

- `toolkit.py` - The main Python program.
- `toolkit_plan.txt` - The project plan and testing plan.
- `README.md` - Project documentation.
- `screenshots/` - Screenshots showing the menu and each tool in action.

## How to Run the Program

### Requirements

Python 3 must be installed on your computer.

### Instructions

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

   ```bash
   py toolkit.py
   ```

4. Select a tool from the menu:
   - Enter `1` for the Simple Calculator.
   - Enter `2` for the To-Do List.
   - Enter `3` for the Number Guessing Game.
   - Enter `4` to quit.

## Testing

I tested the calculator with different mathematical operations, including division by zero. I tested adding, viewing, and removing tasks in the to-do list. I also tested the number guessing game, invalid menu choices, and the quit option.

## Reflection

The hardest part of this project was connecting all three tools to one menu. I learned how loops allow a menu to repeat until the user chooses to quit. Handling invalid input was challenging because the program needed to continue running without crashing. I also learned how lists can store, add, and remove tasks. Testing helped me understand how conditionals and functions work together. I am proud that I combined several Python concepts in one program. If I had one more week, I would add a feature to save tasks in a file so they remain available after the program closes.
