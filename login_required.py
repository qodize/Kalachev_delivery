from flask import redirect
from flask_login import current_user
from functools import wraps


#  Вместо декоратора из библиотеки нам понадобится свой, т.к. у нас несколько ролей
#  Сам я взял этот декоратор с какого-то треда на каком-то сайте
def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                # return login_manager.unauthorized()
                if role == 'client':
                    return redirect('/login')
                return redirect(f'/{role}/login')
            if not (current_user.role == role or role == "ANY"):
                # return login_manager.unauthorized()
                if role == 'client':
                    return redirect('/login')
                return redirect(f'/{role}/login')
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
