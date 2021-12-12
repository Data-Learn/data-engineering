# Создаем лямбда функцию в AWS Console

## Введение
В этом практическом лабораторном сценарии вы напишете лямбда-функцию Node.js, которая проверяет URL-адрес (например, www.amazon.com) и возвращает код состояния, который показывает, работает ли веб-сайт или нет. Во время этой лабораторной работы у вас будет возможность изучить консоль Lambda, код функции, роли выполнения, тестовые события и результаты выполнения. AWS Lambda позволяет писать краткие функции и беспокоиться только о своем коде. Поскольку Lambda является бессерверной, AWS управляет базовой инфраструктурой за вас. 

## Решение
Авторизуйтесь на сайте https://aws.amazon.com/free/. 
Откройте код в соседней вкладке. Он нам понадобиться для выполнения задания. https://github.com/linuxacademy/content-aws-ccp-labs/blob/master/creating-a-lambda-function-using-the-aws-console/index.js

### Создаем Node.js лямбда функцию в AWS Console
1. В AWS console выберите Lambda > Functions

![ServiceSelect](./img/ServiceSelect.jpg)

2. Нажмите кнопку `Create function`

![CreateFunction](./img/CreateFunction.jpg)

3. Выберите `Author from scratch`

![AuthorFromScratch](./img/AuthorFromScratch.jpg)

4. Установите следующие значения:
    - _Function name_: **holURLChecker**
    - _Runtime_: **Node.js**

![FunctionName](./img/FunctionName.jpg)

5. Расширьте **Change default execution role**. Затем для _Execution role_ выберите **Create a new role with basic Lambda permissions**

![ChangeDefaultExecutionRole](./img/ChangeDefaultExecutionRole.jpg)

6. На вкладке в которой открыт GitHub, скопируйте код из index.js.

![CodeSnippet](./img/CodeSnippet.jpg)

7. Вернитесь на вкладку AWS console и нажмите на кнопку **Create function**.

8. На открывшейся странице Lambda функции удалите существующий код в функции и вставьте только что скопированный код из index.js.

![CreateLambdaIndex](./img/CreateLambdaIndex.jpg)

9. Нажмите **Deploy**. 

![Deploy](./img/Deploy.jpg)

### Тестируем функцию, используя тестовое событие.
1. Нажмите на кнопку **Test**, расположенную наверху.

![ClickTest](./img/ClickTest.jpg)

2. В появившемся модальном окне, в поле _Event name_ укажите значение **myTestEvent**. Затем нажмите **Create**.

![CreateTest](./img/CreateTest.jpg)

3. Теперь снова нажмите на кнопку **Test**. Посмотрите на ответ. 
    - В ответе должно быть <span style="color:red" style="font-weight: bold">*200*</span>. Это значит, что сайт работает.

![resultTest](./img/resultTest.jpg)

### Посмотрите на CloudWatch Logs

1. Нажмите на **Monitor**

![ClickMonitor](./img/ClickMonitor.jpg)

2. Нажмите на **View logs in CloudWatch**.

![ViewLogs](./img/ViewLogs.jpg)

3. Нажмите на самый свежий лог из списка логов. 

![SelectLogStream](./img/SelectLogStream.jpg)

4. Обратите внимание на **Billed Duration**

![BilledDuration](./img/BilledDuration.jpg)

## Заключение
Поздравляем с успешным завершением лабораторной работы!
