import sqlite3
from datetime import datetime
import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db(schema_only=False):
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    if not schema_only:
        with current_app.open_resource('data.sql') as f:
            db.executescript(f.read().decode('utf8'))


def init_app(app):
    app.teardown_appcontext(close_db)

    @app.cli.command('init-db')
    @click.option('--empty', is_flag=True, help="Create schema only, no mock data")
    def init_db_command(empty):
        """Clear the existing data and create new tables."""
        init_db(schema_only=empty)
        click.echo('Initialized the database' + ('' if empty else ' with mock data.'))


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)