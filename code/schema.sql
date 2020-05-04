DROP SCHEMA IF EXISTS Event CASCADE; 
DROP SCHEMA IF EXISTS EventLocation CASCADE;
DROP SCHEMA IF EXISTS StationInformation CASCADE; 
DROP SCHEMA IF EXISTS AirQuality CASCADE;

CREATE TABLE Event (
    episode_id INT,
    event_id INT,
    state VARCHAR(255),
    year INT,
    month_name VARCHAR(20),
    event_type VARCHAR(255),
    begin_date_time DATE,
    end_date_time DATE, 
    cz_timezone VARCHAR(10),
    episode_title VARCHAR(255),
    PRIMARY KEY (episode_id, event_id)
);

CREATE TABLE EventLocation (
    episode_id INT REFERENCES Event, 
    event_id INT REFERENCES Event, 
    location_index INT, 
    location VARCHAR(255),
    lat NUMERIC(3,2),
    lon NUMERIC(3,2),
    PRIMARY KEY (episode_id, event_id, location, location_index)
);
  
CREATE TABLE StationInformation (
    name VARCHAR(255),
    lat NUMERIC(3,2),
    lon NUMERIC(3,2),
    station_id INT, 
    elevation INT,
    PRIMARY KEY (station_id)
);

CREATE TABLE AirQuality (
    station_id INT REFERENCES StationInformation,
    avg_temperature NUMERIC(3,2), 
    min_temperature NUMERIC(3,2),
    max_temperature NUMERIC(3,2),
    visibiliy NUMERIC(3,2,),
    precipitation NUMERIC(3,2),
    wind_speed NUMERIC(3,2),
    pressure NUMERIC(3,2)
);

CREATE INDEX station_id ON AirQuality;
CREATE INDEX location ON EventLocation;
CREATE INDEX episode_id ON Event;
CREATE INDEX event_id ON Event; 
