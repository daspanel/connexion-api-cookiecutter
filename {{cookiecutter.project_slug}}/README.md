# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

The API can be reached under ```http://localhost:5000/v1.0/pets/```.

You can test the API using your browser under 
<http://localhost:5000/v1.0/pets/ui>

The default API auth key is ```apikey```

## Requirements

- Python 2.7/3.5
- Gunicorn
- TinyDB: <https://github.com/msiemens/tinydb>
- TinyDB-JsonOrm: <https://github.com/abnerjacobsen/tinydb-jsonorm>

## Installation

Run 
```shell
pip install -r requirements/dev.txt
```
for a local install of all Python modules required to run the sample app.

To start the sample app Gunicorn server, run:
```shell
{{cookiecutter.project_slug}}/wsgi_gunicorn
```

To see all avaiable options to run your server run:
```shell
{{cookiecutter.project_slug}}/wsgi_gunicorn --help
```

You can set permanent configuration otions editing:
* {{cookiecutter.project_slug}}/config.py
* {{cookiecutter.project_slug}}/gunicorn_conf.py
* {{cookiecutter.project_slug}}/gunicorn_logging.conf

## How to develop an API

First, define your REST API in the configuration under 
```{{cookiecutter.project_slug}}/swagger/pets.yml```, 
then add the Python logic for the *operationId* under 
```{{cookiecutter.project_slug}}/modules/pets/api.py```.

Also, you can create additional api modules. Let's say you want to add a new 
module called ```orders```:

- First define the swagger file 
```{{cookiecutter.project_slug}}/swagger/orders.yml```

- Then create ```{{cookiecutter.project_slug}}/modules/orders/api.py``` with all 
Python logic for every *operationId* you defined in the orders.yml file.

- Edit ```{{cookiecutter.project_slug}}/app.py``` and add an new module blueprint. 
    You app.py code is to become like this:
    ```python
    # Add api blueprints
    app.add_api(
        'swagger/pets.yaml', base_path='/v1.0/pets'
    )
    app.add_api(
        'swagger/orders.yaml', base_path='/v1.0/orders'
    )
    ```

## SwaggerUI

Go to [here](http://localhost:5000/v1.0/pets/ui) to view the brilliant SwaggerUI documentation of your API.

## Resources
### Connexion
[Documentation](https://connexion.readthedocs.io/en/latest/)
[Github](https://github.com/zalando/connexion)

## Credits
* <https://github.com/jgontrum/connexion-cookiecutter>
* <https://github.com/celery/cookiecutter-celeryproject>


