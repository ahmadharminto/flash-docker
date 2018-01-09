from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/')
    def index():
        return render_template('index.html', TITLE='Flask-Docker')

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='Flask-Docker')

    @app.route('/db_test')
    def db_test():
        import psycopg2

        connection = psycopg2.connect('dbname=flask user=postgres password=postgres host=postgresql')
        cursor = connection.cursor()
        cursor.execute('select * from page')
        id, title = cursor.fetchone()
        connection.close()

        return 'Test query fetch one : {} | {}'.format(id, title)

    return app
