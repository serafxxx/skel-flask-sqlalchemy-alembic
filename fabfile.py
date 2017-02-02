from fabric.api import *


def make_migration(migration_name):
    """Generate new migration"""
    local('alembic revision --autogenerate -m "%s"' % migration_name)

def migrate():
    """Apply all new migrations"""
    local('alembic upgrade head')