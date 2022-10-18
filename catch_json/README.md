<h1>Task 1</h1>
<p>Задача на алгоритмы.
Решена за счет: <br>
- рекурсии
- переопределения исходного кортежа в более удобный тип данных</p>
<h4>Запуск после клонирования: <br><br></h4>

    python3 find_a_way/main.py

<h2>Task 2</h2>
<p>Парсинг сайта. Порядок запуска:<br>
1. клонирование<br>
2. создание файла .env в директории с manage.py:<br>

    export SECRET_KEY=<какой-тосекретныйключ>
    export POSTGRES_DB=<названиебд>
    export POSTGRES_PASSWORD=postgres
    export POSTGRES_USER=postgres
    export HOST_NAME=pdb
3. Запуск сборки
    

    docker-compose up --build
4. После успешной сборки, необходимо выполнить миграции


    docker-compose down
    docker-compose run appd python manage.py migrate

5. Повторно поднимаем:


    docker-compose up

Проходим по http://0.0.0.0:8000/from_file/ для подгрузки файла с расширением xlsx, а для ввода единичного артикула 
проходим по http://0.0.0.0:8000/article/