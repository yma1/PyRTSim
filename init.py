from hardware import *
from core import *
from task import *

def init_task(file_path):
	taskset = []

	conf_file = open(file_path, "r")
	line = conf_file.readline()
	while line != "":
		if line == '\n' or line[0] == '#':
			line = conf_file.readline()
			continue
			
		key = line.split(':')[0]
		value = line.split(':')[1]
		if key == "name":
			new_task = task(value)
			taskset.append(new_task)
		if key == "priority":
			new_task.priority = int(value)
		if key == "deadline":
			new_task.deadline = int(value) + new_task.release
		if key == "period":
			new_task.period = int(value)
		if key == "release":
			new_task.release = int(value)
		if key == "cpu":
			new_task.cpu = int(value)

		line = conf_file.readline()
	conf_file.close()
	return taskset

def init_hardware(cores):
	hardware_platform = hardware(cores)
	return hardware_platform

def init(cores, file_path):
	exp_system = init_hardware(cores)
	taskset = init_task(file_path)
	for task in taskset:
		exp_system.core_set[task.cpu].taskset.append(task)

#	exp_system.print_hardware()

	return exp_system