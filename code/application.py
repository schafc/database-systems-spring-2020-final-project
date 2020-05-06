from database import SQLConnectorClass

def main():
	running_program = True
	database_search = SQLConnectorClass("host='localhost' dbname='dbms_final_project' user='dbms_project_user' password='dbms_password'")
	while(running_program == True):
		user_input = input().lower()
		if(user_input == "exit"):
			running_program = False
			print("exiting program")
		elif(user_input == 'menu'):
			print("To exit the program, enter \'exit\'")
			print("------")
			print("Queries - Enter \'query #\', where # is replaced with the number of the query desired, to select a query")
			print("------")
			print("Query 1:")
			print("Query 2:")
			print("Query 3:")
			print("Query 4:")
			print("Query 5:")

		elif(user_input == 'query 1'):
			print("Query 1: This query....")
			print("Enter the name of the location you\'d like to search")
			location = input().upper().replace("'", "''") # protect from SQL injection
			database_search.queryLocation(location)
			print("Query complete, to view other possible queries, enter \'menu\'")

		elif(user_input == 'query 2'):
			print("Query 2: This query....")
			database_search.sortStatesByEvents()
			print("Query complete, to view other possible queries, enter \'menu\'")

		elif(user_input == 'query 3'):
			print("Query 3: This query....")
			print("Enter the name of the event type you\'d like to search")
			event_type = input().upper().replace("'", "''") # protect from SQL injection
			database_search.eventAirInformation(event_type)
			print("Query complete, to view other possible queries, enter \'menu\'")

		elif(user_input == 'query 4'):
			print("Query 4: This query....")
			print("Enter the name of the state you\'d like to search")
			state = input().upper().replace("'", "''") # protect from SQL injection
			database_search.avgTempOfState(state)
			print("Query complete, to view other possible queries, enter \'menu\'")

		elif(user_input == 'query 5'):
			print("Query 5: This query....")
			database_search.sortEvents()
			print("Query complete, to view other possible queries, enter \'menu\'")

		else:
			print("Invalid command. To see a list of commands, enter 'menu'")


if __name__ == "__main__":
	print("Welcome to the storm data and location weather data aplication")
	print("To exit the program, enter \'exit\'. To see the list of queries, enter \'menu\'")
	main()
