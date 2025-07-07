import os
from fastapi import UploadFile, HTTPException

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "pdf", "mp4"}
MAX_FILE_SIZE_MB = 50

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

async def save_upload(file: UploadFile, folder: str = "uploads/"):
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="Estensione non permessa")
    if file.spool_max_size > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File troppo grande")
    path = os.path.join(folder, file.filename)
    os.makedirs(folder, exist_ok=True)
    with open(path, "wb") as f:
        f.write(await file.read())
    # Qui puoi aggiungere: scan antivirus, compressione, watermark...
    return path
