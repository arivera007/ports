###################################################################################
# Interview project for ClearMetal
# Author: Adriana Rivera
# Usage: python task_A_1.1.py
###################################################################################

import task
import os

script_name = os.path.basename(__file__)
a_task = task.AsyncTask(script_name, 'UNLOADING VESSEL')
a_task.queue_task(a_task)
