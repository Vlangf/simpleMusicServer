from pydantic import BaseModel
from typing import List


class SongListFilters(BaseModel):
    year: int = None
    genre: str = None
    album: str = None
    artist: str = None
    title: str = None


class Song(BaseModel):
    song_id: int
    year: int = None
    file_size: int
    duration: int = None
    bit_rate: int = None
    genre: str = None
    album: str = None
    artist: str = None
    title: str = None


class SongsList(BaseModel):
    songs: List[Song]
