
from task import *

power_par = {0.8010: [0.85, 7.3249, 0.1666, 15], 
             0.8291: [0.90, 8.6126, 0.1754, 15], 
             0.8553: [0.95, 10.238, 0.1846, 15],
             0.8797: [1.00, 12.315, 0.1942, 15],
             0.9027: [1.05, 14.998, 0.2043, 15],
             1.0000: [1.10, 18.497, 0.2149, 15]}

T_amb = 330 - 273.15
R = 0.8
C = 340

class core(object):
	def __init__(self, idx):
		self.core_id = idx
		self.power = []
		self.taskset = []
		self.frequency = 1.0
		self.busy = 0
		self.temperature = T_amb
		self.temperature_list = []
		self.utilization = 0.0

	def print_core(self):
		print "core: " + str(self.core_id) + "\tutilization: " + str(self.utilization) + "\tfrequency: " + str(self.frequency)
		for task in self.taskset:
			task.print_task()

	def run(self, cur_time):
		for task in self.taskset:
			#check whethe current time is the deadline of a task
			if task.deadline == cur_time:
				task.deadline += task.period
				task.completed += 1
				if task.execution > 0:
					task.miss += 1
					# terminate this task
					task.execution = 0 

			#check whether current time is the release time of a task
			if task.release == cur_time:
				task.release += task.period;
				task.execution = task.overhead

		#find the task having highest priority then execute
		h_prio = -1
		for task in self.taskset:
			if task.priority > h_prio and task.execution > 0:
				h_prio = task.priority
				h_task = task

		if h_prio != -1:
			h_task.execution -= self.frequency
			self.busy += 1

	#calculate power at the end of each sampling window
	def get_power(self, lsw):
		self.utilization = float(self.busy) / (lsw * 1000)
		self.busy = 0

		voltage = power_par[self.frequency][0]
		C0 = power_par[self.frequency][1]
		C1 = power_par[self.frequency][2]
		C2 = power_par[self.frequency][3]
		current_power = (C0 + C1 * self.temperature) * voltage + C2 * voltage * voltage * voltage * self.utilization
		self.temperature = self.temperature + (T_amb + R * current_power - self.temperature) / (R * C)
		self.power.append(current_power)

	def set_frequency(self, value):
		if value <= 0.8010:
			self.frequency = 0.8010
		else:
			for freq_candidate in [1.0000, 0.9027, 0.8797, 0.8553, 0.8291, 0.8010]:
				if value > freq_candidate:
					self.frequency = freq_candidate
					break



