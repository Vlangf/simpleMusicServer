import os
import hashlib
from tinytag import TinyTag
from db.queries import DBSongs
from settings import file_dir
from fastapi import FastAPI, UploadFile

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
                          artist=song_tags.artist, title=song_tags.title, hash_=hash_md5)
    return {"Result": "OK"}


@app.post("/unload_song")
def unload_song(file: UploadFile):
    with open(os.path.join(file_dir, file.filename), 'wb') as song:
        song.write(file.file.read())

    song_tags = TinyTag.get(file.filename)
    DBSongs().insert_song(year=song_tags.year, file_size=song_tags.filesize, duration=song_tags.duration,
                          bit_rate=song_tags.bitrate, genre=song_tags.genre, album=song_tags.album,
                          artist=song_tags.artist, title=song_tags.title)
    return {"Result": "OK"}


@app.delete("/delete_song/<song_id>")
def delete_song(song_id: int):
    DBSongs().delete_song(song_id)
    return {"Result": "OK"}
