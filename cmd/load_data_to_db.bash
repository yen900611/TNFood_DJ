export PROJECT_HOME=$(pwd)
cd $PROJECT_HOME/mysite
python manage.py loaddata ./db/latest_db.json
cd $PROJECT_HOME