from pydantic import BaseModel


class Song(BaseModel):
    duration: float
    author: str
    name: str
    id: int


class UploadSong(BaseModel):
    file: bytes
