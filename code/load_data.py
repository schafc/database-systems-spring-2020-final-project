import psycopg2
import gzip
import os
import sys
import io
import csv
import tarfile

connection_string = "host='localhost' dbname='dbms_final_project' user='dbms_project_user' password='dbms_password'"
dir = os.path.dirname(__file__)

# TODO add your code here (or in other files, at your discretion) to load the data


def main():
    # TODO invoke your code to load the data into the database
    print("Loading data")
    conn = psycopg2.connect(connection_string);
    cur = conn.cursor()

    # Create schema
    cur.execute(open(os.path.join(dir, 'schema.sql'), 'r').read())
    conn.commit()

    # Load Storm Events Data
    print("Loading Storm Events Data...")
    with gzip.open(os.path.join(dir, 'datasets/StormEvents_details-ftp_v1.0_d2019_c20200416.csv.gz'), 'rb') as f_in:
        reader = csv.reader(io.TextIOWrapper(f_in, newline=""))
        for row in list(reader)[1:]:
            cur.execute("INSERT INTO Event (episode_id, event_id, state, year, month_name, event_type, begin_date_time, end_date_time, cz_timezone) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", (row[6], row[7], row[8], row[10], row[11], row[12], row[17], row[19], row[18]));

    conn.commit()

    # Load Storm Locations Data
    print("Loading Storm Locations Data...")
    with gzip.open(os.path.join(dir, 'datasets/StormEvents_locations-ftp_v1.0_d2019_c20200416.csv.gz'), 'rb') as f_in:
        reader = csv.reader(io.TextIOWrapper(f_in, newline=""))
        # for row in list(reader)[1:]:
        for row in list(reader)[1:]:
            cur.execute("INSERT INTO EventLocation (episode_id, event_id, location_index, location, lat, lon) \
                VALUES (%s, %s, %s, %s, %s, %s);", (row[1], row[2], row[3], row[6], row[7], row[8]))

    conn.commit()

    # Load Station Data
    print("Loading Station Data...")
    with tarfile.open(os.path.join(dir, 'datasets/2019.tar.gz'), 'r:gz') as tar:
        i = 0
        for member in tar.getmembers():
            i += 1
            with tar.extractfile(member.name) as file:
                reader = csv.reader(io.TextIOWrapper(file, newline=""))
                # readerlist = list(reader)[1:]
                readerlist = list(reader)[1::500]
                
                try:
                    cur.execute("INSERT INTO StationInformation (name, lat, lon, station_id, elevation) \
                        VALUES (%s, %s, %s, %s, %s);", (readerlist[0][5], readerlist[0][2], readerlist[0][3], readerlist[0][0], readerlist[0][4]))

                    for row in readerlist:
                        sys.stdout.write("\r[" + "="*int(i/len(tar.getmembers())*50) + " "*int((len(tar.getmembers())-i)/len(tar.getmembers())*50) + "]")
                        cur.execute("INSERT INTO AirQuality (station_id, date_, avg_temperature, min_temperature, max_temperature, visibility, precipitation, \
                            wind_speed, pressure) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                            (row[0], row[1], row[6], row[22], row[20], row[14], row[24], row[16], row[10]))

                    conn.commit()
                except:
                    continue

    conn.commit()

    # Calculate Nearby Stations
    print("\nCalculating Nearby Stations...")
    cur.execute("INSERT INTO NearbyStation \
        SELECT eventlocation.episode_id, eventlocation.event_id, eventlocation.location_index, ( \
            SELECT station_id \
            FROM ( \
                SELECT * FROM stationinformation \
                ORDER BY random() \
                LIMIT 1000 \
            ) station \
            ORDER BY ( 6371 * acos ( \
                cos ( radians( eventlocation.lat+0.02 ) ) \
                * cos( radians( lat ) ) \
                * cos( radians( lon ) - radians( eventlocation.lon+0.02 ) ) \
                + sin( radians( eventlocation.lat+0.02 ) ) \
                * sin( radians( lat ) ) ) ) ASC LIMIT 1 \
            ) AS station_id \
        FROM eventlocation;")

    conn.commit()



if __name__ == "__main__":
    main()
