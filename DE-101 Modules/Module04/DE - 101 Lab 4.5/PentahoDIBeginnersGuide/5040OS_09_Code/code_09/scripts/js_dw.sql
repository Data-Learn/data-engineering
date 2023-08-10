DROP DATABASE IF EXISTS js_dw;
CREATE DATABASE js_dw;
USE js_dw;

CREATE TABLE LK_THEMES (
                id INT(10) NOT NULL,
                theme CHAR(50) NOT NULL,
                PRIMARY KEY (id)
);

ALTER TABLE LK_THEMES COMMENT '';


CREATE TABLE LK_PIECES (
                id INT(10) NOT NULL,
                min INT(6) DEFAULT 0 NOT NULL,
                max INT(6) DEFAULT 0 NOT NULL,
                description CHAR(30) NOT NULL
);

ALTER TABLE LK_PIECES COMMENT '';


CREATE TABLE LK_REGIONS_2 (
                id INT(4) NOT NULL,
                city CHAR(30) DEFAULT 'N/A' NOT NULL,
                country CHAR(30) DEFAULT 'N/A' NOT NULL,
                region CHAR(30) DEFAULT 'N/A' NOT NULL,
                id_js INT(4) DEFAULT 0 NOT NULL,
                start_date DATE,
                end_date DATE,
                version INT(4) DEFAULT 1 NOT NULL,
                current CHAR(1) DEFAULT 'Y' NOT NULL,
                lastupdate DATE,
                PRIMARY KEY (id)
);

ALTER TABLE LK_REGIONS_2 COMMENT '';


CREATE TABLE FT_PUZZ_SALES (
                date CHAR(8) NOT NULL,
                id_manufacturer INT(10) NOT NULL,
                id_region INT(10) NOT NULL,
                id_junk_prod INT(4) NOT NULL,
                id_puzzle INT(10) NOT NULL,
                id_pieces INT(10) NOT NULL,
                quantity INT(6) NOT NULL
);

ALTER TABLE FT_PUZZ_SALES COMMENT '';


CREATE TABLE FT_SALES (
                date CHAR(8) NOT NULL,
                id_manufacturer INT(10) NOT NULL,
                id_region INT(4) NOT NULL,
                id_junk_sales INT(10) NOT NULL,
                product_type CHAR(10) NOT NULL,
                quantity INT(6) DEFAULT 0 NOT NULL,
                amount NUMERIC(8,2) DEFAULT 0 NOT NULL
);

ALTER TABLE FT_SALES COMMENT '';

CREATE TABLE LK_JUNK_SALES (
                id INT(4) NOT NULL,
                buy_method CHAR(25) NOT NULL,
                payment_method CHAR(25) NOT NULL,
                PRIMARY KEY (id, buy_method, payment_method)
);

ALTER TABLE LK_JUNK_SALES COMMENT '';


CREATE TABLE LK_JUNK_PROD (
                id INT(4) NOT NULL,
                glowsInDark CHAR(1) NOT NULL,
                is3D CHAR(1) NOT NULL,
                wooden CHAR(1) NOT NULL,
                isPanoramic CHAR(1) NOT NULL,
                nrPuzzles INT(1) NOT NULL,
                PRIMARY KEY (id, glowsInDark, is3D, wooden, isPanoramic, nrPuzzles)
);

ALTER TABLE LK_JUNK_PROD COMMENT '';


CREATE TABLE LK_PUZZLES (
                id INT(10) NOT NULL,
                name CHAR(35) DEFAULT 'N/A' NOT NULL,
                theme CHAR(50) DEFAULT 'N/A' NOT NULL,
                id_js_prod CHAR(8) DEFAULT 00000000 NOT NULL,
                id_js_man CHAR(3) DEFAULT 000 NOT NULL,
                start_date DATE,
                end_date DATE,
                version INT(4) DEFAULT 1 NOT NULL,
                current CHAR(1) DEFAULT 'Y' NOT NULL,
                lastupdate DATE,
                PRIMARY KEY (id)
);

ALTER TABLE LK_PUZZLES COMMENT '';


CREATE TABLE LK_MANUFACTURERS (
                id INT(4) NOT NULL,
                name CHAR(25) DEFAULT 'N/A' NOT NULL,
                id_js CHAR(3) NOT NULL,
                lastupdate DATE,
                PRIMARY KEY (id)
);

ALTER TABLE LK_MANUFACTURERS COMMENT '';


CREATE TABLE LK_REGIONS (
                id INT(4) NOT NULL,
                city CHAR(30) DEFAULT 'N/A' NOT NULL,
                country CHAR(30) DEFAULT 'N/A' NOT NULL,
                region CHAR(30) DEFAULT 'N/A' NOT NULL,
                id_js INT(4) NOT NULL,
                lastupdate DATE,
                PRIMARY KEY (id)
);

ALTER TABLE LK_REGIONS COMMENT '';


CREATE TABLE LK_TIME (
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

ALTER TABLE LK_TIME COMMENT 'Time Dimension';