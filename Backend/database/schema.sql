DROP TABLE if exists login_details;

CREATE TABLE login_details (
    user_id varchar(100) PRIMARY KEY,
    --todo: Change this to Hash.
    password varchar(100) NOT NULL
)