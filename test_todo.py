import unittest
from io import StringIO
from unittest.mock import patch
import todo


class TestTodoState(unittest.TestCase):
    def setUp(self):
        todo.tasks.clear()
        todo.stats.clear()

    # ---------- create_task ----------
    def test_create_single_task(self):
        tid = todo.create_task("Read book")
        self.assertEqual(tid, 1)
        self.assertIn(tid, todo.tasks)
        self.assertFalse(todo.stats[tid])

    def test_create_multiple_tasks_id_increment(self):
        t1 = todo.create_task("Task 1")
        t2 = todo.create_task("Task 2")
        t3 = todo.create_task("Task 3")
        self.assertEqual(t2, t1 + 1)
        self.assertEqual(t3, t2 + 1)
        self.assertEqual(len(todo.tasks), 3)

    # ---------- show_tasks ------------
    def test_show_tasks_output(self):
        t1 = todo.create_task("Task 1")
        t2 = todo.create_task("Task 2")
        t3 = todo.create_task("Task 3")

        todo.complete_task(t2)

        with patch("sys.stdout", new_callable=lambda: StringIO()) as fake_out:
            todo.show_tasks()
            output = fake_out.getvalue()

        self.assertIn("=== Your Todo List ===", output)
        self.assertIn("Task 1", output)
        self.assertIn("Task 3", output)
        self.assertNotIn("Task 2", output)

    # ---------- complete_task ----------
    def test_complete_valid_task(self):
        tid = todo.create_task("Task A")
        result = todo.complete_task(tid)
        self.assertTrue(result)
        self.assertTrue(todo.stats[tid])

    def test_complete_invalid_task(self):
        result = todo.complete_task(999)
        self.assertFalse(result)

    def test_complete_task_already_completed(self):
        tid = todo.create_task("Task B")
        todo.complete_task(tid)
        result = todo.complete_task(tid)
        self.assertTrue(result)
        self.assertTrue(todo.stats[tid])

    # ---------- delete_task ----------
    def test_delete_valid_task(self):
        tid = todo.create_task("Task C")
        result = todo.delete_task(tid)
        self.assertTrue(result)
        self.assertNotIn(tid, todo.tasks)
        self.assertNotIn(tid, todo.stats)

    def test_delete_invalid_task(self):
        result = todo.delete_task(42)
        self.assertFalse(result)

    def test_delete_task_already_deleted(self):
        tid = todo.create_task("Task D")
        todo.delete_task(tid)
        result = todo.delete_task(tid)
        self.assertFalse(result)

    # ---------- main menu: add & show ----------
    def test_main_add_and_show(self):
        inputs = ["2", "Task 1", "2", "Task 2", "1", "5"]
        with patch("builtins.input", side_effect=inputs):
            todo.main()

        self.assertIn(1, todo.tasks)
        self.assertIn(2, todo.tasks)
        self.assertEqual(todo.tasks[1], "Task 1")
        self.assertEqual(todo.tasks[2], "Task 2")
        self.assertFalse(todo.stats[1])
        self.assertFalse(todo.stats[2])

        incomplete_tasks = [tid for tid, done in todo.stats.items() if not done]
        self.assertListEqual(incomplete_tasks, [1, 2])

    # ---------- main menu: complete & delete ----------
    def test_main_complete_and_delete(self):
        inputs = [
            "2",
            "Task 1",
            "2",
            "Task 2",
            "3",
            "1",
            "4",
            "2",
            "1",
            "5",
        ]
        with patch("builtins.input", side_effect=inputs):
            todo.main()

        self.assertIn(1, todo.tasks)
        self.assertTrue(todo.stats[1])

        self.assertNotIn(2, todo.tasks)
        self.assertNotIn(2, todo.stats)

        incomplete_tasks = [tid for tid, done in todo.stats.items() if not done]
        self.assertListEqual(incomplete_tasks, [])

    # ---------- edge cases ----------
    def test_task_ids_after_deletion(self):
        t1 = todo.create_task("A")
        t2 = todo.create_task("B")
        todo.delete_task(t1)
        t3 = todo.create_task("C")
        self.assertEqual(t3, max(todo.tasks.keys()))

    def test_no_duplicate_task_ids(self):
        ids = [todo.create_task(f"Task {i}") for i in range(5)]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()