# Тестовое задание FastAPI

### Краткое описание

 Написать простой каталог для книжного магазина с фильтрацией по тегам и пагинацией. 

### Подробное описание

Написать сервис, который хранит информацию о книгах: Название, описание, автор, страна, год публикации, жанр и категории типа “Фантастика”, “Историческая литература”, “Про здоровье”, “Классика”, и так далее. 

Эту информацию можно вносить, редактировать и удалять. 

По любой информации о книге можно проводить фильтрацию и пагинацию. 

### Ключевые вопросы

1. Как реализовать схему бд?
2. Как реализовать механизм обновления структуры данных при изменении
   требований?
3. Как будет выглядеть структура кода?
4. Как будет реализована валидация входных данных?
5. Как будет реализована фильтрация?
6. Какова структура эндпоинтов?

### Дополнительные вопросы

1. Как реализовать фильтрацию типа: “Хочу отфильтровать зарубежную классическую
   фантастику 20-го века?”
2. Как добавить книгу с двумя авторами?
3. Реализовать условие валидации, чтобы дата рождения автора была раньше даты
   его смерти

### Критерии хорошего решения

Умение пользоваться миграциями
Реализованы связи many_to_many
Хорошая архитектура кода и читаемость











### Ответы на дополнительные вопросы

1. Чтобы сделать такую фильтрацию нужно передать на GET /books/ параметры через запятую . Т.е вы можете передать 
   
   ```http
   /books/?types=classic,fantastic&before_publication_year=2000&after_publication_year=1901
   ```

2. В модели Book я сделал связь Many-to-Many для авторов , поэтому на создании передается список id авторов







### Развертывание проекта

-  Скопировать проект  
   ```bash
   git clone https://github.com/y0gurt-dv/WIS-Software-test-project.git
   ```
- Установка зависимостей
   ```bash
   pip install -r requirements.txt
   ```
- Создать файл .env
- Вынести константы в .env
   ```
   DB_NAME=
   DB_USER=
   DB_PASSWORD=
   DB_HOST=
   DB_PORT=
   ```
- Запуск миграций
   ```bash
   alembic upgrade head
   ```
- Запуск проекта
   ```bash
   python main.py
   ```




