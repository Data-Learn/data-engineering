# How to: Как установить Jupiter Notebook

## Introduction
Jupyter Notebook - это веб-приложение с открытым исходным кодом, позволяющее создавать документы, содержащие интерактивный код, уравнения, визуализации,  текст и обмениваться ими. Используется для очистки и преобразования данных, численного моделирования, статистического моделирования, визуализации данных, машинного обучения и многого другого.<br><br>

![image](https://jupyter.org/assets/jupyterpreview.png)

## Requirements
<ul>
<li>Операционная система: Windows, Mac, Linux</li>
<li>Python 3.3 или выше. Или Python 2.7 (но это уже устаревшая версия, просто часть старых программ работает только на ней)</li>
</ul>

## Installation


<ol>
  <li>Установка Python</li><br>
Для начала нужно убедиться, что у вас установлен python версии 3.3 и выше.
На Mac и во многих дистрибутивах Linux python уже установлен по умолчанию.
В Windows же его нужно устанавливать дополнительно.<br><br>

Для того, чтобы узнать установлен ли в нашей системе python и какая у него версия введите в командной строке Windows или терминале Linux/Max<br><br>

python --version<br><br>

Если python уже установлен, то будет выведена его версия <br>
![image](https://i.ibb.co/D4GhNX9/python-version.png)<br><br>
  
 В случае, если python не установлен на вашем компьютере или его версия ниже, чем 3.3, то заходим на официальный сайт  https://www.python.org/downloads/ и скачиваем последнюю версию для своей операционной системы. <br>
 ![image](https://i.ibb.co/5BqwVJX/install-python.png)<br><br>
 Далее на примере Windows<br>
 
 Запускаем установочный файл. На первом пункте отметьте Add Python 3.8 to PATH и нажмите  “Install Now”. <br>
 ![image](https://i.ibb.co/N3VTFJB/install-python-2.png)<br><br>
 
 
 
  <li>Установка Jupiter Notebook</li>
Чтобы установить Jupiter Notebook, выполните следующую команду на терминале (Mac/Linux) или в командной строке (Windows):<br><br>

pip install notebook

</ol>


## Launch

Чтобы запустить Jupiter Notebook, выполните следующую команду на терминале (Mac/Linux) или в командной строке (Windows):<br><br>

jupyter notebook<br><br>

Это запустит сервер Jupyter, а браузер откроет новую вкладку со следующим URL: https://localhost:8888/tree 
