class tick_update():
	
	def __init__(self, hive, tick):
		self._hive = hive
		self._tick = tick

	def caller(self):
		self.update_hive()

	def update_hive(self):

		self._hive.ressource_gain("honey", self._tick)