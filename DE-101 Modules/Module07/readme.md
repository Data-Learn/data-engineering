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
- [https://sparkbyexamples.com/pyspark/install-pyspark-in-jupyter-on-mac-using-homebrew/](https://sparkbyexamples.com/spark/install-apache-spark-on-mac/)
- [Beginners Guide to PySpark](https://towardsdatascience.com/beginners-guide-to-pyspark-bbe3b553b79f#:~:text=Beginners%20Guide%20to%20PySpark%201%20Setting%20Environment%20in,Values%20...%208%20Querying%20Data%20...%20More%20items)

### Лабораторная Работа

1. Ваша задача установить Apache Spark на ваш компьютер и запустить `PySpark`. Этого может хватить вам для изучения спарка, практически до конца модуля. Так как команды везде очень похожи, а вот интерфейс и конфигурация разные. 
2. Вам нужно взять программу про M&Ms из нашего [репозитория](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module07/DE%20-%20101%20Lab%207.2/mnmcount.py) и также взть файл с данными в том же репозитории в папке `data`.
3. Запустить спарк программу используя `spark-submit` и передать в качестве аргумента месторасположения файла с данными.
4. Вам необходимо взять тот же код про M&Ms, но теперь нужно будет его выполнить в интерактивном режиме. Я это сделал на примере Databricks, если есть доступ к нему, сделайте там, если нет, используйте командную строку или попробуйте вот этот рецепт [Get Started with PySpark and Jupyter Notebook in 3 Minutes](https://medium.com/sicara/get-started-pyspark-jupyter-guide-tutorial-ae2fe84f594f#:~:text=There%20are%20two%20ways%20to%20get%20PySpark%20available,Jupyter%20Notebook%20and%20load%20PySpark%20using%20findSpark%20package)
## Модуль 7.4 Знакомство с Spark API

## Модуль 7.5 Знакомство с Spark SQL и DataFrame

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
