# Устанавливаем Python и Spark для работы с модулем 6

## Windows

#### 1. Устанавливаем Java
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Скачиваем отсюда:
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https://www.java.com/ru/download/

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Нас устроит любая версия начиная с Java 7 и выше

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Проверить что Java установлена можно с помощью команды
```
java -version
```
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;или
  
  ```
  java --version
```

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Результат должен выглядеть примерно так:
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/e-dobrynin/data-engineering/blob/master/DE-101/Module-07/img/1.JPG?raw=true)

#### 2. Устанавливаем переменную JAVA_HOME

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Этот компьютер -> Правая кнопка -> Свойства -> Дополнительные параметры системы (слева) -> Переменные среды (внизу)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/e-dobrynin/data-engineering/blob/master/DE-101/Module-07/img/2.JPG?raw=true)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;В разделе *"Системные переменные"* нажимаем *"Создать"*, называем переменную **JAVA_HOME**. В качестве значения переменной 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;проставьте путь, куда вы установили Java.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;В моем случае это

```
C:\Program Files\Java\jdk1.8.0_172
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Выглядит вот так:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/e-dobrynin/data-engineering/blob/master/DE-101/Module-07/img/3.JPG?raw=true)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;После этого вам нужно отредактировать переменную *Path*.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Откройте *Path* в том же списке переменных, и добавьте новой строкой:

```
%JAVA_HOME%\bin
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Должно выглядеть вот так:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/e-dobrynin/data-engineering/blob/master/DE-101/Module-07/img/4.JPG?raw=true)

#### 3. Устанавливаем Python

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ВАЖНО!**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Не скачивайте самый новый релиз Python, у него есть проблемы с совместимостью со Spark (проверено лично).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Рекомендую релиз 3.7.5, на нём всё точно работет (опять же, проверено лично).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Скачиваем установочник отсюда:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https://www.python.org/downloads/

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Самый удобный вариант - *"Windows x86-64 executable installer"*, то есть обычный exe-шник.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Во время установки необходимо  поставить галочку рядом с
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*"Add python.exe to Path"* (это нужно чтобы не добавлять в *Path* ничего руками, как мы делали с Java)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/e-dobrynin/data-engineering/blob/master/DE-101/Module-07/img/5.JPG?raw=true)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Проверяем что Python успешно установлен с помощью команды

```
python --version
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Результат должен выглядеть так:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/e-dobrynin/data-engineering/blob/master/DE-101/Module-07/img/6.JPG?raw=true)

&nbsp;&nbsp;**4. Устанавливаем Spark**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Идем вот сюда:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://spark.apache.org/downloads.html

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Выбираем версию **Spark 2.4.6** и версию **Hadoop 2.7 (Pre-built for Apache Hadoop 2.7)**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Кликаем вот на эту ссылку:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/e-dobrynin/data-engineering/blob/master/DE-101/Module-07/img/7.JPG?raw=true)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Оказываемся на новой странице, и кликаем вот сюда:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/e-dobrynin/data-engineering/blob/master/DE-101/Module-07/img/8.JPG?raw=true)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;После этого начнется скачивание архива в формате .tgz (размером около 200Мб)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Когда он скачается, создайте в удобном вам месте папку "Spark", и разархивируйте содержимое вашего архива в неё.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Зайдите в папку "Spark", перейдите в папку bin, откройте командную строку и наберите в ней команду

```
pyspark
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Если установка прошла корректно, вы увидите следующую картину:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/e-dobrynin/data-engineering/blob/master/DE-101/Module-07/img/9.JPG?raw=true)


#### 4. Устанавливаем winutils

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Обязательная для Windows штука, без которой ничего не заработает!

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Внутри папки, куда вы установили Spark, создайте папку *hadoop\bin*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Скачайте winutils.exe для версии Hadoop 2.7 по этой ссылке:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https://github.com/steveloughran/winutils/blob/master/hadoop-2.7.1/bin/winutils.exe

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Скопируйте winutils.exe в папку *hadoop\bin* внутри вашей папки со Spark

#### 5. Настраиваем Spark

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Нам нужно создать ещё несколько переменных окружения.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Этот компьютер -> Правая кнопка -> Свойства -> Дополнительные параметры системы (слева) -> Переменные среды (внизу)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;В разделе "Системные переменные" нажимаем "Создать", создаем переменную под названием *SPARK_HOME*.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Значение переменной - путь к вашей папке со Spark.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;У меня выглядит вот так:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/e-dobrynin/data-engineering/blob/master/DE-101/Module-07/img/10.JPG?raw=true)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Далее, таким же образом создаём переменную *HADOOP_HOME*.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;В качестве значения для нее указываем:

```
%SPARK_HOME%\hadoop
```