###################################################################################
# Interview project for ClearMetal
# Author: Adriana Rivera
# Purpose: Main System running a singleton for the port.
# Usage: "python port.py", once started, enter script filename when asked.
# If task_B_1.py is run, it needs to be exit manually. It launches a timer for recurring tasks, but do not start a separate thread.
###################################################################################

import task
import subprocess
import sched, time

class Port():
    class __Port():                             # Created a singleton to have only one port.
        def __init__(self, pool_size=100):
            #self.pool = None * pool_size       # If I were to cap pool size we can do it like this.
            self.pool = []
            self.tasks_handled = {}
            self.timer = sched.scheduler(time.time, time.sleep)      # Interrupting timer for recurring tasks
            
        def __str__(self):
            return repr(self)

        def queue_task(self, running_task):
            task_group = 'A'                     # If I had more groups of task with dependencies, they would have a wunique grouptype
            self.tasks_handled[task_group] = self.tasks_handled.get(task_group, None)
            if running_task.dependency == None or self.tasks_handled[task_group] == running_task.dependency:
                # self.pool.append(task)        # If I had it in Asynch mode. This would be the task queue
                running_task.run_task()
                self.tasks_handled[task_group] = running_task.curr_task         # To check dependency for next task
                if type(running_task) is task.RecurTask:                        # If task is class that auto-occur, then I set a timer to call it again later.
                    self.timer.enter(running_task.timer, 1, self.run_sched_task, (running_task.curr_task,))
                    self.timer.run()                                            # Should run in a separate thread.                
            else:
                running_task.terminate("To run this task, you need to run first: " + running_task.dependency)
                
        def run_sched_task(self, script_name):
            print script_name
            proc1 = subprocess.Popen(['python', script_name])
            proc1.wait()
                
        def dispatch_tasks(self):                   # Doesn't do anythong for now. Single threaded.
            while len(self.pool) > 0:
                task = self.pool.pop(0)

    instance = None
    
    def queue_task(self, task):
        self.instance.queue_task(task)
        
    
    def __init__(self):
        if not Port.instance:
            Port.instance = Port.__Port()
            
            
if __name__== "__main__":
    port = Port()
    while True:
        task_name = raw_input("Enter filename for task: ")
        if task_name != 'exit':
            proc1 = subprocess.Popen(['python', task_name])
            proc1.wait()
            #port.dispatch_tasks()                  # If it was multithreaded, I would add the task here.
        else:
            break

    
            