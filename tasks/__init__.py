import invoke

import tasks.backend.linting as backend_linting
import tasks.backend.type_checking as backend_type_checking
from tasks import django, testing

namespace = invoke.Collection(
    *(
        backend_linting.run_python_formatter,
        backend_linting.run_python_ruff_linter,
        backend_type_checking.run_python_type_checker,
    ),
    *(testing.run_tests,),
    *(django.run_server, django.makemigrations, django.migrate),
)
