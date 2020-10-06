from myqueue import myqueue
import time
class Elevator:
	"""
	A class to represent a single elevator that can handle requests from multiple floors and meet certain features
	*Optimization
	------------
	The elevator is optimized based on the direction and time the request is received.
	It follows the following rules:
		1. It will complete all the requests in the same direction of its motion before fulfill the requests for the opposite direction. 
		2. For requests of the same direction, the elevator will complete the requests based on the time of the request and the total distance it needs to move. 

		For example, if the elevator is at floor 5 and moving up to floor 9. Now it receives a request from floor 8 to floor 11, and then a request from floor 3 to floor 6.
		Then the elevator will go to 5 -> 8 -> 9 -> 11 -> 3 -> 6.


	Attributes
	----------
	current_floor: int
		Starting floor of the elevator. 
	max_capacity: int
		Represents the maximum number of customers that could stay inside the elevator at the same time. 
	max_speed: int
		Represents the speed the elevator moves up/down. Its unit is second/level.
	actions_log_file_write:
		The path of the elevator actions log.
	direction: str
		"up" indicates the elevator is moving up, and "down" indicates the elevator is moving down. 
	current_floor: int
		Represents the floor the elevator is at. 
	up_queue1: myqueue
		Represents the current queue of floor requests with upward direction. For example a customer who wants to move from floor 2 to floor 4 will be includede here.
	down_queue1: myqueue
		Represents the current queue of floor requests with downward direction. For example a customer who wants to move from floor 4 to floor 2 will be includede here.
	up_queue2: myqueue
		Represents the next queue of floor requests with upward direction. 
		For example, if the elevator is at floor 5 and moving up, now it receives a customer request from floor 2 and moving upward, then the request will be included here.
	down_queue2: myqueue
		Represents the next queue of floor requests with upward direction. 
		For example,if the elevator is at floor 5 and moving down, now it receives a customer request from floor 6 and moving downward, then the request will be included here.
	population: int
		Number of customers inside the elevator.
	customer_inside: list of int
		Shows the list of customer id to represent customers that are inside the elevator
	time_now: int
		Keeps track of the elevator operating time.
	increment: int 
		1 represents 1 floor up, -1 represents 1 floor down.
	message: str
		Log information.
	switch: str
		Whethere the elevator should be running.

	
	Methods
	-------
	emergency_stop
		Send the elevator.
	update_level_and_time


	"""
	def __init__(self,starting_floor, max_capacity, max_speed, actions_log_file_path):
		self.current_floor = starting_floor
		self.max_capacity = max_capacity
		self.max_speed = max_speed
		self.actions_log_file_write = open(actions_log_file_path, "w")

		self.direction = "up"

		self.up_queue1 = myqueue()
		self.down_queue1 = myqueue(True)
		self.up_queue2 = myqueue()
		self.down_queue2 = myqueue(True)
		
		self.population = 0
		self.customer_inside = []

		
		self.time_now = 0
		self.increment = 0

		self.message = ""

		self.switch = "on"

	def emergency_stop(self):
		"""
		Turn swtich off to stop the elevator.
		"""
		self.switch="off"
		self.message = "EMERGENCY STOP! \n"
		self.log_actions()
	def update_level_and_time(self,increment = 0, wait_time = 0):
		"""
		Update the time and level of the elevator and send the log the information.

		Parameters
		----------
		increment: int
			1 for moving up, -1 for moving down. Default is 0
		wait_time: int
			If there is no floor requests, the elevator will be waiting according to wait_time. The default value is 0 (not waiting).
		"""
		if wait_time != 0:
			self.time_now += wait_time
		else:
			self.time_now += self.max_speed
			self.current_floor += increment
		self.move_message()

	def log_actions(self):
		"""
		Log current message into actions log file.
		"""
		self.actions_log_file_write.write(self.message)
		# self.actions_log_file_write.write("up_queue1 = " + str(self.up_queue1.queue) + "\n")
		# self.actions_log_file_write.write("down_queue1 = " + str(self.down_queue1.queue)+ "\n")
		# self.actions_log_file_write.write("up_queue2 = " + str(self.up_queue2.queue)+ "\n")
		# self.actions_log_file_write.write("down_queue2 = " + str(self.down_queue2.queue)+ "\n")

	def move_message(self):
		"""
		Update the message accroding to the current state of the elevator.
		"""
		self.message = "At " + str(self.time_now) + "s" + " the elevator is on floor " + str(self.current_floor) + ". " +"Customers now inside the elevator are: " + str(self.customer_inside) + " \n"
		self.log_actions()

	def overload_message(self):
		"""
		If overloading occurs, the message will ask the customer to step out of the elevator into the lobby and wait for the next elevator.
		"""
		self.message = "The elevator is overloaded, please wait for the next one. \n"
		self.log_actions()

	def push_button(self, floor_from, customerID, floor_to):
		"""
		Receive floor requests and insert requests accordingly to 4 different queues specified in the docstring of elevator class.
		
		Parameters
		----------
		floor_from: int
			Represents the floor where the customer sent the request.
		customerID: int
			Represents the customer
		floor_to:
			Represents the floor the customer wants to go to.
		"""

		# Button 0 represents the emergency button.
		if floor_from == 0 or floor_to == 0:
			self.emergency_stop()

		print ("Received a request from customer ", customerID)


		# Get the direction from the customer request.
		if floor_to > floor_from:
			direction = "up"
			
		elif floor_to < floor_from:
			direction = "down"

		customer_request_information = [floor_from,customerID,floor_to]


		if direction == "up" and self.direction == "up":
			if not self.up_queue1.is_empty() and self.current_floor >= floor_from:
				# For example, customer pressed upward button at floor 5, and the elevator is at floor 6 and moving up
				self.up_queue2.insert(customer_request_information)
			else:
				## For example, customer pressed upward button at floor 5, and the elevator is at floor 3 and moving up
				self.up_queue1.insert(customer_request_information)

		if direction == "down" and self.direction == "down":
			if not self.down_queue1.is_empty() and self.current_floor <= floor_from:
				# For example, customer pressed downward button at floor 5, and the elevator is at floor 4 and moving down
				self.down_queue2.insert(customer_request_information)
			else:
				# For example, customer pressed downward button at floor 5, and the elevator is at floor 6 and moving down
				self.down_queue1.insert(customer_request_information)

		if direction == "down" and self.direction =="up":
			# For example, customer pressed downward button at floor 5, and the elevator is at floor x and moving up
			self.down_queue1.insert(customer_request_information)

		if direction == "up" and self.direction =="down":
			# For example, customer pressed upward button at floor 5, and the elevator is at floor x and moving down
			self.up_queue1.insert(customer_request_information)

		"""
		If the elevator just finished all the requests in a queue, and is about to fulfill requests in the next queue, then the elevator is in the transition period.
		"""
		# The elevator just finished a queue of requests of moving down, and is about to execute next available queue of requests of moving up. 
		if self.direction == "transition_up" and direction == "up":
			if floor_from < self.up_queue1.next()[0]:
				# The elevator just finished a downward queue and stopped at level 5, and is about to execute the upward queue starting from level 3. 
				# When it's moving from 5 to 3 (downward) for the  upward queue, a customer sent a request on floor 2 and wants to move up, then it will be included to the next upward queue.
				self.up_queue2.insert(customer_request_information)
			else:
				# The elevator just finished a downward queue and stopped at level 5, and is about to execute the upward queue starting from level 3. 
				# When it's moving from 5 to 3 (downward) for the  upward queue, a customer sent a request on floor 4 and wants to move up, then it will be included to this upward queue.
				self.up_queue1.insert(customer_request_information)

		if self.direction == "transition_up" and direction == "down":
			# The elevator and customer wants to move in different directions, therefore just insert the request to the queue of opposite direction.
			self.down_queue1.insert(customer_request_information)
	
		if self.direction == "transition_down" and direction == "down":
			if floor_from > self.down_queue1.next()[0]:
				# The elevator just finished an upward queue and stopped at level 15, and is about to execute the downward queue starting from level 17. 
				# When it's moving from 15 to 17 (upward) for the downward queue, a customer sent a request on floor 18 and wants to move down, then it will be included to the next downward queue.
				self.down_queue2.insert(customer_request_information)
			else:
				# The elevator just finished an upward queue and stopped at level 15, and is about to execute the downward queue starting from level 17. 
				# When it's moving from 15 to 17 (upward) for the downward queue, a customer sent a request on floor 16 and wants to move down, then it will be included to this downward queue.
				self.down_queue1.insert(customer_request_information)
				
		if self.direction == "transition_down" and direction == "up":
			# The elevator and customer wants to move in different directions, therefore just insert the request to the queue of opposite direction.
			self.up_queue1.insert(customer_request_information)


	def handle_queue(self, queue, increment):
		"""
		Elevator moves up/down and let customers come in/out according to the queue.

		Parameters
		----------
		queue: myqueue
			A queue of customer requests.
		increment: int
			1 for moving up, -1 for moving down.
		"""

		# If emergency stop is pressed, stop the program
		if self.switch != "on":
			return

		print ("Elevator now on floor ",self.current_floor, " and  time is ", self.time_now)
		self.move_message()

		# Initialize a list for floors that may encounter overloading issue.
		overload_floors = []

		while not queue.is_empty():
			# If emergency stop is pressed, stop the program
			if self.switch != "on":
				return
			print ("The next floor to be visited in the queue is = ", queue.next()[0])
			print ("The queue is = ",queue.queue)

			# move up/down to reach the next floor request in the queue
			while self.current_floor != queue.next()[0] and self.switch == "on":
				print ("elevator now on floor ",self.current_floor, " and  time is ", self.time_now)
				self.move_message()
				time.sleep(1)
				self.update_level_and_time(increment)
			print ("elevator arrives at floor ",self.current_floor, " and  time is ", self.time_now)

			"""
			When the customer sent the request, a list of 3 elements including the floor that the customer is at, the customer id, and the destiny floor.
			However, the information of the destiny floor will not be processed until the elevator reaches the floor the customer is at to pick up the customer.
			Once the elevator picks up the customer, it will pop the list of 3 elements and insert a list of 2 elements that only include the destiny floor and the customer ID.
			So we pop and insert elements from the queue according to different situations. 
			One other situation is that, the elevator is empty and it's moving up/down because it's going to execute the next available queue, in this case the request does not 
			come from the customer, so it will only contain 1 element, which is the floor the elevator is moving to. 
			"""
			# 1 element
			if len(queue.next()) == 1 and self.switch == "on":
				queue.pop_visited()
			# 2 elements
			elif len(queue.next()) == 2 and self.switch == "on":
				self.population -= 1
				self.customer_inside.remove(queue.next()[1])
				self.message = "Customer " + str(queue.next()[1]) + " on floor " + str(queue.next()[0]) + " gets off the elevator.  \n"
				self.log_actions()
				print (self.message)
				queue.pop_visited()
			# 3 elements
			else: 
				if self.switch != "on":
					return
				# Before letting the customer enter inside the elevator, check if it will cause the overloading issue.
				if self.population < self.max_capacity:
					self.population += 1

					customer_now, goto_floor = queue.next()[1:]

					self.customer_inside.append(customer_now)
					self.message = "Customer " + str(queue.next()[1]) + " on floor " + str(queue.next()[0]) + " get on the elevator. \n"
					self.log_actions()
					print (self.message)

					queue.pop_visited()
					queue.insert([goto_floor,customer_now])
				else:
					print ("OVERLOAD")
					self.overload_message()
					# If the elevator is already full, remove the request from the current queue, and save it to a temporary list. 
					# Repeat the process until someone get off the elevator. (request with only 2 elements)
					while len(queue.next()) != 2:
						overload_floors.append(queue.next())
						self.message = "Customer " + str(queue.next()[1]) + " on floor " + str(queue.next()[0]) + " need to wait for the next elevator. \n"
						self.log_actions()
						print (self.message)
						queue.pop_visited()

		print ("Customers inside the elevator: ", self.customer_inside)

		# If emergency stop is pressed, stop the program
		if self.switch != "on":
			return
		# Update all 4 queues
		if queue == self.up_queue1:
			self.up_queue2.combine(overload_floors)
			self.up_queue1 = self.up_queue2
			self.up_queue2 = myqueue()

		elif queue == self.down_queue1 and self.down_queue2:
			self.down_queue2.combine(overload_floors)
			self.down_queue1 = self.down_queue2
			self.down_queue2 = myqueue(True)




	def run(self):
		"""
		Always check if there is a queue of requests need to be processed.
		"""
		while self.switch=="on":
			# No requests
			if self.up_queue1.is_empty() and self.down_queue1.is_empty():
				self.update_level_and_time(increment = 0, wait_time = 1)
				time.sleep(1)
				# print("The elevator is waiting and the time now is ", self.time_now)
				continue

			# Initialize a temporary queue for the elevator to move from the floor it stops at to the beginning floor of the next queue
			temp = myqueue()

			if not self.up_queue1.is_empty():
				# If the elevator needs to move downward first to reach the first floor in its upward queue
				if self.current_floor > self.up_queue1.next()[0]:
					temp.insert([self.up_queue1.next()[0]])
					self.direction = "transition_up"
					self.handle_queue(temp, -1)
				self.direction = "up"
				self.handle_queue(self.up_queue1, 1)

			if not self.down_queue1.is_empty():
				# If the elevator needs to move upward first to reach the first floor in its downward queue
				if self.current_floor < self.down_queue1.next()[0]:
					temp.insert([self.down_queue1.next()[0]])
					self.direction = "transition_down"
					self.handle_queue(temp,+1)
				self.direction = "down"
				self.handle_queue(self.down_queue1, -1)
