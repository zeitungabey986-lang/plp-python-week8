
import random


# Tool 1: A simple calculator for two numbers.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Choose an operation: +, -, *, /")
        operation = input("Enter operation: ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Sorry, you cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation.")
            return

        print(f"Result: {result:g}")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: A to-do list that allows users to add, view, and remove tasks.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter your task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
                continue

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            try:
                task_number = int(input("Enter task number to remove: "))

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Removed task: {removed_task}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a whole number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please choose from 1 to 4.")


# Tool 3: A number guessing game.
def number_guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("Guess a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 10:
                print("Please choose a number from 1 to 10.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(
                    f"Correct! You guessed the number "
                    f"in {attempts} attempt(s)."
                )
                break

        except ValueError:
            print("Please enter a valid whole number.")


# Main program: Display the menu until the user chooses Quit.
def main():
    print("Welcome to My Personal Mini-Toolkit!")

    while True:
        print("\nChoose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            number_guessing_game()
        elif choice == "4":
            print("Thank you for using my toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


# Run the program.
if __name__ == "__main__":
    main()
