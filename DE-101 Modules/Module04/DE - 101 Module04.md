# Модуль 4:  Интеграция и трансформация данных - ETL и ELT

[Обратно в содержание курса :leftwards_arrow_with_hook:](https://github.com/Data-Learn/data-engineering/blob/master/DE%20-%20101%20Guide.md) 

В 4-ом модуле нашего курса вы узнаете про интеграцию и трансформацию данных - ETL и ELT. Это ключевой элемент в аналитическом решении, с помощью которого мы наполняем данными хранилище данных и автоматизируем загрузку и трансформацию данных. Мы рассмотрим примеры популярных on-premise batch решений. Узнаете в чем отличие ETL от ELT, для чего нужны такие решения, что значит batch и on-premise, как с помощью ETL/ELT можно создавать модели данных, на примере dimensional modeling, рассмотрим рынок ETL/ELT. Потренируюмся на классическом open-source ETL решении Pentaho DI и рассмотрим настольный инструмент от Tableau - Tableau Prep. 

## Модуль 4.1 Введение

**Видео лекция - теория** - [Введение](https://youtu.be/VPFf8Ck_AUU). 

## Модуль 4.2 Что такое ETL и ELT? 

Мы часто слышим термин ETL, а иногда мы слышим про ELT. Это неотъемлемая часть любого аналитического решения, когда необходимо консолидировать данные из различных систем источников (Source) в едином месте, обычно, корпоративное  или аналитическое хранилище данных (DW, которое является target для нас). Так же есть термин data pipeline, mapping и другие. Помимо терминов, есть еще роли - ETL разработчик и Data Engineer. В этом видео мы попробуем разобраться, что такое ETL, как термин и как инструмент. 

**Видео лекция - теория** - [Что такое ETL и ELT?](https://youtu.be/3IRU-E_BnYc). 

### Дополнительные материалы для изучения
1. [What is ETL?](https://medium.com/hashmapinc/etl-understanding-it-and-effectively-using-it-f827a5b3e54d) (English)
2. [Введение в Data Engineering. ETL, схема «звезды» и Airflow](https://habr.com/ru/company/newprolab/blog/358530/) (Русский)
3. [Основные функции ETL-систем](https://habr.com/ru/post/248231/) (Русский)
4. [SQL Server Integration Services (SSIS) для начинающих – часть 1 (ETL от Microsoft)](https://habr.com/ru/post/330618/) (Русский)
5. [Как было устроено хранилище DWH в TELE2](https://habr.com/ru/post/463245/) (Русский) `вы уже должны быть в состоянии прочесть диаграмму в статье`
6. [Нужен ли вашей команде Data Engineer?](https://habr.com/ru/company/skyeng/blog/439504/) (Русский)
7. [Метрики Хранилища Данных](https://habr.com/ru/post/144568/) (Русский)


## Модуль 4.3 Обзор рынка решений ETL

Инструментов для интеграции и трансформации данных (ETL/ELT) существует огромное множество. В этом уроке мы рассмотрим самые популярные решения на рынке и разделим их на типы по цене и удобству. 

**Видео лекция - теория** - [Обзор рынка ETL решений](https://youtu.be/wksfXoeNO7Y). 

### Дополнительные материалы для изучения
1. [Data Build Tool или что общего между Хранилищем Данных и Смузи](https://habr.com/ru/company/otus/blog/501380/) (Русский)
2. [Словарь модели данных](https://habr.com/ru/company/mkb/blog/470153/) (Русский)
3. [Airflow — инструмент, чтобы удобно и быстро разрабатывать и поддерживать batch-процессы обработки данных](https://habr.com/ru/company/mailru/blog/339392/) (Русский)
4. [Apache NiFi: что это такое и краткий обзор возможностей](https://habr.com/ru/company/rostelecom/blog/432166/) (Русский)
5. [Работа c Talend Open Studio на примере парсинга CSV файла](https://habr.com/ru/post/338352/) (Русский) 
6. [Getting Started with AWS Glue ETL](https://youtu.be/z3HeHlWg88M) (English)
7. [Azure Data Factory Tutorial | Introduction to ETL in Azure](https://youtu.be/EpDkxTHAhOs) (English)
8. [Matillion: Orchestrating Data Flows and Transformations on AWS](https://youtu.be/ip004IMIacQ) (English)
9. [What is Fivetran?](https://youtu.be/OEM0-_g6o94) (English)

### Практика
Вам необходимо скачать и запустить Pentaho Data Integration Community Edition. Это бесплатный ETL инструмент, который работает на Windows, Linux и Mac. Вы можете скачать его [отсюда](https://sourceforge.net/projects/pentaho/). Pentaho DI требует установку Java 8. Попробуйте скачать архив и распаковать его. Вам нужно запустить spoon.sh для Linux/Mac и spoon.bat для Windows. У меня на Mac есть, например, иконка, `Data integration`. Если появятся вопросы, то задавайте их в Slack канале `#de-module04-cohort1`

## Модуль 4.4 2 ETL Компоненты и начало работы с ETL на примере Pentaho Data Integration

Мы уже должны понимать основные компоненты любого аналитического решения для больших и маленьких данных - это BI/DW/ETL. Понимать концептуально. В этом уроки мы поговорим про ETL решения и про требования и рекомендации, которые неплохо продумать перед началом создания data pipelines или data integration. Так же мы узнаем основные элементы open-source решения - Pentaho DI и потренируемся выполнять упражнения 2го модуля с помощью UI ETL инструмента.

**Видео лекция - теория** - [ETL Компоненты](https://youtu.be/-oCBttnefMQ). 

**Видео лекция - практика** - `Начало работы с Pentaho DI`

### Практика
В качестве практики вам необходимо:
1. Скачать и запустить Pentaho DI, [отсюда](https://sourceforge.net/projects/pentaho/).
2. [Скачать мои примеры Pentaho jobs](https://github.com/Data-Learn/data-engineering/tree/master/DE-101%20Modules/Module04/DE%20-%20101%20Lab%204.4) для `Staging` и `Dimension Tables` и доделать их, чтобы получить такойже результат, как в модуле 2.
3. Создайте еще одну трансформацию, в которой вы создатите `sales_fact` таблицу

## Модуль 4.5 34 ETL Подсистемы и Техники хранилищ данных в Pentaho DI

## Модуль 4.6 Другие ETL инструменты

## Проект по ETL
