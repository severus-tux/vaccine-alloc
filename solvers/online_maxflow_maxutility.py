from pulp import *
import sys
import os
import copy
import numpy as np
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from vaccine_alloc_instance import *
from allocation_solution import *

class LPOnlineMaxFlowMaxUtility:
	def __init__(self, vaccine_obj):
		self.vaccine_obj = copy.deepcopy(vaccine_obj)

	def solve(self):

		lmda=0.5*(1/np.sum(self.vaccine_obj.U_nxd))

		#Storing the quotas locally to update after every iteration
		local_q = self.vaccine_obj.q
		local_Q_d = self.vaccine_obj.Q_d.copy()
		local_Q_c = self.vaccine_obj.Q_c.copy()
		local_Q_cxd = self.vaccine_obj.Q_cxd.copy()
		vaccination_status = [False for i in range(self.vaccine_obj.n)]

		#Create a solution instance to keep track of agents who gets vaccinated
		sol = AllocationSolution(self.vaccine_obj.n,self.vaccine_obj.d)

		for d_i in range(self.vaccine_obj.d):
			catagories = ["c_"+str(i) for i in range(self.vaccine_obj.c)]
			agents = []
			for i in range(self.vaccine_obj.n):
				if (self.vaccine_obj.availability[i][d_i]==1 and vaccination_status[i]==False):
					agents.append("a_"+str(i))
			catagory_nodes = ["c_"+str(d_i)+"_"+str(j) for j in range(self.vaccine_obj.c)]
			nodes = ["s","v","d_"+str(d_i)]+catagory_nodes+agents+["t"]

				# supply or demand of nodes
			            #NodeID : [Supply,Demand]
			nodeData = {x:[0,0] for x in nodes}
			nodeData["s"] = [local_q,0]
			nodeData["t"] = [0,local_q]

			# Arcs List
			arcs = [("s","v"),("v","d_"+str(d_i))]

			for j in range(self.vaccine_obj.c):
				arcs.append(("d_"+str(d_i),"c_"+str(d_i)+"_"+str(j)))

			for i in range(self.vaccine_obj.n):
				if (self.vaccine_obj.availability[i][d_i]==1 and vaccination_status[i]==False):
					for k in range(self.vaccine_obj.c):
						if (self.vaccine_obj.belongsToCatagory[i][k]):
							arcs.append(("c_"+str(d_i)+"_"+str(k),"a_"+str(i)))


			for i in range(self.vaccine_obj.n):
				if(vaccination_status[i]==False):
					arcs.append(("a_"+str(i),"t"))

			#Arcs Data
			# arcs cost, lower bound and capacity
			   		#Arc : [Cost,MinFlow,MaxFlow]
			arcData = {("s","v"):[0,0,local_q]}
			arcData[("v","d_"+str(d_i))]=[0,0,local_Q_d[d_i]]

			for j in range(self.vaccine_obj.c):
				arcData[("d_"+str(d_i),"c_"+str(d_i)+"_"+str(j))]=[0,0,local_Q_cxd[j][d_i]]

			for i in range(self.vaccine_obj.n):
				if (self.vaccine_obj.availability[i][d_i]==1 and vaccination_status[i]==False):
					for k in range(self.vaccine_obj.c):
						if (self.vaccine_obj.belongsToCatagory[i][k]):
							arcData[("c_"+str(d_i)+"_"+str(k),"a_"+str(i))]=[self.vaccine_obj.U_nxd[i][d_i],0,1]

			for i in range(self.vaccine_obj.n):
				if(vaccination_status[i]==False):
					arcData[("a_"+str(i),"t")]=[0,0,1]	

			# Splits the dictionaries to be more understandable
			(supply, demand) = splitDict(nodeData)
			(costs, mins, maxs) = splitDict(arcData)

			## BEGIN: Setup LP
			# Creates the boundless Variables as Continues_valued_variables
			vars = LpVariable.dicts("Route",arcs,None,None,cat='Continuous')#LpInteger) 

			# Creates the upper and lower bounds on the variables
			for a in arcs:
			    vars[a].bounds(mins[a], maxs[a])

			##LP
			# Creates the 'prob' variable to contain the problem data    
			prob = LpProblem(name="Online_maxFlow_max_Utility_Qd_Qdxc",sense=LpMaximize)

			# Creates the objective function
			obj = [vars[arcs[0]]]+[vars[a]* costs[a]*lmda for a in arcs[1:]]
			prob += lpSum(obj), "Total Cost of Transport"

			# Creates all problem constraints - this ensures the amount going into each node is equal to the amount leaving
			for k in nodes[1:-1]: #Except for last node node t and first node s
			    prob += (supply[k]+ lpSum([vars[(i,j)] for (i,j) in arcs if j == k]) ==
			             demand[k]+ lpSum([vars[(i,j)] for (i,j) in arcs if i == k])), \
			            "Flow Conservation in Node %s"%k


			# The problem data is written to an .lp file
			# prob.writeLP("simple_MCFP.lp")

			## END: Setup LP
			# The problem is solved using PuLP's choice of Solver
			prob.solve()

			sol.status = prob.status
			sol.total_flow += value(vars[("s","v")])
			local_q = local_q - value(vars[("s","v")])


			for i in range(self.vaccine_obj.n):
				if (self.vaccine_obj.availability[i][d_i]==1 and vaccination_status[i] == False):
					for k in range(self.vaccine_obj.c):
						if (self.vaccine_obj.belongsToCatagory[i][k]==1):
							if ((value(vars[("c_"+str(d_i)+"_"+str(k),"a_"+str(i))]))==1.0):
								sol.Allocation[i][d_i]=k
								sol.total_utility += self.vaccine_obj.U_nxd[i][d_i]
								local_Q_d[d_i] -= 1 
								local_Q_c[k] -= 1 
								local_Q_cxd[k][d_i] -= 1 
								vaccination_status[i] = True
								

			# print("Today's vaccine",value(vars[("s","v")]),value(vars[("v","d_"+str(d_i))]))
			# print("Agents",todays_agents)
			# print("MF: Day: ",d_i,"- utility:",todays_util)

		return sol