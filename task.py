###################################################################################
# Interview project for ClearMetal
# Author: Adriana Rivera
# Purpose: Class declarations for Tasks
###################################################################################

import port
import os

class Task(object):
    def __init__(self):
        self.port = port.Port()
        self.dependency = None
        self.timer = 0
        self.curr_task = None
        self.action = "Using Port"
        
    def queue_task(self, task_info):
        print self.port
        print self.port.instance
        response = self.port.queue_task(task_info)
        if response != "Ok":
            print response
            
    def run_task(self):
        print self.action
        
    def terminate(self, msg):
        print msg
        

class AsyncTask(Task):
    def __init__(self, curr_task, action, dependency_value = None):
        Task.__init__(self)
        self.curr_task = curr_task
        self.dependency = dependency_value
        self.action = action

class RecurTask(Task):
    def __init__(self, curr_task, action, timer_value = 0, dependency_value = None):
        Task.__init__(self)
        self.curr_task = curr_task
        self.dependency = dependency_value
        self.timer = timer_value
        self.action = action
        


