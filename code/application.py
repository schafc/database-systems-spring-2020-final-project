import psycopg2

class SQLConnecterClass():
    
    def __init__(self, connection_string):
        # connection_string = "host='localhost' dbname='dbms_final_project' user='dbms_project_user' password='dbms_password'"
        self.conn = psycopg2.connect(connection_string)
    
    # Query : Retrieve events for a location 
    # Input : location 
    # Output: returns all events in that location 
    def queryLocation(self, location):
        pass
        
    # Query : sort states by # of events 
    # Input : None
    # Output: Output count of events for each state sorted 
    def sortStatesByEvents(self):
        pass
        
    # Query : Event air quality information for an event_type
    # Input : Event_type
    # Output: Return average values from AirQuality table for that event_type
    def eventAirInformation(self, event_type):
        pass
    
    # Query : Average temperature of the state this year
    # Input : state 
    # Output: return average temperature of that state
    def avgTempOfState(self, state):
        pass
    
    # Query : Display all information for all events (sort & join) 
    # Input : 
    # Output: 
    def sortEvents(self):
        pass