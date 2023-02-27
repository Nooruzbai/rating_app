Для запуска проекта установите python версии Python 3.10.6 и pip
Установите PostgreSQL

После клонирования перейдите в склонированную папку и выполните следующие команды:

Создайте виртуальное окружение командой:
python3 -m venv venv

Активируйте виртуальное окружение командой:
Для Linux:
source venv/bin/activate

Для Windows:
python3 venv\Scripts\activate

Установите зависимости командой:

pip install -r requirements.txt

Примените миграции командой

./manage.py migrate
Загрузите фикстурные статьи командой

./manage.py loaddata fixtures/auth.json
./manage.py loaddata fixtures/dump.json


Создайте в директории с проектом файл .env и заполните по примеру:

SECRET_KEY=secret_key

DEBUG=(1 for True, 0 for False)

DJANGO_ALLOWED_HOSTS=''

EMAIL_HOST=smtp_host

EMAIL_HOST_USER=email_of_host_user

EMAIL_HOST_PASSWORD=password

EMAIL_PORT=port

POSTGRES_DB=db_name

POSTGRES_USER=db_user_name

POSTGRES_PASSWORD=db_user_password

POSTGRES_PORT=db_port

POSTGRES_HOST=db_host

DATABASE=postgres

Чтобы запустить сервер выполните:

./manage.py runserver

Для доступа в панель администратора перейдите по ссылке http://localhost:8000/admin