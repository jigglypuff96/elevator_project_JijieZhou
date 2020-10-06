import threading

class myqueue:
	"""
	A class used to represent the data structure used for the elevator. It can be seen as a priority queue. 

	Attributes
	----------
	order: Boolean
		a boolean variable to tell whether it the queue should be sorted in reversed order
	queue: list
		a queue that represents the sequence of the floors to be visited.
	Methods
	-------
	insert(new_floor_request)
		Insert the floor request received to the current queue.
	next
		Get first element in the queue.
	pop_visited
		Remove the first element in the queue.
	is_empty
		Check if the current queue is empty.
	get_queue
		Print out all the elements in the queue.
	
	"""
	def __init__(self,reverse=False):
		self.order = reverse
		self.queue = []
		# self.lock = threading.Lock()
	def insert(self,new_floor_request):
		"""
		Insert the requested floor number to the current queue, and sorted in the specified order by the first element of the list. 
		Parameters
		----------
		new_floor_request:list of int
			depending on whether the customer is sending the request outside the elevator (the customer is not picked up yet) or 
			inside the elevator (the customer will tell the elevator which floor he/she wants to go)
		"""
		# self.lock.acquire()
		self.queue.append(new_floor_request) 
		self.queue.sort(reverse = self.order)
		# self.lock.release()
	def combine(self, overload_queue):
		"""
		Combine the list of customer requests that failed to complete due to elevator overload into the new queue.
		Parameters
		----------
		overload_queue:list of lists of int
			Customer requests that did not get fulfilled due to elevator overload.
		"""
		for request in overload_queue:
			self.queue.append(request)
		self.queue.sort(reverse = self.order)
	def next(self):
		"""
		Get the next floor to visit. 
		"""
		return self.queue[0]
	def pop_visited(self):
		"""
		Remove the floor just visited from the current queue.
		"""
		# self.lock.acquire()
		if not self.is_empty():
			self.queue.pop(0)
		# self.lock.release()

	def is_empty(self):
		"""
		Get if the queue is empty. 
		"""
		# self.lock.acquire()
		size = len(self.queue)
		# self.lock.release()
		return size==0
	def get_queue(self):
		"""
		Print out the queue including the rest of the floors to be visited. 
		"""
		# self.lock.acquire()
		print ("start queue")
		for i in self.queue:
			print (i[0])
		print ("end queue")
		# self.lock.release()