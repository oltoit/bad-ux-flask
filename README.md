# bad-ux-flask

### Flask installation

If you haven't installed python, flask or an environment like venv please follow this [flask starter guide](https://flask.palletsprojects.com/en/stable/installation/)


### Dependencies

If this is started locally for the first time you might need to install some dependecies. You can do this by executing ```pip install -r requirements.txt```. This will install all dependencies from the ```requirements.txt``` file locally.

<br>

Any locally installed dependencies that are used in the code need to be added back into the ```requirements.txt``` file so the docker-container knows to install those dependecies. This can be done automatically be executing ```pip freeze > requirements.txt``` locally and commiting the ```requirements.txt``` file.