from vaccine_alloc_instance import *
from allocation_solution import *
from generators.random_instance_generator_1 import *
from solvers.offline_maxflow_maxutility import *

def main():
	gen1 = RandomInstanceGenerator(number_of_instances=1,
											n=20,c=3,d=5,q=20,
											Q_d_min=2,Q_d_max=5,
											Q_c_min=1,Q_c_max=6,
											p_availability=0.6 )
	instance_list = gen1.generate()

	for i in instance_list:
		offlinemaxflow = LPOfflineMaxFlowMaxUtility(i)
		sol = offlinemaxflow.solve()
		print(sol.total_flow, sol.total_utility)
		print(np.matrix(sol.Allocation))
		print(sol.status)

if __name__ == '__main__':
	main()