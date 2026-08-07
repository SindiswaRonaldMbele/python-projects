# Storing Tasks

menu = ["Add task", "View tasks", "Exit"]
size = len(menu)
tasks = []
is_running = True  # 1. Added a flag to control the main loop

def smart_print(*output):
    print(
        "=" * 37,
        *output,
        "=" * 37,
        sep = "\n"
    )

def show_menu():
    output = []
    for num, task in enumerate(menu, 1):
        output.append(f"{num}. {task}")
    smart_print(*output)

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    smart_print("Task successfully added!")

def view_tasks():
    if not tasks:  # 2. Check if empty BEFORE printing
        smart_print("No tasks added yet!")
    else:
        # Enumerate tasks so they print with numbers on separate lines
        task_output = [f"{i}. {t}" for i, t in enumerate(tasks, 1)]
        smart_print(*task_output)

def select_task():
    global is_running  # Allows us to modify the loop flag
    show_menu()
    try:
        menu_choice = int(input("Choose an option: "))
            
        if menu_choice in range(1, size + 1):
            selected = menu[menu_choice - 1]
            
            if menu_choice == 1:
                add_task()
                # 3. Cleaned up the "add another" loop
                while True:
                    action = input("Do you want to add another task? (y/n): ").lower().strip()
                    if action == "y":
                        add_task()
                    elif action == "n":
                        break
                    else:
                        print("Invalid input. Type 'y' or 'n'.")
            
            elif menu_choice == 2:
                 view_tasks()
                 
            elif menu_choice == 3:
                smart_print("Goodbye!")
                is_running = False  # 4. Breaks the main loop
        else:
            smart_print("Invalid choice. Choose again.")
    except ValueError:
        smart_print("Invalid input. Choose a number.")
                    
# Main program loop
while is_running:
    select_task()