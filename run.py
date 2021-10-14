from vaccine_alloc_instance import *
from allocation_solution import *
from generators.random_instance_generator_1 import *
from solvers.offline_maxflow_maxutility import *
from solvers.offline_maxutility import *
from solvers.online_maxflow_maxutility import *

def main():
	gen1 = RandomInstanceGenerator(number_of_instances=1,
											n=40,c=10,d=10,q=40,
											Q_d_min=1,Q_d_max=25,
											Q_c_min=1,Q_c_max=20,
											p_availability=0.6 )
	instance_list = gen1.generate()

	for i in instance_list:
		i.print_instance()
		offlinemaxflow = LPOfflineMaxFlowMaxUtility(i)
		offline_max_utility = LPOfflineMaxUtility(i)
		onlinemaxflow = LPOnlineMaxFlowMaxUtility(i)
		sol = offlinemaxflow.solve()
		sol2 = offline_max_utility.solve()
		sol3 = onlinemaxflow.solve()
		print(sol.total_flow, sol.total_utility)
		print(sol2.total_flow,sol2.total_utility)
		print(sol3.total_flow,sol3.total_utility)
		# print(np.matrix(sol.Allocation))
		# print(sol.status)

if __name__ == '__main__':
	main()