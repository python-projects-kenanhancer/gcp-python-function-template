import os
import functools


def env_parameter(env_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self):
            return os.environ.get(env_name)

        return wrapper

    return decorator
