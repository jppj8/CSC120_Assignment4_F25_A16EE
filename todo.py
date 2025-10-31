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

# TODO: create two empty dictionaries called 'tasks' and 'stats'
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

    # If there are no tasks yet, start IDs at 1
    if len(tasks) == 0:
        new_id = 1
    else:
        # Otherwise, get the max key and add 1
        new_id = max(tasks.keys()) + 1

    # Add to both dictionaries
    tasks[new_id] = description
    stats[new_id] = False  # new task starts as not completed

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

    # If there are no tasks at all
    if len(tasks) == 0:
        print("No tasks yet!")
        return

    # Track if we printed anything
    printed_any = False

    # Loop through all task IDs in increasing order
    for tid in sorted(tasks.keys()):
        # Skip completed tasks
        if stats.get(tid, False) is True:
            continue

        # We only print tasks that are not completed
        status_text = "completed" if stats[tid] else "not completed"
        print(f"{tid}: {tasks[tid]} - {status_text}")
        printed_any = True

    # If everything was completed, nothing printed above
    if not printed_any:
        print("No incompleted tasks! Great job!")


def complete_task(tid):
    """
    Function complete_task() change the task status from False to True.
    If the task id can be found in dictionary 'stats', change the value of the
    specific key from False to True.

    @param [id] tid: id of the task

    @return [bool] True if changed, False otherwise
    """

    # Check if the task id exists
    if tid in stats:
        stats[tid] = True
        return True
    else:
        return False


def delete_task(tid):
    """
    Function delete_task() removes the entry from both dictionaries.
    If the task id can be found, delete the entry from both dictionaries.

    @param [id] tid: id of the task

    @return [bool] True if changed, False otherwise
    """

    # Check if task exists
    if tid in tasks and tid in stats:
        del tasks[tid]
        del stats[tid]
        return True
    else:
        return False


def main():
    """
    Main logic of the program.
    The program will keep waiting for user actions, so implement this with
    infinite while loop.
    For every iteration of the loop, we print the menus, and ask for user to
    enter the option.

    If option is 1, call show_tasks().

    If option is 2, ask for the name of the task, then call create_task(),
    remember to pass the argument and accept the return of the function.
    Then print "Added tasks {task_id}: {task_name}".

    If option is 3, ask for the task id (integer), send it to complete_task().
    The function returns boolean value, use variable to accept the return.
    If the return is True, print "Task #{task_id} marked as completed!",
    otherwise, print "Invalid task id".

    If option is 4, ask for the task id (integer), send it to delete_task().
    The function returns boolean value, use variable to accept the return.
    If the return is True, print "Task #{task_id} deleted",
    otherwise, print "Invalid task id".

    If option i 5, print "Goodbye!" and quit the while loop

    Otherwise, print "Invalid choice.".
    """
    while True:
        print("\n=== Todo Menu ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            # Show tasks
            show_tasks()

        elif choice == "2":
            # Add task
            task_name = input("Enter task description: ").strip()
            if task_name == "":
                print("Task description cannot be empty.")
            else:
                new_id = create_task(task_name)
                print(f"Added task {new_id}: {task_name}")

        elif choice == "3":
            # Complete task
            try:
                tid = int(input("Enter task id to complete: ").strip())
            except ValueError:
                print("Invalid task id (must be a number).")
                continue

            changed = complete_task(tid)
            if changed:
                print(f"Task #{tid} marked as completed!")
            else:
                print("Invalid task id")

        elif choice == "4":
            # Delete task
            try:
                tid = int(input("Enter task id to delete: ").strip())
            except ValueError:
                print("Invalid task id (must be a number).")
                continue

            removed = delete_task(tid)
            if removed:
                print(f"Task #{tid} deleted")
            else:
                print("Invalid task id")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
