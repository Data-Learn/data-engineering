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
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://s438sas.storage.yandex.net/rdisk/41d2d5df9be692eaad548e965750850840f259ae738b4c57216c162fc25c96a8/5eebdf5c/GqH3a1ee2zemXlYuVGmUv_sthCtOe1O_2j8E5FHlZlhNNamC4enmBRE4vrDenaqaLZ7ltfKIhj9amcXybWH3XQ==?uid=86236828&filename=1.JPG&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&tknv=v2&owner_uid=86236828&etag=fcc9e65a4e1e05373ec3042332248af4&fsize=18743&media_type=image&hid=2ece86542ff3afe3f94760cb6e682c75&rtoken=aUY0ZQVEV4Bk&force_default=yes&ycrid=na-51b6eff0d32b5c5b3bf14501cf1d4ebe-downloader10h&ts=5a862a0e24cc0&s=337dfc4144022d8eebc4d9f77221a6d58e2077e635276fed722358afb5847ac3&pb=U2FsdGVkX1_t40f3VBfvEMrFDXIMAwKvd6dW3QpdSs0NP3UYNw-yO1n12Ve0bA81Eq5ssuw34LRdmWsdKvIiNZioq7OJy9MU_DS0lIaMeYE)

#### 2. Устанавливаем переменную JAVA_HOME

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Этот компьютер -> Правая кнопка -> Свойства -> Дополнительные параметры системы (слева) -> Переменные среды (внизу)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://s201sas.storage.yandex.net/rdisk/f10d7aab974ebc118bced3a6db48741f9c67af60579d70aa8f761af03bd54561/5eebe152/GqH3a1ee2zemXlYuVGmUvwrCQhvVEze16-5cxP8Ui9fUpbkQZXGMMVKk4egE53Thdgu70jIvgNDjazoxKOHfeg==?uid=86236828&filename=2.JPG&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&tknv=v2&owner_uid=86236828&media_type=image&fsize=45400&hid=00aa1bc69fb2b6525903b33e357c5a96&etag=fd4a1b0fe38deeffb0c5d2353cb7fc0a&rtoken=o7xwdMJVs6SY&force_default=yes&ycrid=na-de06750c57ab2eb1416c3f676364bf23-downloader12h&ts=5a862bedd7880&s=a13fb7d8e0256f5f16cfc25dbb04ca360958308bcce568070699132d38e4747b&pb=U2FsdGVkX18TOgGjuZmp-AZCvSKNM_3UiReEK9DUPvkkyP4GvNmKBJOVBmJrgNadaJrWLTfsnZUsri5wOqtP77mmDzQhSENl59WbXCh2LFY)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;В разделе *"Системные переменные"* нажимаем *"Создать"*, называем переменную **JAVA_HOME**. В качестве значения переменной 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;проставьте путь, куда вы установили Java.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;В моем случае это

