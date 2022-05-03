import enum
from sqlalchemy import Column, Enum, Integer, MetaData, SmallInteger, String, Table

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


songss_table = Table(
    'songs',
    metadata,
    Column('song_id', Integer, primary_key=True),
    Column('title', String(256), nullable=False),
    Column('artist', String(256), nullable=True),
    Column('album', String(256), nullable=True),
    Column('genre', String(256), nullable=True),
    Column('bit_rate', SmallInteger, nullable=True),
    Column('duration', SmallInteger, nullable=True),
    Column('file_size', SmallInteger, nullable=False),
    Column('year', SmallInteger, nullable=True)
)
