from vaccine_alloc_instance import *
from allocation_solution import *
from generators.random_instance_generator_1 import *
from solvers.offline_maxflow_maxutility import *
from solvers.offline_maxutility import *
from solvers.online_maxflow_maxutility import *
from solvers.online_maxutility import *

def main():
	gen1 = RandomInstanceGenerator(number_of_instances=200,
											n=100,c=20,d=20,q=100,
											Q_d_min=1,Q_d_max=25,
											Q_c_min=1,Q_c_max=20,
											p_availability=0.6 )
	instance_list = gen1.generate()

	file = []
	header = "Sl.No, n, c, d, q, Total Flow, Total Utility\n"
	for i in range(4):
		file.append(open("results/Data_"+str(i),'w'))
		file[i].write(header)



	sl_no=0
	for i in instance_list:
		print("\n")
		# i.print_instance()
		sl_no +=1
		LP1 = LPOfflineMaxFlowMaxUtility(i)
		LP2 = LPOfflineMaxUtility(i)
		LP3 = LPOnlineMaxUtility(i)
		LP4 = LPOnlineMaxFlowMaxUtility(i)

		sol1 = LP1.solve()
		data = str(sl_no)+", "+str(i.n)+", "+str(i.c)+", "+str(i.d)+", "+str(i.q)+", "+str(sol1.total_flow)+", "+str(sol1.total_utility)+"\n"
		file[0].write(data)
		sol2 = LP2.solve()
		data = str(sl_no)+", "+str(i.n)+", "+str(i.c)+", "+str(i.d)+", "+str(i.q)+", "+str(sol2.total_flow)+", "+str(sol2.total_utility)+"\n"
		file[1].write(data)
		sol3 = LP3.solve()
		data = str(sl_no)+", "+str(i.n)+", "+str(i.c)+", "+str(i.d)+", "+str(i.q)+", "+str(sol3.total_flow)+", "+str(sol3.total_utility)+"\n"
		file[2].write(data)
		sol4 = LP4.solve()
		data = str(sl_no)+", "+str(i.n)+", "+str(i.c)+", "+str(i.d)+", "+str(i.q)+", "+str(sol4.total_flow)+", "+str(sol4.total_utility)+"\n"
		file[3].write(data)

		# print(np.matrix(i.availability))

		# for j in range(4):
		# 	data = str(sl_no)+", "+str(i.n)+", "+str(i.c)+", "+str(i.d)+", "+str(i.q)+", "+str(sol[j].total_flow)+", "+str(sol[j].total_utility)+"\n"
		# 	file[j].write(data)			

	for j in range(4):
		file[j].close()
if __name__ == '__main__':
	main()