```
C:\Program Files\Java\jdk1.8.0_172
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Выглядит вот так:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://s559sas.storage.yandex.net/rdisk/c0e9d8a1ebd72a54a6cf846d606ec27b28a2785185c0d41b28293c0cb6f1f905/5eebe1a9/GqH3a1ee2zemXlYuVGmUvxfNAs_Kb1MpvaJ26sCt-XeEToPPXlF2LPvgkkZ_drf3rcCKeM9Im4pM1IwzNlgEqw==?uid=86236828&filename=3.JPG&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&tknv=v2&owner_uid=86236828&etag=86644c2c6e6547080e56ba8d4274e308&hid=6853d41330fbaea9e5ac68b10d96d092&fsize=28029&media_type=image&rtoken=Ar958wN28A19&force_default=yes&ycrid=na-5ddbcf146f1a05f97a0d56ad5c79b890-downloader12h&ts=5a862c3fdba00&s=c342af878e942311c56fee207bb9463efcbe95fc73219934f2277c6ac6768b6d&pb=U2FsdGVkX18YRV2FsWf2U4JmC1b87x6HFHI-Ui8Zp36IUHwXB3Qoj28rPRt-wIDcx0DXhX7Tv3L23x-BaW0XnCW_kw1tLfyTDPtqz4teka0)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;После этого вам нужно отредактировать переменную *Path*.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Откройте *Path* в том же списке переменных, и добавьте новой строкой:

```
%JAVA_HOME%\bin
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Должно выглядеть вот так:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://s663sas.storage.yandex.net/rdisk/295e4984d4af0698f274c1a93bc9e7edb5334624dea071a266265f31bf780e3c/5eebe206/GqH3a1ee2zemXlYuVGmUv3ntYN3qOJKYrzNlOIzYgKYDSgIIwMVAZ_l6VoCljGx_zsxHdBG9vu4yrpeySvj06g==?uid=86236828&filename=4.JPG&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&tknv=v2&owner_uid=86236828&media_type=image&hid=2d52e4142fb7173f223d71b1c86fca84&fsize=24920&etag=4cb6baee2e2ed27ab068416757883d1f&rtoken=7EZxKBru6vUF&force_default=yes&ycrid=na-a892eda84446688ded08f68232ef28c3-downloader12h&ts=5a862c988cb40&s=3762390e9c074c20dcffd4bc6bc6a87232117a20c00a49c30bbcb04ab4e6a965&pb=U2FsdGVkX19U5sULXwh4I5btcnTVclJWMOXFFuvHNV3BL6KCWOFDjGejgDBeE0qqYw0w4Bvs3BAnRGvs8lFLM5sR9ZfZXubmjqJc_j7F9BM)

#### 3. Устанавливаем Python

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ВАЖНО!**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Не скачивайте самый новый релиз Python, у него есть проблемы с совместимостью со Spark (проверено лично).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Рекомендую релиз 3.7.5, на нём всё точно работет (опять же, проверено лично).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Скачиваем установочник отсюда:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https://www.python.org/downloads/

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Самый удобный вариант - *"Windows x86-64 executable installer"*, то есть обычный exe-шник.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Во время установки необходимо  поставить галочку рядом с
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*"Add python.exe to Path"* (это нужно чтобы не добавлять в *Path* ничего руками, как мы делали с Java)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://s137vla.storage.yandex.net/rdisk/6eee32c15e2e6747e5ec29b21ed8a85cccfbcca662a9d6dd3bf3d7a77eabcc40/5eebe30b/GqH3a1ee2zemXlYuVGmUv23gX0x2SAcWBzd8s2Zeje4K6jfLeBRkjSdawgMABMEHGYse_i_-kcEoJFI9OLd5Hg==?uid=86236828&filename=5.JPG&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&tknv=v2&owner_uid=86236828&fsize=46366&media_type=image&etag=14295c6bc8c0cbc5e0dccb1741076a56&hid=3f54cde87f29f5fdc6b344f89f49d17e&rtoken=E6kvDrV9Klzi&force_default=yes&ycrid=na-3ea7413395426e0f58346abc40a7c795-downloader23e&ts=5a862d92698c0&s=848257c74cc135205e501b5987f9c4aa13bbacc0bc36e8f1ef4c031074d7b7b2&pb=U2FsdGVkX19HUJQK4qfpG_IHRDJ0xcFDMjiWNuSkaYuzWgLW47rEmC8_hd6cnEVs1vVxc4DZXxv0Ma2qdfzHQV51_W1OohDHVDc0d4taj1I)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Проверяем что Python успешно установлен с помощью команды

