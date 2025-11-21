"""
This program implements a todo list application.
This program allows us to print the list, add new todo, delete an existing todo,
and set the todo status to be completed.

The program uses two global dictionary variables to track the todo items.
First dict called "tasks", has key of task id, and value of task description.
Second dict called "stats", has key of task id, and value of task status.
Boolean value True stands for completed, boolean False means not completed.

Examples of two dictionaries look like the followings:
tasks = {1: "Do homework", 2: "Clean room"}
stats = {1: False, 2: True}
"""

# create two empty dictionaries called 'tasks' and 'stats'
tasks = {}
stats = {}


def create_task(description):
    """
    Function create_task is used to add a new task into the application.
    Since dictionaries 'tasks' and 'stats' share the same task id, a new
    task id must be generated first.
    If currently no task, we assign 1 to the new task id.
    If currently one or more tasks exist, we get the maximum key of all tasks,
    and then adding 1 to the max key to get the new task id.

    Afterwards, add entry to both dictionaries.

    @param [str] description: name of the task

    @return [int] id of the newly added tasks
    """
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = max(tasks.keys()) + 1

    tasks[new_id] = description
    stats[new_id] = False
    return new_id


def show_tasks():
    """
    Display all the todo tasks (incompleted).
    Firstly, print the header line (provided already).
    Then check the length of either dictionary, if empty, print "No tasks yet!",
    and then terminate the function by "return" statement.
    Otherwise, use for loop to print incompleted tasks with the following format
    task_id: task_description - task_status

    During the for loop, if the task is completed, skip the current iteration.

    @return None
    """

    print("\n=== Your Todo List ===")

    if len(tasks) == 0 or len(stats) == 0:
        print("No tasks yet!")
        return

    for tid in sorted(tasks.keys()):
        if stats[tid] is True:
            continue
        print(f"{tid}: {tasks[tid]} - {stats[tid]}")


def complete_task(tid):
    """
    Function complete_task() change the task status from False to True.
    If the task id can be found in dictionary 'stats', change the value of the
    specific key from True to False.

    @param [id] tid: id of the task

    @return [bool] True if changed, False otherwise
    """
    if tid in stats:
        stats[tid] = True
        return True
    return False


def delete_task(tid):
    """
    Function delete_task() removes the entry from both dictionaries.
    If the task id can be found, delete the entry from both dictionaries.

    @param [id] tid: id of the task

    @return [bool] True if changed, False otherwise
    """
    if tid in tasks and tid in stats:
        del tasks[tid]
        del stats[tid]
        return True
    return False


def main():
    """
    Main logic of the program.
    The program will keep waiting for user actions, so implement this with
    infinite while loop.
    For every iteration of the loop, we print the menus, and ask for user to
    enter the option.
    """
    while True:
        print("\n=== Todo Menu ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        option = input().strip()

        if option == "1":
            show_tasks()

        elif option == "2":
            task_name = input()
            task_id = create_task(task_name)
            print(f"Added tasks {task_id}: {task_name}")

        elif option == "3":
            try:
                task_id = int(input())
            except ValueError:
                print("Invalid task id")
                continue

            changed = complete_task(task_id)
            if changed:
                print(f"Task #{task_id} marked as completed!")
            else:
                print("Invalid task id")

        elif option == "4":
            try:
                task_id = int(input())
            except ValueError:
                print("Invalid task id")
                continue

            changed = delete_task(task_id)
            if changed:
                print(f"Task #{task_id} deleted")
            else:
                print("Invalid task id")

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
