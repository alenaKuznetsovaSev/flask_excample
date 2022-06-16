# flask_excample
иду по The Flask Mega-Tutorial

Before running Flask you need to set the FLASK_APP environment variable:<br>
*(venv) $ export FLASK_APP=main.py*
<br>
To create the migration repository for site you should write:<br>
*(venv) $ flask db init*

Need to install:
    <li>*(venv) $ pip3 install flask-wtf*</li>
    <li>*(venv) $ pip3 install flask-sqlalchemy*</li>
    <li>*(venv) $ pip install flask-migrate*</li>
You can run your first web application, with the following command:<br>
*(venv) $ flask run*
<br><br>
Since I have updates to the application models, a new database migration needs to be generated:<br>
*(venv) $ flask db migrate -m "posts table"*<br>
And the migration needs to be applied to the database:<br>
*(venv) $ flask db upgrade*



