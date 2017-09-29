class GoogleIdNeTrovita(Exception):
	def __init__(self, message):
		super().__init__(message)
		self.message = str(message)


class RetposxtoPrenita(Exception):
	def __init__(self, message):
		super().__init__(message)
		self.message = str(message)


class RetposxtoNeEnUzo(Exception):
	def __init__(self, message):
		super().__init__(message)
		self.message = str(message)


class NevalidaUzantoId(Exception):
	def __init__(self, message):
		super().__init__(message)
		self.message = str(message)


class NevalidaPasvorto(Exception):
	def __init__(self, message):
		super().__init__(message)
		self.message = str(message)


class NevalidaRetpoŝto(Exception):
	def __init__(self, message):
		super().__init__(message)
		self.message = str(message)
