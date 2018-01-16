import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app import create_app
from models import Page, db

app=create_app()

with app.app_context():
    page=Page()
    page.title="Home Page"
    page.content="<h1><b>Hello from flask - docker!<b></h1>"
    page.is_homepage=True

    db.session.add(page)
    db.session.commit()
