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
			print("Query 1: Takes a user-input location (typically a town), and returns all weather events that took place at that location")
			print("Query 2: Returns a sorted list of states (and other geographic regions, such as lakes/other bodies of water), sorted by the number of weather events that took place in that area")
			print("Query 3: Takes a weather event type,and returns the average temperature, wind speed, pressure and precipitation for weather events of that type")
			print("Query 4: Takes a state, or other geographic region, and returns the average temperature of that state/region for 2019")
			print("Query 5: Returns a list of information for all events, including event location, average temp on day of event, wind speed, precipitation, visibility, and id of station data was taken at")

		elif(user_input == 'query 1'):
			print("Query 1: This query takes a user-input location (typically a town), and returns all weather events that took place at that location")
			print("Enter the name of the location you\'d like to search")
			location = input().upper()
			database_search.queryLocation(location)
			print("Query complete, to view other possible queries, enter \'menu\'")

		elif(user_input == 'query 2'):
			print("Query 2: This query returns a sorted list of states (and other geographic regions, such as lakes/other bodies of water), sorted by the number of weather events that took place in that area")
			database_search.sortStatesByEvents()
			print("Query complete, to view other possible queries, enter \'menu\'")

		elif(user_input == 'query 3'):
			print("Query 3: This query takes a weather event type,and returns the average temperature, wind speed, pressure and precipitation for weather events of that type")
			print("Enter the name of the weather event type you\'d like to search")
			event_type = input().upper()
			database_search.eventAirInformation(event_type)
			print("Query complete, to view other possible queries, enter \'menu\'")

		elif(user_input == 'query 4'):
			print("Query 4: This query takes a state, or other geographic region, and returns the average temperature of that state/region for 2019")
			print("Enter the name of the state/geographic region you\'d like to search")
			state = input().upper()
			database_search.avgTempOfState(state)
			print("Query complete, to view other possible queries, enter \'menu\'")

		elif(user_input == 'query 5'):
			print("Query 5: This query returns a list of information for all events, including event location, average temp on day of event, wind speed, precipitation, visibility, and id of station data was taken at")
			database_search.sortEvents()
			print("Query complete, to view other possible queries, enter \'menu\'")

		else:
			print("Invalid command. To see a list of commands, enter 'menu'")


if __name__ == "__main__":
	print("Welcome to the storm data and location weather data application")
	print("To exit the program, enter \'exit\'. To see the list of queries, enter \'menu\'")
	main()
