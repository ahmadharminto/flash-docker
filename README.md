<p align="center"><img src="https://www.python.org/static/img/python-logo@2x.png"></p>

# flask-docker
Implementation flask using docker (hot reload)

## How to

Config : 
* web_app/settings.py
* migrations/env.py

For start instance :
> sudo docker-compose up --build

For login into instance, then initialize migrations :
> sudo docker-compose exec web_app bash

> alembic init migrations

Command migrations version table from instance :
> alembic revision --autogenerate -m "comment"

> alembic upgrade head

> alembic downgrade -1

> alembic downgrade base

> alembic history

For recreate initial migration scripts from instance :
> ./web_app/console/recreate_migration_files.sh