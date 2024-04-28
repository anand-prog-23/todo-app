from functions import get_todos, write_todos
import time

while True:
    user_action = input("Type add , show , edit or exit and todo:\n").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            index = index + 1
            row = f"{index}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            user_edit = int(user_action[:5])
            user_edit = user_edit - 1

            todos = get_todos()
            user_input = input("Add new edited \n")
            todos[user_edit] = user_input + "\n"

            write_todos(todos)

        except ValueError:
            print("Not valid ")
            continue

    elif user_action.startswith("complete"):
        try:
            user_complete = int(user_action[9:])
            user_complete = user_complete - 1
            todos = get_todos('todos.txt')
            todo_to_remove = todos[user_complete].strip("\n")

            todos.pop(user_complete)
            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("no such item")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Not valid")

print("bye")
