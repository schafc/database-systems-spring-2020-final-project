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


