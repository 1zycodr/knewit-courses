# Installation:
git clone https://github.com/1zycodr/knewit-courses
<br>
cd knewit-courses
python -m venv env
source env/bin/activate
pip install -U pip && pip install -r requirements.txt
./manage.py makemigrations && python manage.py migrate
./manage.py createsuperuser
./manage.py runserver
