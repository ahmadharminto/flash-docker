from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from web_app.models import db, Page, Menu


def create_app():
    app=Flask(__name__)
    app.config.from_pyfile('settings.py', silent=True)

    db.init_app(app);

    admin=Admin(app, name='Flask-Docker', template_mode='bootstrap3')
    admin.add_view(ModelView(Menu, db.session))
    admin.add_view(ModelView(Page, db.session))

    @app.route('/')
    def index():
        page=Page.query.filter_by(id=1).first()
        content=''
        if page is not None:
            content=page.content
        return render_template('index.html', TITLE='Flask-Docker', CONTENT=content)

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='Flask-Docker')

    @app.route('/db_test')
    def db_test():
        import psycopg2

        connection=psycopg2.connect('dbname=flask user=postgres password=postgres host=postgres')
        cursor=connection.cursor()
        cursor.execute('select * from page')
        id, title, content=cursor.fetchone()
        connection.close()

        return 'Test query fetch 1 : {} | {}'.format(id, title)

    return app
