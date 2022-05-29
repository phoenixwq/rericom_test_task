# rericom_test_task
Для запуска необходимо собрать и запустить контейнеры
```
docker-compose build
docker-compose up
```
Также необходимо, подключится к контейнеру backend и выполнить следующие команды
```
docker-compose exec backend bash 
python manage.py makemigrations --noinput
python manage.py migrate --noinput
```
Также необходимо создать пользователя для тестирования, можно воспользоваться следующей командой
```
python manage.py createsuperuser
```
