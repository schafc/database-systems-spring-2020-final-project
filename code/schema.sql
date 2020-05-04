DROP TABLE IF EXISTS Event CASCADE; 
DROP TABLE IF EXISTS EventLocation CASCADE;
DROP TABLE IF EXISTS ClosestStation CASCADE;
DROP TABLE IF EXISTS StationInformation CASCADE; 
DROP TABLE IF EXISTS AirQuality CASCADE;

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
    PRIMARY KEY (episode_id, event_id)
);

CREATE TABLE EventLocation (
    episode_id INT, 
    event_id INT, 
    location_index INT, 
    location VARCHAR(255),
    lat NUMERIC(3,2),
    lon NUMERIC(3,2),
    PRIMARY KEY (episode_id, event_id, location, location_index),
    FOREIGN KEY (episode_id, event_id) REFERENCES Event (episode_id, event_id)
);

CREATE TABLE ClosestStation (
  episode_id INT,
  event_id INT,
  station_id INT
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
    station_id INT REFERENCES StationInformation (station_id),
    date_ DATE,
    avg_temperature NUMERIC(3,2), 
    min_temperature NUMERIC(3,2),
    max_temperature NUMERIC(3,2),
    visibiliy NUMERIC(3,2),
    precipitation NUMERIC(3,2),
    wind_speed NUMERIC(3,2),
    pressure NUMERIC(3,2)
);

CREATE INDEX station_id ON AirQuality (station_id);
CREATE INDEX location ON EventLocation (location);
CREATE INDEX episode_id ON Event (episode_id);
CREATE INDEX event_id ON Event (event_id); 
