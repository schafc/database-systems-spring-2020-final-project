import psycopg2
import gzip
import os
import io
import csv

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

    print("Loading Storm Events Data...")
    with gzip.open(os.path.join(dir, 'datasets/StormEvents_details-ftp_v1.0_d2019_c20200416.csv.gz'), 'rb') as f_in:
        reader = csv.reader(io.TextIOWrapper(f_in, newline=""))
        for row in list(reader)[1:]:
            cur.execute("INSERT INTO Event (episode_id, event_id, state, year, month_name, event_type, begin_date_time, end_date_time, cz_timezone) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", (row[6], row[7], row[8], row[10], row[11], row[12], row[17], row[19], row[18]));

    conn.commit()

    print("Loading Storm Locations Data...")
    with gzip.open(os.path.join(dir, 'datasets/StormEvents_locations-ftp_v1.0_d2019_c20200416.csv.gz'), 'rb') as f_in:
        reader = csv.reader(io.TextIOWrapper(f_in, newline=""))
        for row in list(reader)[1:]:
            cur.execute("INSERT INTO EventLocation (episode_id, event_id, location_index, location, lat, lon) \
                VALUES (%s, %s, %s, %s, %s, %s);", (row[1], row[2], row[3], row[6], row[7], row[8]))

    conn.commit()



if __name__ == "__main__":
    main()
