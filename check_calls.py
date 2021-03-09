from functools import wraps
import asyncio
import inspect

def calltracker(func):
    print(func.__name__)
    async def helper(func, *args, **kwargs):
        if inspect.iscoroutinefunction(func):
                print(func)
                return await func(*args, **kwargs)
        else:
                print(f"not a coroutine: {func.__name__}")
                return func(*args, **kwargs)

    @wraps(func)
    async def wrapper(*args, **kwargs):
        if func.__name__ == 'create':
            print("True")
            result = await func(*args, called=True)
        if func.__name__ == 'get_db':
            print(func)
            # result = await func(*args, **kwargs)
            return func(*args, **kwargs)
        
        return result
    return wrapper