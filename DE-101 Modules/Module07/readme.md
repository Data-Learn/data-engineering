# Модуль 7: Знакомство с Apache Spark.

[Обратно в содержание курса :leftwards_arrow_with_hook:](https://github.com/Data-Learn/data-engineering/blob/master/DE%20-%20101%20Guide.md) 

В 7м модуле мы познакомимся с open source решением  для аналитики и инжиниринга данных - Apache Spark и его коммерческой версией Databricks. Вы узнаете примеры использования в индустрии и популярные use cases. Я расскажу о своем опыте с Apache Spark в Амазоне и Майкрософт и научу вас работать с данными с помощью PySpark и Spark SQL, покажу вам лучшие книги и материалы по Spark. 

## Модуль 7.1 Введение

**Видео лекция - теория** - [Введение](https://youtu.be/3qhcMVsVc5A). 

## Модуль 7.2 Что такое Apache Spark

Apache Spark является самый популярным инструментом среди инженеров данных, аналитиков и инженеров машинного обучения. Его главная задача это обработка данных. С помощью Spark можно подключаться к любому источнику данных, читать большие данные и обрабатывать их в оперативной памяти с использованием распределенного вычисления (distributed computing). 

**Видео лекция - теория** - [Что такое Apache Spark](https://youtu.be/Tl9YzC-dQLI). 

В этом видео:
- Узнаем история Apache Spark
- Посмотрим примеры архитектур с использованием Spark
- Разберемся когда его можно использовать
- Узнаем про основные компоненты
- Узнаем, обозначает термин Unified Analytics

### Вебинар от эксперта
- [ВВЕДЕНИЕ В PYSPARK И SPARKSQL / ОЛЕГ АГАПОВ](https://youtu.be/OfS5o8vz-O8)

**Видео лекция - практика** - [САМЫЙ МИНИМУМ PYTHON ДЛЯ SPARK (JUST ENOUGH PYTHON FOR SPARK)](https://youtu.be/ylaby_czbSI)


Прежде, чем начать работать с Apache Spark, мы должны иметь необходимый минимум работы хотя бы одного из поддерживаемых языков программирования. Один из самых популярных языков - Python. Поэтому в этом уроке мы посмотрим, какие команды нам необходимо знать на примере Databricks notebooks. У вас будет замечательная возможно попрактиковаться, и если вдруг вы мало используете Python, то самое время попробовать его, так как дальше нам очень понадобится.

В этом видео:
- Что такое Databricks
- Как запустить Community Edition Databricks и какие есть еще варианты для бесплатного Spark
- Переменные и типы данных в Python
- Условия и циклы
- Методы, функции и библиотеки
- Коллекции и классы

### Дополнительные материалы для изучения
- [Книга Learnin Spark V2 PDF](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module07/LearningSpark2.0.pdf)
- [Welcome to Spark… on Java: Интервью с Евгением Борисовым](https://habr.com/ru/company/jugru/blog/311146/)
- [Знакомство с Apache Spark](https://habr.com/ru/company/piter/blog/276675/)
- [Spark local mode: обработка больших файлов на обычном ноутбуке](https://habr.com/ru/post/274705/)
- [Apache Spark Key Terms, Explained](https://databricks.com/blog/2016/06/22/apache-spark-key-terms-explained.html)
- [Spark 101: What Is It, What It Does, and Why It Matters](https://developer.hpe.com/blog/spark-101-what-is-it-what-it-does-and-why-it-matters/)
- [PySpark on Google Colab 101](https://towardsdatascience.com/pyspark-on-google-colab-101-d31830b238be)

### Papers 
- [The Google File System](http://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)
- [MapReduce: Simplified Data Processing on Large Clusters](http://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)
- [Bigtable: A Distributed Storage System for Structured Data](http://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf)
- [The Hadoop Distributed File System](https://storageconference.us/2010/Papers/MSST/Shvachko.pdf)
- [Spark: Cluster Computing with Working Sets](https://www.usenix.org/legacy/event/hotcloud10/tech/full_papers/Zaharia.pdf)

### Лабораторная Работа
Для лабораторной работы вам нужно:
	- Создать Databricks Community Edition. Если какие-то проблемы с Databricks, можно все делать на локальном спарке. В следующем уроке покажу, как можно его установить.
    - Испортировать Notebooks с примерами для `Just Enougth Python for Spark` - [Репозиторий с кодом](https://github.com/Data-Learn/data-engineering/tree/master/DE-101%20Modules/Module07/DE%20-%20101%20Lab%207.1)
    - Выполнить задачки в папке `Labs`

Так же вы можете использовать Google Collab или локальный Spark. Для решения Notebooks может подойти Jupyter Notebooks.

## Модуль 7.3 Начало работы с Apache Spark

Продолжаем наше изучение Apache Spark. В этом уроке мы частично повторим детали из прошлого урок и заодно скачаем и установим Apache Spark на Windows 11. Если вы захотите устновить на Linux/MacOs, то вам будет ещё проще.

В этом уроке:

- Скачаем и запустим Apache Spark
- Посмотрим как запустить Spark на Windows
- Посмотрим на Spark UI
- Узнаем про основные компоненты Spark
- Начнем использовать `PySpark`
- Начнем использовать `spark-submit`

**Видео лекция - теория** - [Начало работы с Apache Spark](https://youtu.be/FiaZnMMOV-A). 

**Видео лекция - практика** - [Запуск программы в Apache Spark](https://youtu.be/FiaZnMMOV-A?t=1944)

### Дополнительные материалы для изучения

- [Что такое Apache Spark?](https://learn.microsoft.com/ru-ru/dotnet/spark/what-is-spark)
- [Apache Spark Installation on Windows](https://sparkbyexamples.com/spark/apache-spark-installation-on-windows/)
- [Install PySpark in Jupyter on Mac using Homebrew](https://sparkbyexamples.com/pyspark/install-pyspark-in-jupyter-on-mac-using-homebrew/)
- [Get Started with PySpark and Jupyter Notebook in 3 Minutes](https://sparkbyexamples.com/spark/install-apache-spark-on-mac/)
- [Beginners Guide to PySpark](https://towardsdatascience.com/beginners-guide-to-pyspark-bbe3b553b79f#:~:text=Beginners%20Guide%20to%20PySpark%201%20Setting%20Environment%20in,Values%20...%208%20Querying%20Data%20...%20More%20items)

### Лабораторная Работа

1. Ваша задача установить Apache Spark на ваш компьютер и запустить `PySpark`. Этого может хватить вам для изучения спарка, практически до конца модуля. Так как команды везде очень похожи, а вот интерфейс и конфигурация разные. 
2. Вам нужно взять программу про M&Ms из нашего [репозитория](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module07/DE%20-%20101%20Lab%207.2/mnmcount.py) и также взть файл с данными в том же репозитории в папке `data`.
3. Запустить спарк программу используя `spark-submit` и передать в качестве аргумента месторасположения файла с данными.
4. Вам необходимо взять тот же код про M&Ms, но теперь нужно будет его выполнить в интерактивном режиме. Я это сделал на примере Databricks, если есть доступ к нему, сделайте там, если нет, используйте командную строку или попробуйте вот этот рецепт [Get Started with PySpark and Jupyter Notebook in 3 Minutes](https://medium.com/sicara/get-started-pyspark-jupyter-guide-tutorial-ae2fe84f594f#:~:text=There%20are%20two%20ways%20to%20get%20PySpark%20available,Jupyter%20Notebook%20and%20load%20PySpark%20using%20findSpark%20package)
## Модуль 7.4 Знакомство с Spark API

В этом модуле мы познакомимся еще ближе с Apache Spark. 

В этом видео вы узнаете про:
- что такое RDD (Resilient Distributed Datasets)
- что такое DataFrame
- посмотрим на пример синтаксиса Scala vs Python
- типы данных Spark
- схему(schema) dataframe
- колонки (colums) и вычисляемы (expressions) поля dataframe
- основные операции при работе с dataframe (Reader, Wrtiter)
- примеры чтения разных источников и файлов (API, база данных, JSON, Parquet, CSV, TXT)
- различные операции для трансформации, фильтрации и агрегации данных в Spark DataFrame (прям как в SQL)
- Spark SQL, Catalyst Optimizer
- план запроса Spark
- примеры advance Spark функций и ноутбуков в Databticks

**Видео лекция - теория** - [Знакомство с Spark API](https://youtu.be/gg1uip_i2KY). 

В качестве лаборатнорной работы мы будем анализировать данные по пожраной службе Сан-Франциско. Я покажу, как можно прочитать файл и выполнить просты запросы на PySpark.

**Видео лекция - практика Apache Spark CLI** - [Запросы PySpark](https://youtu.be/gg1uip_i2KY?t=2297)

Так же мы посмотрим на курс от Databricks про Apache Spark Developer. Мы посмотрим лишь, часть, которая относится к этой лекции:
- Reader & Writer
- DataFrame & Column
- Aggregations
- Datetime functions
- Complex Types
- Additional Spark Functions

**Видео лекция - практика Databricks** - [Обзор курса Databrick - Programming with Apache Spark](https://youtu.be/gg1uip_i2KY?t=3567)

### Дополнительные материалы для изучения
Новых материало особо нет. В этом уроке мы практикуемся с запросами на `PySpark`.

Есть целый курс `Apache Spark Programming` в 2х вариантах:
- `HTML` - вы можете посмотреть на пример кода
- Databricks Notebooks - вы можете загрузить ноутбуки в Databricks Community Edition

Так же я создал небольшой `docker-compose.yml` - как шаблон для запуска:
- Spark 3.2.0
- Jupyter notebooks

Чтобы запустить - `docker-compose up` и Jupyter будет доступен по адресу `http://localhost:8888`

### Лабораторная Работа

В качестве лабораторной работу, вам нужно будет ответить на вопросы про пожарную службу Сан-Франциско используя файлик с данными [sf-fire-calls.csv](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module07/DE%20-%20101%20Lab%207.4/examples/sf-fire-calls.csv)

Вопросы находятся в файлике [sf_fire.py](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module07/DE%20-%20101%20Lab%207.4/examples/sf_fire.py):

```
# Q-1) How many distinct types of calls were made to the Fire Department?
# To be sure, let's not count "null" strings in that column.

# Q-2) What are distinct types of calls were made to the Fire Department?
# These are all the distinct type of call to the SF Fire Department

# Q-3) Find out all response or delayed times greater than 5 mins?
# Rename the column Delay - > ReponseDelayedinMins
# Returns a new DataFrame
# Find out all calls where the response time to the fire site was delayed for more than 5 mins


# Q-3) Find out all response or delayed times greater than 5 mins?
# Rename the column Delay - > ReponseDelayedinMins
# Returns a new DataFrame
# Find out all calls where the response time to the fire site was delayed for more than 5 mins

# Q-4a) What zip codes accounted for most common calls?
# Let's investigate what zip codes in San Francisco accounted for most fire calls and what type where they.
# Filter out by CallType
# Group them by CallType and Zip code
# Count them and display them in descending order
# It seems like the most common calls were all related to Medical Incident, and the two zip codes are 94102 and 94103.

# Q-4b) What San Francisco neighborhoods are in the zip codes 94102 and 94103
# Let's find out the neighborhoods associated with these two zip codes. In all likelihood, these are some of the contested neighborhood with high reported crimes.

# Q-5) What was the sum of all calls, average, min and max of the response times for calls?
# Let's use the built-in Spark SQL functions to compute the sum, avg, min, and max of few columns:
# Number of Total Alarms
# What were the min and max the delay in response time before the Fire Dept arrived at the scene of the call

# ** Q-6b) What week of the year in 2018 had the most fire calls?**
# Note: Week 1 is the New Years' week and week 25 is the July 4 the week. Loads of fireworks, so it makes sense the higher number of calls.

# ** Q-7) What neighborhoods in San Francisco had the worst response time in 2018?**
# It appears that if you living in Presidio Heights, the Fire Dept arrived in less than 3 mins, while Mission Bay took more than 6 mins.

# ** Q-8a) How can we use Parquet files or SQL table to store data and read it back?**

# ** Q-8c) How can read data from Parquet file?**
# Note we don't have to specify the schema here since it's stored as part of the Parquet metadata
```

## Модуль 7.5 Знакомство с Spark SQL и DataFrame

Мы уже познакомились с Spark и писали запросы с помощью PySpark, так сказать Python  flavor. А теперь мы посморим на Spark SQL

В этом видео вы узнаете про:

- Методы SparkSession для работы с SQL 
- Как создавать таблицы и вьюхи
- Виды таблиц - Managed vs Unmanaged
- Примеры SQL запросов в PySpark
- Кеш в Spark
- Рельтат SQL запроса в DataFrame и наоборот
- Пример работы с различными файлами в Spark - Parquet, CSV, JSON, AVRO, ORC
- Пример использования Spark для бинарных файлов и изображений
- Функции и операции Spark
- UNION, JOIN для DataFrame
- Window Functions
- UDF
- Партиционирование данных и оптимизация с командами coalesce, repartition.

**Видео лекция - теория** - [Знакомство с Spark API](https://youtu.be/MHt_s0-q_PM). 

В качестве лаборатнорной работы вам нужно будет выполнить все [запросы](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module07/DE%20-%20101%20Lab%207.5/examples/) из примеров в CLI и Databricks.


### Дополнительные материалы для изучения

- [Практика использования Spark SQL, или Как не наступить на грабли](https://habr.com/ru/companies/sberbank/articles/496310/)
- [https://habr.com/ru/companies/neoflex/articles/578654/](https://habr.com/ru/companies/sberbank/articles/496310/)
- [Spark SQL, DataFrames and Datasets Guide](https://spark.apache.org/docs/3.2.0/sql-programming-guide.html)
- [Spark SQL Explained with Examples](https://sparkbyexamples.com/spark/spark-sql-explained/)
- [Databricks: Working with SQL at Scale - Spark SQL Tutorial](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3137082781873852/3704545280501166/1264763342038607/latest.html)
- [Databricks: Functions](https://docs.databricks.com/sql/language-manual/sql-ref-functions.html)
- [Databricks: WindowFunctions](https://docs.databricks.com/sql/language-manual/sql-ref-window-functions.html)


## Модуль 7.6 Подключение Spark к внешним приложениям

## Модуль 7.7 Оптимизация Spark

## Модуль 7.8 Знакомство с AWS Glue

## Модуль 7.9 Знакомство с Synapse Spark




По окончанию модуля 7, вы можете расшарить значок `07 | Apache Spark` в социальных сетях и рассказать о своих достижениях. 

![img]()

А также добавить в Linkedin сертификат:

![img]()

PS Если материал оказался полезным, вы можете поддержать авторов через 
[ЮMoney](https://yoomoney.ru/to/4100116864248269) или [Patreon](https://www.patreon.com/dmitryanoshin) или [Paypal](https://paypal.me/dmitryanoshin)
