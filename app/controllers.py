from fastapi import FastAPI, UploadFile
from tinytag import TinyTag
import uvicorn

app = FastAPI()


@app.post("/upload_song")
def upload_song(file: UploadFile):
    with open(file.filename, 'wb') as song:
        song.write(file.file.read())

    tags = TinyTag.get(file.filename)

    return {"Result": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
