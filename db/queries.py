import sqlalchemy
from db.schema import songs_table
from settings import db_connect_string
from app.models import Song


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBSongs(metaclass=Singleton):
    def __init__(self):
        self.engine = sqlalchemy.create_engine(db_connect_string)

    def insert_song(self, year, file_size, duration, bit_rate, genre, album, artist, title, hash_, file_name):
        with self.engine.connect() as conn:
            query = songs_table.insert().values(year=year, file_size=file_size, duration=duration, bit_rate=bit_rate,
                                                genre=genre.lower(), album=album.title(), artist=artist.title(),
                                                title=title.title(), hash_=hash_,
                                                file_name=file_name).returning(songs_table)
            return conn.execute(query).fetchone()

    def delete_song(self, song_id):
        with self.engine.connect() as conn:
            query = songs_table.delete().where(songs_table.c.song_id == song_id)
            return conn.execute(query)

    def get_song_by_hash(self, hash_):
        with self.engine.connect() as conn:
            query = songs_table.select().where(songs_table.c.hash_ == hash_)
            return conn.execute(query).fetchone()

    def get_song_by_id(self, id_):
        with self.engine.connect() as conn:
            query = songs_table.select().where(songs_table.c.song_id == id_)
            return Song(**conn.execute(query).fetchone())

    def get_songs(self, limit, **kwargs):
        with self.engine.connect() as conn:
            query = songs_table.select().filter_by(**kwargs).limit(limit)
            return conn.execute(query).fetchall()

# print(DBSongs().get_songs(1, song_id=7))
