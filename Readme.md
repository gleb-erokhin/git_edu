# I. Инструкция для работы с Git и удалёнными репозиториями

## 1. Что такое Git?
Git - это одна из реализаций распределённых систем контроля версий, имеющая как и локальные, так и удалённые репозитории. Является самой популярной реализацией систем контроля версий в мире.

## 2. Начало работы
Для начала работы с __*git*__ необходимо задать имя и почту для того чтобы коммиты помечались при создании данными владельца. Для этого необходимо выполнить 2 команды: 

1. *git config --global user.name __"name"__*
2. *git config --global user.email __"email address"__* 
3. *git config --global core.editor __"program" -wait__*

## 3. Подготовка репозитория
Для создания репозитория необходимо выполнить команду *__git init__*  в папке с репозиторием и у Вас создаться репозиторий (появится скрытая папка .git)

## 4. Создание коммитов

### 4.1. Git add
Для добавления измений в коммит используется команда *git add*. Чтобы использовать команду *git add* напишите *git add <имя файла>*

### 4.2. Просмотр состояния репозитория
Для того, чтобы посмотреть состояние репозитория используется команда *git status*. Для этого необходимо в папке с репозиторием написать *git status*, и Вы увидите были ли измения в файлах, или их не было.

### 4.3. Создание коммитов
Для того, чтобы создать коммит(сохранение) необходимо выполнить команду *git commit*. Выполняется она так: *git commit -m "<сообщение к коммиту>*. Все файлы для коммита должны быть ***ДОБАВЛЕНЫ*** и сообщение к коммиту писать ***ОБЯЗАТЕЛЬНО***.

## 5. Перемещение между сохранениями
Для того, чтобы перемещаться между коммитами, используется команда *git checkout*. Используется она в папке с пепозиторием следующим образом: *git checkout <номер коммита>*

## 6. Журнал изменений
Для того, чтобы посмтреть все сделанные изменения в репозитории, используется команда *git log*. Для этого достаточно выполнить команду *git log* в папке с репозиторием. Для короткого отображения используется параметр *git log __--oneline__*

## 7. Ветки в Git

### 7.1. Создание ветки

Для того, чтобы создать ветку, используется команда *git branch*. Делается это следующим образом в папке с репозиторием: *git branch <название новой ветки>*

## 8. Слияние веток

Для того чтобы дабавить ветку в текущую ветку используется команда *git merge __name branch__*

## 9. Удаление веток
Для удаления ветки ввести команду "git branch -d 'name branch'"

## Проверка конфликта ветка new
