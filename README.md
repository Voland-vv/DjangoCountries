## ДЗ
### Часть-1
- [x] Сгенерирована заготовка django-проекта
- [x] Добавлено приложение(App)
- [x] По корневому url'у доступна html-страница с приветствием и минимальным оформлением
- [x] В проект добавлен `.gitignore` (venv, настройки IDE и файл БД не под репозиторием)
- [x] Проект загружен на github

### Часть-2
- [x] При отображении всех страниц используются html-шаблоны(templates)
- [x] В корень проекта добавлен файл countries.json со списком всех стран
- [x] По url: `/countries-list/` отображается нумерованный список всех стран (только названия стран)
- [x] Название каждой страны гиперссылка, которая ведет на персональную страницу данной страны.
- [x] Реализована персональная страница для каждой страны
- [x] На главной странице добавлена ссылка “Языки”(url: `/languages/`), на которой отображается список всех языков

### Часть-3
- [x] Создайте модель-класс Country.
- [x] Перенесите все страны из исходного json файла в базу данных(БД).
- [x] Измените работу вашего приложения на работу с БД
- [x] Выгрузите данные из БД в фикстуру(fixture) countries.json

### Часть-4
- [x] Используя информацию с занятия, измените структуру БД, реализовав связь “многие-ко-многом” для стран и языков.
Не забудьте: выгрузить обновленные данные из БД fixture: countries.json
- [x] Добавьте в проект файл README.md, добавив в него:
  - Информацию о запуске проекта после клонирования
  - Список всех заданий, пометив выполненные

### Часть-5
Примечание: Модуль-5 “работа с формами”, в рамках проекта “Django Countries” мы не будем использовать формы, поэтому задания с формами не связаны.

- [ ] Добавьте в проект файл requirements.txt
- [ ] На странице “Языки”, все языки в списке сделайте гиперссылками, каждая ведет на отдельную страницу, на которой отображаются страны, которые говорят на выбранном языке.
- [x] Все ваши шаблоны(templates) используют наследование от базового шаблона.
- [x] Все используемые url’ы являются именованными.

### Часть-7
- [ ] На верху страницы со списком стран добавьте алфавит, каждая буква которого является гиперссылкой. Каждая гиперссылка(на букве) ведет на страницу на которой отображаются только страны на выбранную букву. См. аналогию тут.
- [ ] Внизу страницы со списком стран реализуйте пагинацию. На каждой странице отобразите 10 стран.