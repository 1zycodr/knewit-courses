# Installation:
git clone https://github.com/1zycodr/knewit-courses
<br>
cd knewit-courses
<br>
python -m venv env <br>
source env/bin/activate <br>
pip install -U pip && pip install -r requirements.txt <br>
./manage.py makemigrations && python manage.py migrate <br>
./manage.py createsuperuser <br>
./manage.py runserver <br>
