# Create the menu

tasks = ["Add task", "View tasks", "Exit"]

size = len(tasks)

for i in range(size):
    print(str(i+1) + ".", tasks[i])

try:
    tasks_choice = int(input("Choose an option: "))

    if tasks_choice in range(1,size+1):
        print(tasks[tasks_choice - 1], "selected.")
    else:
        print("Invalid choice. Choose again.")
except ValueError:
    print("Invalid input. Choose a number.")