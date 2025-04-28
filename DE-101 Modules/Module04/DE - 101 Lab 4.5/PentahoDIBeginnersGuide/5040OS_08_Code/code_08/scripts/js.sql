-- CREATE DATABASE js;

USE js;

CREATE TABLE js.manufacturers (
                man_code CHAR(3) NOT NULL,
                man_desc CHAR(25) NOT NULL,
                PRIMARY KEY (man_code)
);

ALTER TABLE js.manufacturers COMMENT 'Puzzle Manufacturers';


CREATE TABLE js.products (
                pro_code CHAR(8) NOT NULL,
                man_code CHAR(3) NOT NULL,
                pro_name CHAR(35) NOT NULL,
                pro_description CHAR(100),
                pro_type CHAR(10) DEFAULT 'PUZZLE' NOT NULL,
                pro_theme CHAR(50),
                pro_pieces INT(5),
                pro_packaging CHAR(20),
                pro_shape CHAR(20),
                pro_style CHAR(20),
                pro_buy_price NUMERIC(6,2) DEFAULT 0 NOT NULL,
                pro_sel_price NUMERIC(6,2) DEFAULT 0 NOT NULL,
                pro_stock INT(6) DEFAULT 0 NOT NULL,
                pro_stock_min INT(6) DEFAULT 0 NOT NULL,
                pro_stock_max INT(6) DEFAULT 0 NOT NULL,
                PRIMARY KEY (pro_code, man_code)
);

ALTER TABLE js.products COMMENT 'Products (Puzzles & Accesories)';


ALTER TABLE js.products ADD CONSTRAINT manufacturers_products_fk
FOREIGN KEY (man_code)
REFERENCES js.manufacturers (man_code)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
