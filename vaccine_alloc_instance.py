class VaccineAllocInstance:
	def __init__(self,n,c,d,q,availability,belongsToCatagory,Q_d,Q_c,Q_cxd,U_nxd):
		self.n = n #Number of agents
		self.c = c #Number of catagories
		self.d = d #Numenr of days
		self.q = q #Total Vaccines
		self.availability = availability
		self.belongsToCatagory = belongsToCatagory
		self.Q_d = Q_d
		self.Q_c = Q_c
		self.Q_cxd = Q_cxd
		self.U_nxd = U_nxd