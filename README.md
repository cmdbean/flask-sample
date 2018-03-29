# flask-sample

Flask sample application with mysql


# Init Database
```
mysql -u root
drop database flask_sample
create database flask_sample
exit
```

# InitApplication
```
git clone git@github.com:cmdbean/flask-sample.git
cd flask-sample
pip install -r requirements.txt
FLASK_APP=run.py flask db init
FLASK_APP=run.py flask db migrate
FLASK_APP=run.py flask db upgrade
```
