#!/bin/sh
alembic downgrade base
rm -rf migrations/versions/*
alembic revision --autogenerate -m "initial"
alembic upgrade head
python ./web_app/init_seeding.py