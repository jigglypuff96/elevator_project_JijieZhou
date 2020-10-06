from Elevator import Elevator
from Customer import Customer
import threading # CPU bound
import csv
import time
from test import generate_pseudo_input
from config import *

# elevator = Elevator(building_floors,max_capacity,max_speed)


class Simulator(object):
	"""
	A class to represent a simulator for up to 50 customers. 

	Attributes
	----------
	customerID: int
		An id to represent the customer.

	Methods
	-------
	start_elevator
		Start the threading to run the elevator run function in background.
	opeerate
		Take the customer data and operate the elevator 

	"""
	def __init__(self, building_floors, elevator):
		self.building_floors = building_floors
		self.elevator = elevator
		self.threading = threading.Thread(target = self.elevator.run)

	def start_elevator(self):
		"""
		Initiate a threading to run a function in background. 

		"""
		self.threading.start()
		return self.threading

	def operate(self, all_data, requests_log_file_path):
		"""
		Start running the elevator and pass the customer requests to the elevator. 

		Parameters
		----------
			all_data: list of lists of int
				Include data for each customer in a sequence of the time they send the requests.
			requests_log_file_path: str
				File name to save all the requests from customer.
			actions_log_file_path: str
				File name to save all the actions of the elevator.


		"""

		# Open a txt file to log the requests
		requests_log_file_write = open(requests_log_file_path, "w")
		# actions_log_file_write = open(actions_log_file_path, "w")

		customer_index = 0
		# initiate the elevator
		myelevator = self.elevator
		my_thread = self.start_elevator()

		customer_total_number = len(all_data)
		while customer_index < customer_total_number : 
			customerID, request_time, floor_from, floor_to = all_data[customer_index]
			if request_time <= myelevator.time_now:
				# Initialize a Customer object
				user = Customer(customerID)
				# Read customer information from the input data, and then receive requests from the customer
				request_time, floor_from, floor_to = user.send_request(request_time, floor_from, floor_to)
				if floor_to > floor_from:
					move_dir = "up"
				else:
					move_dir = "down"
				requests_log_file_write.write("Customer " + str(customerID) + " sent a " + move_dir + "ward direction request at " + str(request_time) + "s" + " on floor " + str(floor_from) + " and wants to go to floor " + str(floor_to) + " \n")
				# actions_log_file_write.write("At " + str(myelevator.time_now) + "s" + " the elevator is on floor " + str(myelevator.current_floor) + " the customers now inside the elevator are: " + str(myelevator.customer_inside) + " \n")
				try:
					# Send the customer requests to the elevator
					myelevator.push_button(floor_from, user.customerID, floor_to)
					# time.sleep(1)
					customer_index += 1
					if floor_from == 0 or floor_to == 0 or myelevator.switch != "on":
						myelevator.emergency_stop()
						my_thread.join()
						return
				except:
					print("An exception occurred")

		if myelevator.up_queue1.is_empty() and myelevator.down_queue1.is_empty():
			print ("Program finished.")
			myelevator.emergency_stop()
			my_thread.join()
			return
