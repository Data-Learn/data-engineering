# Установка PySpark локально на ваш компьютер

Эта инструкция поможет вам установить PySpark локально на ваш компьютер чтобы вы могли спокойно потренироваться и получить опыт работы на спарке с питоном.

Есть несколько способов это сделать:
1. Использовать готовый докер образ (это легче в настройке, но требует установки докера)
2. Использовать только питон (это требует больше настроек, немного дольше по времени и могут всплыть некоторые проблемы)

# Вариант 1: запуск в Docker

## Предварительные требования

Нам понадобится установить непосредственно Docker. Шаги следующие:

0. [Если у вас Windows Home Edition] Установить WLS2. Откройте командную строку (CMD) или PowerShell от имени администратора и выполните:
        
        wsl --install
    
    В первый раз это может занять некоторое время.
1. Скачайте и запустите инсталятор [докера](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)
2. Убедитесь что во время установки вы выбрали опцию "Enable Hyper-V Windows Features" или "Install required Windows components for WSL 2" (если вы на Home Edition)

Более подробно модно почитать в официальной документации: https://docs.docker.com/desktop/windows/install/

### Процесс запуска Pyspark

Будем использовать образ [Jupyter notebooks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html) с установленным Apache Spark.

Запускаем контейнер в интерактивном режиме:
- если вы запускаете в CMD в Windows
    ```
    docker run -it -p 8888:8888 -p 4040:4040 -v %cd%:/home/jovyan/work jupyter/pyspark-notebook
    ```
- если вы запускаете в PowerShell в Windows
    ```
    docker run -it -p 8888:8888 -p 4040:4040 -v ${PWD}:/home/jovyan/work jupyter/pyspark-notebook
    ```
- если вы запускаете в терминале Linux/macos
    ```
    docker run -it -p 8888:8888 -p 4040:4040 -v $(pwd):/home/jovyan/work jupyter/pyspark-notebook
    ```

Первоначальная загрузка может занять некоторое время на скачивание образа.

Остановка контейнера по CTRL + C.

## Вариант 2: Установка Pyspark локально из pip

### Предварительные требования

1. Python 3.6+
2. Установленная Java/OpenJDK версии 11 или выше
        
    Установщик JDK можно скачать например [отсюда](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)
    
    Проверить установку можно из терминала:

        java -version

    Вы должны увидеть какая версия установлена:
        
        openjdk version "15.0.1" 2020-10-20
        OpenJDK Runtime Environment (build 15.0.1+9)
        OpenJDK 64-Bit Server VM (build 15.0.1+9, mixed mode, sharing)

### Процесс установки

0. Подготовьте отдельную папку. Откройте эту папку в терминале (CMD, PowerShell, Terminal)
1. Делаем виртуальное окружение Python:

    ```
    python -m venv venv
    ```
    
    (!) В линуксе и макоси скорее всего надо ипользовать команду `python3`, чтобы создать окружение именно третьего питона.

2. Активируем окружение:

    ```
    # Windows
    venv\Scripts\activate.bat

    # Linux, macOs
    source venv/bin/activate
    ```

    [Официальная инструкция](https://docs.python.org/3/library/venv.html) по активации окружения.

3. Ставим pyspark (и заодно jupyter) из pip:

    ```
    (venv) pip install pyspark jupyter
    ```

4. Проверяем что всё установилось

### Возможные проблемы с запуском

- Проблемы с кодировкой на Windows. Может возникнуть если у вас имя юзера набрано кориллическими буквами. Попробуйте создать свою папку в корне диска (`c:/` или `d:/`)
- Питон не найден при попытке запуска спарка на Windows. Попробуйте задать переменную окружения PYSPARK_PYTHON и установить туда полный путь к интерпретитатору питона из вашего виртуального окружения, например
    ```
    set PYSPARK_PYTHON=c:\Users\John\pyspark\venv\Scripts\python.exe
    ```
