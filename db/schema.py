import enum
from sqlalchemy import Column, Integer, MetaData, String, Table

convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': (
        'fk__%(table_name)s__%(all_column_names)s__'
        '%(referred_table_name)s'
    ),
    'pk': 'pk__%(table_name)s'
}

# Registry for all tables
metadata = MetaData(naming_convention=convention)


class Gender(enum.Enum):
    female = 'female'
    male = 'male'


songs_table = Table(
    'songs',
    metadata,
    Column('song_id', Integer, primary_key=True),
    Column('title', String(256), nullable=True),
    Column('artist', String(256), nullable=True),
    Column('album', String(256), nullable=True),
    Column('genre', String(256), nullable=True),
    Column('bit_rate', Integer, nullable=True),
    Column('duration', Integer, nullable=True),
    Column('file_size', Integer, nullable=False),
    Column('year', Integer, nullable=True),
    Column('hash_', String(256), nullable=False),
    Column('file_name', String(256), nullable=False),
)
