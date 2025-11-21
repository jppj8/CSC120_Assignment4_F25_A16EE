"""
todo.py

A simple todo list module used for Lab Assignment 12.
Global state:
    tasks: dict[int, str]  -> task id to task description
    stats: dict[int, bool] -> task id to completion status (False = incomplete)
"""

tasks = {}
stats = {}
_next_id = 1  # internal counter for unique task IDs


def create_task(description: str) -> int:
    """
    Create a new task with a unique id, mark it incomplete, and return the id.
    """
    global _next_id
    tid = _next_id
    _next_id += 1

    tasks[tid] = description
    stats[tid] = False
    return tid


def show_tasks():
    """
    Print only incomplete tasks.
    """
    print("=== Your Todo List ===")
    for tid in sorted(tasks.keys()):
        if not stats.get(tid, False):
            print(f"{tid}. {tasks[tid]}")


def complete_task(tid: int) -> bool:
    """
    Mark a task complete.
    Return False if task id doesn't exist, True otherwise.
    """
    if tid not in tasks or tid not in stats:
        return False
    stats[tid] = True
    return True


def delete_task(tid: int) -> bool:
    """
    Delete a task from both tasks and stats.
    Return True if deletion happened, False if id not found.
    """
    if tid not in tasks or tid not in stats:
        return False
    del tasks[tid]
    del stats[tid]
    return True


def main():
    """
    Simple menu loop.
    Options expected by tests:
        1 = Show tasks
        2 = Add task
        3 = Complete task
        4 = Delete task
        5 = Quit
    """
    while True:
        choice = input().strip()

        if choice == "1":
            show_tasks()

        elif choice == "2":
            desc = input()
            create_task(desc)

        elif choice == "3":
            try:
                tid = int(input())
            except ValueError:
                continue
            complete_task(tid)

        elif choice == "4":
            try:
                tid = int(input())
            except ValueError:
                continue
            delete_task(tid)

        elif choice == "5":
            break

        else:
            # invalid option, just loop again
            continue


if __name__ == "__main__":
    main()
