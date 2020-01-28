class Vehicle(object):
	def __init__(self,location,velocity,acceleration):
		self.location=location
		self.velocity=velocity
		self.acceleration=acceleration

	def update(self):
		self.velocity.add(acceleration)
		self.velocity.limit()
