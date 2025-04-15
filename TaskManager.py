# # Simple Task Manager using Python lists

# task_list = []


# def show_menu():
#     print("\nTask Manager Menu:")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Remove Task")
#     print("4. Mark Task as Done")
#     print("5. Exit")

# def add_task():
#     task = input("Enter the task: ")
#     task_list.append(task)
#     print("✅ Task added!")

# task_list = {"tasks": [], "done": []}


# def show_menu():
#     print("\nTask Manager Menu:")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Remove Task")
#     print("4. Mark Task as Done")
#     print("5. View Done Tasks")
#     print("6. Exit")


# def add_task():
#     task = input("Enter the task: ")
#     task_list["tasks"].append(task)
#     print(" Task added!")


# def view_tasks():
#     if not task_list["tasks"]:
#         print(" No tasks available.")
#     else:
#         print("\n Your Tasks:")
#         for i, task in enumerate(task_list["tasks"]):
#             print(f"{i + 1}. {task}")


# def view_done_tasks():
#     if not task_list["done"]:
#         print(" No done tasks available.")
#     else:
#         print("\n Your Done Tasks:")
#         for i, task in enumerate(task_list["done"]):
#             print(f"{i + 1}. {task}")


# def remove_task():
#     view_tasks()
#     try:
#         index = int(input("Enter the task number to remove: ")) - 1
#         removed = task_list["tasks"].pop(index)
#         print(f" Removed task: {removed}")
#     except (IndexError, ValueError):
#         print(" Invalid task number.")


# def mark_task_done():
#     view_tasks()
#     try:
#         index = int(input("Enter the task number to mark as done: ")) - 1
#         task_list["done"].append(task_list["tasks"].pop(index))
#         print(f" Task marked as done.")
#     except (IndexError, ValueError):
#         print(" Invalid task number.")


# # Main loop
# while True:
#     show_menu()
#     choice = input("Choose an option (1-6): ")

#     if choice == "1":
#         add_task()
#     elif choice == "2":
#         view_tasks()
#     elif choice == "3":
#         remove_task()
#     elif choice == "4":
#         mark_task_done()
#     elif choice == "5":
#         view_done_tasks()
#     elif choice == "6":
#         print(" Exiting Task Manager. Goodbye!")
#         break
#     else:
#         print(" Invalid option. Please choose from 1 to 6.")
#         task_list = {"tasks": [], "done": []}


# def show_menu():
#     print("\nTask Manager Menu:")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Remove Task")
#     print("4. Mark Task as Done")
#     print("5. View Done Tasks")
#     print("6. Exit")


# def add_task():
#     task = input("Enter the task: ")
#     task_list["tasks"].append(task)
#     print(" Task added!")


# def view_tasks():
#     if not task_list["tasks"]:
#         print(" No tasks available.")
#     else:
#         print("\n Your Tasks:")
#         for i, task in enumerate(task_list["tasks"]):
#             print(f"{i + 1}. {task}")


# def view_done_tasks():
#     if not task_list["done"]:
#         print(" No done tasks available.")
#     else:
#         print("\n Your Done Tasks:")
#         for i, task in enumerate(task_list["done"]):
#             print(f"{i + 1}. {task}")


# def remove_task():
#     view_tasks()
#     try:
#         index = int(input("Enter the task number to remove: ")) - 1
#         removed = task_list["tasks"].pop(index)
#         print(f" Removed task: {removed}")
#     except (IndexError, ValueError):
#         print(" Invalid task number.")


# def mark_task_done():
#     view_tasks()
#     try:
#         index = int(input("Enter the task number to mark as done: ")) - 1
#         task_list["done"].append(task_list["tasks"].pop(index))
#         print(f" Task marked as done.")
#     except (IndexError, ValueError):
#         print(" Invalid task number.")


# # Main loop
# while True:
#     show_menu()
#     choice = input("Choose an option (1-6): ")

#     if choice == "1":
#         add_task()
#     elif choice == "2":
#         view_tasks()
#     elif choice == "3":
#         remove_task()
#     elif choice == "4":
#         mark_task_done()
#     elif choice == "5":
#         view_done_tasks()
#     elif choice == "6":
#         print(" Exiting Task Manager. Goodbye!")
#         break
#     else:
#         print(" Invalid option. Please choose from 1 to 6.")
#         task_list = {"tasks": [], "done": []}


