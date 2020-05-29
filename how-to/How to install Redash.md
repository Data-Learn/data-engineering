# How to: Как установить Redash

## Introduction
Redash — это сервис для сбора и анализа данных. Умеет подключаться к любому источнику данных (Redshift, BigQuery, MySQL, PostgreSQL, MongoDB и многим другим), запрашивать инормацию, визуализировать и делиться данными.

## Requirements
В этом руководстве установим Ubuntu Server в виртуальное окружение Vrtualbox на своем компьютере под управлением **Windows или MacOS**.

## Installation
Варианты установки можно посмотреть по ссылке: https://redash.io/help/open-source/setup
Здесь используется вариант развертывания инфраструктуры Docker в Ubuntu Server 18.04 с помощью скрипта установки https://github.com/getredash/setup

1. Сначала установим чистый Ubuntu Server в Virtualbox по инструкции:
https://codebots.com/library/techies/ubuntu-18-04-virtual-machine-setup

2. Дальше можно настроить подключение к новому серверу из вашей операционной системы. Это удобнее, чем использовать консоль Virtualbox.
Здесь описаны несколько необходимых шагов для Windows и MacOS:
https://codebots.com/library/techies/connect-to-your-server

3. Следующие команды вводим в консоли вашего сервера после успешного подключения.

Установим обновления (команды вводятся без знака $)
```
$ sudo apt-get update && sudo apt-get upgrade -y
```
Склонируем репозиторий с файлами установки в домашний каталог и проверяем, что создалась директория "setup". Переходим в нее.
```
$ git clone https://github.com/getredash/setup.git
$ ls
$ cd setup/
```
Делаем установочный скрипт выполняемым и запускаем установку
```
$ chmod +x setup.sh 
$ ./setup.sh 
```

4. Если при установке не возникло ошибок - проверяем, что все контейнеры запущены:

```
$ docker-compose ps

          Name                         Command               State              Ports           
------------------------------------------------------------------------------------------------
redash_adhoc_worker_1       /app/bin/docker-entrypoint ...   Up      5000/tcp                   
redash_nginx_1              nginx -g daemon off;             Up      443/tcp, 0.0.0.0:80->80/tcp
redash_postgres_1           docker-entrypoint.sh postgres    Up      5432/tcp                   
redash_redis_1              docker-entrypoint.sh redis ...   Up      6379/tcp                   
redash_scheduled_worker_1   /app/bin/docker-entrypoint ...   Up      5000/tcp                   
redash_scheduler_1          /app/bin/docker-entrypoint ...   Up      5000/tcp                   
redash_server_1             /app/bin/docker-entrypoint ...   Up      0.0.0.0:5000->5000/tcp
```

Если вывод команды выглядит как в листинге выше - поздравляю.
Все контейнеры были запущены скриптом установки. Если нужно остановить Redash сервисы (перед выключением сервера, к примеру), используем команду:
```
$ docker-compose stop
```
Запустить опять:
```
$ docker-compose start
```

## Launch

Для входа в интерфейс Redash, нужно в браузере ввести IP адрес вашего виртуального сервера, к которому вы подключались в консоли.
http://server_ip_address/ 

При первом запуске будет диалог создания пользователя-администратора.
Дальше рекомендую просмотерть довольно доступные короткие инструкции на сайте разработчика: https://redash.io/help/

---
В случае проблем с установкой и вопросов - лучше обращаться в Slack.