class C1:
	def x(self):
		print(1)
	def y(self):
		print(3)
class C2:
	def x(self):
		print(2)
	def z(self):
		print(4)
class C3(C1, C2):
	def f(self):
		print(5)
xxx = C3()
xxx.x()
xxx.y()
xxx.z()
xxx.f()
