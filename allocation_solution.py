class AllocationSolution:
	def __init__(self,n,d):
		self.Allocation = [["X" for j in range(d)] for i in range(n)]
		self.total_flow = 0
		self.total_utility = 0
		self.status = 0