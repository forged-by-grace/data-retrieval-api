import asyncio

after_start_functions = []
before_migrate_functions = []
after_migrate_functions = []


def register_after_start(func):
    after_start_functions.append(func)
    return func


def register_before_migrate(func):
    before_migrate_functions.append(func)
    return func


def register_after_migrate(func):
    after_migrate_functions.append(func)
    return func


async def after_start_hooks(*args, **kwargs):
    print("Executing after_start hooks...")
    await asyncio.gather(*[func(*args, **kwargs) for func in after_start_functions])
    print("after_start hooks executed successfully.")


async def before_migrate_hooks(*args, **kwargs):
    print("Executing before_migrate hooks...")
    await asyncio.gather(*[func(*args, **kwargs) for func in before_migrate_functions])
    print("before_migrate hooks executed successfully.")


async def after_migrate_hooks(*args, **kwargs):
    print("Executing after_migrate hooks...")
    await asyncio.gather(*[func(*args, **kwargs) for func in after_migrate_functions])
    print("after_migrate hooks executed successfully.")


@register_after_start
async def function1_after_start(arg1, arg2, kwarg1=None):
    print(f"Function 1 after_start executed with args: {arg1}, {arg2}, kwargs: {kwarg1}")


@register_after_start
async def function2_after_start(arg, *args, **kwargs):
    print(f"Function 2 after_start executed with arg: {arg}, args: {args}, kwargs: {kwargs}")


@register_after_start
async def function3_after_start(*args, **kwargs):
    print(f"Function 3 after_start executed with args: {args}, kwargs: {kwargs}")


@register_before_migrate
async def function1_before_migrate(*args, **kwargs):
    print("Function 1 before_migrate executed")


@register_before_migrate
async def function2_before_migrate(*args, **kwargs):
    print("Function 2 before_migrate executed")


@register_before_migrate
async def function3_before_migrate(*args, **kwargs):
    print("Function 3 before_migrate executed")


@register_after_migrate
async def function1_after_migrate(*args, **kwargs):
    print("Function 1 after_migrate executed")


@register_after_migrate
async def function2_after_migrate(*args, **kwargs):
    print("Function 2 after_migrate executed")


@register_after_migrate
async def function3_after_migrate(*args, **kwargs):
    print("Function 3 after_migrate executed")

