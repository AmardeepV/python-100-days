# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False


# def is_authanticate_decorator(func):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             func(args[0])
#     return wrapper


# @is_authanticate_decorator
# def create_blog_post(user):
#     print(f"this is {user.name}'s new blog post")


# new_user = User('ad')
# new_user.is_logged_in = True
# create_blog_post(new_user)


def logging_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        print(f"You called {function.__name__}{(args)}")
        print(f"It returned: {result}")
    return wrapper

# TODO: Use the decorator 👇


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)
