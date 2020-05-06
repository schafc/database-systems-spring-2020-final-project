import psycopg2

class SQLConnectorClass():
    
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
        q = "SELECT event_type, AVG(avg_temperature), AVG(min_temperature), AVG(max_temperature), AVG(wind_speed), AVG(pressure), AVG(precipitation), AVG(visibility) \
             FROM ( \
                   SELECT * \
                   FROM ( \
                         SELECT * \
                         FROM Event \
                         WHERE event_type='%s' \
                   ) AS t1 JOIN NearbyStation ON t1.episode_id=NearbyStation.episode_id \
             ) AS t2 JOIN AirQuality on t2.station_id=AirQuality.station_id \
             GROUP BY event_type;" % (event_type,)
        cur = self.conn.cursor()
        cur.execute(q)
        result = cur.fetchall()

        if (len(result) == 0):
        	print("ERROR: Event \'{}\' not found in data. List of valid events:".format(event_type))
        	q = "SELECT event_type FROM Event GROUP BY event_type;"
        	cur.execute(q)
        	for event in cur.fetchall():
        		print(event[0])
        else:
        	result = result[0]
	        print("AIR INFORMATION FOR {}".format(event_type.upper()))
	        print("Average Temperature:\t {:.2f}°F".format(result[1]))
	        print("Average Min Temperature: {:.2f}°F".format(result[2]))
	        print("Average Min Temperature: {:.2f}°F".format(result[3]))
	        print("Average Wind Speed:\t {:.2f} knots".format(result[4]))
	        print("Average Air Pressure:\t {:.2f} psi".format(result[5]))
	        print("Average Precipitation:\t {:.2f} in".format(result[6]))
	        print("Average Visibility:\t {:.2f} mi".format(result[7]))
    
    # Query : Average temperature of the state this year
    # Input : state 
    # Output: return average temperature of that state
    def avgTempOfState(self, state):
        q = "SELECT state, AVG(avg_temperature) \
        	 FROM ( \
        	 	   SELECT * \
        	 	   FROM ( \
        	 	   		SELECT * \
        	 	   		FROM Event \
        	 	   		WHERE state='%s' \
        	 	   ) AS X JOIN NearbyStation ON X.episode_id=NearbyStation.episode_id \
        	 ) AS Y JOIN AirQuality ON Y.station_id=AirQuality.station_id \
        	 GROUP BY state;" % (state,)
        cur = self.conn.cursor()
        cur.execute(q)
        result = cur.fetchall()
        
        if (len(result) == 0):
            print("ERROR: State \'{}\' not found in data. List of valid stats:".format(state))
            q = "SELECT state FROM Event GROUP BY state;"
            curr.execute(q)
            for state in cur.fetchall():
                print(state[0])
        
        else:
            print("The average temperature in {} in 2019 was {:.2f}°F".format(result[0][0], result[1][1]))
    
    # Query : Display all information for all events (sort & join) 
    # Input : 
    # Output: 
    def sortEvents(self):
        query = "SELECT event.event_type, AirQuality.date_, event.state, eventlocation.location, NearbyStation.station_id, AirQuality.avg_temperature, \
        				AirQuality.wind_speed, AirQuality.precipitation, AirQuality.visibility \
        		 FROM event, eventlocation, airQuality, NearbyStation \
        		 WHERE event.episode_id=eventlocation.episode_id \
        		 	AND event.episode_id=NearbyStation.episode_id \
        		 	AND event.event_id=eventlocation.event_id \
        			AND event.event_id = NearbyStation.event_id \
        			AND eventlocation.location_index=NearbyStation.location_index \
        			AND NearbyStation.station_id=airQuality.station_id \
        			AND event.begin_date_time = AirQuality.date_ \
        		 ORDER BY event.event_type,event.state,eventlocation.location,AirQuality.date_,NearbyStation.station_id;"
        cur = self.conn.cursor()
        cur.execute(query)
        count = 0
        for value in cur.fetchall():
            count += 1
            print("#" + str(count) + ")")
            print("Event Type:", value[0], "\nDate:", value[1], "\nState:", value[2], "\nLocation:", value[3], "\nClosest Station:", value[4])
            print("Average temperature:", value[5],"°F\nWind Speed:",value[6],"knots\nPrecipitation quantity:", value[7], "in\nVisibility distance:", value[8], "mi")
            print()
