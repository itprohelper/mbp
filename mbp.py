from app import create_app, db
from app.models import (
)


app = create_app()


@app.shell_context_processor
def make_shell_context():
    shell_context = {
        'db': db,
    }

    return shell_context