###################################################################################
# Interview project for ClearMetal
# Author: Adriana Rivera
# Usage: python task_B_1.py
###################################################################################

import task
import os

script_name = os.path.basename(__file__)
a_task = task.RecurTask(script_name, 'CHECKING FOR VESSEL', 3)
a_task.queue_task(a_task)
