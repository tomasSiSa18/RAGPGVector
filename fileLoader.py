from fastapi import FastAPI, File, UploadFile
import requests


app = FastAPI()

urlFiles = "https://n8n.virtual.uniandes.edu.co/webhook-test/fba4005f-cf21-4bcb-b29d-4234835afbf5"

from fastapi import FastAPI, File, UploadFile
import requests

app = FastAPI()

urlFiles = "https://n8n.virtual.uniandes.edu.co/webhook-test/fba4005f-cf21-4bcb-b29d-4234835afbf5"

@app.post("/predict/file")
async def upload_file(file: UploadFile = File(...)):
    # Read the file content
    contents = await file.read()

    # Send it using requests
    response = requests.post(
        url=urlFiles,
        files={"file": (file.filename, contents, file.content_type)}
    )

    return {
        "message": "File sent",
        "status_code": response.status_code,
        "response_text": response.text
    }