```
python --version
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Результат должен выглядеть так:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://s681sas.storage.yandex.net/rdisk/d1eb11efec99171af2e9982f9edcb66d500544908f8baa1bb36a44d0d9c32ae2/5eebe3be/GqH3a1ee2zemXlYuVGmUv7EWEgUx9cLjmiUJ1ouMyrIEQS5yqFRYPd-Q0KI6CijskmMffn7eluo9dfPxUPtSIw==?uid=86236828&filename=6.JPG&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&tknv=v2&owner_uid=86236828&fsize=10892&hid=fb7a83f961ab21bc7896b5ba43cd180f&media_type=image&etag=640e1e4f525de39c57a83f497719011d&rtoken=7ZPTWJPk0Yds&force_default=yes&ycrid=na-b1045968675ad1d7078eed0f60a542e0-downloader23e&ts=5a862e3c2a940&s=9588277029afca7ef632b15d3831578c0d1f2194ef20909d44781a09bd56748c&pb=U2FsdGVkX18SwoMPZIQ94I8r7drZAK21IqQKjmNlnPAdhumUazhjWcWAEfT_sbHdlB6ekJ8mv0fiKHr6N-id-Fhw1sbgoUxjuL4oQGB2Ltg)

&nbsp;&nbsp;**4. Устанавливаем Spark**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Идем вот сюда:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://spark.apache.org/downloads.html

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Выбираем версию **Spark 2.4.6** и версию **Hadoop 2.7 (Pre-built for Apache Hadoop 2.7)**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Кликаем вот на эту ссылку:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://s155myt.storage.yandex.net/rdisk/47b2bd0e518e20bae40c8f06caa468f153b511939db66b231f8385f42f388e97/5eebe4ad/GqH3a1ee2zemXlYuVGmUvw6RXzzruMMem0yH1gbOUVWF5xYHwH8ubhLY8kVktjY8AtNXM4au_zMZD7GVe7tcqw==?uid=86236828&filename=7.JPG&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&tknv=v2&owner_uid=86236828&fsize=39215&media_type=image&etag=3f1c65e72d156e94d690cecd6e5551aa&hid=c00cbaa93062f315cc08dd51f19f707f&rtoken=2lm93J6ndxKT&force_default=yes&ycrid=na-aa01a7a0ee5c28fb2d5a7502cebddb76-downloader7f&ts=5a862f210c540&s=24baf9e5d54b6112aea62efe72d7ebf67eb4484468516be0548004140dfbbfb6&pb=U2FsdGVkX1931YR5uB30WbGOISLmZX4IZdA5eoFADztI9PLrb1g6pBWKqdJWWzs9QcGZY_zqF7P8bDwo7yDdO1Xhqy0KyPbLoWI4S2TQKEY)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Оказываемся на новой странице, и кликаем вот сюда:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://s687sas.storage.yandex.net/rdisk/fc52988739f0dbf2eb517361c0d366944864361f7a452d36d5157d8656a73dbc/5eebe5ac/GqH3a1ee2zemXlYuVGmUv3Ss_aRcz5k-cvnNtafxXnbjRSivLqTrqGm5U0EWQUT2Uufyuj1OtOPx9qIznUQYEw==?uid=86236828&filename=8.JPG&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&tknv=v2&owner_uid=86236828&etag=fe9fe2353da92d5f346849084a6d4d8e&fsize=75154&media_type=image&hid=82b14416271766c0e7c2e6d166e3e94e&rtoken=Xnq6FY5IZMXA&force_default=yes&ycrid=na-ae8966db95040b9ac35fb8632abe984b-downloader7f&ts=5a8630143c300&s=f6e0ca28c9a607b8828c5799ec8c26169130a08a4502924911ebf8f3cc2fb9dd&pb=U2FsdGVkX1_NcRq9JnTTD3qqXOscfOvGM-4of4zvKmzl52IVaYBn7qsJRR2vQC0-n8uexzh2JWrLw_GU8zLCj21JLWUI482cnsNbzaXwfp8)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;После этого начнется скачивание архива в формате .tgz (размером около 200Мб)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Когда он скачается, создайте в удобном вам месте папку "Spark", и разархивируйте содержимое вашего архива в неё.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Зайдите в папку "Spark", перейдите в папку bin, откройте командную строку и наберите в ней команду

```
pyspark
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Если установка прошла корректно, вы увидите следующую картину:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://s259vla.storage.yandex.net/rdisk/ccdf136efb9370ce58922b18d9d3a97b1bdbf9388008f14d2f722edcdb74bb76/5eebe675/GqH3a1ee2zemXlYuVGmUv6GsOqhvE-LWBRaw_hvWXbqz6hKX56DhV5aKWG3QT-sGexRTWoT6M-ZNPEHrOnEm_w==?uid=86236828&filename=9.JPG&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&tknv=v2&owner_uid=86236828&media_type=image&fsize=20149&hid=9800e6036de244342989ebf07952ccf1&etag=ba038fad001d7cd3f6eaf7677d9027d8&rtoken=sjN9RVNo2uBM&force_default=yes&ycrid=na-df00ad590ac528d3de68c962018d7d09-downloader11h&ts=5a8630d3ec740&s=f195164f328c4f62d70ae994ce8085e68b52cb12c580c3de76392ca7625db4ff&pb=U2FsdGVkX19ja7sJ_N-XxOkmraE8ssPDakQVtbPJ5xsT1cMOoLdIaXTutTuHb055lKZS9kmrkAm5LXEd_-WuggELU2h_ghlW3hQpxe1YkgI)


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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://s225vla.storage.yandex.net/rdisk/9e19f04ddda0c22d9f7f0d414899ab8fa55d2fd09a991ab87b8fbf20ed966622/5eebe82e/GqH3a1ee2zemXlYuVGmUv_lQf1r4Ly5Pees1pAgzJfeuXnufzeUlJL5mfgmk4G9Jnd17xZ5UAuZl5NfWVE1sPg==?uid=86236828&filename=10.JPG&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&tknv=v2&owner_uid=86236828&media_type=image&fsize=33834&hid=bd420325d1a7207210a2bd336c3f0114&etag=b84a70da7f80c1c68af1ee0659a06a99&rtoken=RK0T3iNkFe7A&force_default=yes&ycrid=na-5f66eff3843db120397b098c6007e827-downloader13h&ts=5a8632787e780&s=292cd0508c1a09f12bb0931882240bc7514b663a77e4eecbcdababe390a50d52&pb=U2FsdGVkX18-idm6J7TSVOzJ-hXCMjY8R5GkmllV4khzTZM4avAxU3uiRWt4-rE4GJ9VSAlzR9797kWzJ2sTxrlF1YRO66aJFtiOG-E94g0)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Далее, таким же образом создаём переменную *HADOOP_HOME*.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;В качестве значения для нее указываем:

```
%SPARK_HOME%\hadoop
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://s192sas.storage.yandex.net/rdisk/9762aa736617a6243577e26fc3d82f2105c194ca047d4b08d93d6c7ed8ab2eb8/5eebe8bc/GqH3a1ee2zemXlYuVGmUvzh2_11gdTz0l0K010eUso7w0QN1HYYyvJSdMQyu1R5nxEMKfkwfNba7DQggmJgDHg==?uid=86236828&filename=11.JPG&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&tknv=v2&owner_uid=86236828&media_type=image&fsize=35569&etag=1c7e065e1bfa407a7e37b2e671dfb7de&hid=6432c198840b76dfb7d186429c05598d&rtoken=xRiYJbPgUeoo&force_default=yes&ycrid=na-741238939463e183526a6223f2cfd940-downloader13h&ts=5a8632ffea700&s=0f8b5e6ad64d6cb08c534f4615d37ce984de4be19f205917f171520db686bc34&pb=U2FsdGVkX1-etnTunPzUiYQjhsdkdF2GG18swOZ4nibHViV9fBGSO-YoFIATIrEGvSP6YU9fHVs8GGyCVeGXQvLyp6oUMUXG66EOKpZJacU)
