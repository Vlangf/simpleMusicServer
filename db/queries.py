import sqlalchemy
from db.schema import songs_table
from settings import db_connect_string


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBSongs(metaclass=Singleton):
    def __init__(self):
        self.engine = sqlalchemy.create_engine(db_connect_string)

    def insert_song(self, year, file_size, duration, bit_rate, genre, album, artist, title, hash_):
        with self.engine.connect() as conn:
            query = songs_table.insert().values(year=year, file_size=file_size, duration=duration, bit_rate=bit_rate,
                                                genre=genre, album=album, artist=artist,
                                                title=title, hash_=hash_).returning(songs_table)
            return conn.execute(query).fetchone()

    def delete_song(self, song_id):
        with self.engine.connect() as conn:
            query = songs_table.delete().where(songs_table.c.song_id == song_id)
            return conn.execute(query)

    def get_song_by_hash(self, hash_):
        with self.engine.connect() as conn:
            query = songs_table.select().where(songs_table.c.hash_ == hash_)
            return conn.execute(query).fetchone()
