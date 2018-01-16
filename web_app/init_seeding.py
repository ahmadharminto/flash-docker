import os
import sys

from flask_security import utils

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app import create_app
from models import Page, db, Role, User

app=create_app()

with app.app_context():
    admin_role=Role()
    admin_role.name='admin'
    db.session.add(admin_role)
    db.session.commit()

    root=User()
    root.email='ahmad.harminto@sociolabs.io'
    root.password=utils.hash_password("123456")
    root.active=True
    root.roles.append(admin_role)
    db.session.add(root)
    db.session.commit()

    page=Page()
    page.title="Home Page"
    page.content="<h1><b>Hello from flask - docker!<b></h1>"
    page.is_homepage=True

    db.session.add(page)
    db.session.commit()
