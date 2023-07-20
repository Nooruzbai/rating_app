SchoolRatingAPI Application intended to help parents to choose the best school for their kids' needs and help them make an informed decision.

Technologies utilized: Django, DjangoREST, PostgreSQL, PyJWT, social-auth-app-django, Docker, DockerCompose, Git.

In order to install and launch the application, please follow the steps bellow:

1. Install Python 3.10.6
2. If you do not have GIT, please install it.
3. Install PostgreSQL.
4. Install Docker(If you want to start the application with docker services)
4. Clone the repository from the GitHub using the command.

    git clone https://github.com/Nooruzbai/rating_app.git

5. After cloning the repository, please go to cloned folder and execute the commands in Linux or Windows command line bellow:

6. Create virtual environment:  
python3 -m venv venv.  
7. Activate the virtual environment:  
for Linux: source venv/bin/activate  
for Windows: python3 venv\Scripts\activate
8. Install the dependencies:  
pip install -r requirements.txt

9.Execute the command to apply migrations by going to "source" folder:  
python3 manage.py migrate  
9.Load the fixtures staying in "source" folder:  
python3 manage.py loaddata fixtures/auth.json  
python3 manage.py loaddata fixtures/dump.json
10. Create the ".env" file and fill it with data:

SECRET_KEY=secret_key

DEBUG=(1 for True, 0 for False)

DJANGO_ALLOWED_HOSTS=*

EMAIL_HOST=smtp_host

EMAIL_HOST_USER=email_of_host_user

EMAIL_HOST_PASSWORD=password

EMAIL_PORT=port

POSTGRES_DB=postgres

POSTGRES_USER=postgres

POSTGRES_PASSWORD=postgres

POSTGRES_PORT=5432

POSTGRES_HOST=localhost  

    (Attention: in case if you are running in docker, please put "db", for local machine put "localhost")

DATABASE=postgres  

11. In order to start the project, please enter the command in the command line:

python3 manage.py runserver

12. If you want to run it in docker, please input command bellow:  
docker compose up --build

In order to go to the admin dashboard, please go to the following url http://localhost:8000/admin  
If you have encountered any issues while installing the application, please contact me to nooruzbay@gmail.com