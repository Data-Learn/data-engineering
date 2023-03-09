/*Средняя цена (за месяц) с учетом всех депозитов и налогов в каждом районе*/

WITH TMP AS (SELECT SUBSTRING_INDEX(listings.monthly_price, '$', -1)    AS monthly_price,
                    SUBSTRING_INDEX(listings.security_deposit, '$', -1) AS security_deposit,
                    SUBSTRING_INDEX(listings.cleaning_fee, '$', -1)     AS cleaning_fee,
                    listings.neighbourhood_cleansed
             FROM listings
             WHERE listings.monthly_price IS NOT NULL)

SELECT ROUND(AVG(REGEXP_REPLACE(TMP.monthly_price, ',', '') +
                 IF(TMP.security_deposit IS NULL, 0, TMP.security_deposit) +
                 IF(TMP.cleaning_fee IS NULL, 0, TMP.cleaning_fee))) AS Average,
       TMP.neighbourhood_cleansed                                    AS neighborhood_cleansed
FROM TMP
GROUP BY neighborhood_cleansed
ORDER BY Average DESC;


/*Самая дорогая цена за аренду комнаты в Англии */
WITH TMP AS (SELECT SUBSTRING_INDEX(listings.monthly_price, '$', -1)    AS monthly_price,
                    SUBSTRING_INDEX(listings.security_deposit, '$', -1) AS security_deposit,
                    SUBSTRING_INDEX(listings.cleaning_fee, '$', -1)     AS cleaning_fee
             FROM listings
             WHERE listings.monthly_price IS NOT NULL
               AND listings.room_type = 'Private room')

SELECT CONCAT(MAX(REGEXP_REPLACE(TMP.monthly_price, ',', '') +
                  IF(TMP.security_deposit IS NULL, 0, TMP.security_deposit) +
                  IF(TMP.cleaning_fee IS NULL, 0, TMP.cleaning_fee)), '$') AS max_price
FROM TMP;



/*Самая дешевая цена за аренду комнаты в Англии */
WITH TMP AS (SELECT SUBSTRING_INDEX(listings.monthly_price, '$', -1)    AS monthly_price,
                    SUBSTRING_INDEX(listings.security_deposit, '$', -1) AS security_deposit,
                    SUBSTRING_INDEX(listings.cleaning_fee, '$', -1)     AS cleaning_fee
             FROM listings
             WHERE listings.monthly_price IS NOT NULL
               AND listings.room_type = 'Private room')

SELECT CONCAT(MIN(REGEXP_REPLACE(TMP.monthly_price, ',', '') +
                  IF(TMP.security_deposit IS NULL, 0, TMP.security_deposit) +
                  IF(TMP.cleaning_fee IS NULL, 0, TMP.cleaning_fee)), '$') AS min_price
FROM TMP;



/*Самая дешевая цена за аренду дома/аппартов в Лондоне и в каком районе*/
SELECT CONCAT(min_price, '$') AS 'Минимальная стоимость',
       neighbour              AS 'Район',
       neighbourhood_cleansed AS 'Округ'
FROM (WITH TMP AS (SELECT SUBSTRING_INDEX(listings.monthly_price, '$', -1)    AS monthly_price,
                          SUBSTRING_INDEX(listings.security_deposit, '$', -1) AS security_deposit,
                          SUBSTRING_INDEX(listings.cleaning_fee, '$', -1)     AS cleaning_fee,
                          listings.neighbourhood,
                          listings.neighbourhood_cleansed
                   FROM listings
                   WHERE listings.monthly_price IS NOT NULL
                     AND listings.room_type = 'Entire home/apt')

      SELECT (REGEXP_REPLACE(TMP.monthly_price, ',', '') +
              IF(TMP.security_deposit IS NULL, 0, TMP.security_deposit) +
              IF(TMP.cleaning_fee IS NULL, 0, TMP.cleaning_fee)) AS min_price,
             TMP.neighbourhood                                   AS neighbour,
             TMP.neighbourhood_cleansed
      FROM TMP) AS m
WHERE min_price IN (SELECT MIN(min_price)
                    FROM (WITH TMP AS (SELECT SUBSTRING_INDEX(listings.monthly_price, '$', -1)    AS monthly_price,
                                              SUBSTRING_INDEX(listings.security_deposit, '$', -1) AS security_deposit,
                                              SUBSTRING_INDEX(listings.cleaning_fee, '$', -1)     AS cleaning_fee,
                                              listings.neighbourhood,
                                              listings.neighbourhood_cleansed
                                       FROM listings
                                       WHERE listings.monthly_price IS NOT NULL
                                         AND listings.room_type = 'Entire home/apt')

                          SELECT (REGEXP_REPLACE(TMP.monthly_price, ',', '') +
                                  IF(TMP.security_deposit IS NULL, 0, TMP.security_deposit) +
                                  IF(TMP.cleaning_fee IS NULL, 0, TMP.cleaning_fee)) AS min_price,
                                 TMP.neighbourhood                                   AS neighbour,
                                 TMP.neighbourhood_cleansed
                          FROM TMP) m);




/*Самая дорогая цена за аренду дома/аппартов в Лондоне и в каком районе*/
SELECT CONCAT(max_price, '$') AS 'Максимальная стоимость',
       neighbour              AS 'Район',
       neighbourhood_cleansed AS 'Округ'
FROM (WITH TMP AS (SELECT SUBSTRING_INDEX(listings.monthly_price, '$', -1)    AS monthly_price,
                          SUBSTRING_INDEX(listings.security_deposit, '$', -1) AS security_deposit,
                          SUBSTRING_INDEX(listings.cleaning_fee, '$', -1)     AS cleaning_fee,
                          listings.neighbourhood,
                          listings.neighbourhood_cleansed
                   FROM listings
                   WHERE listings.monthly_price IS NOT NULL
                     AND listings.room_type = 'Entire home/apt')

      SELECT (REGEXP_REPLACE(TMP.monthly_price, ',', '') +
              IF(TMP.security_deposit IS NULL, 0, TMP.security_deposit) +
              IF(TMP.cleaning_fee IS NULL, 0, TMP.cleaning_fee)) AS max_price,
             TMP.neighbourhood                                   AS neighbour,
             TMP.neighbourhood_cleansed
      FROM TMP) AS m
WHERE max_price IN (SELECT MAX(max_price)
                    FROM (WITH TMP AS (SELECT SUBSTRING_INDEX(listings.monthly_price, '$', -1)    AS monthly_price,
                                              SUBSTRING_INDEX(listings.security_deposit, '$', -1) AS security_deposit,
                                              SUBSTRING_INDEX(listings.cleaning_fee, '$', -1)     AS cleaning_fee,
                                              listings.neighbourhood,
                                              listings.neighbourhood_cleansed
                                       FROM listings
                                       WHERE listings.monthly_price IS NOT NULL
                                         AND listings.room_type = 'Entire home/apt')

                          SELECT (REGEXP_REPLACE(TMP.monthly_price, ',', '') +
                                  IF(TMP.security_deposit IS NULL, 0, TMP.security_deposit) +
                                  IF(TMP.cleaning_fee IS NULL, 0, TMP.cleaning_fee)) AS max_price,
                                 TMP.neighbourhood                                   AS neighbour,
                                 TMP.neighbourhood_cleansed
                          FROM TMP) m);


/*Количество районов внутри округов*/
SELECT neighbourhood_cleansed,
       COUNT(DISTINCT neighbourhood)
FROM listings
GROUP BY neighbourhood_cleansed;