from math import sqrt
from cvxopt import matrix
from cvxopt.blas import dot
from cvxopt.solvers import qp

class extfuncs(object):
	def __init__(self, upper, lower, setpoint):
		self.upper = upper
		self.lower = lower
		self.setpoint = setpoint

	def scaling_lsw(self, r_list):
		return 1

		#warm up at the first 5 profiling windows
		if len(r_list) < 5:
			return 1

		#set the {lsw = (upper + lower) / 2} at the first
		if len(r_list) == 5:
			return int((self.upper + self.lower) / 2)
			
		if r_list[-1][0] > r_list[-2][0]:
			self.lower = r_list[-1][1]
		else:
			self.upper = r_list[-1][1]
		
		return int((self.upper + self.lower) / 2)

	def DVFS(self, freq_list, util_list, temp_list):
#		return self.bf_solver(freq_list, util_list)
		return self.TA(freq_list, temp_list)

	def qp_solver(self, freq_list, util_list):
		return freq_list

	def bf_solver(self, freq_list, util_list):
		freq_scal = []
		for freq_idx in range(0, len(freq_list)):
			freq_scal.append(util_list[freq_idx] / self.setpoint * freq_list[freq_idx])
		return freq_scal
	
	def TA(self, freq_list, temperature_list):
		freq_scal = []
		for freq_idx in range(0, len(freq_list)):
			freq_scal.append(self.setpoint / temperature_list[freq_idx] * freq_list[freq_idx])
		return freq_scal
