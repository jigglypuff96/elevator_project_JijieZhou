from Simulator import Simulator
from Elevator import Elevator
from config import *
from test import generate_pseudo_input, get_pseudo_input
import csv
def main():

	# #Genereate test cases, uncomment the next line to generate input files with random requests
	# generate_pseudo_input(building_floors, customer_total_number, end_time, input_file_path)

	# Read the input file and get all the customer data
	all_data = get_pseudo_input(input_file_path)
	
	# Initialize the elevator
	my_elevator = Elevator(starting_floor, max_capacity,max_speed,actions_log_file_path)

	# Initialize the simulator
	my_simulator = Simulator(building_floors,my_elevator)

	# Operate the simulator
	my_simulator.operate(all_data, requests_log_file_path)
	
if __name__=='__main__':
	main()