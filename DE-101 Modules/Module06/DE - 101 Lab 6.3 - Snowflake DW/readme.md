
## CSV to Snowflake to Tableau

```
#create new database
create or replace database calgaru_tug;

#check current database and schema
select current_database(), current_schema();

#create new table
CREATE TABLE superstore_orders
(
	"rowid" BIGINT  
	,"row id" DOUBLE
	,"order id" VARCHAR(2000)   
	,"order date" TIMESTAMP 
	,"ship date" TIMESTAMP   
	,"ship mode" STRING 
	,"customer id" STRING  
	,"customer name" STRING 
	,segment STRING 
	,country STRING
	,city STRING  
	,state STRING
	,"postal code" DOUBLE  
	,"region" STRING 
	,"product id" STRING
	,category STRING  
	,"sub-category" STRING
	,"product name" STRING
	,sales DOUBLE    
	,quantity DOUBLE
	,discount DOUBLE
	,profit DOUBLE 
);

#connect the external storage or UI
CREATE STAGE "CALGARU_TUG"."PUBLIC".TUG URL = 's3://vancouver-tug/unload_superstore_single.csv' 
CREDENTIALS = (AWS_KEY_ID = 'AKIASUGB3VRQXJIAY74J' AWS_SECRET_KEY = '****************************************');


#create virtual warehouse
create or replace warehouse calgary_tug_wh with
  warehouse_size='X-SMALL'
  auto_suspend = 180
  auto_resume = true
  initially_suspended=true;
  
#check current warehouse
select current_warehouse();
  
#load data from S3
copy into superstore_orders
  from @TUG
  pattern='unload_superstore_single.csv'
  file_format = (type = csv field_delimiter = '|' skip_header = 1);  


#query table
select * from superstore_orders

#download ODBC driver
#Help -> Download

#reconnect excel to Snowflake

```


## JSON to Snowflake
```
#check database
select current_database(), current_schema();

  
#check current warehouse
select current_warehouse();


#create sales table
create or replace temporary table home_sales (
  city string,
  zip string,
  state string,
  type string default 'Residential',
  sale_date timestamp_ntz,
  price string
  );

#create file format
/*A named file format object provides a convenient means to store all of the format information required for loading data from files into tables.*/
create or replace file format json_format
type = 'JSON'
strip_outer_array = true;  

#create stage 
/*The following examples create external stages that specify the file formats*/
create or replace stage json_format_stage
file_format = json_format
url = 's3://vancouver-tug/'
CREDENTIALS = (AWS_KEY_ID = 'AKIASUGB3VRQXJIAY74J' AWS_SECRET_KEY = '****************************************');
  
copy into home_sales(city, state, zip, sale_date, price)
from (select substr(parse_json($1):location.state_city,4), substr(parse_json($1):location.state_city,1,2),
                parse_json($1):location.zip, to_timestamp_ntz(parse_json($1):sale_date), parse_json($1):price from @json_format_stage/sales.json)
  on_error = 'skip_file';
  
 select * from home_sales;
```

## Parquet to Snowflake

```
/*
Parquet Example
{
  "continent": "Europe",
  "country": {
    "city": {
      "bag": [
        {
          "array_element": "Paris"
        },
        {
          "array_element": "Nice"
        },
        {
          "array_element": "Marseilles"
        },
        {
          "array_element": "Cannes"
        }
      ]
    },
    "name": "France"
  }
}
*/


create or replace table cities (
  continent varchar default null,
  country varchar default null,
  city variant default null
);

                                                   
#create file format
create or replace file format parquet_format
  type = 'parquet';

#create stage
create or replace stage parquet_format_stage
  file_format =  parquet_format
  url = 's3://vancouver-tug/'
  CREDENTIALS = (AWS_KEY_ID = 'AKIASUGB3VRQXJIAY74J' AWS_SECRET_KEY = '****************************************');

copy into cities
  from (select
  $1:continent::varchar,
  $1:country:name::varchar,
  $1:country:city.bag::variant
  from @parquet_format_stage/cities.parquet);

/* Query the relational table                                                                                 */

select * from cities;
```

## External Weather to Snowflake
```
/*The following query retrieves the recent high and low temperature readings for New York City, converted from celsius to fahrenheit temperatures, along with the latitude and longitude for the readings:*/
select (v:main.temp_max - 273.15) * 1.8000 + 32.00 as temp_max_far,
       (v:main.temp_min - 273.15) * 1.8000 + 32.00 as temp_min_far,
       cast(v:time as timestamp) time,
       v:city.coord.lat lat,
       v:city.coord.lon lon,
       v
from snowflake_sample_data.weather.weather_14_total
where v:city.name = 'Vancouver'
and   v:city.country = 'CA'
and t >= sysdate() - 30
order by time desc
limit 10;

```

## Covid Data to Snowflake
```
//https://starschema.com/covid-19-data-set
#https://github.com/starschema/COVID-19-data

DROP TABLE WHO_TIMESERIES;

CREATE TABLE IF NOT EXISTS WHO_TIMESERIES (
  COUNTRY_REGION VARCHAR,
  CASES_TOTAL int,
  CASES_TOTAL_PER_100000 float,
  CASES int,
  DEATHS_TOTAL int,
  DEATHS_TOTAL_PER_100000 float,
  DEATHS int,
  TRANSMISSION_CLASSIFICATION varchar,
  DATE timestamp_ntz,
  ISO3166_1 VARCHAR(2)
);

INSERT INTO WHO_TIMESERIES (
  COUNTRY_REGION, 
  CASES_TOTAL, 
  CASES_TOTAL_PER_100000,
  CASES,
  DEATHS_TOTAL,
  DEATHS_TOTAL_PER_100000,
  DEATHS,
  TRANSMISSION_CLASSIFICATION,
  DATE,
  ISO3166_1
)
SELECT COUNTRY_REGION, 
  CASES_TOTAL, 
  CASES_TOTAL_PER_100000,
  CASES,
  DEATHS_TOTAL,
  DEATHS_TOTAL_PER_100000,
  DEATHS,
  TRANSMISSION_CLASSIFICATION,
  DATE,
  ISO3166_1
  FROM "STARSCHEMA_COVID19"."PUBLIC"."WHO_DAILY_REPORT" as r
  WHERE r.DATE > (
    SELECT NVL(MAX(DATE), '1900-01-01') 
  FROM WHO_TIMESERIES
  );

select max(date) from WHO_TIMESERIES
```
