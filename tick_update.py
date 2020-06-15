class tick_update():
	
	def __init__(self, hive, tick):
		self._hive = hive
		self._tick = tick

	def caller(self):
		self.update_hive()

	def update_hive(self):
		if self._hive.ressource()["honey"] >= 0:
			self._hive.ressource_gain("honey", self._tick)
		if self._hive.ressource()["honey"] < 0:
			self._hive.ressource()["honey"] = 0
		
		if self._hive.ressource()["water"] >= 0:
			self._hive.ressource_gain("water", self._tick)
		if self._hive.ressource()["water"] < 0:
			self._hive.ressource()["water"] = 0
		
		if self._hive.ressource()["metal"] >= 0:
			self._hive.ressource_gain("metal", self._tick)
		if self._hive.ressource()["metal"] < 0:
			self._hive.ressource()["metal"] = 0
		
		if self._hive.ressource()["uranium"] >= 0:
			self._hive.ressource_gain("uranium", self._tick)
		if self._hive.ressource()["uranium"] < 0:
			self._hive.ressource()["uranium"] = 0
		
		if self._hive.ressource()["pollen"] >= 0:
			self._hive.ressource_gain("pollen", self._tick)
		if self._hive.ressource()["pollen"] < 0:
			self._hive.ressource()["pollen"] = 0