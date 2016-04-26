exec_list = {"susan": 58.5,
			 "qsort": 89.5,
             "bitcount": 397.0, 
             "sha": 27.5, 
             "stringsearch": 5.0, 
             "blowfish": 608.5, 
             "cjpeg": 54.5, 
             "CRC32": 377.5,
             "dijkstra": 61.5,
             "patricia": 229.0}

class task(object):
	def __init__(self, task_name):
		self.name = task_name[0: -1]
		self.overhead = exec_list[self.name]
		self.execution = 0.0
		self.deadline = -1
		self.period = -1
		self.priority = -1
		self.release = -1
		self.core = -1
		self.completed = 0
		self.miss = 0

	def print_task(self):
		print "name: " + self.name \
		    + "\texec: " + str(self.execution) \
		    + "\tdeadline: " + str(self.deadline) \
		    + "\tperiod: " + str(self.period) \
		    + "\trelease: " + str(self.release) \
		    + "\tpriority: " + str(self.priority) \
		    + "\tmiss: " + str(self.miss) \
		    + "\tcompleted: " + str(self.completed)