import psycopg2
import gzip
import os

connection_string = "host='localhost' dbname='dbms_final_project' user='dbms_project_user' password='dbms_password'"
dir = os.path.dirname(__file__)

# TODO add your code here (or in other files, at your discretion) to load the data


def main():
    # TODO invoke your code to load the data into the database
    print("Loading data")
    conn = psycopg2.connect(connection_string);
    cur = conn.cursor()

    cur.execute(open(os.path.join(dir, 'schema.sql'), 'r').read())

    conn.commit()

    # with gzip.open('datasets/2019.tar.gz') as f_in:
    # 	print(f_in)



if __name__ == "__main__":
    main()
