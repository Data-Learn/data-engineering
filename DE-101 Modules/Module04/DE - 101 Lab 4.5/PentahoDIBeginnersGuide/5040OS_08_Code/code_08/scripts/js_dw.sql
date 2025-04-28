CREATE DATABASE js_dw;

CREATE TABLE js_dw.LK_TIME (
                dateid CHAR(8) NOT NULL,
                year INT(4) NOT NULL,
                month INT(2) NOT NULL,
                day INT(2) NOT NULL,
                week_day INT(1) NOT NULL,
                week_desc CHAR(10) NOT NULL,
                week_short_desc CHAR(3) NOT NULL,
                month_desc CHAR(10) NOT NULL,
                month_short_desc CHAR(3) NOT NULL,
                PRIMARY KEY (dateid)
);

ALTER TABLE js_dw.LK_TIME COMMENT 'Time Dimension';
