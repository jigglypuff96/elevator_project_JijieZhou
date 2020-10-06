class Customer(object):
	"""
	A class to represent a customer.

	Attributes
	----------
	customerID: int
		An id to represent the customer.

	Methods
	-------
	send_request(request_time, floor_from, floor_to)
		Send a request.

	"""
	def __init__(self, customerID):
		self.customerID = customerID

	def send_request(self, request_time, floor_from, floor_to):
		"""
		Customer senf request at request_time on floor floor_from. 
		Parameters
		----------
		request_time: int
			Time (in second) they send the request.
		floor_from: int
			The floor where the customer send the request (press the button).
		floor_to: int
			The floor where the customer wants to go to (the button they pressed after enter inside the elevator).
		Returns
		-------
		List of information of a request including the request is made, on which floor the customer send the request (press the button), and which floor he/she wants to go to.

		"""
		return [request_time, floor_from, floor_to]