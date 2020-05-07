Database Systems Final Project
Due: May 7th, 6:30pm, 2020

Group members:
Sean Lossef - losses@rpi.edu
Daniel Molzahn - molzad@rpi.edu
Joe Om - omj@rpi.edu
Clara Schaffter - schafc@rpi.edu
Eli Wennberg-Smith (wennbe) - wennbe@rpi.edu

Project Datasets:
Global Surface Summary of the Day: https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc:C00516
NCDC Storm Events Database: https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc:C00510

Dataset Licensing
License for Global Surface Summary of the Day - Government work, Cite this dataset when used as a source.
Licence for NCDC Storm Events Database - Government work, Cite this dataset when used as a source.


---

-Application Use Procedure

1. First, have python install all modules present in requirements.txt. This will ensure that the application is able to run properly.

2. Next, run db-setup, to setup the database basics that the application assumes to exist

3. Then, run retrieve data.py. This will download the datafiles present at the URLs linked in datasets.txt. There are 3 links, the first two of which are for the same overall dataset, as the national weather service split storm event data into two separate data sets, which was not realized until fairly late on, so both are used here in order to acquire the data needed to complete the queries. The third link is for the surface summary data, which contains a very large number of files, one for each weather station, so it will take a fairly long time to download (couple minutes).

For these data sets, the data sets for 2019 were selected in order to have the most current and complete data, while also not overwhelming the system with way way too much data.

4. After the data has been retrieved, run load_data.py. This will take a significant amount of time, mostly for the third section where it parses the surface summary data. Runtime varies a lot depending on the computer used, but its estimated to take approximately 10-15 minutes to load. It runs through 4 load steps, each which prints an indicator when it starts: Storm events data, storm locations data, station data and nearby stations.

5. Once the data has been loaded into the database, run application.py. This allows the user to select from a list of queries, which, as needed, will prompt the user to enter additional values which will be used to search the database for desired information. More detailed specifics can be found in the application, by entering ‘menu’ as the user input value.

6. Three of the queries take user inputs, examples of which are provided below, to get the user started

Query 1 takes a location (typically a town): examples include - Princeton, Andover, Memphis

Query 3 takes a weather event type: examples include - hail, flood, tornado

Query 4 takes a state or geographic region: examples include - Texas, Atlantic South, Gulf of Mexico

Query 5 takes an integer representing the number of events to display within the query - 1, 25, 100
