Implement a simulator that simulates a single elevator that operates in a n-floor building.
	● An elevator class
		○ Able to handle requests from multiple floors
		○ Able to fulfill requests “optimally” (Describe your metrics in the submitted code)
		○ Safety features
			■ Maximum capacity
			■ Maximum speed
			■ Emergency stop
	● A customer class
		○ Able to request the elevator from floors
		○ Able to send the elevator
	● A simulator class
		○ Able to simulate up to 50 customers
		○ Can generate a detailed log of the elevator operation
			■ List of requests (with time) made
			■ List of action (with time) the elevator took
			● Test cases
		○ Test capability of fulfilling customer requests
		○ Test safety




This is a readme file for Take Home Coding Test - Single Elevator Project.


The project includes the following files:

Customer.py: Include a Customer class that can send requests from floors
Elevator.py: Include an Elevator class that can handle requests from multiple floors anytime and fulfill requests based on the following metric
			1. The elevator always completes all the requests in the same direction of its motion before fulfill the requests for the opposite direction. 
			For requests of the same direction, the elevator compares the floor that sent the request with the its own current floor and priotize floors that is in its moving direction. 
			For example, if the elevator is at floor 5 and moving up to floor 9. Now it receives a request from floor 8 to floor 11, and a request from floor 3 to floor 6.
			Then the elevator will go to 5 -> 8 -> 9 -> 11 -> 3 -> 6.
			2. If two requests are made at the same time, a request will be randomly selected to be processed.
			3. For overloading situations, customers with later time of requests need to wait for the next elevator.
Simulator.py: Include a Simulator class that eceives requests from customers and send the messages to the elevator, it also enerate a detailed log of the elevator operation.
myqueue.py: Include a myqueue class that represents the data structure of my elevator queue.
config.py: Include all the parameters such as building levels, elevator maximum capacity.
main.py: Read input files, initialize the elevator and simulator object and operate everything.
test.py: Generate test cases/input files. 

Installation:
Python 3.7.3, no other modules needed to be installed 

- How to run the project:
Download the project.
Open the terminal (MacOS), and go to the directory of the project folder, then type in the command:
> python3 main.py
"requests_log.txt" and "actions_log.txt" will be generated as outputs. 
Stop the program by press ctrl+c.
A demo on how to run the project: 

- Run the project with a different set of inputs
"sample_input.csv" was set as the default input file, if you would like to try with other random inputs, you can change the input_file_path variable in "config.py" to a new file name, and uncomment line 9 in "main.py": generate_pseudo_input(building_floors, customer_total_number, end_time, input_file_path) 

- Test with special cases:
	-- overload: set max_capacity in "config.py" to a small value (eg. 3) and run main.py
	-- emergency stop: In this project, I assign floor 0 to be the emergency button, you can either change one floor value (column 3 & 4) from "sample_input.csv" to 0 or change the input_file_path variable in "config.py" to "stop_input.csv" and run main.py, you will see that the elevator stops right after receiving the request from customer 10.




Author: Jijie Zhou# elevator_project_JijieZhou
