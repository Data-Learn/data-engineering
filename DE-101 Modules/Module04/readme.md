# Модуль 4:  Интеграция и трансформация данных - ETL и ELT

[Обратно в содержание курса :leftwards_arrow_with_hook:](https://github.com/Data-Learn/data-engineering/blob/master/DE%20-%20101%20Guide.md) 

В 4-ом модуле нашего курса вы узнаете про интеграцию и трансформацию данных - ETL и ELT. Это ключевой элемент в аналитическом решении, с помощью которого мы наполняем данными хранилище данных и автоматизируем загрузку и трансформацию данных. Мы рассмотрим примеры популярных on-premise batch решений. Узнаете в чем отличие ETL от ELT, для чего нужны такие решения, что значит batch и on-premise, как с помощью ETL/ELT можно создавать модели данных, на примере dimensional modeling, рассмотрим рынок ETL/ELT. Потренируемся на классическом open-source ETL решении Pentaho DI и рассмотрим настольный инструмент от Tableau - Tableau Prep. 

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

Павел Новичков, куратор 4-го модуля и ETL специалист, записал видео по установке Pentaho DI на примере Windows 10, с которым вы можете ознакомиться [здесь](https://www.youtube.com/watch?v=RL-EZCi51gc&feature=youtu.be&ab_channel=DataLearn)

## Модуль 4.4 2 ETL Компоненты и начало работы с ETL на примере Pentaho Data Integration

Мы уже должны понимать основные компоненты любого аналитического решения для больших и маленьких данных - это BI/DW/ETL. Понимать концептуально. В этом уроки мы поговорим про ETL решения и про требования и рекомендации, которые неплохо продумать перед началом создания data pipelines или data integration. Так же мы узнаем основные элементы open-source решения - Pentaho DI и потренируемся выполнять упражнения 2-го модуля с помощью UI ETL инструмента.

**Видео лекция - теория** - [ETL Компоненты](https://youtu.be/-oCBttnefMQ). 

**Видео лекция - практика** - [Начало работы с Pentaho DI](https://youtu.be/-oCBttnefMQ?t=2087)

[Видео по основам Pentaho DI](https://youtu.be/K3X9wIC0jO8) от Павла Новичкова и [ссылка на исходные файлы из видео](https://drive.google.com/file/d/1yw0E7Gqm4Rocui_pQYPdfmmnFtGfx3LY/view?usp=sharing)

### Практика
В качестве практики вам необходимо:
1. Скачать и запустить Pentaho DI, [отсюда](https://sourceforge.net/projects/pentaho/).
2. [Скачать мои примеры Pentaho jobs](https://github.com/Data-Learn/data-engineering/tree/master/DE-101%20Modules/Module04/DE%20-%20101%20Lab%204.4) для `Staging` и `Dimension Tables` и доделать их, чтобы получить такой же результат, как в модуле 2.
3. Создайте еще одну трансформацию, в которой вы создадите `sales_fact` таблицу

------
**Подсказка для пользователей MacOS:**
Всё, что показано в видео выше выполняется аналогично и на Windows и на MacOS, кроме двух моментов:
  * Установка PentahoDI. Можно посмотреть подробнее в [этой статье.](https://medium.com/@originaleye/how-to-install-pentaho-8-2-on-a-mac-4e4f8d526df2)
  * Загрузка файла *Sample - Superstore.xls* через командную строку. Для этого используйте команду:

        curl -s -o <директория_куда_сохранится_файл>/<указать_имя_файла> -L <ссылка_на_файл_в_интернете>

    Например: 

        curl -s -o /Users/dm/Documents/Pentaho-Demo/source/sample-superstore-shell.xls -L https://github.com/Data-Learn/data-engineering/raw/master/DE-101%20Modules/Module01/DE%20-%20101%20Lab%201.1/Sample%20-%20Superstore.xls


## Модуль 4.5 34 ETL Подсистемы

Согласно Ральфу Кимбаллу (тот самый, который изобрел Dimensional Modeling), существует 34 ETL подсистемы, которые делятся на 4 основных категории:
- **Data Extracting** (получить данные из систем - E в ETL)
- **Cleaning and Conforming Data** (интеграция данных и подготовка к загрузке в DW - T в ETL)
- **Delivering Data for Presentation** (обработка данных в DW - L в ETL)
- **Managing the ETL environment** (управление и мониторинг компонентов ETL)

Само по себе понятие ETL подсистема - это некая абстракция. Не нужно копать глубоко. Как правило - это либо компонент ETL решения, например готовый компонент в Pentaho DI для создания SCD Type 2 (подсистема 9) или компонент для создания последовательности чисел, в случае необходимости генерации суррогатных ключей (подсистема 10). Это может быть функциональность ETL инструмента для обработки ошибок (подсистема 5) или возможность мониторинга выполнения ETL job (подсистема 27). 

В этом уроке мы рассмотрим все 34 ETL подсистемы и при необходимости вы можете изучить их более детально.

**Видео лекция - теория** - [ETL Подсистемы](https://youtu.be/iiFHHbajrdE). 

В качестве практики мы с вами рассмотрим упражнения из книги [Pentaho Data Integration Beginner's Guide - Second Edition](https://github.com/happyapple668/gavin-repo/blob/master/books/BI/Kettle/Pentaho%20Data%20Integration%20Beginner's%20Guide%2C%20Second%20Edition.pdf) глава 8 и 9 - работа с базой данных. Мы планируем записать отдельное видео и инструкцию. Если вы хотите самостоятельно решить упражнение, то вы можете найти данную книгу и приступить к упражнениям. Если вы хотите более детально разобраться, то можете приступать к прочтению этой книги. Я сохранил все материалы для лабораторных работ в нашем [git](https://github.com/Data-Learn/data-engineering/tree/master/DE-101%20Modules/Module04/DE%20-%20101%20Lab%204.5).

### Дополнительные материалы для изучения

1. [Pentaho Kettle Solutions](https://github.com/kyosuke1018/tips/blob/master/Wiley%20Pentaho%20Kettle%20Solutions%2C%20Building%20Open%20Source%20ETL%20Solutions%20with%20Pentaho%20Data%20Integration%20(2010).pdf) (English) `отсюда я брал описание ETL подсистем`
2. [Pentaho Data Integration Beginner's Guide - Second Edition](https://github.com/happyapple668/gavin-repo/blob/master/books/BI/Kettle/Pentaho%20Data%20Integration%20Beginner's%20Guide%2C%20Second%20Edition.pdf) (English) `практика основ ETL на примере Pentaho DI`
3. [Архитектура хранилищ данных: традиционная и облачная](https://habr.com/ru/post/441538/) (Русский)
4. [Subsystems of ETL Revisited](https://www.kimballgroup.com/2007/10/subsystems-of-etl-revisited/) (English)
5. [What are Slowly Changing Dimensions?](https://www.datawarehouse4u.info/SCD-Slowly-Changing-Dimensions.html) (Русский)
6. [Медленно меняющиеся измерения](https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B4%D0%BB%D0%B5%D0%BD%D0%BD%D0%BE_%D0%BC%D0%B5%D0%BD%D1%8F%D1%8E%D1%89%D0%B8%D0%B5%D1%81%D1%8F_%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D1%8F) (Русский)
7. [Версионность и история данных](https://habr.com/ru/post/101544/) (Русский)
8. [Data Warehousing - 34 Kimball Subsytems](https://datacadamia.com/data/warehouse/subsystem) (English)

### Практика
1. В качестве практики вам необходимо выявить 8-10 подсистем в ETL Pentaho DI и написать небольшой отчет, в котором вы приложите print screen компонента (ETL подсистемы) и напишите про его свойства. Результат сохраните в вашем Git.
2. Самостоятельно попробовать сделать упражнения из главы 9 книги `Pentaho Data Integration Beginner's Guide - Second Edition`. В книге вы найдете необходимую информацию по установки тестовой базы данных. Я сохранил все материалы для лабораторных работ в нашем [git](https://github.com/Data-Learn/data-engineering/tree/master/DE-101%20Modules/Module04/DE%20-%20101%20Lab%204.5).
Это достойная задача для будущего ETL разработчика или Инженера Данных.

## Модуль 4.6 Data Prep на примере Tableau Prep и Alteryx
С ETL/ELT мы более-менее разобрались. К счастью или к сожалению, на сегодняшний день существует огромное количество программ для интеграции и трансформации данных. Некоторые программы относятся к классу Data Prep. Я их называю настольными ETL инструментами для бизнес пользователей. Если BI инструмент нам позволяет с помощью drag and drop создать красивый дашборд, то data prep позволит нам подготовить данные для BI. 

**Видео лекция - теория** - [Data Prep на примере Tableau Prep и Alteryx](https://youtu.be/KfuY2J9h5B0). 

**Видео лекция - практика** - [Установка и Обзор Tableau Prep и Alteryx](https://youtu.be/KfuY2J9h5B0?t=900)

### Дополнительные материалы для изучения
1. [Начало работы с Tableau prep](https://help.tableau.com/current/prep/en-us/prep_get_started.htm) (English)
2. [Начало работы с Alteryx Designer](https://help.alteryx.com/learn/learningguide.html) (English)

### Практика
Вам необходимо построить `Tableau Prep Flow` или `Alteryx Workflow` и сохранить результат в своем `git`. Вы можете использовать данные `Sales Superstore` из модуля 1 и 2 или подключиться к БД Postgres (из 2-го и 3го модуля), в которую мы загружали данные. Альтернативно вы можете просто повторить существующие задания из Alteryx/Tableau tutorial, чтобы понять как работает инструмент.

**Для пользователей MacOS** (для windows есть инфо в видео): Если у Вас истёк срок действия пробной лицензии на Tableau Desktop после работы над 3-м модулем, можно скачать Tableau Prep и активировать для него отдельную пробную версию.

## Модуль 4.7 Fancy ETL инструменты

Моя любимая категория иснтрументов "Fancy", то есть чем-то не обычные, но очень популярные. В нашем уроке я упомяну 4 самых популярных иснтрумента, к тому open source. Я с ними плотно не работал, поэтому я лишь слегка их коснусь, чтобы вы знали об их существовании и по возможности попробовали. Ну а если вы уже про них знаете, то приходите к нам поделится опытом!


**Видео лекция - теория** - [Fancy ETL инструменты](https://youtu.be/SYeU8EZEO-k). 


**Запись вебинара c Экспертом** 
[Путь Инженера Аналитики: Решение для Маркетинга / Артемий Козырь и обзор DBT tool](https://youtu.be/SoOcvYPSm7o)

### Дополнительные материалы для изучения

#### Apache Airflow
1. [Введение в Apache Airflow](https://khashtamov.com/ru/apache-airflow-introduction/) (Русский)
2. [Как мы оркестрируем процессы обработки данных с помощью Apache Airflow](https://habr.com/ru/company/lamoda/blog/518620/) (Русский)
3. [Apache Airflow: делаем ETL проще](https://habr.com/ru/post/512386/) (Русский)
4. [ETL процесс получения данных из электронной почты в Apache Airflow](https://habr.com/ru/post/495676/) (Русский)
5. [Getting started with Apache Airflow](https://towardsdatascience.com/getting-started-with-apache-airflow-df1aa77d7b1b) (English)
#### Apache NiFi
1. [Apache NiFi: что это такое и краткий обзор возможностей](https://habr.com/ru/company/rostelecom/blog/432166/) (Русский)
2. [Динамическое создание кластера Apache NiFi](https://habr.com/ru/post/331444/) (Русский)
3. [Apache NIFI — Краткий обзор возможностей на практике](https://habr.com/ru/post/465299/) (Русский)
4. [How Apache Nifi works — surf on your dataflow, don’t drown in it](https://medium.com/free-code-camp/nifi-surf-on-your-dataflow-4f3343c50aa2)
5. [Побег от скуки — процессы ETL](https://habr.com/ru/post/508620/) (Русский)
#### Data Build Tool (dbt) tool 
1. [Data Build Tool или что общего между Хранилищем Данных и Смузи](https://habr.com/ru/company/otus/blog/501380/) (Русский)
2. [DBT: A new way to transform data and build pipelines at The Telegraph](https://medium.com/the-telegraph-engineering/dbt-a-new-way-to-handle-data-transformation-at-the-telegraph-868ce3964eb4) (English)
3. [What, exactly, is dbt?](https://blog.getdbt.com/what--exactly--is-dbt-/) (English)
4. [Работа с dbt на базе Google BigQuery](https://habr.com/ru/post/542008/) (Русский)
5. [Сквозная Аналитика на Azure SQL + dbt + Github Actions + Metabase](https://habr.com/ru/post/538106/) (Русский)

#### Luigi
1. [Строим Data Pipeline на Python и Luigi](https://khashtamov.com/ru/data-pipeline-luigi-python/) (Русский)
2. [Обзор фреймворка Luigi для построения последовательностей выполнения задач](https://habr.com/ru/company/otus/blog/339904/) (Русский)
3. [Airbnb’s Airflow Versus Spotify’s Luigi](https://medium.com/better-programming/airbnbs-airflow-versus-spotify-s-luigi-bd4c7c2c0791) (English)
4. [Data pipelines, Luigi, Airflow: everything you need to know](https://towardsdatascience.com/data-pipelines-luigi-airflow-everything-you-need-to-know-18dc741449b7) (English)

### Вебинары с экспертами
- [ВВЕДЕНИ В DBT / СОЗДАНИЕ МОДЕЛЕЙ ПРИ ПОМОЩИ DBT / УПРАВЛЕНИЕ ТРАНСФОРМАЦИЕЙ ДАННЫХ / РИШАТ МИНГАЗОВ](https://youtu.be/btaH7P0U_2g)
- [ЧАСТЬ 1 - ВВЕДЕНИЕ В AIRFLOW / ПОНЯТИЕ DAG'а / НАСТРОЙКА DAG'а В AIRFLOW](https://youtu.be/cVDIbEsCTow)
- [ЧАСТЬ 2 - ВВЕДЕНИЕ В ДОКЕР КОНТЕЙНЕР / DOCKER / ДМИТРИЙ БРАЖЕНКО](https://youtu.be/JQCTjz_PzSM)


### Практика
Вы можете выполнить один или несколько tutorial(s), чтобы попробовать `fancy etl` в деле. Это будет прекрасный пример вашего интереса к данному вопросу, который вы можете продемонстрировать на собеседовании и рассказать, как вы любите пробовать новые инструменты и изучать их особенности:
1. [Apache Airflow tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html) и [Airflow tutorial 1: Introduction to Apache Airflow](https://youtu.be/AHMm1wfGuHE)
2. [Apache Nifi tutorial](https://nifi.apache.org/docs/nifi-docs/html/getting-started.html)
3. [dbt tool tutorial](https://docs.getdbt.com/docs/introduction/) и [dbt (data build tool) Tutorial from Fishtown Analytics](https://youtu.be/M8oi7nSaWps)
4. [Luigi tutorial](https://luigi.readthedocs.io/en/stable/)
5. [Clickhouse tutorial](https://clickhouse.tech/docs/ru/getting-started/tutorial/)

А также вы сможете взять данные из модуля 2 по Superstore на Postres и использвать инструменты выше, чтобы получить результат. Это уже серьезная заявка на звание Data Engineer.

## Модуль 4.8 Требования к ETL разработчику и отличия от Data Engineer

Практически в описание к любой data вакансии мы можем встретить термин ETL. ETL роль очень важная, так как эти процессы отвечают за консолидацию данных в едином хранилище данных, а в некоторых случаях это может быть озеро данных. Концептуально вакансия ETL разработчик/инженер Data Engineer очень похоже, разница лишь в скилах и названии позиции. 

**Видео лекция - теория** - [Требования к ETL разработчику и отличия от Data Engineer](https://youtu.be/YF15Nh7DdOs). 

## Заключительный Проект по ETL
Павел Новичков подготовил для вас интересный проект на Pentaho DI.

Пожалуйста пройдите [опрос по завершении Модуля 4](https://forms.gle/F5EgyonrpUcunm6ZA). Так я смогу посмотреть, сколько человек закончило модуль, что было хорошо, а что можно улучшить.

По окончанию модуля 4, вы можете расшарить значок `04 | ETL` в социальных сетях и рассказать о своих достижениях. 

![img](https://github.com/Data-Learn/data-engineering/blob/master/img/de101-module04.png)

**PS Если материал оказался полезным, вы можете поддержать авторов через**
[ЮMoney](https://yoomoney.ru/to/4100116864248269) или [Patreon](https://www.patreon.com/dmitryanoshin) или [Paypal](https://paypal.me/dmitryanoshin)
