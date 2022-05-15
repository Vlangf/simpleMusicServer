import os
import hashlib
from tinytag import TinyTag
from db.queries import DBSongs
from settings import file_dir
from fastapi import FastAPI, UploadFile
from app.models import SongListFilters, SongsList, Song

app = FastAPI()


@app.post("/upload_song")
def upload_song(file: UploadFile):
    song = file.file.read()
    hash_md5 = hashlib.md5(song).hexdigest()

    if DBSongs().get_song_by_hash(hash_md5) is not None:
        return {"Result": "False", 'Error': 'Song already exist'}

    song_path = os.path.join(file_dir, file.filename)
    with open(song_path, 'wb') as song_file:
        song_file.write(song)

    song_tags = TinyTag.get(song_path)
    DBSongs().insert_song(year=song_tags.year, file_size=song_tags.filesize, duration=song_tags.duration,
                          bit_rate=song_tags.bitrate, genre=song_tags.genre, album=song_tags.album,
                          artist=song_tags.artist, title=song_tags.title, hash_=hash_md5, file_name=file.filename)

    return {"Result": "OK"}


@app.delete("/delete_song/<song_id>")
def delete_song(song_id: int):
    file_name = DBSongs().get_song_by_id(song_id)['file_name']
    os.remove(os.path.join(file_dir, file_name))
    DBSongs().delete_song(song_id)

    return {"Result": "OK"}


@app.post("/get_songs_list")
def get_songs_list(body: SongListFilters, limit=20):
    filter_json = {k: v for k, v in body if v is not None}
    songs = DBSongs().get_songs(limit, **filter_json)
    return SongsList(**{'songs': songs})


@app.get("/get_song_by_id/<song_id>")
def get_song_by_id(song_id: int) -> Song:
    song = DBSongs().get_song_by_id(song_id)
    return Song(**song)
