import sys
import os 
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from vaccine_alloc_instance import *
import numpy as np
import random

class RandomInstanceGenerator:
	def __init__(self,number_of_instances, n,c,d,q, Q_d_min, Q_d_max, Q_c_min, Q_c_max, p_availability=0.6 ):
		self.number_of_instances = number_of_instances
		self.Q_d_min = Q_d_min
		self.Q_d_max = Q_d_max
		self.Q_c_min = Q_c_min
		self.Q_c_max =Q_c_max
		self.p_availability = p_availability
		self.n = n
		self.c = c
		self.d = d
		self.q = q

	def generate(self):
		random_instances = []
		
		for i in range(self.number_of_instances):	
			availability = [[np.random.choice([0,1], p=[1-self.p_availability, self.p_availability]) for j in range(self.d) ] for i in range(self.n)]
			belongsToCatagory = [[random.randint(0,1) for j in range(self.c)] for i in range(self.n)]
			Q_d = [random.randint(self.Q_d_min,self.Q_d_max) for i in range(self.d)]
			Q_c = [random.randint(self.Q_c_min,self.Q_c_max) for i in range(self.c)]
			Q_cxd = [[random.randint(0,min(Q_d[j],Q_c[i])) for j in range(self.d)] for i in range(self.c)]

			#Setting Utility values
			U_nxd = []
			for i in range(self.n):
				delta=random.random()
				U_nxd.append([1*(delta**i) for i in range(self.d)])

			new_instance = VaccineAllocInstance(self.n,self.c,self.d,self.q,availability,belongsToCatagory,Q_d,Q_c,Q_cxd,U_nxd)
			random_instances.append(new_instance)

		return random_instances