from vaccine_alloc_instance import *
from allocation_solution import *
from generators.random_instance_generator_1 import *
from generators.random_instance_generator_2 import *
from solvers.offline_maxflow_maxutility import *
from solvers.offline_maxutility import *
from solvers.online_maxflow_maxutility import *
from solvers.online_maxutility import *

def main():
	# gen1 = RandomInstanceGenerator(number_of_instances=1,
	# 										n=4,c=2,d=3,q=4,
	# 										Q_d_min=1,Q_d_max=3,
	# 										Q_c_min=1,Q_c_max=3,
	# 										p_availability=0.6 )
	# instance_list = gen1.generate()

	# # file = []
	# # header = "Sl.No, n, c, d, q, Total Flow, Total Utility\n"
	# # for i in range(4):
	# 	# file.append(open("results/gen_2_Data_"+str(i),'a'))
	# 	# file[i].write(header)




	# sl_no=0
	# # for i in instance_list:
	# 	# print("\n")
	# 	i.print_instance()
	# 	print("\n")
	# 	sl_no +=1
	# 	LP1 = LPOfflineMaxFlowMaxUtility(i)
	# 	LP2 = LPOfflineMaxUtility(i)
	# 	LP3 = LPOnlineMaxUtility(i)
	# 	LP4 = LPOnlineMaxFlowMaxUtility(i)

	# 	sol1 = LP1.solve()
	# 	data = str(sl_no)+", "+str(i.n)+", "+str(i.c)+", "+str(i.d)+", "+str(i.q)+", "+str(sol1.total_flow)+", "+str(sol1.total_utility)+"\n"
	# 	# file[0].write(data)
	# 	print("LPOfflineMaxFlowMaxUtility:\n",data)
	# 	sol2 = LP2.solve()
	# 	data = str(sl_no)+", "+str(i.n)+", "+str(i.c)+", "+str(i.d)+", "+str(i.q)+", "+str(sol2.total_flow)+", "+str(sol2.total_utility)+"\n"
	# 	# file[1].write(data)
	# 	print("LPOfflineMaxUtility:\n",data)
	# 	sol3 = LP3.solve()
	# 	data = str(sl_no)+", "+str(i.n)+", "+str(i.c)+", "+str(i.d)+", "+str(i.q)+", "+str(sol3.total_flow)+", "+str(sol3.total_utility)+"\n"
	# 	# file[2].write(data)
	# 	print("LPOnlineMaxUtility:\n",data)
	# 	sol4 = LP4.solve()
	# 	data = str(sl_no)+", "+str(i.n)+", "+str(i.c)+", "+str(i.d)+", "+str(i.q)+", "+str(sol4.total_flow)+", "+str(sol4.total_utility)+"\n"
	# 	# file[3].write(data)
	# 	print("LPOnlineMaxFlowMaxUtility:\n",data)

	# 	# print(np.matrix(i.availability))

		# for j in range(4):
		# 	data = str(sl_no)+", "+str(i.n)+", "+str(i.c)+", "+str(i.d)+", "+str(i.q)+", "+str(sol[j].total_flow)+", "+str(sol[j].total_utility)+"\n"
		# 	file[j].write(data)			

	# for j in range(4):
		# file[j].close()


		fixed_instance = VaccineAllocInstance(n=2,c=1,d=2,q=2,availability=[[1,1],[1,0]],
											belongsToCatagory=[[1],[1]],Q_d=[1,1],Q_c=[2],
											Q_cxd=[[1,1]],U_nxd=[[1,0.5],[1,0]])

		fixed_instance.print_instance()

		LP1 = LPOfflineMaxFlowMaxUtility(fixed_instance)
		LP2 = LPOfflineMaxUtility(fixed_instance)
		LP3 = LPOnlineMaxUtility(fixed_instance)
		LP4 = LPOnlineMaxFlowMaxUtility(fixed_instance)

		sol1 = LP1.solve()
		sol2 = LP2.solve()
		sol3 = LP3.solve()
		sol4 = LP4.solve()

		print("\nLPOfflineMaxFlowMaxUtility")
		print(str(fixed_instance.n)+", "+str(fixed_instance.c)+", "+str(fixed_instance.d)+", "+str(fixed_instance.q)+", "+str(sol1.total_flow)+", "+str(sol1.total_utility)+"\n")
		print("LPOfflineMaxUtility")
		print(str(fixed_instance.n)+", "+str(fixed_instance.c)+", "+str(fixed_instance.d)+", "+str(fixed_instance.q)+", "+str(sol2.total_flow)+", "+str(sol2.total_utility)+"\n")
		print("LPOnlineMaxUtility")
		print(str(fixed_instance.n)+", "+str(fixed_instance.c)+", "+str(fixed_instance.d)+", "+str(fixed_instance.q)+", "+str(sol3.total_flow)+", "+str(sol3.total_utility)+"\n")
		print("LPOnlineMaxFlowMaxUtility")
		print(str(fixed_instance.n)+", "+str(fixed_instance.c)+", "+str(fixed_instance.d)+", "+str(fixed_instance.q)+", "+str(sol4.total_flow)+", "+str(sol4.total_utility)+"\n")




if __name__ == '__main__':
	main()