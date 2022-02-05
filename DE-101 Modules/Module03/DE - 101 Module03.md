# Модуль 3: Визуализация данных, дашборды и отчетность - Business Intelligence.

[Обратно в содержание курса :leftwards_arrow_with_hook:](https://github.com/Data-Learn/data-engineering/blob/master/DE%20-%20101%20Guide.md) 

В 3-ом модуле нашего курса вы узнаете про системы Business Intelligence. Мы рассмотрим примеры из реальной жизни, популярные инструменты BI - Tableau, Power BI и другие. Научимся создавать отчетность и поговорим про лучшие практики визуализации данных и ее применении для пользы бизнеса.


## 3.1 Введение 

**Видео лекция** - [Введение](https://youtu.be/sj2qRK7NRMQ) 

## 3.2 Что такое Business Intelligence (BI)

**Видео лекция - теория** - [Что такое BI?](https://youtu.be/8dcISZnrlcw) 


### Дополнительные материалы для изучения

1. [Короткое видео - что такое BI на примере Lamoda BI Academy и SAP Business Objects](https://youtu.be/xYExt37a9Qg) (Русский)
2. [Business Intelligence: принципы, технологии, обучение](https://habr.com/ru/post/134031/) (Русский)
3. [Что такое BI?](https://habr.com/ru/company/navicon/blog/250875/) (Русский)
4. [What is business intelligence? Transforming data into business insights](https://www.cio.com/article/2439504/business-intelligence-definition-and-solutions.html) (English)
5. [What is business intelligence? Your guide to BI and why it matters](https://www.tableau.com/learn/articles/business-intelligence) (English)
6. [Курс Data Warehousing for Business Intelligence Specialization](https://www.coursera.org/specializations/data-warehousing) (English)
7. [Книга Hyper: Changing the way you think about, plan, and execute business intelligence for real results, real fast!](https://www.amazon.ca/Hyper-Changing-execute-business-intelligence-ebook/dp/B011MXBW96/ref=sr_1_17?crid=LHAXKU4X0H3Y&dchild=1&keywords=business+intelligence&qid=1594192470&sprefix=business+intel%2Caps%2C208&sr=8-17) (English)


## 3.3 Обзор рынка решений BI

**Видео лекция - теория** - [Рынок BI?](https://youtu.be/CKDGGOzYg9w) 


### Дополнительные материалы для изучения

1. [Куда движется рынок BI-аналитики в 2019 году](https://habr.com/ru/post/475470/) (Русский)
2. [Топ-10 технологических трендов в обработке данных и аналитике в 2019 году по мнению Gartner](https://habr.com/ru/company/otus/blog/457450/) (Русский)
3. [Технические отличия BI систем (Power BI, Qlik Sense, Tableau)](https://habr.com/ru/post/444758/) (Русский)
4. [Gartner BI отчет 2020 оригинал](https://www.tableau.com/reports/gartner) (English)
5. [Forrester 2019 Enterprise BI Platform Wave™ Evaluations — Research Update](https://go.forrester.com/blogs/enterprise-bi-platform-waves/) (English)


## 3.4 2 Типа решений BI

**Видео лекция - теория** - [2 типа решений BI?](https://youtu.be/VklEzWpFZIk) 


### Дополнительные материалы для изучения

1. [Traditional vs. Self-Service BI: Analytics Alternatives Explained](https://www.softwareadvice.com/resources/traditional-bi-vs-self-service/) (English)
2. [Презентация Tool Comparison: Enterprise BI vs Self-Service Analytics: Choosing the Best Tool for the Job](https://www.slideshare.net/senturus/tool-comparison-enterprise-bi-vs-selfservice-analytics-choosing-the-best-tool-for-the-job) (English)
3. [Семь раз отмерь, один раз внедри BI инструмент](https://habr.com/ru/company/ods/blog/460807/) (Русский)

## 3.5 Ох уж эти кубы (Molap vs Rolap)

Когда мы работаем с аналитикой мы часто слышим про кубы. Если честно, кубами и OLAP называют все в подряд без разбора, включая BI и хранилище данных. Давайте решим, что для нас OLAP куб это MOLAP, закэшированные данные в файле или in-memory, где мы используем язык MDX для работы с ними по средством Excel или BI инструмента. А все остальное пусть будет ROLAP или просто классический BI. Чем я и пользуюсь, например в Tableau. MDX я тоже не знаю и не собираюсь его использовать.

**Так как я не использую MOLAP c 2011 года и стараюсь вообще его избегать, то я не являюсь экспертом. Если есть неточности, смело добавляйте сюда.**

**Видео лекция - теория** - [Ох уж эти кубы (Molap vs Rolap)](https://youtu.be/FWEQYomEbqw) 


### Дополнительные материалы для изучения

1. [Введение в многомерный анализ](https://habr.com/ru/post/126810/) (Русский)
2. [Многомерные кубы, OLAP и MDX](https://habr.com/ru/post/66356/) (Русский)
3. [Запуск OLAP-сервера на базе Pentaho по шагам](https://habr.com/ru/post/187782/) (Русский)

## 3.6 Из чего состоит любой BI инструмент?

Мы рассматриваем Business Intelligence как класс инструментов для создания аналитического решения и коммуникации с бизнес пользователями. Существует огромное кол-во инструментов BI, но если посмотреть поближе, они все похожи и имею много общего.


**Видео лекция - теория** - [Из чего состоит любой BI инструмент?](https://youtu.be/vtGjvKjZpmU) 

### Практика
Есть ли у вас доступ к BI решению? Если есть, то попробуйте отыскать все элементы, про которые я рассказывал. Если нет, то попробуйте найти любой продукт BI, установить его, и посмотреть, что внутри.

## 3.7 Основы визуализации данных
Визуализация данных это неотъемлемая часть любого BI решения. Эксперты пишут книги, университеты готовят специалистов и все для того, чтобы научить нас эффективно коммуницировать данные с конечным пользователем. Каждый раз когда вы будет создавать дашборд или строить отчет, вы должны задуматься о том, как лучше рассказать историю на основе данных и какой метод визуализации использовать.

**Видео лекция - теория** - [Основы визуализации данных](https://youtu.be/zUpKIFFy-ok) 

**Запись вебинара c Экспертом** 
[Алгоритм проектирования дашборда / Роман Бунин](https://youtu.be/xSp5ykKcQho)

### Дополнительные материалы для изучения

1. [Вебинар DataLearn: Алгоритм Проектирования Дашборда с Романом Буниным](https://youtu.be/xSp5ykKcQho) (Русский)
2. [10 примеров визуализации из истории](https://www.tableau.com/learn/articles/best-beautiful-data-visualization-examples) (English)
3. [Влияние цвета на качество визуализации](https://hbr.org/2014/04/the-right-colors-make-data-easier-to-read) (English)
4. [Хорошая визуализация должна быть скучной](https://everydayanalytics.ca/2015/10/good-data-visualization-should-be-boring.html) (English)
5. [Курс ВШЭ - Основы анализа и визуализация данных для медиа 2019/2020](http://wiki.cs.hse.ru/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B_%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0_%D0%B8_%D0%B2%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85_%D0%B4%D0%BB%D1%8F_%D0%BC%D0%B5%D0%B4%D0%B8%D0%B0_2019/2020#.D0.9C.D0.B0.D1.82.D0.B5.D1.80.D0.B8.D0.B0.D0.BB.D1.8B_.D0.BA.D1.83.D1.80.D1.81.D0.B0) (Русский)
6. [Специализация на Coursera - Information Visualization Specialization](https://www.coursera.org/specializations/information-visualization) (English)
7. [Курс на Coursera - Data Analysis and Presentation Skills: the PwC Approach Specialization](https://www.coursera.org/specializations/pwc-analytics) (English)
8. [Курс на Coursera - Data Visualization with Advanced Excel](https://www.coursera.org/learn/advanced-excel) (English)
9. [Курс на Coursera - Data Visualization and Communication with Tableau](https://www.coursera.org/learn/analytics-tableau) (English)
10. [Как не врать с помощью статистики: основы визуализации данных](https://habr.com/ru/company/pixonic/blog/453828/) (Русский)

### Практика
Посмотрите на ваши дашборды на работе или в модуле 1 и 2. Что вы могли бы улучшить?

Tableau один из самых популярных продуктов среди BI. На западе Tableau очень популярен. Среди отечественных компаний он широко известен, но часто его считают дорогим. Хотя всем и так известно, что покупка BI - это инвестиция, если его правильно внедрить и хорошо настроить, обучить пользователей и дать им возможность самостоятельно ковыряться в данных (self-service BI). В этом уроке мы рассмотрим Tableau Desktop - клиент решения Tableau, который позволяет работать с большими и маленькими данными, подключаться ко множеству систем и сервисов и создавать офигительные дашборды.

## 3.8 Знакомство с BI Tableau Desktop

**Видео лекция - теория** - [Знакомство с Tableau Desktop](https://youtu.be/QY1FYMnxElw) 

**Видео лекция - практика** - [Демонстрация Tableau Desktop](https://youtu.be/QY1FYMnxElw?t=2710) 

**Запись вебинара c Экспертом** 
[АДАПТИВНАЯ ВЕРСТКА ДАШБОРДОВ В ТАБЛО / РОМАН БУНИН](https://youtu.be/GE1czOiI-8o)

### Дополнительные материалы для изучения

1. [Tableau Tutorial](https://help.tableau.com/current/guides/get-started-tutorial/en-us/get-started-tutorial-home.htm) (English)
2. [Как создать Sparkline в Tableau](https://www.vizwiz.com/2015/09/kpisandsparklines.html) (English)
3. [Обзор 43 графика за 50 минут](https://www.vizwiz.com/2017/10/43-charts-in-50-minutes.html) (English)
4. [Шаблон 5 дашбордов](http://duelingdata.blogspot.com/2019/01/5-types-of-dashboards.html) (English)
5. [Курс на Coursera - Data Visualization and Communication with Tableau](https://www.coursera.org/learn/analytics-tableau) (English)
6. [Примеры работ в Tableau - Tableau Zen Мастером](https://photos.google.com/share/AF1QipPtbvxIRuoBESlPztSPTsryjD0ehd8SmpLBHp4aKdpUu0vcVqLZZP81DH1uzoRzKA?key=THpkYTRRT2JKU1ZVQzJBdTh4UDF6T3FoWVB0MUVn) (English)
7. [Соревнования по Tableau - Iron Viz](https://www.tableau.com/iron-viz) (English)
8. [Как создать Sankey график](https://www.flerlagetwins.com/2018/04/sankey-template.html) (English)

### Практика
Вы уже хорошо знакомы с SuperStore Dataset. Оказалось, что это самый популярный датасет в мире Табло. И вы даже увидите sample dashboard в вашем новеньком Tableau Desktop. 

1. Если еще нет Tableau Desktop и лицензии, то следуйте [инструкции](https://github.com/Data-Learn/data-engineering/blob/master/how-to/how-to-tabelau-desktop.md).
2. Подключитесь к БД Postgres и нарисуйте дашборд, который вы уже делали раньше. Вы можете использовать Табло пример для своего, главное понять как работает:
- Tableau Data Sources
- Live/Extract
- Dimensions/Measures/Filters
- Calculation Fields
- Parameters
- Table Calculations
- LOD
- Blending
- Federated Data Source
- Dashboard/View/Story
- Forecast/Trend/Clustering

Вы можете просто разобрать на части дашборд из примера и создать свой на этой базе. Главное понять принципы работы.

В качестве результата вы должны создать дашборд и создать себе аккаунт на [Tableau Public](https://public.tableau.com/s/), куда вы сможете его загрузить. Постарайтесь использовать как можно больше Tableau функциональности, но не забывайте о красоте и простоте.

## 3.9 Знакомство с BI Tableau Сервером (обзор Tableau Server)

**Видео лекция - теория** - [Знакомство с Tableau Server](https://youtu.be/TYEQir1seqI) 

**Видео лекция - практика** - [Демонстрация и Установка Tableau Server на виртуальную Машину Windows](https://youtu.be/TYEQir1seqI?t=1218) 

### Дополнительные материалы для изучения

1. [Tableau Server бесплатный обучающие видео](https://www.tableau.com/learn/training/20203) (English)
2. [Tableau Форум](https://tableau-forum.ru/viewforum.php?id=2) (Русский)
3. [Установка Tableau Server на Windows 10](https://medium.com/ampersand-academy/how-to-install-tableau-server-on-windows-10-server-2012-e9c7cab9b21f) (English)

### Практика
В данном упражнении вам необходимо будет скачать и установить Tableau Сервер. Как вы поняли из видео, вам необходимо минимум 8 Гб оперативки (если ставить на Windows без виртуальной машины) и 16 Гб (если использовать виртуальную машину). 

1. Вы скачиваете Tableau Server [отсюда](https://www.tableau.com/support/releases/server). Можно версию 2018.1 если ограничения по оперативной памяти. Более свежая версия требует минимум 16 Гб.
2. Вы устанавливаете Tableau Server на Windows (можно использовать Windows 10 или Windows Server, главное 64x бит)
3. После установки заходите в него через браузер.
4. Если вы используете виртуальную машину, то вам необходимо настроить сетевой адаптер виртуальной машины, чтобы машины могли между собой соединяться. Я загрузил [PDF файл](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module03/DE%20-%20101%20Lab%203.1/Vmware%20network%20example.pdf), про который рассказывал в видео. Если будут трудности с настройкой, пишите в slack канале 3го модуля.
5. Используя свой дашборд, который вы построили в Tableau Desktop на базе Postgres, загрузите его в Tableau Server 2 раза. 1й раз как `Live Connection`, 2ой раз как `Tableau Extract`. Попробуйте понять в чем разница.
6. Установите tabcmd там же, где и клиент Tableau и попробуйте обновить экстракт и скачать PDF файл дашборда.
7. Хотите больше? Попробуйте использовать [TabPy](https://github.com/tableau/TabPy) для Tableau Desktop/Server.

Если совсем все плохо, тогда оставайтесь с Tableau Public.

## 3.10 Знакомство с Power BI

[Эдгар Лакшин](https://www.linkedin.com/in/edgar-lakshin-b9386b22/) записал для вас интересную лекцию по Power BI, где вы можете познакомиться с этим BI инструментом.

**Видео лекция - теория** - [Знакомство с Power BI](https://youtu.be/6no5xbpF3_o) 

**Видео лекция - практика** - [Демонстрация Power BI](https://youtu.be/6no5xbpF3_o?t=524)

### Дополнительные материалы для изучения

1. [Что такое Power BI от Microsoft](https://powerbi.microsoft.com/ru-ru/what-is-power-bi/) (Русский)
2. [Официальная документация про Power BI](https://docs.microsoft.com/ru-ru/power-bi/guidance/) (Русский)
3. [Самый крутой YouTube канал про Power BI - Guy in a Cube](https://www.youtube.com/channel/UCFp1vaKzpfvoGai0vE5VJ0w) (English)

### Практика
Эдгар подготовил для вас задание. Вы сможете его найти [здесь](https://github.com/Data-Learn/data-engineering/tree/master/DE-101%20Modules/Module03/DE%20-%20101%20Lab%203.1/3_11_PowerBI).
Вы сможете скачать Power BI дашборд и файл Excel с данными и постарайтесь выполнить задание. Если появятся вопросы спрашивайте в Slack в канале, посвященным 3го модуля.


## 3.11 BI опросы или как управлять клиентским опытом BI пользователей

Один из главных принцип лидерства ([Leadership Principles](https://www.amazon.jobs/en/principles)) в Амазон - Любовь к Клиентам (Customer Obsession). Да и не только у Амазона, многие компании являются клиентоориентированными. 

Когда мы внедряем или сопровождаем аналитическое решение, мы тоже должны быть customer obsession. Только для нас клиенты - это пользователи BI решения. Лучший способ узнать у коллег - провести опрос и визуализировать результат. Таким образом вы сможете собрать обратную связь, быть проактивным и приоритизировать или выявить ключевые проблемы у ваших пользователей, которые вы сможете решить. Таким образом, вы повысите клиентский опыт и у вас будет, что рассказать вашему руководителю или другой компании на собеседовании. ;)

**Видео лекция - теория** - [ Voice of Customers (опросы  пользователей аналитического решения)](https://youtu.be/kKI5PMVC6A4) 

### Дополнительные материалы для изучения

1. [Визуализацию опросов в Tableau](https://www.datarevelations.com/visualizing-survey-data/) (English)
2. [How to measure Customer Satisfaction](https://blog.hubspot.com/service/how-to-measure-customer-satisfaction) (English)

### Практика
Используйте мои вопросы или придумайте свои. Вы можете использовать Google Forms или Survey Monkey, чтобы создать опрос, разошлите коллегам на работе (если есть такая возможность и вы работаете с данными). Визуализируйте результат и расскажите, что получилось. Для выполнения домашнего задания, сам опрос (или его пример) и пример визуализации опроса нужно сохранить в ваш Git.

## 3.12 Требования к BI разработчику/инженеру

Мы уже изучили достаточно, чтобы перейти к более серьезным шагам. То есть 3х модулей, который вы могли пройти будет достаточно, чтобы найти работу BI разработчика. Мы говорили про много вещей - BI, SQL, базы данных, задачи аналитики и BI разработчика, посмотрели примеры решений. Так же я вам давал много вспомогательных материалов, чтобы у вас нарисовалась картинка - кто такой BI разработчик и какие у него обязанности. Инструмент BI это уже 2ой приоритет. В этом видео я поделюсь с вами очень ценной и полезной информацией, на базе своего 10ти летнего опыта в индустрии. Сам я проходил много собеседований по всему миру и так же собеседовал много людей для Амазона.

**Видео лекция - теория** - [Требования к BI разработчику](https://youtu.be/DxRTAqpjowY) 

### Дополнительные материалы для изучения

1. [Indeed Worldwide](https://youtu.be/DxRTAqpjowY) (English)
2. [Методика STAR для прохождения структурированных собеседований](https://hr-portal.ru/story/metodika-star-dlya-prohozhdeniya-strukturirovannyh-sobesedovaniy) (Русский)
3. [О собеседовании в Амазон](https://medium.com/@allo/%D0%BE-%D1%81%D0%BE%D0%B1%D0%B5%D1%81%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B8-%D0%B2-%D0%B0%D0%BC%D0%B0%D0%B7%D0%BE%D0%BD-27e649323c4b) (Русский)

### Практика
1. Используя систему STAR попробуйте описать несколько кейсов из вашего BI опыта. 
2. На сайте HH.ru или Indeed сделайте себе еженедельную рассылку на интересные вам вакансии (изучайте рынок заранее).
3. Хотите удивить работодателя своим резюме? Сделайте его в git, используя markdown как в [примере](https://elipapa.github.io/markdown-cv/) или опубликуйте в Tableau Public, как в [примере](https://public.tableau.com/en-us/s/interactive-resume-gallery).

## 3.13 Обзор "модных" решений для визуализации и отчетности (Fancy BI tools)

На рынке существует огромное количество BI инструментов. В модуле 3 мы уже познакомились с лидерами индустрии и попробовали их в деле. Так же мы попробовали разные сервисы для визуализации. А теперь, чтобы полностью закрыть тему Business Intelligence, я хочу вас познакомить еще с рядом интересных BI решений, которые активно используются на западе. 

**Видео лекция - теория** - [Fancy BI tools](https://youtu.be/GEl6NNpnZYQ)

### Дополнительные материалы для изучения
Вы может посмотреть примеры решений и даже попробовать скачать и подключиться к существующей базе данных Postgres или файлику с данными.

1. [Looker](https://looker.com/)
2. [Sigma BI](https://www.sigmacomputing.com/)
3. [Mode](https://mode.com/)
4. [Plotly and Dash](https://plotly.com/)
5. [Redash](https://redash.io/)
6. [Chartio](https://chartio.com/)
7. [ThoughtSpot](https://www.thoughtspot.com/)

Если вы хотите поддержать отечественного производителя, то рекомендую вам попробовать сервис по визуализации данных - [Yandex Data Lens](https://cloud.yandex.ru/services/datalens).

### Практика
Если вам интересно потренироваться на решении [Looker](https://rockyourdata.looker.com/login), то вы можете написать мне в личку в Slack, и я вам сделаю учетную запись для Looker и вы сможете потренироваться в работы с облачным BI решением. 

## Финальный проект для модуля 3: Аналитика по данным Airbnb London

Как вы знаете 3й модуль был про визаулизацию данных, business intelligence и BI продукты. Наш эксперт по BI и Tableau и автор Телеграмм канала Reveal the Data, Роман Бунин, подготовил для вас [очень интересный проект](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module03/CapstoneProject/readme.md).

Удачи!

## Опрос Модуль 3
Пожалуйста пройдите [опрос по завершении Модуля 3](https://forms.gle/pqLxifWBPTCzRcFW9). Так я смогу посмотреть, сколько человек закончило модуль, что было хорошо, а что можно улучшить.

По окончанию модуля 3, вы можете расшарить значок `03 | BI` в социальных сетях и рассказать о своих достижениях. 

![img](https://github.com/Data-Learn/data-engineering/blob/master/img/de101-module03.png)

**PS Если материал оказался полезным, вы можете поддержать авторов через**
Условная цена одного модуля 500р ;)

[ЮMoney](https://yoomoney.ru/to/4100116864248269) или [Patreon](https://www.patreon.com/dmitryanoshin) или [Paypal](https://paypal.me/dmitryanoshin)