# def show_menu():
#     print("\nTask Manager Menu:")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Remove Task")
#     print("4. Mark Task as Done")
#     print("5. View Done Tasks")
#     print("6. Exit")


# def add_task():
#     task = input("Enter the task: ")
#     task_list["tasks"].append(task)
#     print(" Task added!")


# def view_tasks():
#     if not task_list["tasks"]:
#         print(" No tasks available.")
#     else:
#         print("\n Your Tasks:")
#         for i, task in enumerate(task_list["tasks"], start=1):
#             print(f"{i}. {task}")


# def view_done_tasks():
#     if not task_list["done"]:
#         print(" No done tasks available.")
#     else:
#         print("\n Your Done Tasks:")
#         for i, task in enumerate(task_list["done"], start=1):
#             print(f"{i}. {task}")


# def remove_task():
#     view_tasks()
#     try:
#         index = int(input("Enter the task number to remove: ")) - 1
#         removed = task_list["tasks"].pop(index)
#         print(f" Removed task: {removed}")
#     except (IndexError, ValueError):
#         print(" Invalid task number.")


# def mark_task_done():
#     view_tasks()
#     try:
#         index = int(input("Enter the task number to mark as done: ")) - 1
#         task_list["done"].append(task_list["tasks"].pop(index))
#         print(f" Task marked as done.")
#     except (IndexError, ValueError):
#         print(" Invalid task number.")


# # Main loop
# while True:
#     show_menu()
#     choice = input("Choose an option (1-6): ")

#     if choice == "1":
#         add_task()
#     elif choice == "2":
#         view_tasks()
#     elif choice == "3":
#         remove_task()
#     elif choice == "4":
#         mark_task_done()
#     elif choice == "5":
#         view_done_tasks()
#     elif choice == "6":
#         print(" Exiting Task Manager. Goodbye!")
#         break
#     else:
#         print(" Invalid option. Please choose from 1 to 6.")
# def view_tasks():
#     if not task_list:
#         print("📭 No tasks available.")
#     else:
#         print("\n📋 Your Tasks:")
#         for i, task in enumerate(task_list):
#             print(f"{i + 1}. {task}")


# def remove_task():
#     view_tasks()
#     try:
#         index = int(input("Enter the task number to remove: ")) - 1
#         removed = task_list.pop(index)
#         print(f"❌ Removed task: {removed}")
#     except (IndexError, ValueError):
#         print("⚠️ Invalid task number.")


# def mark_task_done():
#     view_tasks()
#     try:
#         index = int(input("Enter the task number to mark as done: ")) - 1
#         task_list[index] += " ✅"
#         print(f"🎉 Task marked as done: {task_list[index]}")
#     except (IndexError, ValueError):
#         print("⚠️ Invalid task number.")


# # Main loop
# while True:
#     show_menu()
#     choice = input("Choose an option (1-5): ")

#     if choice == "1":
#         add_task()
#     elif choice == "2":
#         view_tasks()
#     elif choice == "3":
#         remove_task()
#     elif choice == "4":
#         mark_task_done()
#     elif choice == "5":
#         print("👋 Exiting Task Manager. Goodbye!")
#         break
#     else:
#         print("⚠️ Invalid option. Please choose from 1 to 5.")




task_list = []

while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        task_list.append(task)
        print("✅ Task added!")

    elif choice == "2":
        if not task_list:
            print("📭 No tasks available.")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(task_list):
                print(f"{i + 1}. {task}")

    elif choice == "3":
        if not task_list:
            print("⚠️ No tasks to remove.")
        else:
            for i, task in enumerate(task_list):
                print(f"{i + 1}. {task}")
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                removed = task_list.pop(index)
                print(f"❌ Removed task: {removed}")
            except (IndexError, ValueError):
                print("⚠️ Invalid task number.")

    elif choice == "4":
        if not task_list:
            print("⚠️ No tasks to mark.")
        else:
            for i, task in enumerate(task_list):
                print(f"{i + 1}. {task}")
            try:
                index = int(input("Enter the task number to mark as done: ")) - 1
                task_list[index] += " ✅"
                print(f"🎉 Task marked as done: {task_list[index]}")
            except (IndexError, ValueError):
                print("⚠️ Invalid task number.")

    elif choice == "5":
        print("👋 Exiting Task Manager. Goodbye!")
        break

    else:
        print("⚠️ Invalid option. Please choose from 1 to 5.")
