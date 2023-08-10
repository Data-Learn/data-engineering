DROP DATABASE IF EXISTS js;
CREATE DATABASE js;
USE js;

CREATE TABLE buy_methods (
                buy_code CHAR(4) NOT NULL,
                buy_desc CHAR(25) NOT NULL,
                PRIMARY KEY (buy_code)
);

ALTER TABLE buy_methods COMMENT 'store, internet, TE.';


CREATE TABLE payment_methods (
                pay_code CHAR(4) NOT NULL,
                pay_desc CHAR(25) NOT NULL,
                PRIMARY KEY (pay_code)
);

ALTER TABLE payment_methods COMMENT 'method of payment: cash, credit card, check.';


CREATE TABLE countries (
                cou_id INT(4) NOT NULL,
                country_name CHAR(30) NOT NULL,
                PRIMARY KEY (cou_id)
);

ALTER TABLE countries COMMENT '';


CREATE TABLE cities (
                city_id INT(4) NOT NULL,
                city_name CHAR(30) NOT NULL,
                cou_id INT(4) NOT NULL,
                PRIMARY KEY (city_id)
);

ALTER TABLE cities COMMENT '';


CREATE TABLE customers (
                cus_id INT(10) NOT NULL,
                cus_name CHAR(30) NOT NULL,
                cus_lastname CHAR(30) NOT NULL,
                add_street CHAR(50),
                add_zipcode CHAR(10),
                city_id INT(4) NOT NULL,
                PRIMARY KEY (cus_id)
);

ALTER TABLE customers COMMENT '';


CREATE TABLE invoices (
                invoice_number INT(10) NOT NULL,
                buy_code CHAR(4) NOT NULL,
                inv_date DATE NOT NULL,
                pay_code CHAR(4) NOT NULL,
                inv_price NUMERIC(8,2) DEFAULT 0 NOT NULL,
                cus_id INT(10) NOT NULL,
                PRIMARY KEY (invoice_number)
);

ALTER TABLE invoices COMMENT '';


CREATE TABLE manufacturers (
                man_code CHAR(3) NOT NULL,
                man_desc CHAR(25) NOT NULL,
                PRIMARY KEY (man_code)
);

ALTER TABLE manufacturers COMMENT 'Puzzle Manufacturers';


CREATE TABLE products (
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

ALTER TABLE products COMMENT 'Products (Puzzles & Accesories)';


CREATE TABLE invoices_detail (
                invoice_number INT(10) NOT NULL,
                linenr INT(4) NOT NULL,
                pro_code CHAR(8) NOT NULL,
                man_code CHAR(3) NOT NULL,
                cant_prod INT(2) NOT NULL,
                price_unit NUMERIC(6,2) NOT NULL,
                price NUMERIC(8,2) NOT NULL,
                PRIMARY KEY (invoice_number, linenr)
);

ALTER TABLE invoices_detail COMMENT '';


ALTER TABLE invoices ADD CONSTRAINT buy_place_invoices_fk
FOREIGN KEY (buy_code)
REFERENCES buy_methods (buy_code)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE invoices ADD CONSTRAINT payment_methods_invoices_fk
FOREIGN KEY (pay_code)
REFERENCES payment_methods (pay_code)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE cities ADD CONSTRAINT countries_cities_fk
FOREIGN KEY (cou_id)
REFERENCES countries (cou_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE customers ADD CONSTRAINT cities_clients_fk
FOREIGN KEY (city_id)
REFERENCES cities (city_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE invoices ADD CONSTRAINT clients_invoices_fk
FOREIGN KEY (cus_id)
REFERENCES customers (cus_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE invoices_detail ADD CONSTRAINT invoices_invoices_detail_fk
FOREIGN KEY (invoice_number)
REFERENCES invoices (invoice_number)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE products ADD CONSTRAINT manufacturers_products_fk
FOREIGN KEY (man_code)
REFERENCES manufacturers (man_code)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE invoices_detail ADD CONSTRAINT products_invoices_detail_fk
FOREIGN KEY (pro_code, man_code)
REFERENCES products (pro_code, man_code)
ON DELETE NO ACTION
ON UPDATE NO ACTION;