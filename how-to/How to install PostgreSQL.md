# How to: Как установить PostgreSQL 

## Introduction
В данной инструкции информация по скачиванию и установке PostgreSQL.

PostgreSQL - это реляционная СУБД с открытым исходным кодом, базирующаяся на языке SQL. PostgreSQL имеет преимущество соответствия стандартам (в том числе SQL) и обладает множеством продвинутых возможностей, например, надёжные транзакции (reliable transactions) и параллелизм без блокировки чтения (concurrency without read locks).

### Requirements
Операционная система: [Windows](./How%20to%20install%20PostgreSQL.md#windows), [Mac](./How%20to%20install%20PostgreSQL.md#mac-os-x), [Linux](./How%20to%20install%20PostgreSQL.md#linux-ubuntu)<br>
Лицензия: бесплатная, свободное ПО

## Windows

### Installation
Перейти по ссылке<br>
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads<br>
Выбрать версию 12.2 и ОС Windows x86-64 или	Windows x86-32 и нажать Download
<ol>
<li>Запустить исполняемый файл.</li><br>
<li>Выбрать директорию установки и нажать Next 3 раза.</li><br>
<li>Выбрать пароль суперпользователя базы данных и нажать Next 3 раза.</li><br>
<li>После окончания установки снимаем галочку с Launch Stack Builder и нажимаем Finish.</li><br>
</ol>

### Launch
<ol>
<li>Переходим в Меню Пуск — > PostgreSQL 12 -> pgAdmin 4.</li><br>
<li>Вводим пароль суперпользователя.</li>
</ol>


## Mac OS X

### Installation
Перейти по ссылке<br>
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads<br>
Выбрать версию 12.2 и ОС Mac OS X и нажать Download
<ol>
<li>Запустить исполняемый файл.</li><br>
<li>Нажать "Открыть" если появится предупреждение об открытии файла из сети интернет и ввести пароль для учетной записи пользователя Mac OS</li><br>
<li>Выбрать директорию установки и нажать Next 3 раза.</li><br>
<li>Выбрать пароль суперпользователя базы данных и нажать Next 5 раз.</li><br>
<li>После окончания установки снимаем галочку с Launch Stack Builder и нажимаем Finish.</li><br>
</ol>

### Launch
<ol>
<li>Переходим в Launchpad -> pgAdmin 4.</li><br>
<li>Вводим пароль суперпользователя.</li>
</ol>

## Linux (Ubuntu)

### Installation
Открыть терминал  
Обновить локальный список пакетов
```
sudo apt-get update
```
Устанавливаем приложение
```
sudo apt-get install postgresql-12
```

### Launch
После установки проверим, что служба запущена
```
sudo systemctl status postgresql
```
В строке `Active:` вы должны увидеть статус `active (exited)` зеленого цвета. Это значит служба активна, все в порядке.  

Отключить службу можно:
```
sudo systemctl stop postgresql
```
Включить заново:
```
sudo systemctl start postgresql
```
