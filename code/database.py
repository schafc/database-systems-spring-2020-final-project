import psycopg2

class SQLConnecterClass():
    
    def __init__(self, connection_string):
        # connection_string = "host='localhost' dbname='dbms_final_project' user='dbms_project_user' password='dbms_password'"
        self.conn = psycopg2.connect(connection_string)
    
    # Query : Retrieve events for a location 
    # Input : location 
    # Output: returns all events in that location 
    def queryLocation(self, location):
        cur = self.conn.cursor()
        q = "SELECT * FROM event e LEFT JOIN eventlocation el ON e.event_id = el.event_id WHERE el.location = '%s' ORDER BY state;" % (location)
        try:
            cur.execute(q)
            rs = cur.fetchall()
            if rs == []:
                print("No data for that location")
            else:
                count = 0
                for rslt in rs:
                    count += 1 
                    print("#" + str(count) + ")")
                    print("Episode ID:",rslt[0])
                    print("Event ID:",rslt[1])
                    print("State:",rslt[2])
                    print("Year:",rslt[3])
                    print("Month:",rslt[4])
                    print("Event Type:",rslt[5])
                    print("Begin Date:",rslt[6])
                    print("End Date:",rslt[7])
                    print()

        except Exception as error:
            print ("An exception has occured:", error)
            print ("Exception TYPE:", type(error))

    # Query : sort states by # of events 
    # Input : None
    # Output: Output count of events for each state sorted 
    def sortStatesByEvents(self):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT state, COUNT(event_id) count FROM Event GROUP BY state ORDER BY count DESC;")
            count = 0
            for rslt in cur.fetchall():
                count += 1
                print("#" + str(count) + ")")
                print("State:", rslt[0])
                print("Number of Events:", rslt[1])
                print()
        except Exception as error:
            print ("An exception has occured:", error)
            print ("Exception TYPE:", type(error))

    # Query : Event air quality information for an event_type
    # Input : Event_type
    # Output: Return average values from AirQuality table for that event_type
    def eventAirInformation(self, event_type):
        pass
    
    # Query : Average temperature of the state this year
    # Input : state 
    # Output: return average temperature of that state
    def avgTempOfState(self, state):
        q = "SELECT state, AVG(avg_temperature) FROM ( SELECT * FROM ( SELECT * FROM Event WHERE state = %s ) AS X JOIN ClosestStation USING episode_id ) AS Y JOIN AirQuality USING station_id GROUP BY state;" % state
        cur = self.conn.cursor()
        cur.execute(q)
        
        for result in cur.fetchall():
            print("The average temperature in %s in 2019 was %.2f." % result[0], result[1])
    
    # Query : Display all information for all events (sort & join) 
    # Input : 
    # Output: 
    def sortEvents(self):
        query = """SELECT event.event_type,  AirQuality.date_, event.state, eventlocation.location, closestStation.station_id, AirQuality.avg_temperature, 
        AirQuality.wind_speed, AirQuality.precipitation, AirQuality.visibiliy FROM event, eventlocation, airQuality, closestStation 
        WHERE event.episode_id = eventlocation.episode_id and event.episode_id = closestStation.episode_id and event.event_id = eventlocation.event_id 
        and event.event_id = closestStation.event_id and eventlocation.location_index = closestStation.location_index and  
        closestStation.station_id = airQuality.station_id and event.begin_date_time = AirQuality.date_ 
        Order by event.event_type,event.state,eventlocation.location,AirQuality.date_,closestStation.station_id;"""
        cur = self.conn.cursor()
        cur.execute(query)
        count = 0
        for value in cur.fetchall():
            count += 1
            print("#" + str(count) + ")")
            print("Event Type:", value[0], "Date:", value[1], "State:", value[2], "Location:", value[3], "Closest Station:", value[4])
            print("\t Average temperature:", value[5],"Wind Speed:",value[6],"Precipitation quantity:", value[7], "Visibility distance:", value[8])
            print()


