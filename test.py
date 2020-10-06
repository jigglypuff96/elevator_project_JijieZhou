import random
import csv

def generate_pseudo_input(building_floors, customer_total_number, end_time, input_file_path):
	"""
	A function that generates an input file (csv file) for the project file. 
	The data generated is in the format of: customerID, request_time, floor where the request was sent, customer's destiny floor.
	Assumption
	----------
	The customer does not go to floor x from floor x (same floor).

	Parameters
	----------
	building_floors: int
		Highest level the customer can be at.
	customer_total_number: int
		Total number of customers.
	end_time: int
		The time range (in second) of all the requests.
	input_file_path: str
		The file name of the generated input data.
	"""
	starting_time = 1
	ending_time = end_time
	step = 1
	limit = customer_total_number
	random_requested_time_list = sorted([random.randrange(starting_time, ending_time, step) for iter in range(limit)])
	with open(input_file_path, mode='w') as customer_file:
		for i in range(customer_total_number):
			customer_writer = csv.writer(customer_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			customer_writer.writerow([i+1, random_requested_time_list[i]]+ random.sample(range(1, building_floors + 1), 2))

def get_pseudo_input(input_file_path):
	"""
	Read the data from the file and convert all the string values to integer.
	Get the input data.

	Parameters
	----------
	input_file_path: str
		The file name of the input.
	"""
	with open(input_file_path,"r") as csv_file:
		input_data=list(csv.reader(csv_file, delimiter=','))
	all_data = []
	for user_data in input_data:
		all_data.append([int(i) for i in user_data])
	return all_data
