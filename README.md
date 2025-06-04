This application was created to enhance the functionalities of an existing solution Learning and Development solution.
After the skills required per job type were gathered across the organization, the existing solution was used to analyze and identify the top ten skill gaps per job type. 
The functionality of this application consumes the top 10 skill gaps per jobtype and uses that to run a questionnaire to drill down the skill gaps to individual level and there by identify who to train for the different skills. 

To set up Training Gap Survey and Analysis, open the cmd/terminal and clone the main branch.

cd to the backend directory.

Create a virtual env (pip/conda).

python -m venv env

Run installations using the below command.
pip install -r requirements.txt

In the project root directory, create a file called .env and add the below env configs.

SECRET_KEY="Your secure secret key"

DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1 


Run migrations using the below command.
python manage.py makemigrations

python manage.py migrate

Run server using the below command
python manage.py runserver

This will have the backend running.

For the frontend, change to the frontend directory.

Run npm install

Run npm start

The app will lauch automatically in port 3000.
