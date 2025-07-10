from typing import List
from fastapi import Body, FastAPI, File, UploadFile
import requests

app = FastAPI()

urlFiles = "https://n8n.virtual.uniandes.edu.co/webhook/fba4005f-cf21-4bcb-b29d-4234835afbf5"
urlQuery = "https://n8n.virtual.uniandes.edu.co/webhook/509ac137-da63-400f-93fd-e247a7cb3971"


@app.post("/upload/file")
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
    
@app.post("/upload/file")
async def upload_files(files: List[UploadFile] = File(...)):
    responses = []
    
    for file in files:
    
        # Read the file content
        contents = await file.read()

        # Send it using requests
        response = requests.post(
            url=urlFiles,
            files={"file": (file.filename, contents, file.content_type)}
        )

        responses.append(response)
        
    return {
        "message": f"{len(responses)} files sent"
    }
@app.post("/retrieve/question")
def receive_string(data: str = Body(..., embed=True)):

    response = requests.post(
        url=urlQuery,
        data={"query": data}
    )
    
    responseJson = response.json()

    print(responseJson["output"])

    return {"received": responseJson["output"]}
