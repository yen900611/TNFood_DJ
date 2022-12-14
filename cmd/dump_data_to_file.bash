export PROJECT_HOME=$(pwd)
cd $PROJECT_HOME/mysite
python manage.py dumpdata --natural-foreign --natural-primary \
-e contenttypes -e auth -e admin -e sessions \
--indent 2 -o ./db/latest_db.json
cp ./db/latest_db.json ./db/$(date -I ).json
cd $PROJECT_HOME