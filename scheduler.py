import time
from task_queue import TaskQueue
import schedule

class Scheduler:
    def __init__(self):
        self.task_queue = TaskQueue()

    def add_task(self, task):
        self.task_queue.add_task(task)
        print(f"Scheduled task: {task}")

    def schedule_task(self, task, interval):
        schedule.every(interval).seconds.do(self.add_task, task)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.schedule_task("Sample Task", 10)
    scheduler.run()
