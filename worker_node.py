import time
import random
from task_queue import TaskQueue

class WorkerNode:
    def __init__(self):
        self.task_queue = TaskQueue()

    def execute_task(self, task):
        # Simulate task execution
        print(f"Executing task: {task}")
        time.sleep(random.randint(1, 5))
        print(f"Task {task} completed")

    def run(self):
        while True:
            task = self.task_queue.get_task()
            if task:
                self.execute_task(task)
            else:
                print("No tasks in queue. Waiting...")
                time.sleep(5)

if __name__ == "__main__":
    worker = WorkerNode()
    worker.run()
