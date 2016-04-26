from task import *
from core import *
from hardware import *
from init import *
from extfuncs import extfuncs
import sys
import os

sim_time = 60 * 1000 * 20
upper_bound = 5
lower_bound = 1
lsw = 1
lpw = 50
cur_time = 0
CORES = 4
reliability_list = []

T_setpoint = 60
U_setpoint = 0.66

exp_funcs = extfuncs(upper_bound, lower_bound, T_setpoint)
exp_system = init(CORES, sys.argv[-2])
os.system("cp ./hotspot/hotspot.sample.init ./hotspot/hotspot.init")

#exp_system.print_hardware()

while cur_time < sim_time:
	for core_idx in range(0, CORES):
		exp_system.core_set[core_idx].run(cur_time)

	if cur_time % (lsw * 1000) == 0:
		exp_system.DVFS(lsw, exp_funcs)

	if cur_time % (lsw * lpw * 1000) == 0:
		exp_system.get_temperature()
		reliability_list.append([exp_system.get_reliability(lsw), lsw])
		lsw = exp_funcs.scaling_lsw(reliability_list)

	cur_time += 1

#exp_system.print_hardware()
exp_system.output(sys.argv[-1])
