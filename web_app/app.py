from flask import Flask, render_template
from web_app.models import db, Page


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py', silent=True)

    db.init_app(app);

    @app.route('/')
    def index():
        page = Page.query.filter_by(id=1).first()
        return render_template('index.html', TITLE='Flask-Docker', CONTENT=page.content)

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
