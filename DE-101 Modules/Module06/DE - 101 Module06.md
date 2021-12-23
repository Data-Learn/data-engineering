# Модуль 6:  Аналитические Хранилища Данных

[Обратно в содержание курса :leftwards_arrow_with_hook:](https://github.com/Data-Learn/data-engineering/blob/master/DE%20-%20101%20Guide.md) 

В 6 модуле мы узнаем про аналитические и облачные хранилища данных которые используются в индустрии. Крупные компания Amazon, Microsoft, Airbnb, и многие другие из списка SP500 используют одну или сразу несколько решений для аналитических хранилищ данных - Amazon Redshift, Microsoft Synapse, Google BigQuery или Snowflake. Но кроме облачных хранилищ есть еще много on-premise Teradata, Greenplum, Vertica, Exasol и тп. 

Из модуля вы узнаете:
- Основы аналитических хранилищ данных
- MPP vs SMP
- Практика с Redshift, Snowflake и Azure Synapse
- Облачные ETL инструменты
- Обзор вакансий мирового рынка
- Обзор решений для операционной аналитики - Splunk, Azure Data Explorer и ElasticSearch

## Модуль 6.1 Введение

**Видео лекция - теория** - [Введение](https://youtu.be/yxNjsrePuqo). 

## Модуль 6.2 Что Такое Аналитическое Хранилище Данных?
В 95 процентах аналитических решений используется хранилище данных. Давайте будем считать, что это аналитическое хранилище данных. Но что это такое? Какие они бывают? Как давно они на рынке? На эти вопросы и другие я отвечу в это уроке. 

На этом уроке мы посмотрим фундаментальные вещи про хранилище данных, а на последующих уроках, мы будем уже пробовать различные решения хранилищ данных и ETL/ELT инструментов.  Практически каждый слайд можно трансформировать в вопрос для собеседования, и я сам, нираз, спрашивал на собеседованиях в Амазон эти вопросы на позицию инженера данных и bi разработчика.

Из модуля вы узнаете:
- История хранилищ данных
- База данных vs Хранилище данных
- Хранилище данных (DW) vs Платформа данных
- Характеристики хранилища данных
- Архитектура Shared Nothing vs Shared Everything
- Cloud vs On-premise Хранилища данных
- Облачная экономика на примере ETL jobs
- Open Source vs Commercial Хранилища данных
- Хранилища данных на базе существующей технологии (Postgres) или свои разработки
- Data warehouse as a Service или в ручную тюнить
- Современные и Legacy Хранилища данных
- OLTP vs OLAP
- ETL vs ELT
- Вендоры Хранилища данных на рынке (Gartner and Forrester)
- Сравнение скорости - benchmarking - TPC
- Benchmarking, отчет Gigaom и Fivetran по облачных хранилищам данных
- История Teradata
- Основы MPP Teradata, Data Distribution, Data Skew и Teradata CLI

**Видео лекция - теория** - [Что Такое Аналитическое Хранилище Данных?](https://youtu.be/JuQCUGUWqgU). 


### Вебинар от эксперта
- [GREENPLUM ЧТО ЗА ЗВЕРЬ И КАК ЕГО ПРИРУЧИТЬ / ДМИТРИЙ ПАВЛОВ](https://youtu.be/cVDIbEsCTow)

### Дополнительные материалы для изучения
- [Отчет по Gigaom DW Benchmarking](https://gigaom.com/report/data-warehouse-cloud-benchmark/)
- [Отчет Fivetran по DW Benchmarking](https://fivetran.com/blog/warehouse-benchmark)
- [Интересный и большой курс по Data Warehouse на Coursera - Data Warehousing for Business Intelligence Specialization](https://www.coursera.org/specializations/data-warehousing)
- [Как получить на Coursera доступ к полному курсу и сертификату бесплатно](https://medium.com/@snipsnapsnoop/%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%BD%D0%B0-coursera-%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF-%D0%BA-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%BC%D1%83-%D0%BA%D1%83%D1%80%D1%81%D1%83-%D0%B8-%D1%81%D0%B5%D1%80%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%82%D1%83-%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE-af9afb7b55e)

Интересные статьи по теме (необязательно все читать, но можно ознакомиться, теперь вы точно будете знать ключевые слова по теме)
- [Что такое Teradata?](https://habr.com/ru/post/209078/)
- [Поколоночное и гибридное хранение записей в СУБД Teradata](https://habr.com/ru/company/teradata/blog/170321/)
- [Oracle vs Teradata vs Hadoop](https://habr.com/ru/post/235465/)
- [Из нагруженной MPP СУБД — бодрый Data Lake с аналитическими инструментами: делимся подробностями создания](https://habr.com/ru/company/vtb/blog/420141/)
- [Колоночные СУБД — принцип действия, преимущества и область применения](https://habr.com/ru/post/95181/)
- [Сравнение аналитических in-memory баз данных](https://habr.com/ru/company/tinkoff/blog/310620/)
- [Колоночные СУБД против строчных, как насчет компромисса?](https://habr.com/ru/post/413051/)
- [Тестирование производительности Oracle In-Memory Option c использованием TPC-H Benchmark](https://habr.com/ru/post/317774/)
- [HP Vertica, первый запущенный проект в РФ, опыт полтора года реальной эксплуатации](https://habr.com/ru/post/190740/)
- [Business Intelligence на очень больших данных: опыт Yota](https://habr.com/ru/company/yota/blog/541266/)
- [HP Vertica, проектирование хранилища данных, больших данных](https://habr.com/ru/post/227111/)
- [Просто и доступно о аналитических БД](https://habr.com/ru/post/149641/)

### Лабораторная работа
На лабораторной работе вы будете использовать виртуальную мащину Teradata DW, вам нужно будет скачать ее и настроить доступ через конфигурацию сети. Дальше вы сможете загрузить данные через CLI инструмент и подключить Power BI. Таким образом у вас будет полноценное аналитическое решение (портативное), которое работает во многих компаниях.

**Видео лекция - практика** - [Что Такое Аналитическое Хранилище Данных? - практика](https://youtu.be/JuQCUGUWqgU?t=2766). 

[Ссылка на лабораторную работу к модулю 6.2](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module06/DE%20-%20101%20Labs/Teradata/Teradata%20Lab.md)

### Опциональное задание:
Вы можете использовать Pentaho DI, чтобы добавить ETL компомент в ваше аналитическое решение. Попробуйте реализовать задание из модуля 4 (любое или все).


## Модуль 6.3 Основы Amazon Redshift
Мы начнем наше погружение в современный мир аналитических хранилищ данных с Amazon Redshift. Этот продует появился в 2012 году и породил целую индустрию облачных продуктов и решений. Сам по себе Redshift прост и удобен, и если вы в облаке AWS, то скорей всего вы будете использовать Amazon Redshift. Я использовал его много раз на различных проектав в Амазоне и за пределами, и он никогда не подводил. С развитием другой облачной DW, в последние годы, Redshift получил много новых фич, такие как ML, разделение storage&compute, и многое другое.

Из видео вы узнаете:
- В чем заключается роль Инженера Данных
- В чем заключается роль BI инженера
- История Amazon Redshift
- S curve в технологическом прогрессе
- Решение по аналитики мобильного приложения на Amazon Redshift
- Решения миграции с Oracle DW на Amazon Redshift в Амазоне
- Дизайн таблиц и оптимизация производительности в Amazon Redshift
- Способы загрузки данных в Amazon Redshift (COPY, Bulk Insert, Row Insert)
- Работа с ETL или ELT для Amazon Redshift
- Утилиты для адмиинстрирования и мониторинга Amazon Redshift
- Встроенный ML для Amazon Redshift
- Про главный недостаток Amazon Redshift - колличество одновременных сессий
- Про Хранилище данных Амазон Алекса и трудности масштабирования
- Несколько примеров архитектуры из индустрии

**Видео лекция - теория** - [Основы Amazon Redshift](https://youtu.be/K0TOh-Pl3q0). 

В этом уроке я не показывал и не рассказывал про Amazon Redshift. По-сути это query engine (как Athena), который помогает нам писать SQL запросы к данные в S3 Data lake. То есть данные, которые находятся за пределами Amazon Redshift. Таким образом Amazon Redshift как бы lake house, но не такой удобный как Snowflake. Расскажу про него на модуле 8 или 9.

### Вебинар от эксперта
- [Путь Инженера Аналитики: Решение для Маркетинга / Артемий Козырь](https://youtu.be/SoOcvYPSm7o)

### Дополнительные материалы для изучения
- [Amazon Redshift Paper](https://homepages.cwi.nl/~manegold/UvA-ABS-MBA-BDBA-ISfBD/p1917-gupta.pdf)
- [Статья про S кривую и начало развития индустрии - The Modern Data Stack: Past, Present, and Future](https://blog.getdbt.com/future-of-the-modern-data-stack/)
- [Статья 2012 года! - Amazon Redshift: новое хранилище данных на петабайты ](https://habr.com/ru/post/160653/)
- [Мое выступление про 5 лет в Амазон](https://youtu.be/1lUhmSPdIJs)
- [Мое выступление на матемаркетинге 2018 года -  Роль BI-систем и DWH в маркетинге. Архитектура и кейсы](https://youtu.be/MVp7eTdwEyA)
- [Amazon Redshift Admin утилиты](https://github.com/awslabs/amazon-redshift-utils)
-[Мой пост про новое поколение Redshift - Meet a new generation of Redshift Data Platform — RA3](https://medium.com/rock-your-data/meet-a-new-generation-of-redshift-data-platform-ra3-e65544920866)
- [AWS Online Tech Talks - Getting Started with Amazon Redshift - AWS Online Tech Talks](https://youtu.be/dfo4J5ZhlKI)
- [AWS Redshift Architecture: Clusters & Nodes & Data Apps, oh my](https://www.intermix.io/blog/amazon-redshift-architecture/)
- [Гид по параллельному масштабированию Amazon Redshift и результаты тестирования](https://habr.com/ru/company/skyeng/blog/451538/)
- [Аналитический движок Amazon Redshift + преимущества Облака](https://habr.com/ru/company/wheely/blog/539154/)
- [Мое выступление в КРОК - Pizza as a service: как Amazon на Redshift мигрировал](https://habr.com/ru/company/croc/blog/481836/)

### Лабораторная Работа
На лабораторной работе вам нужно будет:
- Создать свой кластер Amazon Redshift
- Настроить сетевой доступ к нему и подключиться SQL Client - DBeaver
- Сгенерировать данные утилитой TPC, той самой, которую используют для benchmarking все вендоры баз данных
- Загрузить данные с использование COPY и манифеста
- Оптимизировать таблицы и запросы с использование функционала Redshift - Distribution, Sort, Compression и Encoding

1. __Лабораторна работа 1__ - генерация данных утилитой TPC в облаке AWS на виртуальной машине EC2 - [Создание выборки данных](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module06/DE%20-%20101%20Labs/AWS%20-%20Redshift/Generating_Datasets.md)
2. **Лабораторная работа 2** - [создание и настройка кластера, загрузка данных и оптимизаци](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module06/DE%20-%20101%20Labs/AWS%20-%20Redshift/Redshift_lab.md).

>Автор лабораторных работ Сергей Сволодарский, контакт в телеграмм @erfolg5862.

**Бонус задание:**
Так же, вы легко можете запустить другую виртуальную машину и установить на нее Tableau Server и/или ETL решение. Или вы можете подключить свои решения с локальной машины. Вы можете загрузить данные superstore и построить модель данных, как было в модуле 4. Возможности безграничны, все в ваших руках, и главное ничего нового!
 

## Модуль 6.4 Основы Azure Synapse для Хранилища данных
У Microsoft тоже есть облако Azure, и в нем есть целая платформа для аналитики, которая называется Azure Synapse Analytics. В него входят уже устоявшиеся инструменты Azure SQL Data Warehouse (теперь называется Dedicated SQL Pool), Azure Data Factory, Azure ML, Power BI Service, так и были добавлены новые Azure Spark Pools, Serverless SQL Pool. Все достаточно удобно, каждый инструмент легко интегрируется с решениями Azure. Если вы работаете с решениями Microsoft, то облако Azure это следующий логический шаг вашего развития. Так же Azure Synapse способен заменить решения Azure HDInsights и Azure Databricks (решения для big data). По опыту я знаю и видел огромное количество решений на Microsoft SQL Server (on-premise), но вообще не знаю ниодного решения на Azure Synapse, но уверен скоро их появится много.


В этом видео мы:
- Посмотрим на история Azure хранилища данных
- Узнаем про стратегию создания продуктов Microsoft
- Узнаем про переход от Azure SQL Data warehouse к Azure Synapse Analytics
- Познакомимся с Azure Synapse Analytics: Deidcated SQL Pools, Spark Pools, Serverl SQL Pools
- Azure Synapse Serverless Pools vs Amazon Redshift Spectrum
- Посмотрим на пример архитектурты Azure Data Platfrom и узнаем какие инстурменты есть в Azure для аналитики
- Детально посмотрим на особенности Azure Dedicated SQL Pools (бывшее Azure SQL DW), узнаем, что внутнри и как с ним работать и оптимизировать (distribution stiles, indexes, statistics)
- Узнаем, что такое PolyBase или как загружать данные из Azure Hadoop
- Узнаем про Azure Data Factory
- Поговорим про бесполезность и полезность Azure Analyses Services
- Поговорим про конкуренция Azure Databricks и Azure Synapse Spark pools

**Видео лекция - теория** - [Знакомство с Azure Synapse](https://youtu.be/gQAGa3xZr_M)

На лабораторных работах я вам покажу:
- Как создать Azure Synapse Workspace
- Как в нем создать Serverless SQL Pools, Dedicated SQL Pool (Azure DW)
- Посмотрим, что внутри Synapse Workspace
- Покажу вам, как можно поиграться с данными NY taxi
- Покажу, где взять открытые данные по COVID-19

**Видео лекция - практика** - [Демонстрация Azure Synapse Workspace и лабораторных работ с DW in a Day воркшопа](https://youtu.be/gQAGa3xZr_M?t=3082)

### Дополнительные материалы для изучения
- [Synapse Tutorials](https://docs.microsoft.com/en-us/azure/synapse-analytics/get-started)
- [Azure Naming conventions](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming)
- [Azure SQL DW paper - POLARIS: The Distributed SQL Engine in Azure Synapse](https://www.vldb.org/pvldb/vol13/p3204-saborit.pdf)
- [Моя статья для Matillion ETL - Creating a Modern Data Platform with Azure Synapse Analytics and Matillion ETL](https://www.matillion.com/resources/blog/creating-a-modern-data-platform-with-azure-synapse-analytics-and-matillion-etl)
- [Статья про Azure Synapse от Medium блоша Towards Data Science](https://towardsdatascience.com/tagged/azure-synapse-analytics)
- [Azure Synapse for Data Analytics — Create Workspaces with CLI](https://medium.com/microsoftazure/azure-synapse-for-data-analytics-create-workspaces-with-cli-bd5ef90fd489)
- [Introduction to Azure Synapse Analytics](https://medium.com/codex/introduction-to-azure-synapse-analytics-ff317e782f7b)
- [Azure Analytics: ясность в мгновение ока](https://habr.com/ru/company/microsoft/blog/503582/)

**Курсы от Курсеры и Microsoft, скорей всего вам дадут кредиты на облако Azure**
- [Introduction to Microsoft Azure Synapse Analytics](https://www.coursera.org/learn/introduction-to-microsoft-azure-synapse-analytics)
- [Data Warehousing with Microsoft Azure Synapse Analytics](https://www.coursera.org/learn/data-warehousing-with-microsoft-azure-synapse-analytics)
- [Azure Synapse SQL Pool - Implement Polybase](https://www.coursera.org/projects/azure-sql-pool-polybase)
- [Data Engineering with MS Azure Synapse Apache Spark Pools](https://www.coursera.org/learn/data-engineering-with-ms-azure-synapse-apache-spark-pools)
- [Modern Data Warehouse Analytics in Microsoft Azure](https://www.coursera.org/learn/data-warehouse-analytics-microsoft-azure)
- [Operational Analytics with Microsoft Azure Synapse Analytics](https://www.coursera.org/learn/operational-analytics-with-microsoft-azure-synapse-analytics)
- [Process Data with Microsoft Azure Synapse Link for Cosmo DB](https://www.coursera.org/projects/process-data-with-microsoft-azure-synapse-link-for-cosmo-db)


### Лабораторная Работа
В качестве домашнего задания вам нужно будет сделать одно-два из 4х заданий на выбор:
1. Сделать лабораторную работу по Synapse. Сергей Сволодарский приготовил для вас детальную инструкцию - [Azure Synapse Analyics Workshop](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module06/DE%20-%20101%20Labs/Azure%20-%20Synapse%20Analytics/Azure-Synapse.MD).
2. Попробовать сделать лаборатные работы Rock Your Data, на которые вы на примере разберете особенности дизайна таблиц.
	- [Лабораторные работы и файлы SQL из RYD labs](https://github.com/Rock-Your-Data/ryd-workshops/tree/master/Azure%20Cloud%20DW%20in%20a%20Day/Labs)
	- [Лабораторная работа по Azure SQL DW в формате PDF] (https://github.com/Rock-Your-Data/ryd-workshops/blob/master/Azure%20Cloud%20DW%20in%20a%20Day/Labs/Cloud%20DW%20in%20a%20Day%20_%20Labs.pdf)
4. Взять данные Superstore из модуля 1 и загрузить их в Azure Dedicated SQL pool (Azure DW) с использованием Azure Data Factory или Pentaho DI. Дальше по примеру модуля 4 вы можете создать таблицу фактов и таблицы измерения (схема звезда) и подключить BI инструмент - Power BI, Tableau или любой другой. Такое вот end-to-end решение.
	- [Данне Superstore из модуля 1]( https://github.com/Data-Learn/data-engineering/tree/master/DE-101%20Modules/Module01/DE%20-%20101%20Lab%201.1)
	- [Модуль 4 про Fact и Dimensions таблицы](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module04/DE%20-%20101%20Module04.md#%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C-44-2-etl-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%D1%8B-%D0%B8-%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D1%81-etl-%D0%BD%D0%B0-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D0%B5-pentaho-data-integration)
5. Сделать [Azure Synapse Tutorials](https://docs.microsoft.com/en-us/azure/synapse-analytics/get-started)

## Модуль 6.5 Основы Snowflake
Анилитическое хранилище данных Snowflake появилось в 2015 году и порвало всех конкурентов - on-premise (Oracle, Teradata, Netezza и др) и облачных (Redshift, Azure SQL DW, BigQuery). 


Продукт был создан с 0я выходцами и Оракл и они понимали проблемы индустрии и знали о возможностях облачных вычислений. И подарили нам замечательный продукт, где при помощи SQL, мы можем обрабатывать терабайты данных и не думать слишком много об организации данных. 

Snowflake одноверменно SMP и MPP, если вы смотрели другие уроки этого модуля, то вы должны знать, что это!;) Огромное спасибо команде снежинки за то, что они дали огромный пинок всей индустрии и заставили других вендоров шевелиться и улучшать их продукты. В Северной Америки снежинка в топе хранилищ данных среди организций и больше половины организаций от мало до велика использую снежинку как свое хранилище данных. 

Кстати, а вы знали, что Snowflake - это Lakehouse - смесь хранилища данных и озера данных? Теперь точно знаете!:) 
В этом видео вы узнает про:
- История Snowflake
- Материалы по изучения продукта
- Выход на IPO
- Кейсы миграции
- Архитектуру и особенности снежинки
- О продукта экосистемы снежники - SnowCLI, SnowPipe, SnowSight, SnowPark
- Ключевые фичи - Time Travel, Data Sharing, Zero Cloning
- Экосистему партнеров и конкурентов снежинки

**Видео лекция - теория** - [Основы Snowflake - The Elastic Data Warehouse](https://youtu.be/CzrOa15QbWk)

На hands-on работе:
- Я вам покажу как создать бесплатный кластер снежинки
- Загрузить данные SuperStore в хранилище данных
- Создать Database, Stage, IAM user (AWS)

**Видео лекция - практика** - [Демонстрация Snowflake](https://youtu.be/CzrOa15QbWk?t=2768)

### Вебинар от эксперта
- [SNOWFLAKE ИЛИ КАК БД ВЫБИРАЛИ / НИКОЛАЙ ГОЛОВ / MANYCHAT](https://youtu.be/XJa3gGWidg0)
- [DataVault / Anchor Modeling / Николай Голов](https://youtu.be/-ZgzpQXsxi0)
- [ЧАСТЬ 2 DataVault Anchor Modeling / Николай Голов](https://youtu.be/IZw1cB1uDts)

## Дополнительные материалы для изучения

- [The Snowflake Elastic Data Warehouse Paper](http://pages.cs.wisc.edu/~yxy/cs839-s20/papers/snowflake.pdf)
- [Snowflake, Anchor Model, ELT и как с этим жить](https://habr.com/en/company/manychat/blog/530054/)
- [Обзор первого эластичного хранилища данных Snowflake Elastic Data Warehouse](https://habr.com/en/company/lifestreet/blog/270167/)
- [Пример архитектуры аналитического решения с использованием платформы Snowflake](https://habr.com/en/company/epam_systems/blog/555102/)
- [Руководство по аналитике для основателя стартапа](https://habr.com/en/post/346326/)
- [Вебинар ДатаЛерн SNOWFLAKE ИЛИ КАК БД ВЫБИРАЛИ / НИКОЛАЙ ГОЛОВ / MANYCHAT](https://youtu.be/XJa3gGWidg0)

### Лабораторная Работа

В качестве лабораторной работы вы можете:
- Выполнить оффициальные [tutorial Snowflake](https://www.snowflake.com/snowflake-essentials-training/), но уже переведнный Сергеем для вас - [Snowflake Workshop](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module06/DE%20-%20101%20Labs/Snowflake/snowflake-lab.md)
- Сделать близкий к реальному кейс с SalesForce, Fivetran, Snowflake, Tableau - [Zero To Snowflake](https://github.com/DecisiveData/ZeroToSnowflake)
- Зарегистрироваться и пройти бесплатные курсы [Snowflake Data Academy](https://www.snowflake.com/data-cloud-academy/)

## Модуль 6.6 Обзор современных ETL/ELT инструментов
ETL(ELT) инструменты нам нужны, чтобы наполнять наше хранилище данных, ну или платформу данных. Для современных аналитических инструментов лучше использовать современные инструменты интеграции. Прежде чем выбирать инструмент, нужно понимать фундаментальные основы построения аналитического решения, его слои и компоненты, разницу между ETL и ELT, между Batch и Stream, между on-premise и cloud и многое другое. Задача инженера данных выбрать правильное решение для обработки и хранения данных.

В этом видео:
- Рассмотрим простой пример интернет-магазина и необходимости интеграции данных и аналитического решения
- Что такое Data Pipeline?
- ETL App или Coding? (Python, Scala и тп)
- ETL on-premise и Cloud (AWS, Azure, GCP)
- ETL разработчик или Data Engineer
- Open Source or Not Open Source
- Архитектура современного решения с использованием On-premise tools
- Архитектура современного решения с использованием коммерческих продуктов
- Обзор решений западного рынка
- Пример ETL vs ELT с использованием Pentaho DI и Redshift
- ETL Job = DAG (Direct Acyclic Graph)
- Обзор решений: MatillionETL, Fivetran, Apache Airflow, Azure Data Factory, AWS Glue 

**Видео лекция - теория** - [Основы Snowflake - The Elastic Data Warehouse](https://youtu.be/4PA6IPO4P1A)

На лабораторной работе я покажу как запустить Matillion ETL, DBT cloud, Talend, Informatica, ETL Leap, Qlikview через Snowflake Partner Connect. Особенно детально я покажу как выглядит Matillion ETL и как вы можете выполнить задание 4го модуля по Superstore Star Schema (dimensional modelling) в Matillion ETL. 

**Видео лекция - практика** - [Запуск ETL/ELT из Snowflake Partner Connect](https://youtu.be/4PA6IPO4P1A?t=2835)


### Дополнительные материалы для изучения
- [Вебинар Data Learn - Введение в Apache Airflow](https://youtu.be/cVDIbEsCTow)
- [Код для вебинара](https://github.com/dmitry-brazhenko/airflow_tutorial)
- [Презентация вебинара](https://docs.google.com/presentation/d/1fpKEyoZul6hz2wR4idvHF1FGSoG078TMwwvm3f0yQeI/edit#slide=id.gf7633a37fa_0_20)

### Вебинар от эксперта
- [ВВЕДЕНИЕ В AIRFLOW / ПОНЯТИЕ DAG'а / НАСТРОЙКА DAG'а В AIRFLOW](https://youtu.be/cVDIbEsCTow)
- [ВВЕДЕНИЕ В ДОКЕР КОНТЕЙНЕР / DOCKER / ДМИТРИЙ БРАЖЕНКО](https://youtu.be/JQCTjz_PzSM)


### Лабораторная Работа
Для лабораторной работы вам нужно:
	- Любое современное хранилище данных: Snowflake, Redshift, Synapse, BigQuery, Firebolt
	- ETL/ELT инструмент
	- BI

1. Вам нужно загрузить данных из S3/Azure Storage/Google Storage в DW - Staging (вы можете использовать данные Superstore из модуля 4)
2. Преобразовать данные из Staging в Fact таблицу(ы) и таблицы измерений
3. Подключить BI инструмент (JDBC/ODBC драйвер)
4. Нарисовать архитектуру решения в Draw.io

## Модуль 6.7 Анти SQL решения для операционной аналитики

В этом уроке мы узнаем про термин Операционная Аналитика, и чем он отличается от традиционной аналитики. Заодно мы посмотрим на три самых популярных решения на рынке – Splunk, Azure Data Explorer и Kusto. Если кратко, то такие системы и решения не являются главными для Инженера Данных или BI инженера. Для BI инженера операционная аналитика – это про еще один источник данных, с которым придется работать. А для инженера данных, решения операционной аналитики могут был полезны по многим причинам, мы можем собирать машинные данные (логи) о работе наших data pipelines, ETL, Big Data и тп, мы можем забирать данные из решений операционной аналитики и загружать в хранилище данных или озеро. А иногда, нас просят создать NoSQL решение данных на основе Elastic Stack. (меня не просили никогда, но вдруг!)

В этом видео вы узнаете:

- Что такое операционная аналитика и ее роль в решениях BI/DW/BigData
- Основы и историю Splunk
- Про Azure Data Explorer и Kusto
- Про Elastic Stack
- Основные кейсы использования операционной аналитики и примеры из опыта
**Видео лекция - теория** - [Анти SQL решения для операционной аналитики](https://youtu.be/uDwgJGYI8Mw)

На лабораторной работе я покажу как Splunk и Azure Data Explorer.

**Видео лекция - практика** - [Анти SQL решения для операционной аналитики - демо](https://youtu.be/uDwgJGYI8Mw?t=2349)

### Вебинар от эксперта
- [ADX(KUSTO): INTERACTIVE BIG DATA ANALYTICS / GOR HAYRAPETYAN](https://youtu.be/CAdkL9vM6Do)

### Дополнительные материалы для изучения

- [Вебинар Data Learn про Azure Data Explorer](https://youtu.be/CAdkL9vM6Do)
- [Elastic Search Tutorial]( https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html)
- [Splunk Tutorial]( https://docs.splunk.com/Documentation/Splunk/8.2.3/SearchTutorial/WelcometotheSearchTutorial)
- [Splunk уходит из России (совсем)](https://habr.com/ru/post/441004/)
- [Год без Splunk — как американская компания изменила рынок аналитики машинных данных в РФ и кого оставила после себя](https://habr.com/ru/post/484904/)
- [Splunk — общее описание платформы, базовые особенности установки и архитектуры]( https://habr.com/ru/company/tssolution/blog/323814/)
- [Quickstart: Create an Azure Data Explorer cluster and database](https://docs.microsoft.com/en-us/azure/data-explorer/create-cluster-database-portal)
- [1.Elastic stack: анализ security логов. Введение]( https://habr.com/ru/company/tssolution/blog/480570/)
- [2. Elastic stack: анализ security логов. Logstash]( https://habr.com/ru/company/tssolution/blog/481960/)
- [3. Elastic stack: анализ security логов. Дашборды]( https://habr.com/ru/company/tssolution/blog/482054/)

### Лабораторная Работа

На лабораторной работе вам нужно установить одно из 3х решений, загрузить данные и визуализировать результат. Можно использовать tutorial.


## Модуль 6.8 Обзор профессий и требований

В заключительном уроке нашего модуля про аналитические хранилища данных мы посмотрим на пример описаний вакансий инженера данных на hh.ru, linkedin, indeed.com/worldwide. Так же покажу, как я сканирую вакансии и понимаю сходу насколько хорошая или плохая вакансия по описанию. Все верно - "встречают по одежке!"

**Видео лекция - теория** - [Обзор профессий и требований](https://youtu.be/xXpoegKJUYU)



По окончанию модуля 6, вы можете расшарить значок `06 | Cloud DW` в социальных сетях и рассказать о своих достижениях. 

![img](https://github.com/Data-Learn/data-engineering/blob/master/img/de101-module06.png)

А также добавить в Linkedin сертификат:

![img](https://github.com/Data-Learn/data-engineering/blob/master/img/linkedin06cloud.PNG.jpg)
Другие доступные сертификаты можете посмотреть в этом [linkedin профайле](https://www.linkedin.com/in/lana-naumova-8a1b78171/).


PS Если материал оказался полезным, вы можете поддержать авторов через 
[ЮMoney](https://yoomoney.ru/to/4100116864248269) или [Patreon](https://www.patreon.com/dmitryanoshin) или [Paypal](https://paypal.me/dmitryanoshin)

