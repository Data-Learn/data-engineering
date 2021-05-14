# Модуль 5:  Введение в Облачные Вычисления

[Обратно в содержание курса :leftwards_arrow_with_hook:](https://github.com/Data-Learn/data-engineering/blob/master/DE%20-%20101%20Guide.md) 

В 5 модуле мы узнаем про облачные вычисления, или просто cloud computing. Мы начнем с основ, и поговорим и главных вендорах и их решениях. Я расскажу про свой опыт с облачными решениями и постараюсь вас научить их использовать и дать достаточно знаний, для того, чтобы вы могли понимать, что это такое, и как это используется, а так же применять в работе. Из модуля вы узнаете:

-   Основные вендоры облачных решений AWS, Microsoft Azure и Google Cloud
-   Типы облачных сервисов и их примеры (Cloud Service Models)
-   Модели облачных решений (Cloud Model Types)
-   Безопасность облачных решений и Shared Responsibility Model
-  Научитесь создавать виртуальную машину и подключаться к ней через SSH
-  Настраивать сеть для безопасного доступ (Networking)
-   Попробуете различные облачные сервисы
-  Примеры профессий, сертификации от вендоров и тренинги


## Модуль 5.1 Введение

**Видео лекция - теория** - [Введение](). 

## Модуль 5.2 Введение в Облачные вычисления (Cloud Computing)?
В 2020 году и в 1-м квартале 2021 года западные вендоры (AWS, Azure, GCP) показали рекордные доходы. "Облако" используется повсеместно в западных странах и становится все популярней и востребованнее. Прежде чем мы начнем использовать "облако" для аналитических задач, мы должны познакомиться с основами облачных вычислений. В этом видео вы узнаете:

-   Несколько кейсов из прошлого
-   История зарождения облачных вычислений и идеи utility computing
-   Ключевые бизнес драйверы и риски
-   Определения, терминология и характеристики облачных вычислений
-   Основные компоненты облачных вычислений и датаценров

**Видео лекция - теория** - [Введение в Облачные вычисления](https://youtu.be/JHPa1AhUN_I)

Так же на лабораторной работе я рассмотрел:

-   Free trial account AWS и Azure
-   AWS Virtual Private Cloud, Subnets, Security Groups - (виртуальная сеть, с этого начинается любой проект в облаке).
-   Создали виртуальную машину EC2 и подключились к ней через протокол SSH с использование командной строки и ключа

**Видео лекция - практика** - [Введение в Облачные вычисления - hands-on](https://youtu.be/JHPa1AhUN_I?t=2447). 

### Дополнительные материалы для изучения
- [What is AWS?](https://youtu.be/a9__D53WsUs) (Video English)
- [AWS vs Azure vs GCP ](https://www.youtube.com/watch?v=kd33UVZhnAA) (Video English)
- [Inside a Google data center](https://www.youtube.com/watch?v=kd33UVZhnAA) (Video English)
- [Stephen Fry explains cloud computing](https://youtu.be/J9LK6EtxzgM) (Video English)
- [NIST Definition of the Cloud Computing](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf ) (English)
- [5 Real World Examples of Cloud Computing ](https://www.maropost.com/5-real-world-examples-of-cloud-computing/) (English)
- [Top 10 use cases for cloud computing ](https://blog.newcloudnetworks.com/the-top-10-use-cases-for-cloud-computing) (English)
- [What is virtualization and how it works ](https://searchservervirtualization.techtarget.com/definition/virtualization) (English) 
- [Flexera 2020 State of the Cloud Report](https://info.flexera.com/SLO-CM-REPORT-State-of-the-Cloud-2020) (English)

### Практика
Вам необходимо:
1. Создать Free trial учетные записи в AWS и Azure
2. Создать виртуальную машину в AWS и Azure и сохранить ключ для нее
3. Проверить настройку Security Groups (firewall)
4. Подключится к виртуальной машине через SSH
5. Создать S3 bucket в AWS, и загрузить туда CSV superstore из 1го модуля
6. Создать Storage Account в Azure, и загрузить туда CSV `superstore` из 1го модуля
7. Используя `draw.io` и иконки AWS/Azure, нарисуйте архитектуру решения, на котором будет VPC, Subnet, Internet Gateway, Route Table, Subnet и укажите IP адресс EC2.

Опционально:
Если вы хотите получше разобраться в концепции AWS Virtual Private Cloud, то вам необходимо сделать еще 2 упражнения:
1. Используя документацию AWS, создайте новый VPC, Public и Private Subnets, Availability Zones и все необходимое. Создайте 2 EC2 инстанса (один в public subnet, другой в private) и попробуйте к ним подключится через SSH
2. Нарисуйте диграмму в `draw.io`.

Если хотите, попробуйте тоже само в Azure с Vnet.

## Модуль 5.3 Концепции и модели облачных вычислений
Согласно National Institute of Standards and Technology (NIST) можно выделить несколько типов облачных сервис моделей и тип самого облако. В этом видео мы рассмотрим:
-  Облачные Сервис Модели IaaS, Paas, Saas
-  Cloud Stack
-  Cloud Deployments Models - Public, Private, Hybrid и Community
-  Рост популярности облачных вычисления
-  Рост доли рынка основных вендоров

**Видео лекция - теория** - [Концепции и модели облачных вычислений](https://youtu.be/-TW1oreQLNw)

На лабораторной работе я покажу:
-  AWS QuickStart
-  AWS Load Balancer
-  Рассмотрим основные команды для Bash/Shell (командной строки, которые необходимы для работы специалиста с данными)
-  Инфраструктура as Код на пример AWS CloudFormation и Azure ARM templates
-  Посмотрим на billing (стоимость владения по факту) и на AWS Budgets, AWS Calculator
-  Так же посмотрим на Azure Calculator

**Видео лекция - практика** - [Введение в Облачные вычисления - hands-on](https://youtu.be/-TW1oreQLNw?t=1671)

### Дополнительные материалы для изучения
- [NIST Definition of the service and deployment models](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf) (English)
- [AWS: Type of cloud computing](https://aws.amazon.com/types-of-cloud-computing/) (English)
- [Azure: Cloud service models](https://docs.microsoft.com/en-us/learn/modules/align-requirements-in-azure/3-service-models) (English)
- [Azure: Cloud service models](https://docs.microsoft.com/en-us/learn/modules/align-requirements-in-azure/3-service-models) (Video English)
- [McAffe Cloud Adoption and Risk Report](https://www.mcafee.com/enterprise/en-us/solutions/lp/cloud-adoption-risk-report-business-growth-edition.html) (English)


### Практика
Лабораторная Работа №5.3.1: [Создаем статичный веб-сайт на Amazon S3](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module05/DE%20-%20101%20Labs/AWS%20-%20Static%20web-site%20using%20S3/Static%20web-site%20using%20S3.md). Автор: Эдгар Лакшин. 

Дополнительно вам необходимо:
- В своем AWS Account создать Billing Alert
- Воспользоваться AWS или Azure калькулятором, чтобы посчитать стоимость решения
- Запустить шаблон AWS Cloudformation или Azure ARM, чтобы создать, какой-нибудь ресурс(ы) в облаке.
- Попробовать создать 2 AWS EC2, установить на них Apache Web Server и подключить к Application Load Balancer. Потом отключить один из EC2 и убедиться, что вы все еще можете пользоваться другим EC2. Или можете создать решение EC2+RDS. Не забудьте нарисовать диаграмму решения в `draw.io`. Пример из AWS документации - [Create a web server and an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/TUT_WebAppWithRDS.html)

Если хотите, можете сделать свою лабу и мы загрузим описание к нам в Git и добавим в курс.  

## Модуль 5.4 Основы безопасности облачных решений
**Видео лекция - теория** - [Основы безопасности облачных решений](https://youtu.be/J8V1HeXQmh4)

**Видео лекция - практика** - [Введение в Облачные вычисления - hands-on](https://youtu.be/J8V1HeXQmh4)

### Дополнительные материалы для изучения
- [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) (English)
- [Azure Shared Responsibility for Cloud Computing](https://azure.microsoft.com/en-us/resources/shared-responsibility-for-cloud-computing/) (English)
- [Security, Identity, and Compliance on AWS](https://aws.amazon.com/products/security/)
- [Security services and technologies available on Azure](https://docs.microsoft.com/en-us/azure/security/fundamentals/services-technologies) (English)
- [What is AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) (English)
- [Microsoft Cloud Adoption Framework for Azure](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/) (English)
- [Laws and Regulations Governing the Cloud Computing Environment](https://rickscloud.com/laws-and-regulations-governing-the-cloud-computing-environment/) 


### Практика
Вам нужно:
- Скачать AWS CLI или Azure AZ и сконфигурировать, чтобы вы могли управлять вашим облачным аккаунтом
- Используйте AWS CLI, чтобы создать S3 бакет в AWS и загрузить в него файл
- Создайте KMS ключ в AWS и примените шифрование для данных в S3

Вы также можете использовать похожие сервисы в Azure.

## Модуль 5.5 Данные в облаке

## Модуль 5.6 Архитектура облачных решений

## Модуль 5.7 Миграция в облако

## Модуль 5.8 Аналитические решения в облаке

## Модуль 5.9 Профессии и сертфикация в облачных вычисления





Пожалуйста пройдите [опрос по завершении Модуля 5](https://forms.gle/kyYWXLarcgqz6oTu5). Так я смогу посмотреть, сколько человек закончило модуль, что было хорошо, а что можно улучшить.

По окончанию модуля 5, вы можете расшарить значок `05 | Cloud Computing` в социальных сетях и рассказать о своих достижениях. 

