from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Column, String


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py', silent=True)

    db = SQLAlchemy(app)

    class Page(db.Model):
        __tablename__ = 'page'
        id = Column(Integer, primary_key=True)
        title = Column(String)
        content = Column(String)

    class Post(db.Model):
        __tablename__ = 'post'
        id = Column(Integer, primary_key=True)
        content = Column(String)

    db.create_all()

    @app.route('/')
    def index():
        return render_template('index.html', TITLE='Flask-Docker')

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='Flask-Docker')

    @app.route('/db_test')
    def db_test():
        import psycopg2

        connection = psycopg2.connect('dbname=flask user=postgres password=postgres host=postgres')
        cursor = connection.cursor()
        cursor.execute('select * from page')
        id, title, content = cursor.fetchone()
        connection.close()

        return 'Test query fetch 1 : {} | {}'.format(id, title)

    return app
