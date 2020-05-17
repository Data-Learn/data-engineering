# How to: Как установить утилиту AWS CLI

## Introduction
В данной инструкции информация по установке утилиты AWS CLI.

AWS CLI - это утилита, позволяющая управлять ресурсами AWS с помощью командной строки.

## Requirements
**Linux:** 
1. У вас должен быть любой пакетный менеджер, чтобы разпаковать архив. 
2. Должна стоят: CentOS, Fedora, Ubuntu, Amazon Linux 1, and Amazon Linux 2. 

**Windows**
1. У вас должна быть ОС Windows XP или выше.
2. Обязательно должна быть 64 битная версия ОС


## Installation
[Инструкции](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) взяты с документации AWS.

**Linux**
1. Скачиваем файл: 
а) Можно через курл: curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" (флаг -о указывает имя файла, в который будет загружен пакет)
б) Можно через браузер: https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip
2. Распаковываем архив, в необходимую директорию.
3. Внутри директорий, куда распаковали архив, запускаем установку: sudo ./aws/install

**Windows**
1. Скачиваем [установщик](https://awscli.amazonaws.com/AWSCLIV2.msi)
2. Запускаем скачанный установщик и следуем инструкциям на экране.
По-умолчанию программа устанавливается в C:\Program Files\Amazon\AWSCLIV2

**MacOs**
1. Качаем файл: curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
2. Перед тем как запустить установщик, необходимо создать XML-файл, который укажет папку для установки, следующей структуры

```xml
<?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
   <array>
     <dict>
       <key>choiceAttribute</key>
       <string>customLocation</string>
       <key>attributeSetting</key>
       <string>ЗДЕСЬ НЕОБХОДИМО УКАЗАТЬ ПУТЬ ДО ПАПКИ</string>
       <key>choiceIdentifier</key>
       <string>default</string>
     </dict>
   </array>
 </plist>
```
Заменяем "ЗДЕСЬ НЕОБХОДИМО УКАЗАТЬ ПУТЬ ДО ПАПКИ" на путь до папки куда нужно произвести установку.
3. Запускаем установщик, указывая имя пакета, для установки -pkg, установка только для текущего юзера -target CurrentUserHomeDirectory, и путь до созданного XML файла -applyChoiceChangesXML: installer -pkg AWSCLIV2.pkg -target CurrentUserHomeDirectory -applyChoiceChangesXML choices.xml
4. Создаем ссылку в вашем $PATH, которая указывает на фактические программы aws и aws_completer. 
Поскольку стандартные пользовательские разрешения обычно не разрешают запись в папки в $PATH, установщик в этом режиме не пытается добавить ссылку. 
Вы должны вручную создать ссылки после завершения установки. Если ваш $ PATH включает в себя папку, в которую вы можете писать, вы можете выполнить следующую команду без sudo, если вы указали эту папку в качестве пути к цели. Если у вас нет доступной для записи папки в вашем $ PATH, вы должны использовать sudo в командах, чтобы получить разрешения на запись в указанную папку.
 sudo ln -s /ПУТЬ, КОТОРЫЙ УКАЗАЛИ В XML/aws-cli/aws /folder/in/path/aws
 sudo ln -s /ПУТЬ, КОТОРЫЙ УКАЗАЛИ В XML/aws-cli/aws_completer /folder/in/path/aws_completer

**Альтернативный вариант для MacOS**

Установка через менеджеров пакетов Homebrew (https://brew.sh/index_ru)
Это сторонний менеджеров пакетов, как альтернатива встроенным в Linux, но для Mac, через него можно устанавливать много разных утилит, полный список можно посмотреть на сайте.

1. Устанавливаем сам Homebrew:
Открываем Терминал, вставляем строчку и жмем Enter
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

2. Устанавливаем AWS CLI через Homebrew:
Открываем Терминал, вставляем строчку и жмем Enter
`brew install awscli`


**Для всех**
Проверяем корректность установки, вводя в командную строку: aws --version (получаем (версии могут отличаться) _aws-cli/2.0.6 Python/3.7.4 Linux/4.14.133-113.105.amzn2.x86_64 botocore/2.0.0_)

## Launch
Открываем командную строку и теперь у нас доступна утилита aws

