class A ():
	def __init__(self,n):
		self.n=n


class B(A):
	def __init__(self,n,roll):
		self.roll=roll


		A.__init__( self,  n)


	def show ( self ):
		print(self.n)
		print(self.roll)


s=B("Rahul", 23)

s.show()
