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

На этом уроке мы посмотрим фундаментыльные вещи про хранилище данных, а на последующих уроках, мы будем уже пробовать различные решения хранилищ данных и ETL/ELT инструментов.  Практически каждый слайд можно трансформировать в вопрос для собеседования, и я сам, нераз, спрашивал на собеседованиях в Амазон эти вопросы на позицию инженера данных и bi разработчика.

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

**Видео лекция - теория** - [Введение](https://youtu.be/JuQCUGUWqgU). 

### Дополнительные материалы для изучения
- [Отчет по Gigaom DW Benchmarking](https://gigaom.com/report/data-warehouse-cloud-benchmark/)
- [Отчет Fivetran по DW Benchmarking](https://fivetran.com/blog/warehouse-benchmark)
- (Интерсный и большой курс по Data Warehouse на Coursera - Data Warehousing for Business Intelligence Specialization)[https://www.coursera.org/specializations/data-warehousing]
- (Как получить на Coursera доступ к полному курсу и сертификату бесплатно)[https://medium.com/@snipsnapsnoop/%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%BD%D0%B0-coursera-%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF-%D0%BA-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%BC%D1%83-%D0%BA%D1%83%D1%80%D1%81%D1%83-%D0%B8-%D1%81%D0%B5%D1%80%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%82%D1%83-%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE-af9afb7b55e]

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
На лабораторной работе вы будете использовать виртуальную мащину Teradata DW, вам нужно будет скачать ее и настроить доступ через конфигурацию сети. Дальше вы сможете загрузать данные через CLI инструмент и подключить Power BI. Таким образом у вас будет полноценное аналитическое решение (портативное), которое работает во многих компаниях.

**Видео лекция - практика** - [Введение](https://youtu.be/JuQCUGUWqgU?t=2766). 

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

>Автор лабораторных работ Сергей Сволодарский, конакт в телеграмм @erfolg5862.

**Бонус задание:**
Так же, вы легко можете запустить другую виртуальную мащину и установить на нее Tableau Server и/или ETL решение. Или вы можете подключить свои решения с локальной машины. Вы можете загрузить данные superstore и построить модель данных, как было в модуле 4. Возможности безграничны, все в ваших руках, и главное ничего нового!
 

## Модуль 6.4 Основы Azure Synapse для Хранилища данных



### Дополнительные материалы для изучения



### Лабораторная Работа


### Лабораторная Работа


## Модуль 6.5 Основы Snowflake


## Дополнительные материалы для изучения

### Лабораторная Работа

## Модуль 6.6 Обзор современных ETL/ELT инструментов

### Дополнительные материалы для изучения

### Лабораторная Работа

## Модуль 6.7 Анти SQL решения для операционной аналитики


### Дополнительные материалы для изучения


## Модуль 6.8 Обзор профессий и требований


### Дополнительные материалы для изучения



По окончанию модуля 6, вы можете расшарить значок `06 | Cloud DW` в социальных сетях и рассказать о своих достижениях. 

![img]()

А также добавить в Linkedin сертификат:

![img]()
Все доступные сертификаты можете посмотреть в этом [linkedin профайле](https://www.linkedin.com/in/lana-naumova-8a1b78171/).


PS Если материал оказался полезным, вы можете поддержать авторов через 
[ЮMoney](https://yoomoney.ru/to/4100116864248269) или [Patreon](https://www.patreon.com/dmitryanoshin) или [Paypal](https://paypal.me/dmitryanoshin)

