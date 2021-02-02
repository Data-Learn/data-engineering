# Задание для модуля 1

```
Результаты домашней работы загружайте к себе в git репозиторий. Создайте папки
DE-101/Module1/
DE-101/Module2/
...
И сохраняйте там результат.
```

## Установка GitHub

1. Прочитать про [Git на русском](http://bi0morph.github.io/hello-world/).
2. Если вы не работали с командной строкой, то пройдите это курс [introduction into Shell](https://www.datacamp.com/courses/introduction-to-shell-for-data-science). Не обязательно понимать, что такое Shell/bash. Это для нас просто инструмент для навигации и запуска приложений/команд, когда нет GUI (графического интерфейса). Мы будем использовать командную строку для управления Git и для работы с облаком.
3. Установить Git по этой [инструкции](https://github.com/Data-Learn/data-engineering/blob/master/how-to/How%20to%20get%20git.md)

Наша задача создать свой собственный репозиторий Git, где вы сможете хранить свои наработки, и мы потом сможем проверить по завершению курса. Также вам нужно будет синхронизировать наш репозиторий, чтобы скачать файлик Excel. Это можно сделать через GUI (как я делаю), но лучше лишний раз попрактиковаться с Command Line Interface (CLI - командной строкой).


## Архитектура Аналитического Решения
Необходимо нарисовать верхнеуровневую архитектуру аналитического решения по примеру теоретического видео, где я рассказывал об архитектуре ламоды. Необходимо использовать:
- Source Layer - слой источников данных
- Storage Layer - слой хранения данных 
- Business Layer - слой для доступа к данным бизнес пользователей

Необходимо использовать draw.io, Microsoft Visio Studio, Power Point или инструмент на выбор. 

Здесь вы можете найти [инструкции по установке draw.io](https://github.com/Data-Learn/data-engineering/blob/master/how-to/How%20to%20install%20drawio.md).

## Аналитика в Excel
Используя данные Sample - Superstore.xls сделать:
- Использовать Lookup
- Построить Сводную таблицу
- Построить примеры отчетов
- Создать дашборд
- И другая функциональность Excel на ваш выбор.

Идеи для создания дашборда отчета:
1. Overview (обзор ключевых метрик)
  - Total Sales 
  - Total Profit
  - Profit Ratio
  - Profit per Order
  - Sales per Customer
  - Avg. Discount
  - Monthly Sales by Segment ( табличка и график)
  - Monthly Sales by Product Category (табличка и график)
 2. Product Dashboard (Продуктовые метрики)
  - Sales by Product Category over time (Продажи по категориям)
 3. Customer Analysis
  - Sales and Profit by Customer
  - Customer Ranking
  - Sales per region


**Значения атрибутов в Sample - Superstore.xls**
Название столбца | Значение
----------------|----------------------
Row ID       | Идентификатор строки (уникальный)
Order ID   | Идентификатор заказа
Order Date   | Дата заказа
Ship Date      | Дата доставки
Ship Mode    | Класс доставки
Customer ID | Идентификатор покупателя
Customer Name     | Имя и фамилия покупателя
Segment   | Сегмент покупателя
Country     | Страна
City       | Город
State      | Штат
Postal Code   | Почтовый индекс
Region      | Регион
Product ID    | Идентификатор товара
Category | Категория
Sub-Category     | Подкатегория
Product Name   | Название товара
Sales     | Продажи (Доход)
Quantity       | Количество
Discount    | Скидка в %
Profit   | Прибыль
Person     | Региональный менеджер
Returned   | Возвраты товара 

<br><br>
[Пример отчета](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module01/DE%20-%20101%20Lab%201.1/Sample%20-%20Superstore%20-%20Dashboard.xlsx)
<br>
[Пошаговая инструкция](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module01/DE%20-%20101%20Lab%201.1/build_steps_dashboard.md)
