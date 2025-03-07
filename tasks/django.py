import invoke

from tasks import constants


@invoke.task
def run_server(ctx):
    with ctx.cd(str(constants.PROJECT_ROOT)):
        ctx.run(
            f"DJANGO_SETTINGS_MODULE={constants.DJANGO_SETTINGS_MODULE} "
            f"PYTHONPATH={constants.PYTHON_PATH} "
            f"uv run manage.py runserver"
        )


@invoke.task
def makemigrations(ctx):
    with ctx.cd(str(constants.PROJECT_ROOT)):
        ctx.run(
            f"DJANGO_SETTINGS_MODULE={constants.DJANGO_SETTINGS_MODULE} "
            f"PYTHONPATH={constants.PYTHON_PATH} "
            f"uv run manage.py makemigrations"
        )


@invoke.task
def migrate(ctx):
    with ctx.cd(str(constants.PROJECT_ROOT)):
        ctx.run(
            f"DJANGO_SETTINGS_MODULE={constants.DJANGO_SETTINGS_MODULE} "
            f"PYTHONPATH={constants.PYTHON_PATH} "
            f"uv run manage.py migrate"
        )
