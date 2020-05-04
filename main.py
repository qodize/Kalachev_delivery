from flask import Flask
from data import db_session
from flask_login_multi.login_manager import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '54321qwerty'


def main():
    db_session.global_init('db/PizzaMan_db.db')
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
