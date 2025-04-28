# Создание выборки данных

## Предварительная настройка

Нам необходимо создать EC2 инстанс с диском размером в 100Gb. В идеале нам лучше использовать m5.large, можна использовать менший инстанс (генерация данных тогда займет больше времени). И не забудьте прикрепить IAM роль.

## Руководство по решению

1. Итак, давайте подключимся к созданному вами экземпляру EC2
    
    ``ssh -i datalearn.pem ec2-user@ec2-3-19-26-141.us-east-1.compute.amazonaws.com``

2. Мы будем пользоваться библиотекой для генерации данных [TPC-H benchmark kit](https://github.com/gregrahn/tpch-kit). Сначала нам необходимо предустановить необходимие библиотеки для установки генератора.
    
    ``sudo yum install make git gcc``

3. Клонируем репозиторий и переходим в склонированую директорию
    
    ``git clone https://github.com/gregrahn/tpch-kit``br
    ``cd tpch-kitdbgen``

4. Забускаем билд библиотеки для операционой системы нашего инстанса
    
    ``make OS=LINUX``

5. Создаем дерикторию для нашых данных 
    
    ``cd $HOME``br
    ``mkdir emrdata``

6. Пропипеременую окружение для библиотеки генерации данных
    
    ``export DSS_PATH=$HOMEemrdata``

7. Запускаем генерацию  данных
    
    ``cd tpch-kitdbgen``br
    ``.dbgen -v -T o -s 10``

    -v - для подробного режимаbr
    -T - для уточнения наших таблицbr
    o - для 2 таблиц, которые мы создадимbr
    -s - для размера данных 10Gb

8. Переходим в дирикторию с сгенерироваными данными
    
    ``cd $HOMEermdata``br
    ``ls``
   
    увидим два созанных файла ``lineitem.tbl orders.tbl``

9. Сейчас в s3 создадим bucket чтоб подгрузить туда сгенерированые данные

    ``aws s3api create-bucket --bucket bigdatalabs --region us-east-1``
    - имя bucket должно быть уникальным
    - используй такойже регион как и для ec2 инстанса что-б уменшить разходы на сервисы в AWS

10. копируем созданные файлы в бакет

    ``aws s3 cp $HOMEemrdata s3bigdatalabsemrdata --recursive``

11. Давайте создадим датасет для лабараторной для redshift

    ``cd`` - ето еквивалент команды ``cd $HOME``br
    ``mkdir redshiftdata``br
    ``export DSS_PATH=$HOMEredshiftdata``br
    ``.dbgen -v -T o -s 40``

12. Перейдем в дирикторию с новыми данными

    ``cd $HOMEredshiftdata``br
    ``ls -l``
    
13. Давай поделим ети файлы на более мелкие, ето поможет нам подгрузить данные в s3 хранилище быстрее и является хорошей практикой для работы с redshift. Сначало проверим количество строчек в файле orders.tbl

   ``wc -l orders.tbl``br
     60000000 orders.tbl

14. Давайте разобьем файл на 4 части
    
    ``split -d -l 15000000 -a 4 orders.tbl orders.tbl.``

15. так же разобьем файл lineitem.tbl

    ``wc -l lineitem.tbl``br
    ``240012290 lineitem.tbl``br
    ``split -d -l 60000000 -a 4 lineitem.tbl lineitem.tbl.``

16. На выходе получим

    lineitem.tblbr
    lineitem.tbl.0000br
    lineitem.tbl.0001br
    lineitem.tbl.0002br
    lineitem.tbl.0003br
    lineitem.tbl.0004br
    orders.tblbr
    orders.tbl.0000br
    orders.tbl.0001br
    orders.tbl.0002br
    orders.tbl.0003

17. Нам уже не нужны файлы lineitem.tbl и orders.tbl

    ``rm lineitem.tbl orders.tbl``

18. Копируем новые данные в s3 хранилище

    ``aws s3 cp $HOMEredshiftdata s3bigdatalabsredshiftdata --recursive``

19. Инстанс EC2 нам уже не нужен, можем его отключить
