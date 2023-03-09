# Homework (Module 03)

***Задание 1***

- Есть ли у вас доступ к BI решению? Если есть, то попробуйте отыскать все элементы, про которые я рассказывал. Если нет, то попробуйте найти любой продукт BI, установить его, и посмотреть, что внутри.

***Решение***

В качестве инструмента BI был взят **Apache Superset**. Это open source решение. Запускается через **Docker**. В сравнении с **DataLens** от **Yandex**,  **Superset** мне показался сложнее, хотя по функционалу он явно шире. Подключение к BI инструменту производил через **Amazon RDS (MySQL)**

- Amazon RDS

![amazon_rds](https://github.com/halltape/data-engineering/blob/develop/DE-101%20Modules/Module03/Homework03/png/amazon_rds.png)

- Apache Superset

![superset_interface](https://github.com/halltape/data-engineering/blob/develop/DE-101%20Modules/Module03/Homework03/png/superset_interface.png)

***

***Задание 2***

- Посмотрите на ваши дашборды на работе или в модуле 1 и 2. Что вы могли бы улучшить?

***Решение***

Основная ошибка в моем дашборде во втором модуле - я использовал **pie chart** в запросах, где более трех-четырех категорий. Это совершенно не наглядно и сбивает с толку. Более того, дашборд не дает "быстрой" информации при первом взгляде на него. Поэтому я взял свой предыдущий dataset и переделал **dashboard** в **Apache Superset**.

- Yandex DataLens Dashboard

![yandex_dashboard](https://github.com/halltape/data-engineering/blob/develop/DE-101%20Modules/Module03/Homework03/png/yandex_dashboard.png)


- Apache Superset Dashboard

![superset_dashboard](https://github.com/halltape/data-engineering/blob/develop/DE-101%20Modules/Module03/Homework03/png/superset_dashboard.png)

***

***Задание 3***

- Создать аналитический инструмент на основе Airbnb London

***Решение***

Создал подключение в **Amazon RDS**, дальше подключился к **MySQL** через **DataGrip**. Подгрузил туда все таблицы в формате **.csv**. Написал несколько запросов. Важный момент: Цены в таблице listings в формате **text**. Цены я складывал, так как мне нужна была общая стоимость аренды. Я не менял тип данных в датасете, а лишь временно форматировал их в запросе, отчего запросы стали просто огромными. При этом увеличилась и скорость обраотки до 17 секунд. В будущем учту это. Визуализация осуществлялась в **Yandex DataLens**. Очень быстрый и понятный инструмент, хотя и уступающий **Apache Superset**. 


- Yandex DataLens Dashboard (Airbnb London)

![airbnb_london](https://github.com/halltape/data-engineering/blob/develop/DE-101%20Modules/Module03/Homework03/png/yandex_dashboard.png)

- GeoJSON (Airbnb London)

![map](https://github.com/halltape/data-engineering/blob/develop/DE-101%20Modules/Module03/Homework03/png/yandex_dashboard.png)

test
