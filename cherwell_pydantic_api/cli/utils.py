from functools import wraps



def async_command(command):
    @wraps(command)
    def wrapper(*args, **kwargs):
        import asyncio
        return asyncio.run(command(*args, **kwargs))
    return wrapper
