import  os

from flask import Flask, render_template, send_from_directory, url_for
from flask_admin import Admin
from flask_admin.consts import ICON_TYPE_FONT_AWESOME
from flask_login import login_required
from flask_security import SQLAlchemyUserDatastore, Security

from web_app.models import db, Page, Menu, Role, User
from web_app.views import PageModelView, MenuModelView, SecureAdminIndexView


def create_app():
    app=Flask(__name__)
    app.config.from_pyfile('settings.py', silent=True)

    db.init_app(app);

    admin=Admin(app, name='Flask-Docker CPanel', template_mode='bootstrap3', index_view=SecureAdminIndexView())
    admin.add_view(MenuModelView(Menu, db.session, menu_icon_type=ICON_TYPE_FONT_AWESOME, menu_icon_value='fa-list'))
    admin.add_view(PageModelView(Page, db.session, menu_icon_type=ICON_TYPE_FONT_AWESOME, menu_icon_value='fa-file-o'))

    user_datastore=SQLAlchemyUserDatastore(db, User, Role)
    security=Security(app, user_datastore)

    @app.route('/')
    @app.route('/<url>')
    def index(url=None):
        content=''
        page=None

        if url is not None:
            page=Page.query.filter_by(url=url).first()
        else:
            page=Page.query.filter_by(is_homepage=True).first()

        if page is not None:
            content=page.content
        else:
            return '<b>404</b> : Page not found'

        menu=Menu.query.order_by('order').all()

        return render_template('index.html', TITLE='Flask-Docker', CONTENT=content, MENU=menu)

    @app.route('/db_test')
    def db_test():
        import psycopg2

        connection=psycopg2.connect('dbname=flask user=postgres password=postgres host=postgres')
        cursor=connection.cursor()
        cursor.execute('select id, title, content from page')
        id, title, content=cursor.fetchone()
        connection.close()

        return 'Test query fetch 1 : {} | {}'.format(id, title)

    @app.route('/secret_url')
    @login_required
    def secret_url():
        return '<h1>SECRET PAGE</h1>'


    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

    return app
