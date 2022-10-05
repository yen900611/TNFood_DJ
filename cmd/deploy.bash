git fetch
git pull origin master
git checkout master
source ./venv/bin/activate
pip install -r requirements.txt
cd ./mysite
python manage.py migrate
python manage.py collectstatic