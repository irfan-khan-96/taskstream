import redis

# TaskQueue class to add and get tasks from the queue
class TaskQueue:
    def __init__(self, queue_name='task_queue'):
        self.queue_name = queue_name
        self.redis_conn = redis.Redis(host='localhost', port=6379, db=0)
    
    def add_task(self, task):
        self.redis_conn.rpush(self.queue_name, task)
    
    def get_task(self):
        task = self.redis_conn.blpop(self.queue_name)
        if task:
            return task[1].decode('utf-8')
        return None
