#Создайте декоратор, который ограничивает доступ к функции
# определенным типам пользователей. Предполагается, что
# тип пользователя будет передаваться в качестве аргумента
# user_type (str) в декорируемую функцию. Типы пользователей: "admin", "user",
# "auth_user". Результат должен быть вида: "access", если разрешен
# "denied", если нет.
def decorator (func):
    def wrapper (user_type):
       if user_type == 'user':
           return 'denied'
       elif user_type in ('admin', 'auth_user'):
           return 'access'
       return 'No data'
    return wrapper
@decorator
def main_func(user_type: str):
    return 'Ok'
print(main_func ('user'))
